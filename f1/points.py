"""Formula 1 points and championship standings.

Points follow the standard system used for a Grand Prix: the top ten
finishers score 25, 18, 15, 12, 10, 8, 6, 4, 2 and 1 points.
"""

POINTS_BY_POSITION = {
    1: 25,
    2: 18,
    3: 15,
    4: 12,
    5: 10,
    6: 8,
    7: 6,
    8: 4,
    9: 2,
    10: 1,
}


def points_for(position):
    """Return the points scored for finishing in `position`.

    Positions outside the top ten (or a non-finish, passed as None)
    score nothing.
    """
    if position is None:
        return 0
    if not isinstance(position, int) or position < 1:
        raise ValueError(f"Position must be a whole number of 1 or more, got {position!r}")
    return POINTS_BY_POSITION.get(position, 0)


def race_points(finishing_order):
    """Score one race.

    `finishing_order` is a list of driver names, winner first.
    Returns a dict of driver -> points for that race.
    """
    if len(set(finishing_order)) != len(finishing_order):
        raise ValueError("A driver appears more than once in the finishing order")
    return {driver: points_for(place) for place, driver in enumerate(finishing_order, start=1)}


def standings(races):
    """Build championship standings from several races.

    `races` is a list of finishing orders (each a list of driver names).
    Returns a list of (driver, total_points) tuples, leader first.
    Drivers on equal points are ordered by number of wins, then by name.
    """
    totals = {}
    wins = {}
    for finishing_order in races:
        for driver, pts in race_points(finishing_order).items():
            totals[driver] = totals.get(driver, 0) + pts
            wins.setdefault(driver, 0)
        if finishing_order:
            wins[finishing_order[0]] += 1

    ordered = sorted(totals, key=lambda d: (-totals[d], -wins[d], d))
    return [(driver, totals[driver]) for driver in ordered]
