# Grok Bot Second Brain — Starter Kit

> **02UI** · free and MIT licensed.

A blank, ready-to-use second brain for **Grok Bot**. Download the folder, fill in three short files about yourself, and Grok can read, write, and organise everything inside.

Think of it as a helper that already knows who you are, what you do, and what you want. You set that up once. After that, every session starts with context.

## Start here

**Open `welcome.html` in your browser.** Double-click it — it opens like any web page and walks you through setup in about five minutes.

## Quick start

1. **Download** this folder (click the green Code button on GitHub, then Download ZIP) and unzip it somewhere permanent — your Documents folder, not Downloads.
2. **Double-click `welcome.html`** and follow the numbered steps on the page.
3. **Fill in your stack** — open `who-you-are.md`, `what-you-do.md`, and `what-you-want.md` in any text editor and replace the bracket prompts. Or tell Grok Bot: *help me set up my brain*.
4. **Double-click `index.html`** to see your brain in the browser.
5. **Add a note** — open `01-ideas/inbox.md`, type an idea, save, then close and re-open `index.html`.

## What is inside

```
grok-second-brain/
├── welcome.html          open this first — the full setup guide
├── index.html            your brain in the browser
├── README.md             you are here
├── grok.md               instructions Grok Bot reads every session
├── ONBOARDING.md         the one-time setup interview
├── brain-content.js      generated content for the index (rebuilt by sync.py)
├── sync.py               rebuilds brain-content.js from your .md files
├── who-you-are.md        who you are (blank prompts ready to fill)
├── what-you-do.md        what you do (blank prompts ready to fill)
├── what-you-want.md      what you want (blank prompts ready to fill)
├── 02ui/                 design system (fonts and colours)
├── 01-ideas/
│   └── inbox.md          dump raw thoughts here
├── 02-projects/          active work with a finish line
├── 03-areas/             ongoing responsibilities
├── 04-wiki/              evergreen knowledge
├── 05-resources/         reference material
└── 06-archive/           finished or paused work
```

The folders are numbered so they sort in the order you actually use them: capture an idea, turn it into work, keep it running, build up knowledge, then archive what is done.

## How the browser view works

Your notes live as `.md` files you can open in any text editor. The `index.html` page reads from `brain-content.js` so it works offline with no install step.

`brain-content.js` is **generated**. After any note changes, Grok Bot runs:

```
python3 sync.py
```

That rebuilds the file from your markdown, so the two can never drift apart and you never copy anything across by hand. Python 3 comes preinstalled on macOS and Linux — there is nothing to set up. You can run the same command yourself any time.

Close the browser tab and double-click `index.html` again to see the latest version.

## One rule before you start

Grok Bot is told to show you its plan before it deletes, moves, or overwrites anything it did not create. Your files stay on your computer. You are always in control.

## Licence

MIT. Use it, change it, share it, build on it. See `LICENSE`.

---

Made by **02UI**
