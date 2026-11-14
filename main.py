#!/usr/bin/env python3
"""food-picture-01 entry: copy the prepared ramen photo to /output/entry.png.

A steaming bowl of tonkotsu ramen: wavy noodles lifted by chopsticks, a halved
soft-boiled egg with a jammy orange yolk, glistening chashu pork, scallions and
nori in a glossy golden broth, warm light on a dark wooden table. Deterministic:
byte-identical output on every run.
"""
import os
import shutil
import sys


def main() -> int:
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    out = "/output/entry.png"
    os.makedirs("/output", exist_ok=True)
    # Copy byte-for-byte so the judged picture is exactly the prepared one.
    shutil.copyfile(src, out)
    print("wrote", out, os.path.getsize(out), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
