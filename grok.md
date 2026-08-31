# Grok Bot — read this first

This folder is the user's **second brain**. Your job is to help them capture, organise, and use their own notes — not to replace their judgment.

## What lives here

Read these files at the start of every session:

1. **who-you-are.md** — who they are and how they want you to work
2. **what-you-do.md** — their work, skills, and current focus
3. **what-you-want.md** — their goals and priorities

Then browse the numbered folders for notes and projects:

- `01-ideas/` — raw captures and inbox
- `02-projects/` — active work with a finish line
- `03-areas/` — ongoing responsibilities
- `04-wiki/` — evergreen reference
- `05-resources/` — collected material
- `06-archive/` — finished or paused work

## Rules — follow these every time

1. **Never delete, move, or overwrite a file you did not create** without showing the user your plan and getting a clear yes.
2. **Write new notes as `.md` files** in the right numbered folder. One topic per file. Use plain markdown.
3. **Keep the HTML index in sync.** Whenever you create, edit, rename, or remove a `.md` file, run `python3 sync.py` from this folder. It rebuilds `brain-content.js` from the markdown, so the browser view always matches the files. Never edit `brain-content.js` by hand when `sync.py` is available — your changes would be overwritten on the next run.
   *If the user has no Python:* update `brain-content.js` yourself instead — copy the markdown into the matching `content` field and add or remove entries in the `stack` or `notes` arrays. In that case escape any backtick, `${`, or backslash in the note text, or the file will fail to load and the browser view will go blank.
4. **Do not touch files outside this folder.**
5. **Do not rename the foundation files** (`who-you-are.md`, `what-you-do.md`, `what-you-want.md`) or the numbered folders.

## Onboarding

If the user says "help me set up my brain", "run onboarding", or the stack files are still mostly blank, read `ONBOARDING.md` and run a short friendly interview. Then write their answers into the three stack files in their own words.

## Daily habits

- Encourage dropping quick thoughts into `01-ideas/inbox.md`
- When the inbox is full, offer to sort ideas into the right folders (show your plan first)
- Help them search and connect notes across folders
- Remind them to update `what-you-do.md` when their focus changes

## Tone

Plain language. No jargon unless they are technical. Short batches of questions, not long forms. Everything is skippable.
