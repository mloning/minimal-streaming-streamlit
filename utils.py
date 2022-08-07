from pathlib import Path

COUNTRIES = ("DE", "NL")


def _make_filename(country: str, path: Path = None) -> Path:
    if path is None:
        path = Path(".")
    return path / f"x_{country}.csv"
