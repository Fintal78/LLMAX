# Codebase Concerns

**Analysis Date:** 2026-06-04

## Tech Debt

**Incomplete Normalizer Methods:**
- Issue: Several helper methods in the normalizer are skeleton wrappers or return basic unparsed string blocks.
- Files: `src/normalizer.py` (`_parse_date`, `_parse_camera`, `_extract_ram`)
- Why: Rapid initialization phase.
- Impact: Key fields are stored as unparsed raw text, making calculations in subsequent pipeline steps fragile or overly manual.
- Fix approach: Implement robust regex patterns and dictionary lookups to parse RAM capacities, camera modules, and date strings.

**Hardcoded Architecture Scores:**
- Issue: Arrays mapping processor components to integer scores are duplicated/defined directly in scoring code.
- Files: `src/battery_score_single_test.py` (`CPU_SCORES`, `GPU_SCORES`, `OS_SKIN_SCORES`)
- Why: Simplifies standalone calculations without requiring an external DB setup.
- Impact: Adding support for a new processor requires modifying source code in multiple places, raising regression risks.
- Fix approach: Move these reference lookup lists to a central database file or config sheet (e.g., `data/schema.json` or `docs/scoring_constants.md`).

## Known Bugs

**JSON Parsing of Markdown Blocks:**
- Symptoms: Occasional `JSONDecodeError` when reading JSON blocks embedded inside markdown files.
- Trigger: Complex comments or trailing commas that bypass clean regex regexes inside scoring script.
- Files: `src/battery_score_single_test.py` (line ~680)
- Workaround: Manually clean target markdown code block JSON fields.
- Root cause: Regex cleanup utility fails on specific structures (such as nested arrays/objects containing comments).

## Security Considerations

**Target IP Blocking:**
- Risk: Target site (GSMArena) blocks scraper IP due to automated traffic.
- Files: `src/scraper.py`
- Current mitigation: Standard user-agent headers and standard sleep delay between HTTP calls.
- Recommendations: Integrate rotating proxies or mock user navigation client libraries if blocking becomes more persistent.

## Performance Bottlenecks

**Synchronous Sequential Fetching:**
- Problem: Scraper fetches spec pages one-by-one sequentially.
- Files: `src/scraper.py`
- Measurement: 2-3 seconds per phone spec page due to sleep delays.
- Cause: Synchronous requests.
- Improvement path: Implement async requests (e.g. using `asyncio` and `aiohttp`) with a centralized rate limit queue.

## Fragile Areas

**Regular Expression Specs Normalization:**
- Files: `src/normalizer.py`
- Why fragile: Relies on precise layout formatting on target pages (e.g., matching "inches" or "Hz").
- Common failures: Small changes in spelling or layout on GSMArena will break regex matches, returning `None`.
- Safe modification: Write unit test suites with different input formats to verify parser resiliency.

## Scaling Limits

**Monolithic Database Serialization:**
- Current capacity: ~300 KB database size.
- Limit: Performance degrades significantly as database expands to tens of megabytes.
- Symptoms at limit: Atomic file replacement (`os.replace`) takes longer, higher risk of database file truncation/corruption if script is interrupted.
- Scaling path: Migrate flat-file storage to SQLite or equivalent lightweight relational database.

## Test Coverage Gaps

**Scoring Logic and Interpolation:**
- What's not tested: Math verification for Layer B, Layer C, predicted score weights, and Case 3 nearest neighbor database interpolation.
- Risk: Changes to scoring math go undetected, introducing silent calculations regressions.
- Priority: High.
- Difficulty to test: Requires generating database fixtures with known benchmark layouts.

---

*Concerns audit: 2026-06-04*
*Update as issues are fixed or new ones discovered*
