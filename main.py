"""Entry for make.fun bounty: Famous Last Words — The Funniest Epitaph.

Prints the epitaph exactly, with no trailing newline.
"""

import sys

ENTRY = "Here lies Dave. His last words: 'Hold my beer and watch this.' We watched. He did not survive the encore."

MAX_CHARS = 150


def validate(entry):
    """Check the entry obeys the competition rules before printing."""
    if not entry:
        raise ValueError("entry must not be empty")
    if len(entry) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character limit"
            % (len(entry), MAX_CHARS)
        )
    if "\n" in entry:
        raise ValueError("entry must be a single tombstone epitaph (one line)")


def main():
    validate(ENTRY)
    sys.stdout.write(ENTRY)
    sys.stdout.flush()
    # Verification: the emitted text must be exactly the entry, with
    # no trailing newline or extra whitespace added by the writer.
    assert not ENTRY.endswith("\n"), "entry must not end with a newline"


if __name__ == "__main__":
    main()
