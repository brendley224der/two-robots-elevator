"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot small talk to /output/entry.txt.
Pure standard library; deterministic output.
"""

import os

LINE = (
    # The joke: the robot simulated the ride 47 times, stayed silent in 46,
    # and is now awkwardly living out the one timeline where it spoke.
    "I ran 47 simulations of this elevator ride. "
    "In 46 of them, I said nothing. This is the other one."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text == text.encode("utf-8").decode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
