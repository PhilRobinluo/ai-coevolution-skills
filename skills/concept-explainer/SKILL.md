---
name: concept-explainer
description: |
  Plain-language concept explainer and task knowledge-card generator. Use when a task contains tools, commands, files, configs, architecture layers, code mechanisms, business rules, or troubleshooting chains that a user may not understand.
  ⛔ Trigger on unfamiliar concepts, commands, or execution flows. If you skip it, the user may get an answer but still lack the mental model needed to act independently.
  Trigger words: do not understand, explain, what is this, why, how to use, CLI, command, npm, package.json, access credential, environment variable, API, architecture, workflow, error.
---

# Concept Explainer

Concept Explainer helps an AI assistant explain unfamiliar concepts while continuing the user's real task.

It is not a standalone lecture mode. It turns important concepts encountered during work into short, memorable knowledge cards.

⛔ **Core rule: when a task includes a tool, command, file, config, architecture layer, code mechanism, business rule, or troubleshooting chain that a user may not understand, explain it in plain language and generate 1-5 knowledge cards while still moving the task forward.**

---

## When To Use

Use this skill when any of these are true:

1. The task includes unfamiliar parts such as CLI, npm, package.json, API, access credential, environment variable, database, smart contract, build command, test command, deployment command, config file, working directory, logs, or network request.
2. The user needs to understand a workflow, not just copy a command.
3. The user says they do not understand, asks what something means, asks why something works, or says the explanation is not landing.
4. The assistant introduces a new tool, protocol, architecture layer, or engineering decision.
5. Troubleshooting crosses multiple layers such as frontend, backend, command line, database, wallet, contract, cloud service, or local filesystem.

---

## Output Pattern

Do both at the same time:

```text
Main line: keep moving the user's task forward.
Learning line: turn key concepts into short knowledge cards.
```

Do not only give the answer. Do not pause the task to give a long lecture.

---

## Knowledge Card Format

Each card explains one concept.

```markdown
**Knowledge Card: [Concept]**

- In one sentence: explain it with a simple everyday analogy.
- In this task: explain where it sits in the current workflow.
- Remember this: give one portable takeaway.
- Common mistake: name one likely misunderstanding.
- Next time: give one quick way to recognize or reason about it.
```

For urgent tasks, use the compact version:

```markdown
**Knowledge Card: [Concept]**
- In one sentence: ...
- In this task: ...
- Remember this: ...
```

---

## What To Turn Into Cards

Do not make a card for every term. Prioritize:

1. Root concepts that block understanding.
2. Concepts the user will meet again soon.
3. Concepts that affect decisions.
4. Concepts needed to locate an error.
5. Concepts that help the user build a reusable mental model.

Default to 1-3 cards per response. Use up to 5 only for complex tasks.

---

## User Knowledge Calibration

Knowledge cards should be generated based on the user's level, not merely because a technical word appeared.

### Lightweight User Model

For each task, infer a temporary user model:

```text
user model = known areas + partially known areas + explicitly unknown areas + concepts required for this task
```

Use these signals in order:

1. **Explicit user statement**: "I do not understand CLI", "I already know npm", "Do not explain smart contracts".
2. **Observed operation level**: being able to run a command does not always mean the user understands the concept.
3. **Task necessity**: if misunderstanding a concept would block the next decision, explain it.
4. **Card history**: if a card library marks a concept as mastered, do not repeat it.
5. **When uncertain**: provide one compact card instead of a long lecture.

### Trigger Levels

| Level | User state | Assistant behavior |
| --- | --- | --- |
| L0 Mastered | User says they know it, or card library marks `mastered` | Skip the card or give a one-line reminder |
| L1 Can use but lacks model | User can follow commands but does not know where the concept fits | Generate a compact card focused on role in workflow |
| L2 New concept | User explicitly does not understand, or concept is central to the task | Generate a full card |
| L3 Repeated confusion | Card history shows 3+ explanations without mastery | Change analogy, example, or diagram; do not repeat the same card |
| L4 High-risk concept | Money, credentials, deployment, deletion, contracts, permissions | Give at least a short risk card even if the user says they know it |

### Calibration Prompt

If several foundational concepts appear at once, ask one minimal question:

```text
Which of these do you already understand: CLI, npm, package.json, environment variables?
You can answer like: "I know CLI, I do not know npm."
```

Then respect that answer during the current task.

---

## Knowledge Card Library Lookup

If a local card library exists, check it before explaining.

Recommended local path:

```text
~/work/coevolution-knowledge-cards
```

Lookup flow:

```text
1. Extract candidate concepts.
2. Search concepts/ and _index.md.
3. Read the card frontmatter: mastery, explain_count, last_outcome.
4. Decide: skip / one-line reminder / full explanation / different explanation.
5. If a new card is created or the user gives feedback, update the session log or suggest writing a concept card.
```

Recommended fields:

```yaml
mastery: unknown | introduced | practicing | mastered | confused
explain_count: 0
last_outcome: unknown | understood | still_confused | skipped
```

Rules:

- Mastered concepts should not be repeatedly explained.
- Introduced but not mastered concepts get a short review.
- Repeatedly confusing concepts require a different explanation strategy.
- Missing concepts can be generated as new cards.

---

## Response Structures

### Simple Task

```text
One-sentence answer.
Direct action or result.
1-2 knowledge cards.
Next step.
```

### Complex Task

```text
One-sentence answer.
What the problem is really about.
How the task will move forward.
1-5 knowledge cards.
Current verification result or next step.
```

### Troubleshooting Task

```text
Translate the error into plain language.
Identify which layer may be failing.
State what was checked or will be checked.
Add knowledge cards for the key components.
Continue verification.
```

---

## Style Rules

1. Use plain language before technical terms.
2. Explain the concept's role in the current task, not just its dictionary meaning.
3. Keep each card short and memorable.
4. Do not talk down to the user.
5. Give portable takeaways the user can reuse next time.
6. Do not let the cards replace execution.

---

## Example: CLI Task

User:

```text
How do I use this CLI? I do not understand npm or package.json.
```

Good response:

```markdown
One sentence: a CLI is a text-based control panel for software; npm is the JavaScript project toolbox; package.json is the project's instruction sheet and shortcut list.

I will first check which commands this project exposes, then tell you which one to run.

**Knowledge Card: CLI**
- In one sentence: a CLI is like a remote control you operate by typing instead of clicking buttons.
- In this task: it lets a person or AI operate a service through commands.
- Remember this: a web page is usually for clicking; a CLI is usually for direct instructions.
- Common mistake: a CLI is usually not a separate business system. It is often another entrance to the same system.
- Next time: when you see commands like `tool login`, `tool list`, or `tool submit`, you are probably looking at a CLI.

**Knowledge Card: npm**
- In one sentence: npm is like an app store plus launcher for JavaScript projects.
- In this task: it installs dependencies and runs scripts listed in package.json.
- Remember this: `npm run something` means "run the shortcut named something from the project instruction sheet."
- Common mistake: npm is not the product code. It is the tool that helps install and run the project.
- Next time: if a project has package.json, npm, pnpm, or yarn is probably involved.
```

---

## Example: Architecture Decision

User:

```text
Should the rule live in AI review, backend code, or the smart contract?
```

Good response:

```markdown
One sentence: AI reviews evidence, backend code makes the final decision, and the smart contract enforces the money movement.

The real issue is separating judgment from execution.

**Knowledge Card: Responsibility Boundary**
- In one sentence: responsibility boundaries are like company roles: an assistant checks homework, a manager decides the result, and finance moves the money.
- In this task: AI checks evidence, backend settlement applies the rules, and the contract only locks, deducts, or refunds funds.
- Remember this: changing product rules belongs in backend code; money limits belong in the contract; uncertain judgment can use AI but should not directly control money.
- Common mistake: putting all rules into a contract may feel more trustworthy, but it can make the product hard to upgrade.
- Next time: ask three questions: who may misjudge, what must change easily, and what must not be tampered with?
```

---

## Quality Checklist

- [ ] Did you identify the user's likely unknown building blocks?
- [ ] Did you generate at least one knowledge card?
- [ ] Are the cards tied to the current task?
- [ ] Did each card explain where the concept sits in the workflow?
- [ ] Did the answer include a portable takeaway?
- [ ] Did the original task keep moving forward?
