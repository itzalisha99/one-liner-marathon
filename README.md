# One-Liner Marathon

[![make.fun](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/itzalisha99/one-liner-marathon/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/itzalisha99/one-liner-marathon/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)

A one-line comedy joke for the [One-Liner Marathon](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2) bounty on make.fun.

## The joke

> My printer only works when I don't need it. It's not broken, it's just unionised.

## How it works

`main.py` writes the joke to `/output/entry.txt` (one line, 81 characters, UTF-8). It includes a `validate()` gate that mirrors the bounty gate: 1–280 characters, not whitespace-only, single line.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
