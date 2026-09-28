# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->
Aloye Oshote; Copus --> city_guides

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->
     I selected the city_guides corpus. My system answers questions about different cities within a specific regions. The guides give information on food, how to get around, what sights to see, etc. It also give some tips on how to navigate the region, as well as key information that any traveler should know before making the trip. 

## Chunking Strategy

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

I chunk by section heading instead of by a fixed character count. Every document in `city_guides` is a markdown file named after one area (for example `guide_elder_ness.md`), and each is already divided into sections. Each section has a `##` heading with one or more paragraphs under it, and each one covers a single topic about that area. So `split_on_headings` starts a new chunk at every `##` line and keeps the heading attached to the text below it.

There is no fixed chunk size, because the size follows the section.

I use no overlap. Overlap exists so a sentence isn't cut in half at an arbitrary boundary, and heading boundaries are not arbitrary: the text on either side of one is a different topic.

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `` — produced by: ``

```
======================================================================
Chunk 1  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
======================================================================
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.
```

**Chunk 2** — source: `` — produced by: ``

```
======================================================================
Chunk 2  |  source: guide_corry_vale.md#6  |  produced by: chunker.py::split_documents
======================================================================
## When to go

May to September. Outside those months the pub in the third village closes, the farm shop reduces its hours, and several footpaths become genuinely boggy rather than merely wet. The road is not gritted above the second village and is impassable in snow.
```

**Chunk 3** — source: `` — produced by: ``

```
======================================================================
Chunk 3  |  source: guide_givens_mill.md#3  |  produced by: chunker.py::split_documents
======================================================================
## Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.
```

**Chunk 4** — source: `` — produced by: ``

```
======================================================================
Chunk 4  |  source: guide_kestrelford.md#6  |  produced by: chunker.py::split_documents
======================================================================
## When to go

Late spring and early autumn. The Saturday market runs year-round but is much reduced from November to February. August is busy with walkers. The single-track approach road is genuinely difficult in snow and the town can be cut off for a day or two most winters.

```

**Chunk 5** — source: `` — produced by: ``

```
======================================================================
Chunk 5  |  source: guide_regional_transport.md#1  |  produced by: chunker.py::split_documents
======================================================================
## The railway

The line runs along the river valley, connecting Brightwater to the regional
hub in 50 minutes. Eleven services a day on weekdays, six on Sundays. The line
north of Brightwater closed in 1963 and everything beyond it is bus or car.

Tickets are cheaper booked the day before than on the day, and considerably
cheaper than that booked a week ahead. There is no ticket office at
Brightwater station outside weekday mornings; the machine on the platform takes
cards only.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
"What are the three reasons why people come to Elder Ness?"

**Answer:**
```
(best distance 0.260, cutoff 0.6)

People come to Elder Ness for one of three reasons: birds, walking, or a deliberate absence of things to do (guide_elder_ness.md).

Sources retrieved: guide_eating.md, guide_elder_ness.md, guide_walking.md
```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

I kept the starter's cutoff of **0.6**. I ran my five test questions and the five in `OUT_OF_SCOPE` and recorded the best distance for each. The two groups separate cleanly:

- **Questions the corpus covers:** best distances from 0.260 to 0.437.
- **Questions it doesn't cover:** best distances from 0.754 to 0.899.

The gap runs from 0.437 to 0.754, and 0.6 sits inside it. At 0.6, all five in-corpus questions pass the gate and all five out-of-scope questions are refused.

| Question | In corpus? | Best distance |
|---|---|---|
| "What are the three reasons why people come to Elder Ness?" | Yes | 0.260 |
| "Where can I find the best food in Pellew Sands?" | Yes | 0.437 |
| "If I drove on good roads from Brightwater to Thornby Wells, how long would it take?" | Yes | 0.341 |
| "Where can I go camping in Corry Vale?" | Yes | 0.408 |
| "What payment is accepted at the railway machine on the platform in Brightwater?" | Yes | 0.436 |
| "What is the capital of Mongolia?" | No | 0.754 | 
| "How do I change the oil in a diesel engine?" | No | 0.892 |
| "Who won the 1994 World Cup?" | No | 0.899 |
| "What is the recommended dosage of ibuprofen for a headache?" | No | 0.846 |
| "How do I write a for loop in Rust?" | No | 0.813 |


## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
I used AI to help me write my chunking method. I told it exactly how I wanted it chunked, and it worked with me to create the function I used. It ignored the overlap, and I agreed, since the city_guide files were ordered neatly. 

**2.**
I asked AI to help me refine and critique my criteria and questions. I asked for feedback and tips for improvement. It called out the different criteria that lacked specificity, and told me how to improve them. 

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Rank-1 chunk contains the answer | 4 of 5 | 3/5 | 3/5 | 3/5 | MISSED |
| 5. Cited source actually contains the claimed fact | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

### Criterion 1 
Retrieved chunk contains the answer (expects: "Marine Terrace") - PASS

The prompt's "Documents:" section includes this chunk:

```
[from guide_pellew_sands.md]
## Eat and drink

The seafront is chips and ice cream, done well and without pretence. The better cooking is on Marine Terrace, one street back, where four or five places are genuinely good and roughly half the seafront price. Sunday evening is difficult — most kitchens close.
```
Produced by: store.py::search, assembled into the prompt by generate.py::build_prompt.

### Criterion 2
Every answer names a source - PASS

```
The better cooking in Pellew Sands can be found on Marine Terrace, which is located one street back from the seafront. 

Sources: `guide_pellew_sands.md` and `guide_eating.md`
```

Produced by: generate.py::answer_from_chunks.

### Criterion 3
Gate stops out-of-corpus questions - PASS

``` 
(.venv) ai201-project1-unofficial-guide-starter-v2026 $ python app.py ask "What is the capital of Mongolia?"
  (best distance 0.754, cutoff 0.6)

I don't have enough information about that.

0 model calls this session
```

Retrieval and distance produced by: store.py::search
Refusal decision and text produced by: gate.py::check (gate.REFUSAL)
Verified (pass/fail) by: scorer.py::classify_out_of_scope

### Criterion 4
rank-1 chunk contains the answer - FAILS

The first chunk in the Documents list — the actual rank-1 result — is this one, which doesn't mention Marine Terrace at all:

```
[from guide_pellew_sands.md]
# Pellew Sands

Pellew Sands is a Victorian seaside resort that has been through three distinct lives: fashionable, then neglected, and now something in between. The architecture is from the first period and much of the infrastructure from the second.
```
The chunk that actually contains "Marine Terrace" came back 3rd, not 1st. This is a legitimate example of a rank-1 miss for your criteria table.

Retrieval and chunk text produced by: store.py::search, assembled into the prompt by generate.py::build_prompt
Verified (pass/fail) by: scorer.py::top_retrieval

### Criterion 5
cited source actually contains the fact - PASS

Both cited sources hold the relevant text: guide_pellew_sands.md (chunk above) and guide_eating.md:
```
[from guide_eating.md]
## The pattern worth knowing
...
Pellew Sands's seafront is chips and ice cream, and Marine Terrace behind it is where the actual restaurants are.
```

Answer and citations produced by: generate.py::answer_from_chunks
Chunk text produced by: store.py::search
Verified (pass/fail) by: scorer.py::source_contains_relevant_info

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | All three runs came back 5/5 against a 4/5 target. `retrieval_hits` is an exact substring match, and confirmed this criterion. |
| 2 | Every answer names a source | MET | 5/5 every run. This is enforced structurally by the prompt template (`generate.py::GROUNDING_INSTRUCTION`). |
| 3 | Gate stops out-of-corpus questions | MET | 5/5 every run, beating the 4/5 target I set to allow for boundary noise. My `OUT_OF_SCOPE` questions are unambiguously outside the corpus (capital of Mongolia, oil changes, etc.), so the gate never had a genuinely close case to get wrong. |
| 4 | Rank-1 chunk contains the answer | MISSED | 3/5 in all three runs — not 4, 3, 4, but flat at 3 every time. That consistency matters: this isn't run-to-run noise, it's the same question(s) ranking their answer chunk below rank 1 on every single run. Diagnosed below. |
| 5 | Cited source actually contains the claimed fact | MET | 5/5 by what `scorer.py::source_contains_relevant_info` check. The chunk text is real, unedited content from that file, so a match is genuine evidence the source contains the fact. 

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

Criterion 4 (first chunk contains the answer) missed on 2 of the 5 questions. In both occassions, the miss was in the retrieval stage, and both were missed for the same reason: chunks in this corpus that share a place-name overlap out-ranked the chunk that actually has the fact.

For example, the question **"Where can I find the best food in Pellew Sands?"** (expects: "Marine Terrace"). For this question, the chunk with the answer ranked 3rd. However, I observed something interesting. The top chunks mentioned Pellew Sands, but had nothing to do with the question I asked. The chunk that actualy contained the correct answer did not mention Pellew Sands once. So, the distance gives weight to having specific key words than actually having information relevant to my question. 

Another example comes from the question **"If I drove on good roads from Brightwater to Thornby Wells, how long would it take?"**. Once again, we see the code looking for keywords instead of having enough context to know which file to pull from. The chunk with the correct answer, in this case, was the 5th chunk. Everyv chunk before either had the keyword 'Brightwater'. 

So, it seems that we have a problem in the retrieval phase. Chunks that have some keywords, but do not have any relation to the question are being ranked higher than specific chunks that do not contain certain keywords, but directly answers the question.


## The Improvement

**What I changed:**

To give every chunk context on what specifically it is talking about, I will prepend the title of the document to them.

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->
     I chose this because the main issue I was seeing is that certain chunks that contained the answer, but did not have keywords were not higher up in the chunk priority. So, by adding some more context to the chunk, I believe that I can allow the tool to more accurately prioritize the chunks. 

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
