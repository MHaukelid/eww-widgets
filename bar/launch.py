#!/usr/bin/env python3

from pathlib import Path
from subprocess import run

EXEC = Path("/usr/bin/eww")
BAR_CFG  = Path(f"{Path.home()}/.config/eww/bar")

run([EXEC, "-c", BAR_CFG, "open-many", "bar"])
