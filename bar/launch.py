#!/usr/bin/env python3

from pathlib import Path
import psutil
from subprocess import run

EXEC = Path("/home/mhl/Projects/Personal/eww/target/release/eww")
BAR_CFG  = Path("/home/mhl/.config/eww/bar")

# Start eww daemon
isEwwDeamonAlive = False

for p in psutil.process_iter(["name"]):
    if p.info["name"] == "eww":
        isEwwDeamonAlive = True

if not isEwwDeamonAlive:
    run([str(EXEC), "-c", str(BAR_CFG), "daemon"])

# Open bar
def open_bar():
    run([str(EXEC), "-c", str(BAR_CFG), "open-many", "bar"])

open_bar()
