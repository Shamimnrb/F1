"""Draw the top three drivers standing on a little podium.

    python -m f1 --podium
"""

WIDTH = 12
BRICK = "\u2588"
# How many block rows each step gets, in the order the steps stand: 2nd, 1st, 3rd.
STEPS = [(2, 3), (1, 4), (3, 2)]


def podium(table):
    """Return a podium picture for the top three of a standings `table`.

    `table` is the list of (driver, points) tuples that `standings` returns.
    """
    if len(table) < 3:
        raise ValueError("A podium needs at least three drivers")

    tallest = max(height for _, height in STEPS)
    columns = []
    for place, height in STEPS:
        driver, pts = table[place - 1]
        blanks = [""] * (tallest - height)
        block = [f" {place} ".center(WIDTH - 2, BRICK)] + [BRICK * (WIDTH - 2)] * (height - 1)
        columns.append(blanks + [driver, f"{pts} pts"] + block)

    lines = ["".join(column[row].center(WIDTH) for column in columns).rstrip()
             for row in range(tallest + 2)]
    trophy = "\U0001F3C6".center(WIDTH * 3 - 1).rstrip()
    ground = "=" * (WIDTH * 3)
    return "\n".join([trophy, *lines, ground])
