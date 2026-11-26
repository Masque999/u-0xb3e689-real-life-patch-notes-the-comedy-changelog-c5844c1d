"""One-line patch note for a bug in real life, for make.fun.

The brief: a software changelog entry, at most 160 characters, for a bug in
real life or human biology, in the terse register of a real release note.
Yawning was picked because it is a real, recognisable, contagious bug with a
perfect fix: make the yawns queue politely instead of firing all at once.
"""

LINE = "v2.4.1: fixed a bug where yawning in a meeting triggered a chain reaction across the whole room; yawns now queue politely."

# The entry must be exactly one line of 1-160 characters, and the sealed
# scorer rejects whitespace-only text, so fail loudly instead of writing it.
assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, limit is 160"
assert "\n" not in LINE, "entry must be a single line"
assert LINE.strip(), "entry must not be only whitespace"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
