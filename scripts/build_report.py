import json, datetime

meta = {m["id"]: m for m in json.load(open("meta.json"))}

# (unit, lesson, [video ids], verdict)
ROWS = [
(1, "1. Welcome to CSP", ["nwC42foRtaM"], "Course orientation: explains what CSP covers and how it's assessed; not lesson content. 2022, so exam logistics are dated."),
(1, "2. Representing Information", ["USCBCmwMCDA"], "Concept-first tour from bits to numbers/text/images; the framing still matches this lesson."),
(1, "3. Circle Square Patterns", ["5lfxBBOJLp4"], "Live classroom run-through of the activity; shows the patterns but explains little of the reasoning. No polished 2024+ explainer exists."),
(1, "4. Binary Numbers", ["eJ-xChlgzsE"], "Teaches place value and conversion with worked examples; labelled by AP topic 2.1, not Code.org U1L4."),
(1, "5. Overflow and Rounding", ["WXRL3InpLI8"], "Explains overflow vs round-off, then works the Code.org U1.5 tasks and 5 MCQs — logic-focused."),
(1, "6. Representing Text", ["GMF2Z1EZHXk"], "Builds ASCII → Unicode → UTF-8 by encoding real strings by hand."),
(1, "7. Black and White Images", ["15aqFQQVBWU"], "Explains the pixel grid and bits-per-pixel before adding color; 2015 but the model is unchanged."),
(1, "8. Color Images", ["yPPv3jeM4xw"], "Long but genuinely conceptual: pixel grid → RGB channels → file storage, with worked examples."),
(1, "9. Lossless Compression", ["mNRdjGm03pI"], "Explains why compression works and the lossless trade-offs with simple examples. Pre-2024, but U1 numbering unchanged."),
(1, "10. Lossy Compression", ["RLXC_KSP83s"], "Contrasts lossy/lossless trade-offs in six minutes; audio-led, no byte-level worked example."),
(1, "11. Intellectual Property", ["e1j8jflkBt0"], "Copyright vs Creative Commons vs open access with real cases; deliberately surface-level, as the lesson is."),
(1, "12. Project - Digital Information Dilemmas", ["J-9WF_Pjuvs"], "Teacher walks the project brief and gives assessment advice; does not model the research/reasoning."),
(1, "13. Assessment Day", ["hOKrd1BpXu8"], "Unit-1 review Q&A across representation and compression; older, but U1 content is stable."),

(2, "1. Welcome to the Internet", ["Dxcc6ycZ73M"], "Vint Cerf frames the internet as a packet-switched network; conceptually right, visuals are 2016."),
(2, "2. Building a Network", ["3QhU9jd03a0"], "Explains nodes, links, LAN/WAN and why networks scale, from first principles."),
(2, "3. The Need for Addressing", ["lPPYc_sFLKo"], "Explains why addresses are required and how they are assigned; networking-general, not AP-specific."),
(2, "4. Routers and Redundancy", ["q3VN9g0EZdA"], "Current AP CSP treatment of redundancy and fault tolerance with concrete failure examples."),
(2, "5. Packets", ["aD_yi5VjF78"], "Shows packetisation, headers, reassembly and reliability; AP-aligned Khan Academy segment."),
(2, "6. HTTP and DNS", ["AlkDbnbv7dk"], "Traces URL → DNS → TCP → HTTP → render; strong systems view, not Code.org-specific."),
(2, "7. Project - Internet Dilemmas", ["X22o-pC33CE"], "Teacher reads through the project and advises; no worked example of weighing a dilemma."),
(2, "8. Assessment Day", ["cICKX0EzSTE"], "Short practice set on networks with reasoning shown; thin for a full assessment day."),

(3, "1. Introduction to Apps", ["Z-BO6IYTgJg"], "Defines UI vs UX with everyday examples; does not cover event-driven programs."),
(3, "2. Introduction to Design Mode", ["-EoTeD4mSNU"], "Official App Lab design-mode walkthrough; old UI but the concepts still hold."),
(3, "3. Project - Designing an App Part 1", ["btGE5E-FQjw"], "Walks the planning guide step by step and models requirement/design decisions."),
(3, "4. The Need for Programming Languages", ["EGQh5SZctaE"], "Explains what a programming language is and why abstraction matters; light on AP pseudocode."),
(3, "5. Intro to Programming", ["xlbRL5eOgkI"], "Shows console/UI wiring in App Lab; treats syntax mechanically, little on program flow."),
(3, "6. Debugging", ["AzOPfL3k6bI"], "Models syntax/runtime/logic debugging strategies with examples."),
(3, "7. Project - Designing an App Part 2", ["Sy3PYZ7QLhc"], "Real-time build of the project; mostly demonstrating, some explanation of choices."),
(3, "8. Assessment Day", [None], "No decent coverage — the only 'Unit 3' review found (Emily's Study Guide) follows Project Stem's ordering, not Code.org's."),

(4, "1. Variables Explore", ["VBnvj8jiGro"], "Assignment, scope and tracing with pseudocode + MCQs; labelled AP topic 3.1, not Code.org U4L1."),
(4, "2. Variables Investigate", ["G6X4jByg41I"], "Works every Code.org level live, narrating each debugging fix."),
(4, "3. Variables Practice", ["2DLWC7DMPx0"], "Builds a small app with variables, explaining as it goes; 2020, but U4 numbering unchanged."),
(4, "4. Variables Make", ["kln8rMybTQE"], "Step-by-step app build; teaches wiring, but hands over the finished app."),
(4, "5. Conditionals Explore", ["Xor2E5v_RB4"], "Boolean logic and if/else built up with worked examples; current, AP topic 3.6."),
(4, "6. Conditionals Investigate", ["cmmc-h3347c"], "Dissects exam-style conditional problems, showing evaluation order and short-circuiting."),
(4, "7. Conditionals Practice", ["IsG4Xd6LlsM"], "Teaches if / else-if / else semantics by live coding; JS-general rather than App Lab."),
(4, "8. Conditionals Make", ["rTU79XM8V1Q"], "Builds the museum-ticket app, narrating each condition; largely demonstration."),
(4, "9. Functions Explore and Investigate", ["yPWQfa4CHbw"], "Official define-vs-call animation; predates parameters/return, so only half the lesson."),
(4, "10. Functions Practice", ["qRX1eio_HKE"], "Introduces return values in App Lab with small worked examples."),
(4, "11. Functions Make", ["T5mFiXHqTmo"], "Full build of the quote-maker app; explains reuse as it goes, but is a build-along."),
(4, "12. Project - Decision Maker App", ["ASE01GgeIdc"], "Builds a complete decision app explaining conditionals/functions; solution-oriented but reasoned."),
(4, "13. Assessment Day", [None], "No decent coverage — no Code.org-aligned Unit 4 assessment review exists; closest is Flavio's conditionals review (U4L6)."),

(5, "1. Learning from Data", ["QCtbWup8Bk4"], "Current Code.org-aligned walkthrough of finding questions/patterns in a dataset."),
(5, "2. Exploring One Column", ["fAIRGtC1yJE"], "Walks the bar-chart/one-variable analysis levels and reads the charts out loud."),
(5, "3. Filtering and Cleaning Data", ["vN0WY5MaDz4"], "Shows why dirty data misleads and performs the filtering/cleaning steps live."),
(5, "4. Exploring Two Columns", ["JSw3x0wYbog"], "Works crosstabs/scatterplots and explains association vs causation."),
(5, "5. Big, Open, and Crowdsourced Data", ["bAyrObl7TYE"], "Defines big data and its Vs; no open-data or crowdsourcing detail (lesson needs all three)."),
(5, "6. Machine Learning", [None], "No decent coverage — no AP-CSP-aligned, lesson-mapped explanation surfaced; general ML explainers skip the models-vs-training point the lesson makes."),
(5, "7. Algorithmic Bias", ["IJ8HwMCxbJA"], "Explicitly maps to Code.org Unit 5 Lesson 7 and explains bias sources with MCQs."),
(5, "8. Project - Tell a Data Story", ["JA7cPuCxjjw"], "Walks the project build and modelling decisions; current."),
(5, "9. Assessment Day", ["qu9J-EdsNAs"], "Exam-question walkthrough on data; pre-2024, but data content and skills are unchanged."),

(6, "1. Lists Explore", ["TTq40OoLoZs"], "Class lesson on list anatomy, indexing and mutation; matches current U6L1."),
(6, "2. Lists Investigate", ["gqKVHN22CRI"], "Full class recording working every level; thorough but 71 minutes."),
(6, "3. Lists Practice", ["2tAODBo3anU"], "Works the 'build a playlist' practice path live, explaining each step."),
(6, "4. Lists Make", ["z_OOZ2gaY-s"], "Answer-key walkthrough of the RemindMe app; shows finished code with limited reasoning. Old numbering: lists was U5."),
(6, "5. Loops Explore", ["G8hfAk4PfOM"], "Explains why loops exist with animation and a small App Lab demo; 2015 but still valid."),
(6, "6. Loops Investigate", ["9exT2oq8-fo"], "Shows for-loop mechanics (init/condition/update) in App Lab, step by step."),
(6, "7. Loops Practice", ["s9wW2PpJsmQ"], "Clear for/while semantics with live coding; JS-general, and older than your preference."),
(6, "8. Loops Make", ["B-yYUaC5GxE"], "Answer tutorial for the lock-screen app; demonstrates the finished solution."),
(6, "9. Traversals Explore", ["RQ6GJt9f2vg"], "Official explainer of traversing a list with a loop and index."),
(6, "10. Traversals Investigate", ["IvG_NXSMElc"], "Teacher-recorded walkthrough of the levels, narrating each iteration."),
(6, "11. Traversals Practice", ["d2u7l1_DJTw"], "Works practice problems while tracing loop iterations aloud."),
(6, "12. Traversals Make", ["pk32rysRQAg"], "Answer tutorial for the random-forecaster app; finished code shown."),
(6, "13. Project - Hackathon", ["ChYHvfktgCE"], "Complete example project end-to-end; demonstrates rather than teaching the design process."),
(6, "14. Assessment Day", ["SMmuT7Eccrg"], "Exam-style list/loop tracing with reasoning; pre-2024 but content unchanged."),

(7, "1. Parameters and Return Explore", ["1iAvhS8niM8"], "Explains parameter vs argument and return values with JS examples."),
(7, "2. Parameters and Return Investigate", ["s_8t69m7tcw"], "Shows the abstraction payoff of parameters inside App Lab."),
(7, "3. Parameters and Return Practice", ["8t-HxetA4ns"], "Answer tutorial for the practice levels; very little explanation."),
(7, "4. Parameters and Return Make", ["XFcgoBRHl-c"], "Class walkthrough building the RPS app with parameters and returns."),
(7, "5. Libraries Explore", ["JSo85ORXKqQ"], "Defines library vs program and why sharing code matters; C examples, not JS."),
(7, "6. Libraries Investigate", ["OJv3HeTP7fY"], "Official demo of importing and calling a library in App Lab."),
(7, "7. Libraries Practice", ["QkGytEFaFw0"], "Builds and shares a library with parameters/returns; concept plus demo."),
(7, "8. Project - Make a Library Part 1", ["1joEzBtosrY"], "Full-project answer tutorial; shows the finished library code."),
(7, "9. Project - Make a Library Part 2", [None], "No part-specific coverage — Kaiser's full-project tutorial covers part 2 but skips the planning/revision reasoning."),
(7, "10. Project - Make a Library Part 3", [None], "No part-specific coverage — same limitation as part 2."),
(7, "11. Assessment Day", [None], "No decent coverage — only single-level answer tutorials exist, no unit assessment review."),

(8, "1. Project - Innovation Simulation Part 1", ["4mj4BahsZwc"], "Explains the simulation roles and deliverables; old unit number (cyber was Unit 10 pre-2024)."),
(8, "2. Data Policies and Privacy", ["slyr4tmYPAU"], "Covers PII, data policies and why organisations collect data; old numbering U10L3."),
(8, "3. The Value of Privacy", ["nwOnJndyAeU"], "Weighs privacy trade-offs through exam questions; not lesson-specific."),
(8, "4. Project - Innovation Simulation Part 2", [None], "No decent coverage — no video addresses this project checkpoint."),
(8, "5. Security Risks Part 1", ["8wCTBWAAwvs"], "Current walkthrough of phishing and social-engineering attack patterns."),
(8, "6. Security Risks Part 2", ["6-nghp5Refc"], "Concise explanation of keylogging and rogue access points; very short."),
(8, "7. Project - Innovation Simulation Part 3", [None], "No decent coverage — no video addresses this project checkpoint."),
(8, "8. Protecting Data Part 1", ["6-JjHa-qLPk"], "Explains symmetric vs public-key encryption with a worked key exchange."),
(8, "9. Protecting Data Part 2", ["Xs2EEVs9wlQ"], "Covers encryption, certificates and authentication with 10 MCQs; thorough."),
(8, "10. Project - Innovation Simulation Part 4", [None], "No decent coverage — the final simulation deliverable has no video guide."),
(8, "11. Assessment Day", ["_Er2lyoY0vk"], "Current Big Idea 5 walkthrough (5.1–5.6) with benefit/harm reasoning; not Code.org-specific."),

(9, "1. Create PT Deep Dive", ["fY9gxDjXkBs"], "Explains every requirement and walks a full example, modelling planning decisions."),
(9, "2. Create PT - Make a Plan", ["MulQ7h1jgqc"], "Clarifies what the checklist actually requires before you code; no code shown."),
(9, "3. Create PT - Complete the Task", ["wMz4o3y68XA"], "Thinks aloud through a written-response example against the rubric."),
(9, "4. Create PT Written Response Mock Exam", ["2mGzsh9fu2o"], "Maps responses to the six rubric points; rubric-focused, thin on worked examples."),

(10, "1. Algorithms Solve Problems", ["Beh2SbRqtTU"], "Defines algorithm properties and works Code.org-style MCQs; current."),
(10, "2. Algorithm Efficiency", ["oq5zZjkTboo"], "Explains linear vs binary search reasoning through exam questions."),
(10, "3. Unreasonable Time", ["aPT9fOAXGSU"], "Explicitly walks Code.org Unit 10.3, then six practice MCQs."),
(10, "4. The Limits of Algorithms", ["O_FeCYdvFxs"], "Distinguishes decidable vs undecidable problems with clear examples."),
(10, "5. Parallel and Distributed Algorithms", ["o36O93rpCmk"], "Explains sequential/parallel/distributed trade-offs, then practice questions."),
(10, "6. Assessment Day", ["5Efa7wnDhKE"], "Exam walkthrough of algorithmic efficiency and undecidability; pre-2024 but mapping is stable."),
]

def esc(x):
    return str(x).replace("|", "\\|")

def fmt(s):
    return f"{s//60}:{s%60:02d}"

def video_cells(ids):
    if not ids or ids == [None]:
        return None
    vids = [meta[i] for i in ids]
    title = " / ".join(v["title"] for v in vids)
    ch = " / ".join(v["channel"] for v in vids)
    ln = " / ".join(fmt(v["lengthSeconds"]) for v in vids)
    dt = " / ".join(v["publishDate"][:10] for v in vids)
    url = " / ".join("https://youtu.be/" + v["id"] for v in vids)
    return title, ch, ln, dt, url

lines = []
lines.append("# AP CSP (csp-2025) — lesson-by-lesson YouTube map")
lines.append("")
lines.append("Built 2026-11-17. Lesson list confirmed against curriculum.code.org (csp-current → studio.code.org/courses/csp-2025), 10 units.")
lines.append("")
lines.append("| Unit | Lesson | Video | Channel | Length | Published | URL | Verdict |")
lines.append("|---|---|---|---|---|---|---|---|")
for unit, lesson, ids, verdict in ROWS:
    cells = video_cells(ids)
    if cells is None:
        lines.append(f"| {unit} | {esc(lesson)} | — | — | — | — | — | {esc(verdict)} |")
    else:
        t, c, l, dt, u = cells
        lines.append(f"| {unit} | {esc(lesson)} | {esc(t)} | {esc(c)} | {l} | {dt} | {u} | {esc(verdict)} |")

lines.append("")
lines.append("## Gaps worth knowing")
lines.append("")
lines.append("No decent coverage at all (9): U3 L8, U4 L13, U5 L6, U7 L9, U7 L10, U7 L11, U8 L4, U8 L7, U8 L10.")
lines.append("")
lines.append("Coverage exists but is answer-key/solution-forward rather than explanatory: U1 L3, U1 L12, U2 L7, U5 L5,")
lines.append("U6 L4, U6 L8, U6 L12, U6 L13, U7 L3, U7 L8.")
lines.append("")
lines.append("## Numbering: old vs current")
lines.append("")
lines.append("Units 1–4 kept their numbers; Units 5–10 were reordered for the 2024–25 course. A pre-2024 video labelled")
lines.append("Unit 5/6/7/8/9/10 is probably NOT the lesson with that number today:")
lines.append("")
lines.append("| Pre-2024 unit | Current unit |")
lines.append("|---|---|")
lines.append("| 5 – Lists, Loops, Traversals | 6 |")
lines.append("| 6 – Algorithms | 10 |")
lines.append("| 7 – Parameters, Return, Libraries | 7 (unchanged) |")
lines.append("| 8 – Create PT Prep | 9 |")
lines.append("| 9 – Data | 5 |")
lines.append("| 10 – Cybersecurity and Global Impacts | 8 |")
lines.append("")
lines.append("## Method and limits")
lines.append("")
lines.append("- Video metadata (title, channel, length, upload date, description) was pulled from YouTube on 17 Nov 2026.")
lines.append("- Verdicts are based on stated scope, format and description, not a full watch-through of every minute.")
lines.append("- 'Teaches logic' means the video explains/derives; 'shows a finished solution' means it hands over the answer.")
lines.append("- End-of-unit surveys and the two alternate-path lessons (U4 Lesson 7 alternate, U6 Lesson 3 alternate) are omitted.")

open("/Users/adrian/Desktop/APCSP/notes/csp-2025-video-map.md", "w").write("\n".join(lines) + "\n")
print("wrote", len(ROWS), "rows")
print("\n".join(lines[:8]))
