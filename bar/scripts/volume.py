#!/usr/bin/env python3

from subprocess import check_output

volume = check_output(["wpctl", "get-volume", "@DEFAULT_AUDIO_SINK@"])

print(f"{volume.strip().decode()[10:]}")