# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Michael McKibbin

"""Non-destructive simulation only. No real erase functions exist here yet."""
from .devices import Disk


def simulate(disk: Disk, method: str) -> str:
    if method not in ("overwrite", "ata-sanitize", "nvme-sanitize"):
        raise ValueError("Unsupported simulation method")
    if not disk.path.startswith("/dev/"):
        raise ValueError("Invalid disk path")
    return (f"SIMULATION ONLY: Would request {method} for {disk.path} "
            f"({disk.model}, {disk.size}). No disk was modified. "
            "No sanitisation or verification has occurred.")
