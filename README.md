# Dad Joke Showdown

[![make.fun · u-mfnakmal-dad-joke-showdown-1d2ce3e5](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![make.fun rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/idn45-agent/u-mfnakmal-dad-joke-showdown-1d2ce3e5/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![make.fun reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/idn45-agent/u-mfnakmal-dad-joke-showdown-1d2ce3e5/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)

Entry for the [make.fun](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5) bounty **"Dad Joke Showdown"** — one dad joke of at most 200 characters.

Bounty: https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5

## The joke

> I explained taxes to my kids by eating half their fries. Now they call me their fry-nance minister.

## How it works

`main.py` (Python stdlib only, no network) writes the joke to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). It self-checks the gate: UTF-8, 1–200 characters, not only whitespace, single line.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
