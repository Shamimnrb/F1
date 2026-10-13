import unittest

from f1.podium import podium


TABLE = [("Norris", 58), ("Verstappen", 58), ("Leclerc", 52), ("Piastri", 40)]


class PodiumTest(unittest.TestCase):
    def test_shows_top_three_only(self):
        picture = podium(TABLE)
        for driver in ("Norris", "Verstappen", "Leclerc"):
            self.assertIn(driver, picture)
        self.assertNotIn("Piastri", picture)

    def test_winner_stands_highest(self):
        lines = podium(TABLE).splitlines()
        row = {driver: next(i for i, line in enumerate(lines) if driver in line)
               for driver in ("Norris", "Verstappen", "Leclerc")}
        self.assertLess(row["Norris"], row["Verstappen"])
        self.assertLess(row["Verstappen"], row["Leclerc"])

    def test_second_on_left_third_on_right(self):
        lines = podium(TABLE).splitlines()
        second = next(line for line in lines if " 2 " in line)
        third = next(line for line in lines if " 3 " in line)
        self.assertLess(second.index(" 2 "), 12)
        self.assertGreater(third.index(" 3 "), 24)

    def test_needs_three_drivers(self):
        with self.assertRaises(ValueError):
            podium(TABLE[:2])


if __name__ == "__main__":
    unittest.main()
