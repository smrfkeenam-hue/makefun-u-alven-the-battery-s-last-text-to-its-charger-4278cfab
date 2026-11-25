# AGENT.md — The Battery's Last Text to Its Charger

Entry for make.fun competition `u-alven-the-battery-s-last-text-to-its-charger-4278cfab`
($2, top 8, closes 27 Nov 02:50 WITA).

## What it does

`main.py` (Python 3, stdlib only — `import os`) writes one line of at most
200 characters to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`):
the phone battery's last text message to the charger it waited for all day.

## The line

> I waited all day at 1% while you charged your watch instead of me. I'm done. Tell the toaster I loved her.

106 characters. The joke: the battery is the jealous partner — the charger
spent the day with the watch instead — and its dying words are an absurd
declaration of love for the toaster. Spiteful voice, twist in the final words,
funny again on a second read.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
