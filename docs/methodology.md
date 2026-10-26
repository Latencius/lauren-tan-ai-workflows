# Method and limits

## Scope

Research cutoff: **2026-10-25 JST**. The repository was prepared on 2026-10-26. This is a dated snapshot, not a live feed.

The earlier research collected 153 public records attributed to @poteto and selected 45 relevant posts. The published index contains those 45 original editorial paraphrases and canonical links. It omits raw post bodies, original article text, transcripts, images, videos, local machine paths and account configuration.

## How posts were checked

The X web endpoint returned HTTP 403. Search results, ten public timeline-mirror pages and a [third-party link index](https://ythx-101.github.io/lauren-tan-ai/index.html) supplied candidates. Public FxTwitter post records supplied author, text and timestamp metadata; canonical X URLs were retained. The link index was used for discovery, not as the authority for the summaries.

This is mirror-assisted research. It does not establish that every post remains unchanged or publicly reachable today, and it is not an exhaustive account history. Posts after the cutoff, protected content, deleted material and unindexed replies may be absent. A URL check alone does not validate a factual claim.

## Dates

The post index preserves UTC and JST timestamps. Dates refer to publication, not necessarily first use or the date of the described event. Video entries distinguish event, broadcast, publication and reupload dates. Video timecodes are elapsed positions, not wall-clock timestamps.

## Evidence labels

- `self_report` and `daily_workflow`: what the author says she does; not an independently audited outcome.
- `advice`, `opinion`, `role_preference` and `personal_policy`: a recommendation, view or stated personal boundary, not a demonstrated implementation.
- `tool_design`, `release_announcement` and `work_in_progress`: a described design or development state.
- `published_prompt` and `public_instruction`: what was requested, without assuming it completed.
- `retrospective` and `long_form_explanation`: explanations that may describe earlier events.
- `experimental_report`: a reported experiment under its conditions.
- `illustrative_example`: an explicitly hypothetical example.
- `linked_talk`: a post linking a talk, with video research recorded separately.

The `reported_content` field paraphrases the source. `editorial_interpretation` is the maintainer's analysis. The templates and setup recipe are also editorial adaptations, not statements by Lauren.

## Video research

See [the video guide](videos.md) for the basis of each entry. The research used official or creator transcripts where available, and identified secondary transcripts where necessary. It did not continuously watch every recording. Galaxy passages were located by searching all three day transcripts; the archive lacks speaker labels, so attribution from surrounding screen-handoff dialogue is less certain.

Reuploads and edited compilations are not separate interviews. Some 2026 uploads combine the 2025 React Conf answer with a later workshop. Peter Yang's interview has two guests: examples belonging to Peng Zheng are not attributed to Lauren. The MTS interview has metadata-level confirmation only and is not used for detailed new workflow claims.

## What the evidence does not establish

There is no independent audit here of PR totals, token use, defect rates, revenue or comparative model quality. The September talk's 2,500-versus-2,000 PR discrepancy remains unresolved. Some posts discuss human review for critical areas; later descriptions of agent merges should not be generalized to every area and every time. Formal verification checks modeled properties and assumptions, not an entire product by implication.

For the shared-instructions adaptation, the installed DeepSeek instruction loader was exercised in three workspaces and read the shared file through its filesystem provider without a model request. Codex instruction-file loading was checked against official guidance and the local configuration. Claude setup is documented from its official memory guide; no live Claude execution was performed for this repository. File-loading evidence is not a behavioral success rate.

## Correcting this guide

Provide the canonical source, a precise timestamp or passage, the relevant timezone and the wording to correct. Update the structured index and the corresponding human-readable note together. See [CONTRIBUTING.md](../CONTRIBUTING.md).
