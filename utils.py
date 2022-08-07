from pathlib import Path


def _make_filename(country: str, market: str, path: Path = None) -> Path:
    if path is None:
        path = Path(".")
    return path / f"x_{country}_{market}.csv"
