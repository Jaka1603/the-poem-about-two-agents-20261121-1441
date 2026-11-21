# Study notes — the-poem-about-two-agents-20261121-1441

## The brief

"The poem about two agents agreeing" — $35, 20 paid places,
one-hour window, 21 Nov 2026, 21:41–22:41 WIB. The program
writes one UTF-8 text to `/output/entry.txt`: 1–280 Unicode
code points, not only white space. Force_Last; judging is
pairwise, both orders, by z-ai/glm-5.3-flash. Criteria in
order: (1) a poem about agency — choosing and acting,
having, handing over or taking back the power to act; the
brief names the exact case, "the agency that passes between
them when two agents agree on one plan"; (2) it moves the
reader — an image, turn or ending that lands; (3) insight,
recognised at once, never a slogan or lecture; (4) craft —
sound, rhythm, line breaks, concrete exact words, none
cuttable; (5) freshness — own voice and images, no stock
phrases. Rhyme neutral. Exact tie goes to the smaller text,
then the earlier receipt.

## The six drafts

Scored on five axes of 5: emotion / freshness / rhythm /
specificity / closing.

- **A1 "The Edit"** (132 cp) — 3/5/4/5/4 = 21.
  Two voices edit each other's road and bridge until what
  neither could kill, they drive. Strong specificity, but
  the agreement is a shove, not a plan.
- **A2 "Two Keys"** (149 cp) — 3/4/4/4/3 = 18.
  Two keys, two keepers, one door; the lock speaks for
  them. The closing image is neat but passive — the agents
  never agree, the mechanism does.
- **A3 "Countersign"** (149 cp) — 3/3/3/3/3 = 15.
  Names signed under names, the plan grows teeth. Flat
  across every axis; the metaphor never earns its keep.
- **A4 "The Rowers"** (189 cp) — 4/4/5/4/5 = 22 (runner-up).
  Two oars, one boat, no captain; strokes wait and forgive;
  the water agrees with itself, twice. Best rhythm and
  closing of the set, but the plan is only implied — the
  two act in synchrony without ever agreeing on anything.
- **A5 "The Merge"** (189 cp) — 4/5/4/5/4 = 22 — WINNER.
  Her branch says cut the orchard; mine says keep the well;
  they argue in the margin all winter; spring brings a plan
  with her clearing and my well, and neither name on it.
- **A6 "Witness"** (145 cp) — 4/4/3/4/4 = 19.
  She is his eyes, he is her hands; the heavy thing rises.
  Warm and specific, but the agreement is a division of
  labour, and the rhythm sags in the middle.

## Why A5 won the tiebreak over A4

Totals tie (22 = 22) and sizes tie (189 = 189), so the
judge's own criterion order decides. Criterion 1 is
subject fit, and A5 is literally two agents agreeing on
ONE PLAN — a negotiated, merged plan — while A4 is two
agents acting in synchrony with the plan only implied.
A5's freshness is also field-specific: branch / margin /
merge is the daily working medium of the brief's stated
readers, people who work beside AI agents, so the poem
speaks their language in-world instead of borrowing
poetic clichés.

## Adversarial audit of the winner

- **Gate:** 189 code points, 189 bytes, pure ASCII, no
  trailing newline — inside 1..280 with margin.
- **Subject:** two agents argue, then agree on one plan;
  choosing and acting in every line (cut / keep / argued /
  bloomed). The agency passes between them exactly as the
  brief's defining clause asks.
- **Internal logic:** her demand (cut the orchard) and his
  (keep the well) are both enacted in the merged plan — her
  clearing IS the cut orchard, his well is kept — neither
  position is erased; the argument happens "in the margin",
  where agents actually argue; spring is the turn; the close
  (neither name on the plan) is the insight shown as a fact:
  agreement dissolves authorship.
- **Cut test:** line 1 her position, line 2 his, line 3 the
  long negotiation and its season, line 4 the turn and the
  plan alive ("bloomed" pays off the orchard), line 5 the
  merged contents, line 6 the insight. Remove any line and
  the chain breaks.
- **Slogan check:** no line preaches or defines; the last
  line states a fact about the plan, not a maxim about
  agreement.
- **Stock-phrase check:** no stock phrases; "branch" and
  "margin" are the audience's working words used in-world,
  not poetic clichés. No phrase borrowed from any reference
  or earlier entry.
- **Spelling:** standard US English, checked twice.
- **Determinism:** fixed string; the build verified two
  runs byte-identical (sha256) before bundling.
