# Concept Explainer

Explain unfamiliar tools, commands, files, configs, architecture layers, and troubleshooting chains while still doing the user's task.

This skill turns important concepts into short knowledge cards:

```text
In one sentence
In this task
Remember this
Common mistake
Next time
```

It is useful when a user is working through a real task but lacks the mental model for parts of the workflow. For example:

- CLI, npm, package.json, environment variables, and access credentials
- APIs, databases, services, ports, logs, and error messages
- AI review, backend settlement, smart contracts, and responsibility boundaries
- Build, test, deployment, and local development commands

## Install

Copy this folder into your skills directory:

```bash
cp -R skills/concept-explainer ~/.codex/skills/
```

or:

```bash
cp -R skills/concept-explainer ~/.claude/skills/
```

## Example Prompt

```text
Help me use this CLI. I do not understand npm, package.json, access credentials, or where commands should be run. Explain the key parts as knowledge cards while you help me proceed.
```

## What Good Output Looks Like

The assistant should not stop at:

```text
Run npm install, then npm run dev.
```

It should also explain:

```text
Knowledge Card: npm
In one sentence: npm is the JavaScript project's toolbox.
In this task: it installs the tools this CLI needs and runs shortcuts from package.json.
Remember this: npm run xxx means "run the shortcut named xxx from package.json."
```
