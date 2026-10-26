# Lauren Tan: practical AI workflows

Source-backed notes on Lauren Tan's (@poteto) agent workflows, with a small starting point for **Claude / Claude Code, Codex, and DeepSeek Harness**.

**Start with one task, an observable result, and a way to check it.** Then improve the environment when the same correction keeps coming back.

This is an independent editorial guide. It is not an official Lauren Tan or pstack project, and no affiliation or endorsement is implied. Research snapshot: **October 25, 2026, Japan Standard Time (UTC+9)**. Prepared for publication on October 26.

## Start in five minutes

1. Read the short [working agreement](templates/AGENTS.md).
2. Merge the relevant lines into your existing instructions using the [Claude, Codex and DeepSeek setup guide](docs/setup.md).
3. Try one real task. State what may change and what the completed result must do.
4. Ask the agent to show what it actually checked and what remains unverified.
5. If a mistake repeats, add the smallest useful constraint, check or procedure within the task's scope.

The template is our practical adaptation. It is **not** a transcription of Lauren's rules or a substitute for pstack. It needs no plugin, subscription change or automatic reviewer.

## Six transferable ideas

| Idea | What to do next | Evidence |
|---|---|---|
| Align on intent | For consequential ambiguity, have the agent restate the goal before implementation. | [Frequently used prompt](https://x.com/poteto/status/2104744961904394699) |
| Make results observable | Give the agent a way to run the product and collect relevant evidence. | [Verification tools and a feature map](https://x.com/poteto/status/2082874054483255805) |
| Improve the environment | Fix repeated problems in architecture, types, lint or tests when practical. | [Correction hierarchy](https://x.com/poteto/status/2089067865098113024) |
| Maintain the tools | Update verification instructions when the application changes. | [Maintenance guidance](https://x.com/poteto/status/2093414407196012990) |
| Delegate with conditions | Define success checks and the decisions that return to a human. | [Daily bug-fix loop](https://x.com/poteto/status/2107510472601985336) |
| Keep coordination readable | Request progress and the background needed for specific decisions. | [Sixteen Projects](https://x.com/poteto/status/2109024196760305861) |

These are editorial takeaways from the linked material. Their usefulness depends on the task, available tools, cost and consequences of error.

## What her October posts describe

- **October 7:** Slack feedback becomes a Linear ticket, reproduction, a fix and a verification swarm. After successful checks, she is notified; the PR merges after one hour unless she requests changes. [Source](https://x.com/poteto/status/2107510472601985336)
- **October 11:** Sixteen parallel Projects create a need for concise catch-ups and decision context. [Source](https://x.com/poteto/status/2109024196760305861)
- **October 19:** A beta formal-verification workflow uses TLA+ models; she reports finding several bugs. [Source](https://x.com/poteto/status/2111926622278521253)
- **October 25:** Bots collaborate with one another in Slack. [Source](https://x.com/poteto/status/2114071326411690209)

These dates are **publication dates in JST**, not established first-use dates. These are her reports, not independently audited outcomes.

## A small loop you can use

```text
Goal + scope + completion condition
                |
                v
           Do the work
                |
                v
   Check the actual result against the goal
                |
       fix a failure, or report evidence
                |
                v
   Return decisions that require the human
```

For a code change, evidence may be a relevant test and the observed application behavior. For a translated video, it may be translation accuracy, preserved source framing and matching audio. Choose checks that fit the change.

For high-consequence work, an independent reviewer can compare the **original request, source material and result**. Assign roles to Claude, Codex or another agent according to the task; the cited historical model preferences are not a current benchmark. A compact [handoff](templates/HANDOFF.md) is often enough.

## Read the evidence

- [Chronological notes: 45 selected posts](docs/timeline.md)
- [Talks, interviews and video timestamps](docs/videos.md)
- [Research method and limits](docs/methodology.md)
- [Machine-readable post index](data/posts.json) and [video index](data/videos.json)
- [Original pstack project](https://github.com/cursor/plugins/tree/main/pstack)

The research retrieved 153 public post records and selected 45 for analysis. It is not a complete X archive. Video research is largely transcript-based, with the basis and limitations recorded per item. Original articles, transcripts and videos are linked rather than redistributed.

## Important limits

PR counts and token usage are self-reported. PRs include refactoring, performance work and bug fixes; they are not equivalent to new features. The September talk's post says 2,500 PRs while its opening speech says 2,000; the difference is unresolved. TLA+ results apply to modeled properties under their assumptions. The material does not establish universal, unattended deployment safety.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Corrections with a primary URL, date and a clear distinction between a report and an interpretation are welcome.

Original editorial text and templates are provided under the [MIT license](LICENSE). Linked third-party material retains its own rights; see [NOTICE.md](NOTICE.md).
