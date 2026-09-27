#!/usr/bin/env python3
"""
Check the five criteria in criteria.md across three real runs, and print the
per-criterion table the unit 2 run log asks for:

    | Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |

    python check_criteria.py

This is separate from run_eval.py on purpose: run_eval.py's job is to produce
the raw run log (one row per QUESTION, three runs each). This script's job is
the aggregation step the submission template asks you to do by hand — turning
those questions into one row per CRITERION, with an x/5 count for each run.

Criterion 3 (the relevance gate on out-of-corpus questions) is measured once,
not three times: the gate is a deterministic comparison against a fixed
number, so it comes out the same every run and that same value fills all
three Run columns, same as the example in the assignment.
"""

import datetime as dt

import config
import questions as qs
import scorer
from run_eval import run_once, check_out_of_scope

RUNS = 3


def score_one_pass(items, top_k, threshold, corpus):
    """One run over every question. Returns hit counts for criteria 1, 2, 4, 5."""
    hits = {"1": 0, "2": 0, "4": 0, "5": 0}
    for item in items:
        question = item["question"]
        expects = item.get("expects", "")
        answer, results, _decision = run_once(question, top_k, threshold, corpus, "default")

        hits["1"] += scorer.retrieval_hits(expects, results)
        hits["2"] += scorer.has_source(answer, results)
        hits["4"] += scorer.top_retrieval(expects, results)
        hits["5"] += scorer.source_contains_relevant_info(expects, answer, results)
    return hits


def verdict(counts, target, n):
    """MET only if every run met the target; one shortfall is enough to MISS."""
    return "MET" if all(c >= target for c in counts) else "MISSED"


def build_table(run_hits, n, c3_hits, c3_n):
    targets = {
        "1": (4, "Retrieved chunk contains the answer"),
        "2": (5, "Every answer names a source"),
        "3": (4, "Gate stops out-of-corpus questions"),
        "4": (4, "Rank-1 chunk contains the answer"),
        "5": (5, "Cited source actually contains it"),
    }

    lines = [
        "| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |",
        "|---|---|---|---|---|---|",
    ]

    for key in ["1", "2", "3", "4", "5"]:
        target, label = targets[key]
        if key == "3":
            counts = [c3_hits] * RUNS
            run_cells = [f"{c3_hits}/{c3_n}" for _ in range(RUNS)]
        else:
            counts = [run_hits[i][key] for i in range(RUNS)]
            run_cells = [f"{c}/{n}" for c in counts]

        v = verdict(counts, target, n)
        row = f"| {key}. {label} | {target} of {n if key != '3' else c3_n} | " + \
              " | ".join(run_cells) + f" | {v} |"
        lines.append(row)

    return "\n".join(lines)


def main():
    top_k = config.TOP_K
    threshold = config.THRESHOLD
    corpus = config.CORPUS

    items = qs.answered()
    if not items:
        print("questions.py has no questions in it yet.")
        return
    n = len(items)

    run_hits = []
    for run in range(1, RUNS + 1):
        print(f"Run {run} of {RUNS}...")
        run_hits.append(score_one_pass(items, top_k, threshold, corpus))

    print("\nOut-of-scope questions (the gate should refuse these):")
    gate_rows = check_out_of_scope(top_k, threshold, corpus, "default")
    c3_hits = sum(row["refused"] for row in gate_rows)
    c3_n = len(gate_rows)

    table = build_table(run_hits, n, c3_hits, c3_n)
    print("\n" + table)

    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    path = config.RESULTS_DIR / f"criteria_{stamp}.md"
    path.write_text(table + "\n", encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)} — paste this table into your run log.")


if __name__ == "__main__":
    main()
