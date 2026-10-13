"""Run with:  python -m f1

Prints championship standings for a short made-up season.
"""

from f1.points import standings

SAMPLE_SEASON = [
    ["Verstappen", "Norris", "Leclerc", "Piastri", "Hamilton", "Russell", "Sainz", "Alonso", "Gasly", "Albon"],
    ["Norris", "Piastri", "Verstappen", "Leclerc", "Russell", "Hamilton", "Alonso", "Sainz", "Albon", "Gasly"],
    ["Leclerc", "Verstappen", "Norris", "Hamilton", "Piastri", "Sainz", "Russell", "Gasly", "Alonso", "Albon"],
]


def main():
    print("Championship standings after 3 races\n")
    for rank, (driver, pts) in enumerate(standings(SAMPLE_SEASON), start=1):
        print(f"{rank:>2}. {driver:<12} {pts:>3} pts")


if __name__ == "__main__":
    main()
