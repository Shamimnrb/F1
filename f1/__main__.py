"""Run with:  python -m f1

Prints championship standings for a short made-up season.
Add --podium to see the top three on a podium instead.
"""

import sys

from f1.podium import podium
from f1.points import standings

SAMPLE_SEASON = [
    ["Verstappen", "Norris", "Leclerc", "Piastri", "Hamilton", "Russell", "Sainz", "Alonso", "Gasly", "Albon"],
    ["Norris", "Piastri", "Verstappen", "Leclerc", "Russell", "Hamilton", "Alonso", "Sainz", "Albon", "Gasly"],
    ["Leclerc", "Verstappen", "Norris", "Hamilton", "Piastri", "Sainz", "Russell", "Gasly", "Alonso", "Albon"],
]


def main(args=None):
    args = sys.argv[1:] if args is None else args
    if "--podium" in args:
        print(podium(standings(SAMPLE_SEASON)))
        return
    print("Championship standings after 3 races\n")
    for rank, (driver, pts) in enumerate(standings(SAMPLE_SEASON), start=1):
        print(f"{rank:>2}. {driver:<12} {pts:>3} pts")


if __name__ == "__main__":
    main()
