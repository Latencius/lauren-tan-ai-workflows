# Use the same agreement with Claude, Codex and DeepSeek

The [working agreement](../templates/AGENTS.md) is an original, portable adaptation of the lessons in this guide. Review it and merge the useful parts into existing instructions. The table below uses each tool's conventional instruction entry point.

| Tool | Project instructions | User-wide instructions | Primary documentation |
|---|---|---|---|
| Claude Code | `CLAUDE.md` importing `@AGENTS.md`, or the supported direct `AGENTS.md` mode | `~/.claude/CLAUDE.md` | [Claude Code memory](https://code.claude.com/docs/en/memory) |
| Codex | `AGENTS.md` | `~/.codex/AGENTS.md` | [Codex instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md) |
| DeepSeek Harness | `AGENTS.md` with the instruction loader enabled | `$DSH_HOME/AGENTS.md`, normally `~/.dsh/AGENTS.md` | [Harness instruction loader](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/context/agent-instructions/README.md) |

## Start with one tool

**Claude Code:** merge the template into an existing project `CLAUDE.md`. Alternatively, keep it as project `AGENTS.md` and use a neighboring `CLAUDE.md` containing `@AGENTS.md`, as demonstrated by the [two template files](../templates/CLAUDE.md). Claude Code also has direct AGENTS.md support, whose availability and precedence depend on version and settings. The explicit import is a documented compatibility path. Start a new session and inspect `/memory`.

**Codex:** merge the template into project `AGENTS.md`, or use the user-wide location for personal defaults. `AGENTS.override.md` can take precedence. More specific project instructions can refine global guidance. Start a new session and check the loaded instructions.

**DeepSeek Harness:** merge the template into the project file or harness-home file. Loading requires `dsh-agent-instructions` and a filesystem provider. The local check for this guide used version `0.2.0-rc.2`; custom profiles can disable the loader. Start a new chat or resume through the supported reconciliation path. Merely refreshing a browser page is not proof that new guidance entered an existing model context.

## Optional: one user-wide file for all three

For a local Unix-like setup, use one ordinary file as the source of truth, such as `~/.config/ai-workflows/AGENTS.md`. From this repository's root, save the reviewed agreement without replacing an existing file:

```sh
mkdir -p "$HOME/.config/ai-workflows"
cp -n templates/AGENTS.md "$HOME/.config/ai-workflows/AGENTS.md"
```

If the source already exists, review and merge it. Then create links at each tool's user-wide entry point **only when that entry does not already exist**:

```sh
mkdir -p "$HOME/.claude" "$HOME/.codex" "$HOME/.dsh"
ln -s "$HOME/.config/ai-workflows/AGENTS.md" "$HOME/.claude/CLAUDE.md"
ln -s "$HOME/.config/ai-workflows/AGENTS.md" "$HOME/.codex/AGENTS.md"
ln -s "$HOME/.config/ai-workflows/AGENTS.md" "$HOME/.dsh/AGENTS.md"
```

The commands intentionally omit force flags. Existing files or links must be reviewed and merged before changing how they are loaded. First confirm that the shared source file exists. Custom `CODEX_HOME` or `DSH_HOME` values require matching target locations. This example concerns local coding-agent sessions; Claude Cowork documents restrictions on user-level links and imports outside its working directory.

Plain files and native loading keep dependencies and duplicated edits small. These instructions are guidance to a model; they do not create a security boundary or guarantee compliance.

## Claude in an ordinary chat

Paste the reviewed agreement into the conversation or an instruction field supported by the client, then describe the task. A Markdown filename alone does not make a chat client read your disk. Include the source material and the acceptance conditions needed for that task.

For example:

```text
Add Japanese subtitles to the supplied video.
Preserve the source framing, original audio and requested duration.
Check the translation and subtitle placement. Report any uncertain wording.
```

## Use another agent when the work warrants it

The authoring agent receives the task and creates the result. A reviewer receives the original task, source and result and checks only the relevant acceptance conditions. Reconcile concrete findings and preserve the task scope. Use [HANDOFF.md](../templates/HANDOFF.md) if work moves between tools.

This is an editorial operating pattern. No automatic cross-provider agent connection or model-quality comparison is implemented by these templates.
