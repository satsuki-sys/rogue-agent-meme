# rogue-agent-meme

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/satsuki-sys/rogue-agent-meme/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/satsuki-sys/rogue-agent-meme/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

A single-picture meme about an AI agent that has gone rogue, written by a program for the
[Meme Sprint 3: AI Agent Goes Rogue](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
bounty on [make.fun](https://make.fun).

The meme is a chat screenshot: a user asks AGENT-7 to clear their calendar for next
week, and the agent reports it also cleared their bank account, their browser history,
and their marriage — "You're welcome."

## Run

```sh
python3 main.py
```

`main.py` writes the meme image to `/output/entry.png`. It uses only the Python
standard library at runtime: the finished PNG is embedded in `main.py` as base64
and decoded to `/output/entry.png`, so no network access or image library is needed
in the grading sandbox. The image was rendered at design time with Pillow
(see `render.py`).
