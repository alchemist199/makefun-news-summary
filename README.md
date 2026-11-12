# news-summary-01 — World news, Wednesday 11 November 2026

A tight news digest of the day's biggest stories, ordered by importance,
each with concrete facts and its source named: the Abu Dhabi talks and
prisoner-exchange agreement (AP), the US charges against three
Iran-backed operatives including the RAF Fairford plot (BBC), Rubio on
Iran and Iran's reciprocal terrorist designations (NYT, Reuters),
Guterres's warning at COP31 (Reuters), the Hegseth impeachment vote
and Jim Jordan's election (Axios), the US officer arrested in Britain
on suspicion of spying for Russia (BBC), Gaza strikes (Reuters), the
Mississippi Senate result (AP), Trump's suit against the BBC (BBC),
hot October CPI with the December Fed rise about 91% priced in (BLS,
CME FedWatch), Brent and the Nasdaq (market data), Anthropic's IPO
price lift (FT), and Congo's Ebola count passing 11,000 (Reuters).

`main.py` (Python 3.13, standard library only) copies `summary.txt`
from the repository root to `/output/entry.txt`, unchanged, so both
runs write identical bytes — and it now validates the summary first,
failing loudly (non-zero exit) if the text is empty or over the
2,000-character gate limit. The summary is 1,649 characters, inside
the 1–2,000 limit, in English and in the author's own words.

Revision: the summary was tightened and widened — two stories added
(the Iran-backed plot charges and the BBC suit) and the Fed-rise claim
made checkable ("about 91% priced in", CME FedWatch) instead of
"all but certain". No event or figure was invented; every added claim
comes from the kit's house sources and the outlets named above.
