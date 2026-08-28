/**
 * Brain content for the HTML index.
 * Grok Bot: when you write or edit any .md file, update the matching entry here
 * so index.html shows the latest text after a browser refresh.
 */
window.BRAIN = {
  stack: [
    {
      id: "who-you-are",
      title: "Who you are",
      file: "who-you-are.md",
      section: "stack",
      content: `# Who you are

This file tells Grok Bot who it is working for. Grok reads it at the start of every session, so you stop re-explaining yourself.

> **Not filled in yet.** Tell Grok Bot "help me set up my brain" and it will ask you a few plain questions, or replace the prompts below yourself.

---

## The person

I'm [your name], a [what you do] based in [where].

[One line on your background. For example: just starting out, ten years in the trade, or learning something new.]

[How technical are you? Do you write code, or should Grok keep everything in plain language?]

## How I want Grok to work

[How should Grok talk to you? Short and direct, or more explanation? Patient or fast?]

---

A few honest sentences beat a polished paragraph. You can change any of this later — just edit this file or tell Grok Bot.`
    },
    {
      id: "what-you-do",
      title: "What you do",
      file: "what-you-do.md",
      section: "stack",
      content: `# What you do

Your day-to-day work, roles, and responsibilities. Grok uses this to give relevant answers instead of generic ones.

> **Not filled in yet.** Fill in the prompts below, or ask Grok Bot to help.

---

## My work

[What do you do for a living or as a main focus? One or two lines.]

[Side projects, hobbies, or things you spend serious time on?]

## Skills and tools

[What are you good at? What tools do you use every day?]

## What I'm working on right now

(This part goes stale fastest. Update it often.)

- [Whatever is actually on your plate this week or month.]

---

Keep it current. When your focus shifts, update this file.`
    },
    {
      id: "what-you-want",
      title: "What you want",
      file: "what-you-want.md",
      section: "stack",
      content: `# What you want

Your goals, priorities, and the direction you are heading. Grok reads this to help you make decisions that fit your life.

> **Not filled in yet.** Fill in the prompts below, or ask Grok Bot to help.

---

## Short-term (this month)

- [One thing you want to finish or start soon.]

## Longer-term (this year)

- [A bigger goal or direction you care about.]

## What success looks like

[When this brain is working well for you, what changes? Less stress? More ideas captured? Better writing?]

---

Goals change. That is normal. Edit this file whenever your priorities shift.`
    }
  ],
  notes: [
    {
      id: "inbox",
      title: "Inbox",
      file: "01-ideas/inbox.md",
      folder: "01-ideas",
      section: "notes",
      content: `# Inbox

Drop raw thoughts here. Messy is fine. Speed matters more than neatness.

When the inbox fills up, ask Grok Bot to sort your ideas into the right folders.

---

- [Your first idea goes here]`
    }
  ],
  folders: [
    { id: "01-ideas", label: "01-ideas", description: "Raw thoughts and quick captures" },
    { id: "02-projects", label: "02-projects", description: "Active work with a finish line" },
    { id: "03-areas", label: "03-areas", description: "Ongoing responsibilities" },
    { id: "04-wiki", label: "04-wiki", description: "Evergreen knowledge you look things up in" },
    { id: "05-resources", label: "05-resources", description: "Reference material you collect" },
    { id: "06-archive", label: "06-archive", description: "Finished or paused work" }
  ]
};
