# Contributing

Use English for the main guide. Keep corrections concrete and source-backed.

For a new claim, include a canonical URL, publication or event date with timezone, an original paraphrase and its evidence category. For a video, add the original publisher, a timecode, the transcript basis and any speaker-attribution uncertainty. Separate an author's reported experience from your inference and from a proposed adaptation.

Update `data/posts.json` or `data/videos.json` and the matching document. Preserve publication dates as publication dates. Do not count a reupload as a new event or describe a posted prompt as completed work. Keep outcome figures explicitly attributed and preserve unresolved discrepancies.

Run `python3 scripts/check.py` before submitting a change. This checks local links, structured records, timestamps and publication hygiene. It does not verify the truth of a claim or fetch external sites.

Do not add credentials, local account details, machine-specific paths, raw scraped text or third-party media. Keep working agreements small and preserve existing user files in setup examples.

Contributions to original repository material are made under the repository's MIT license.
