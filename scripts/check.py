"""Validate local publication files without network calls or dependencies."""
import datetime as dt
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


post_index = json.loads((ROOT / 'data/posts.json').read_text())
posts = post_index['posts']
videos = json.loads((ROOT / 'data/videos.json').read_text())['video_groups']
timeline = (ROOT / 'docs/timeline.md').read_text()
video_doc = (ROOT / 'docs/videos.md').read_text()
check(len(posts) == post_index['curated_post_count'], 'Curated count differs')
check(len(posts) <= post_index['retrieved_post_count'], 'Selection exceeds retrieval count')
check(len({p['id'] for p in posts}) == len(posts), 'Duplicate post IDs')
check(len({v['id'] for v in videos}) == len(videos), 'Duplicate video IDs')
allowed_types = {
    'tool_design', 'opinion', 'role_preference', 'self_report', 'advice',
    'retrospective', 'published_prompt', 'long_form_explanation', 'linked_talk',
    'daily_workflow', 'public_instruction', 'personal_policy',
    'release_announcement', 'experimental_report', 'illustrative_example',
    'work_in_progress',
}
previous = None
for p in posts:
    check(p['url'] == f"https://x.com/poteto/status/{p['id']}", f"Bad canonical URL: {p['id']}")
    utc = dt.datetime.fromisoformat(p['published_at_utc'])
    jst = dt.datetime.fromisoformat(p['published_at_jst'])
    check(utc.utcoffset() == dt.timedelta(0), f"Not UTC: {p['id']}")
    check(jst.utcoffset() == dt.timedelta(hours=9), f"Not JST: {p['id']}")
    check(utc == jst, f"Time conversion differs: {p['id']}")
    check(previous is None or utc >= previous, f"Out of order: {p['id']}")
    previous = utc
    check(p['evidence_type'] in allowed_types, f"Unknown evidence type: {p['id']}")
    check(p['url'] in timeline, f"Timeline source missing: {p['id']}")
    check(jst.strftime('%Y-%m-%d %H:%M') in timeline, f"Timeline date missing: {p['id']}")
    check(bool(p['reported_content']) and bool(p['editorial_interpretation']), f"Unseparated analysis: {p['id']}")
for v in videos:
    check(v['url'] in video_doc, f"Video absent from guide: {v['id']}")
    check(bool(v['basis']) and bool(v['limits']), f"Missing provenance: {v['id']}")
    for passage in v['passages']:
        check(passage['seconds'] >= 0, f"Negative offset: {v['id']}")
        check(passage['url'] in video_doc, f"Missing passage link: {v['id']}")

private_patterns = [
    r'/Users/[A-Za-z0-9._-]+/', r'http://(?:127\.0\.0\.1|localhost)',
    r'\bgh[pousr]_[A-Za-z0-9]{20,}', r'\bgithub_pat_[A-Za-z0-9_]{20,}',
    r'\bsk-[A-Za-z0-9_-]{20,}', r'-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----',
]
files = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts]
for path in files:
    rel = path.relative_to(ROOT)
    check(not path.is_symlink(), f"Repository contains symlink: {rel}")
    check(path.suffix.lower() not in {'.mp4', '.mov', '.mp3', '.wav', '.srt', '.vtt', '.png', '.jpg'}, f"Unexpected source media: {rel}")
    check(path.stat().st_size < 1_000_000, f"Unexpectedly large file: {rel}")
    content = path.read_text()
    for pattern in private_patterns:
        check(re.search(pattern, content) is None, f"Possible private data in {rel}")
    if path.suffix == '.md':
        for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', content):
            parsed = urlparse(target)
            if parsed.scheme or target.startswith('#'):
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            check(destination.is_relative_to(ROOT), f"Link leaves repository: {rel}: {target}")
            check(destination.exists(), f"Broken local link: {rel}: {target}")

for prefix in ['', 'templates/']:
    check((ROOT / prefix / 'CLAUDE.md').read_text().strip() == '@AGENTS.md', f"Claude import differs in {prefix}")
    check((ROOT / prefix / 'AGENTS.md').is_file(), f"Claude import target missing in {prefix}")

if errors:
    raise SystemExit('\n'.join(f'FAIL: {e}' for e in errors))
print(f'PASS: {len(posts)} post records, {len(videos)} video groups, {len(files)} publication files.')
print('PASS: timestamps, evidence fields, local links, Claude imports and publication hygiene.')
print('External URL availability and factual truth require source review; no network checks were run.')
