import unittest

from f1.points import points_for, race_points, standings


class PointsForTest(unittest.TestCase):
    def test_winner_scores_25(self):
        self.assertEqual(points_for(1), 25)

    def test_tenth_scores_1(self):
        self.assertEqual(points_for(10), 1)

    def test_outside_top_ten_scores_nothing(self):
        self.assertEqual(points_for(11), 0)

    def test_did_not_finish_scores_nothing(self):
        self.assertEqual(points_for(None), 0)

    def test_invalid_position_is_rejected(self):
        with self.assertRaises(ValueError):
            points_for(0)


class RacePointsTest(unittest.TestCase):
    def test_scores_each_driver(self):
        result = race_points(["A", "B", "C"])
        self.assertEqual(result, {"A": 25, "B": 18, "C": 15})

    def test_duplicate_driver_is_rejected(self):
        with self.assertRaises(ValueError):
            race_points(["A", "B", "A"])


class StandingsTest(unittest.TestCase):
    def test_totals_across_races(self):
        table = standings([["A", "B"], ["B", "A"], ["A", "B"]])
        self.assertEqual(table, [("A", 68), ("B", 61)])

    def test_tie_broken_by_wins(self):
        # B and C both end on 25 points, but B has a win and C does not.
        races = [["B"], ["A", "X", "C"], ["A", "X", "Y", "Z", "C"]]
        table = dict(standings(races))
        self.assertEqual(table["B"], table["C"])
        names = [driver for driver, _ in standings(races)]
        self.assertLess(names.index("B"), names.index("C"))


if __name__ == "__main__":
    unittest.main()
