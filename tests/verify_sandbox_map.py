"""Verify that the migrated UrbanProject sandbox map remains internally consistent."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAP_DIR = ROOT / "maps" / "urban-sandbox-v1"
EXPECTED_SHA256 = {
    "map.pgm": "127542157DED3AE59FAA8DF52CFFC6EB492A4650C65DB0CACDB44CB9EA508B5F",
    "map.yaml": "94E461AA91E6E13B8E505FB8F5FC14261107561180A61A1820827AF47AF9FA3A",
}


def pgm_header(path: Path) -> tuple[str, int, int, int, int]:
    payload = path.read_bytes()
    match = re.match(rb"(P[25])\s+(\d+)\s+(\d+)\s+(\d+)\s", payload)
    if match is None:
        raise AssertionError(f"Invalid PGM header: {path}")
    magic, width, height, maximum = match.groups()
    return magic.decode("ascii"), int(width), int(height), int(maximum), match.end()


def main() -> int:
    for name, expected in EXPECTED_SHA256.items():
        path = MAP_DIR / name
        if not path.is_file():
            raise AssertionError(f"Missing migrated map asset: {path}")
        actual = hashlib.sha256(path.read_bytes()).hexdigest().upper()
        if actual != expected:
            raise AssertionError(f"Checksum mismatch for {name}: {actual}")

    magic, width, height, maximum, data_start = pgm_header(MAP_DIR / "map.pgm")
    if (magic, width, height, maximum) != ("P5", 300, 300, 255):
        raise AssertionError("Unexpected PGM metadata")
    if (MAP_DIR / "map.pgm").stat().st_size != data_start + width * height:
        raise AssertionError("PGM payload size does not match its raster dimensions")

    yaml_text = (MAP_DIR / "map.yaml").read_text(encoding="utf-8")
    for expected_line in ("image: map.pgm", "resolution: 0.05", "origin: [-7.5, -7.5, 0.0]"):
        if expected_line not in yaml_text:
            raise AssertionError(f"Missing ROS map metadata: {expected_line}")

    print("Urban Sandbox v1 verification passed: 300x300 P5 raster, 0.05 m/pixel, source checksums match.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, OSError, ValueError) as error:
        print(f"Sandbox map verification failed: {error}", file=sys.stderr)
        raise SystemExit(1)
