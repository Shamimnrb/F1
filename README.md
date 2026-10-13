# F1

My personal playground for trying out code, testing it, and releasing it.

It starts as a tiny Python project that calculates **Formula 1 points and championship standings**. It's small on purpose, a safe place to learn how a real project works.

## Try it

You need [Python](https://www.python.org/downloads/) 3.11 or newer.

```bash
python -m f1
```

This prints the standings for a short made-up season.

Want to see who made the podium?

```bash
python -m f1 --podium
```

```
                 🏆
               Norris
 Verstappen    58 pts
   58 pts    ███ 1 ████   Leclerc
 ███ 2 ████  ██████████    52 pts
 ██████████  ██████████  ███ 3 ████
 ██████████  ██████████  ██████████
====================================
```

## Run the tests

```bash
python -m unittest discover -s tests -v
```

The tests also run automatically on GitHub every time code is pushed. Look for the green ✓ or red ✗ on the **Actions** tab.

## What's inside

| Path | What it is |
| --- | --- |
| `f1/points.py` | The actual code: points per position, scoring a race, building standings |
| `f1/podium.py` | Draws the top three on a little podium |
| `f1/__main__.py` | What runs when you type `python -m f1` |
| `tests/` | Checks that the code does what it should |
| `.github/workflows/tests.yml` | Runs the tests on GitHub automatically |
| `.github/workflows/release.yml` | Publishes a release when a version tag is pushed |

## Releasing a new version

1. Update the version number in `pyproject.toml` and `f1/__init__.py`.
2. Commit, then tag and push:

   ```bash
   git tag v0.2.0
   git push origin v0.2.0
   ```

3. GitHub runs the tests and, if they pass, publishes the release on the **Releases** page.

Or just ask Claude to "release a new version".
