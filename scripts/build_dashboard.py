#!/usr/bin/env python3
"""
Build the feature dashboard (index.html) from the per-repo weekly report CSVs.

Reads every reports/<slug>/<slug>_<start>_to_<end>.csv, keeps the rows the
tracker flagged as new features, and emits a compact payload that the dashboard
renders client-side. The payload is inlined into index.html so the page works
from file:// as well as GitHub Pages, with no fetch and no dependencies.
"""

import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

from update_dashboard import TRACKED  # noqa: E402  single source of repo metadata

WEEK_RE = re.compile(r"_(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})\.csv$")


def week_key(path: Path) -> str | None:
    m = WEEK_RE.search(path.name)
    return f"{m.group(1)}_to_{m.group(2)}" if m else None


def collect() -> dict:
    weeks: set[str] = set()
    rows: list[dict] = []
    totals: dict[tuple[str, str], list[int]] = {}

    for repo_idx, t in enumerate(TRACKED):
        slug = t["slug"]
        for csv_path in sorted((REPO_ROOT / "reports" / slug).glob(f"{slug}_*.csv")):
            wk = week_key(csv_path)
            if wk is None:
                continue
            weeks.add(wk)

            with csv_path.open(encoding="utf-8", newline="") as fh:
                records = list(csv.DictReader(fh))

            feats = [r for r in records if (r.get("new_feature") or "").strip() == "yes"]
            totals[(slug, wk)] = [len(feats), len(records)]

            for r in feats:
                rows.append({
                    "w": wk,
                    "r": repo_idx,
                    "d": (r.get("date") or "").strip(),
                    "c": (r.get("component") or "Other").strip(),
                    "m": clean_message(r.get("message") or ""),
                    "a": (r.get("author") or "").strip(),
                    "p": (r.get("pr") or "").strip(),
                    "s": (r.get("sha") or "").strip(),
                    "k": 1 if (r.get("rocm") or "").strip() == "yes" else 0,
                })

    week_list = sorted(weeks)
    w_index = {w: i for i, w in enumerate(week_list)}
    for row in rows:
        row["w"] = w_index[row["w"]]
    rows.sort(key=lambda r: (-r["w"], r["r"], r["c"], r["d"]))

    return {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "weeks": week_list,
        "repos": [
            {"slug": t["slug"], "name": t["repo"], "desc": t["desc"], "url": t["link"]}
            for t in TRACKED
        ],
        # totals[repoIdx][weekIdx] = [featureCount, commitCount]
        "totals": [
            [totals.get((t["slug"], w), [0, 0]) for w in week_list]
            for t in TRACKED
        ],
        "features": rows,
    }


def clean_message(msg: str) -> str:
    """Drop the trailing '(#1234)' that duplicates the PR link, and collapse space."""
    msg = re.sub(r"\s*\(#\d+\)\s*$", "", msg.strip())
    return re.sub(r"\s+", " ", msg)


def build_html(payload: dict) -> str:
    data = json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
    return HTML_TEMPLATE.replace("/*__DATA__*/null", data)


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>oss-pulse — weekly feature digest</title>
<style>
  :root {
    --bg:#0d1117; --panel:#161b22; --panel2:#1c2129; --line:#2a313c;
    --fg:#e6edf3; --dim:#8b949e; --accent:#58a6ff; --amd:#f0883e; --ok:#3fb950;
  }
  * { box-sizing:border-box; }
  body {
    margin:0; background:var(--bg); color:var(--fg);
    font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
  }
  a { color:var(--accent); text-decoration:none; }
  a:hover { text-decoration:underline; }
  .wrap { max-width:1180px; margin:0 auto; padding:24px 20px 80px; }

  header h1 { margin:0 0 4px; font-size:22px; letter-spacing:-.2px; }
  header p  { margin:0; color:var(--dim); font-size:13px; }

  .weekbar {
    display:flex; align-items:center; gap:10px; flex-wrap:wrap;
    margin:22px 0 18px; padding:14px 16px;
    background:var(--panel); border:1px solid var(--line); border-radius:10px;
  }
  .weekbar select, .weekbar input {
    background:var(--panel2); color:var(--fg);
    border:1px solid var(--line); border-radius:6px; padding:6px 10px; font-size:13px;
  }
  .weekbar input[type="search"] { min-width:260px; }
  .weekbar input[type="checkbox"] { accent-color:var(--accent); margin:0; }
  .nav {
    background:var(--panel2); border:1px solid var(--line); color:var(--fg);
    border-radius:6px; width:30px; height:30px; cursor:pointer; font-size:15px;
  }
  .nav:disabled { opacity:.3; cursor:default; }
  .spacer { flex:1; }
  .toggle { display:flex; align-items:center; gap:6px; color:var(--dim); font-size:13px; cursor:pointer; }

  .headline { display:flex; align-items:baseline; gap:14px; margin:0 0 16px; flex-wrap:wrap; }
  .headline .big { font-size:40px; font-weight:650; letter-spacing:-1px; }
  .delta { font-size:14px; font-weight:600; }
  .up { color:var(--ok); } .down { color:var(--amd); } .flat { color:var(--dim); }

  .cards { display:grid; grid-template-columns:repeat(auto-fit,minmax(178px,1fr)); gap:10px; margin-bottom:26px; }
  .card {
    background:var(--panel); border:1px solid var(--line); border-radius:10px;
    padding:12px 14px; cursor:pointer; transition:border-color .12s, background .12s;
  }
  .card:hover { border-color:#3d4550; }
  .card.off { opacity:.4; }
  .card .nm { font-size:12px; color:var(--dim); margin-bottom:6px;
              white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
  .card .ct { font-size:26px; font-weight:650; letter-spacing:-.5px; }
  .card .sub { font-size:11px; color:var(--dim); margin-top:3px; }
  .spark { display:flex; align-items:flex-end; gap:2px; height:22px; margin-top:8px; }
  .spark i { flex:1; background:#30363d; border-radius:1px; min-height:1px; }
  .spark i.cur { background:var(--accent); }

  .repo { margin-bottom:30px; }
  .repo > h2 { font-size:16px; margin:0 0 2px; }
  .repo > .meta { color:var(--dim); font-size:12px; margin-bottom:12px; }

  .comp { margin-bottom:12px; border:1px solid var(--line); border-radius:9px; overflow:hidden; }
  .comp > summary {
    background:var(--panel); padding:9px 14px; cursor:pointer; font-size:13px;
    font-weight:600; list-style:none; display:flex; align-items:center; gap:9px;
  }
  .comp > summary::-webkit-details-marker { display:none; }
  .comp > summary::before { content:"▸"; color:var(--dim); font-size:11px; }
  .comp[open] > summary::before { content:"▾"; }
  .pill {
    background:var(--panel2); border:1px solid var(--line); color:var(--dim);
    border-radius:20px; padding:1px 8px; font-size:11px; font-weight:500;
  }

  ul.items { list-style:none; margin:0; padding:0; }
  ul.items li {
    display:flex; gap:11px; padding:9px 14px;
    border-top:1px solid var(--line); align-items:baseline;
  }
  li .dt { color:var(--dim); font-size:11px; font-variant-numeric:tabular-nums; flex:none; width:44px; }
  li .msg { flex:1; min-width:0; }
  li .who { color:var(--dim); font-size:11px; flex:none; }
  .badge {
    display:inline-block; background:rgba(240,136,62,.14); color:var(--amd);
    border:1px solid rgba(240,136,62,.3); border-radius:4px;
    font-size:10px; padding:0 5px; margin-left:7px; vertical-align:1px; font-weight:600;
  }
  mark { background:rgba(88,166,255,.28); color:inherit; border-radius:2px; }
  .empty { color:var(--dim); padding:34px 4px; text-align:center; }
  footer { margin-top:40px; color:var(--dim); font-size:12px;
           border-top:1px solid var(--line); padding-top:14px; }
</style>
</head>
<body>
<div class="wrap">

  <header>
    <h1>oss-pulse</h1>
    <p>New features landing each week across the LLM inference stacks worth watching.</p>
  </header>

  <div class="weekbar">
    <button class="nav" id="prev" title="Previous week">‹</button>
    <select id="week"></select>
    <button class="nav" id="next" title="Next week">›</button>
    <input id="q" type="search" placeholder="Filter features… (e.g. fp8, disagg, MoE)">
    <span class="spacer"></span>
    <label class="toggle"><input type="checkbox" id="rocm"> ROCm / AMD only</label>
  </div>

  <div class="headline">
    <span class="big" id="total">—</span>
    <span id="totalLabel" style="color:var(--dim)">features</span>
    <span class="delta" id="delta"></span>
  </div>

  <div class="cards" id="cards"></div>
  <div id="list"></div>

  <footer>
    <span id="gen"></span> ·
    <a href="https://github.com/lcskrishna/oss-pulse">source</a> ·
    <a href="https://github.com/lcskrishna/oss-pulse/tree/main/reports">full weekly reports</a>
  </footer>

</div>

<script>
const DATA = /*__DATA__*/null;
const REPORT_BASE = "https://github.com/lcskrishna/oss-pulse/blob/main/reports";

const state = {
  week: DATA.weeks.length - 1,
  off:  new Set(),      // hidden repo indices
  q:    "",
  rocm: false,
};

const $ = id => document.getElementById(id);
const esc = s => s.replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const fmtWeek = w => { const [a,b] = w.split("_to_"); return a + "  →  " + b; };

function highlight(text, q) {
  const safe = esc(text);
  if (!q) return safe;
  const rx = new RegExp("(" + q.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig");
  return safe.replace(rx, "<mark>$1</mark>");
}

// Rows for the selected week, after the search and ROCm filters but BEFORE the
// per-repo toggles — the cards need counts for repos that are toggled off.
function weekRows() {
  const q = state.q.toLowerCase();
  return DATA.features.filter(f =>
    f.w === state.week &&
    (!state.rocm || f.k === 1) &&
    (!q || f.m.toLowerCase().includes(q) || f.c.toLowerCase().includes(q) || f.a.toLowerCase().includes(q))
  );
}

function render() {
  const rows = weekRows();
  const visible = rows.filter(f => !state.off.has(f.r));

  // headline + delta vs the previous week, on the same filters
  $("total").textContent = visible.length;
  $("totalLabel").textContent = visible.length === 1 ? "feature" : "features";

  const d = $("delta");
  if (state.week === 0) {
    d.textContent = ""; d.className = "delta";
  } else {
    const prevAll = DATA.features.filter(f =>
      f.w === state.week - 1 && !state.off.has(f.r) && (!state.rocm || f.k === 1));
    const q = state.q.toLowerCase();
    const prev = q ? prevAll.filter(f => f.m.toLowerCase().includes(q) ||
                                         f.c.toLowerCase().includes(q) ||
                                         f.a.toLowerCase().includes(q)) : prevAll;
    const diff = visible.length - prev.length;
    d.textContent = diff === 0 ? "same as last week"
                  : (diff > 0 ? "▲ " : "▼ ") + Math.abs(diff) + " vs last week";
    d.className = "delta " + (diff > 0 ? "up" : diff < 0 ? "down" : "flat");
  }

  renderCards(rows);
  renderList(visible);
}

function renderCards(rows) {
  const per = DATA.repos.map((_, i) => rows.filter(f => f.r === i).length);

  $("cards").innerHTML = DATA.repos.map((repo, i) => {
    const hist  = DATA.totals[i];
    const peak  = Math.max(1, ...hist.map(h => h[0]));
    const bars  = hist.map((h, w) =>
      `<i class="${w === state.week ? "cur" : ""}" style="height:${Math.round(h[0] / peak * 100)}%"></i>`
    ).join("");
    const commits = hist[state.week] ? hist[state.week][1] : 0;

    return `<div class="card ${state.off.has(i) ? "off" : ""}" data-r="${i}"
                 title="click to show/hide ${esc(repo.name)}">
              <div class="nm">${esc(repo.name)}</div>
              <div class="ct">${per[i]}</div>
              <div class="sub">of ${commits} commits</div>
              <div class="spark">${bars}</div>
            </div>`;
  }).join("");

  document.querySelectorAll(".card").forEach(el => {
    el.onclick = () => {
      const i = +el.dataset.r;
      state.off.has(i) ? state.off.delete(i) : state.off.add(i);
      render();
    };
  });
}

function renderList(rows) {
  if (!rows.length) {
    $("list").innerHTML = `<div class="empty">No features match these filters this week.</div>`;
    return;
  }

  let html = "";
  DATA.repos.forEach((repo, i) => {
    const mine = rows.filter(f => f.r === i);
    if (!mine.length) return;

    // group by component, largest group first
    const groups = {};
    mine.forEach(f => (groups[f.c] ||= []).push(f));
    const ordered = Object.entries(groups).sort((a, b) => b[1].length - a[1].length);

    // Pages serves raw .md as plain text, so link the rendered blob view instead.
    const reportUrl = `${REPORT_BASE}/${repo.slug}/${repo.slug}_${DATA.weeks[state.week]}.md`;

    html += `<section class="repo">
      <h2><a href="${repo.url}">${esc(repo.name)}</a></h2>
      <div class="meta">${mine.length} feature${mine.length === 1 ? "" : "s"} ·
        <a href="${reportUrl}">full report</a></div>`;

    ordered.forEach(([comp, items], gi) => {
      const open = gi < 3 ? " open" : "";   // expand the three biggest by default
      html += `<details class="comp"${open}>
        <summary>${esc(comp)}<span class="pill">${items.length}</span></summary>
        <ul class="items">`;

      items.sort((a, b) => b.d.localeCompare(a.d)).forEach(f => {
        const link = f.p
          ? `${repo.url}/pull/${f.p}`
          : `${repo.url}/commit/${f.s}`;
        const label = f.p ? `#${f.p}` : f.s.slice(0, 7);
        html += `<li>
          <span class="dt">${esc(f.d.slice(5))}</span>
          <span class="msg"><a href="${link}">${label}</a>
            ${highlight(f.m, state.q)}
            ${f.k ? '<span class="badge">ROCm</span>' : ""}</span>
          <span class="who">${esc(f.a)}</span>
        </li>`;
      });

      html += `</ul></details>`;
    });

    html += `</section>`;
  });

  $("list").innerHTML = html;
}

// ---- wiring -----------------------------------------------------------------

$("week").innerHTML = DATA.weeks
  .map((w, i) => `<option value="${i}">${fmtWeek(w)}</option>`).join("");
$("week").value = state.week;

$("week").onchange = e => { state.week = +e.target.value; syncNav(); render(); };
$("prev").onclick  = () => { if (state.week > 0) { state.week--; $("week").value = state.week; syncNav(); render(); } };
$("next").onclick  = () => { if (state.week < DATA.weeks.length - 1) { state.week++; $("week").value = state.week; syncNav(); render(); } };
$("rocm").onchange = e => { state.rocm = e.target.checked; render(); };

let t;
$("q").oninput = e => { clearTimeout(t); t = setTimeout(() => { state.q = e.target.value.trim(); render(); }, 120); };

function syncNav() {
  $("prev").disabled = state.week === 0;
  $("next").disabled = state.week === DATA.weeks.length - 1;
}

$("gen").textContent = "Generated " + DATA.generated;
syncNav();
render();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    payload = collect()
    out = REPO_ROOT / "index.html"
    out.write_text(build_html(payload), encoding="utf-8")
    print(
        f"index.html → {out}  "
        f"({len(payload['features'])} features, {len(payload['weeks'])} weeks, "
        f"{out.stat().st_size // 1024} KB)"
    )
