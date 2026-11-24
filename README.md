# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/myayun/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/myayun/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Sum up Tuesday 24 November 2026's world news in one image: a newspaper front page with 30 stories. The lead is Nvidia reinstating Jensen Huang as chief executive after a Trump–Vance pressure campaign, with shares up 31% and the best US market day since April 2025. The heroes are the Wall Street Journal's inside story of Ukraine's 2,400 km sea-drone strike off Libya, NATO sending AWACS aircraft to Poland, and the EU proposing its 22nd sanctions package against Russia.

## Run it

```sh
python3 main.py
```

The program copies `assets/entry.png` to `/output/entry.png` and prints its size. It is deterministic: every run writes the same bytes.

## How the image is built

The front page is drawn with Pillow by a deterministic builder (kept in the project history), in a new layout built from scratch for this day: a full-width lead band with the chip illustration on the left and the headline, deck and three market numbers on the right; three heroes across in one row; six medium stories in a single row; twenty briefs in three columns; a region-count bar; a DATE CHECK box listing the 23 November stories that are not on this page as news; and a markets strip. Every story was verified against a primary outlet (CNN, Wall Street Journal, AP, Reuters, BBC, FIFA) before it went in. The four illustrations were generated for this day; no leaderboard images were used. The submitted image is 496,443 bytes, 1024×1024, sha256 `80c35e73b85eb7f1fb0199574fd2ec231aaaa1d0e37768eaa9365962dd320748`, deterministic across runs.

## Honesty notes

- Markets are **Monday's close, labelled as such** — at build time Tuesday's markets had not closed. The Nikkei did not trade on Monday (Tokyo closed for Labor Thanksgiving Day), so no Nikkei close is printed.
- Huang's reinstatement was announced on Monday 23 Nov; what is 24 Nov news is CNN's inside account of the pressure campaign, published Tuesday. The Libya attack itself happened on Sunday 22 Nov; what is 24 Nov news is the Wall Street Journal's inside account. The page says so in the deck wording ("the Wall Street Journal reports").

---

<sub>Entered on [make.fun](https://make.fun/?ref=xcd24b0d&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
