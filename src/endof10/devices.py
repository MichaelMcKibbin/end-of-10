# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Michael McKibbin

"""Read-only device inventory."""
import json
import subprocess
from dataclasses import dataclass


@dataclass(frozen=True)
class Disk:
    path: str
    size: str
    model: str
    transport: str
    serial: str
    removable: bool
    read_only: bool


def parse_lsblk(payload: str) -> list[Disk]:
    data = json.loads(payload)
    disks = []
    for item in data.get("blockdevices", []):
        if item.get("type") != "disk":
            continue
        disks.append(Disk(
            path=str(item.get("path") or ""),
            size=str(item.get("size") or "unknown"),
            model=str(item.get("model") or "unknown").strip(),
            transport=str(item.get("tran") or "unknown"),
            serial=str(item.get("serial") or "unknown").strip(),
            removable=str(item.get("rm", "0")).lower() in ("1", "true"),
            read_only=str(item.get("ro", "0")).lower() in ("1", "true"),
        ))
    return disks


def discover_disks() -> list[Disk]:
    result = subprocess.run(
        ["lsblk", "--json", "--bytes", "--paths", "--output", "NAME,PATH,TYPE,SIZE,MODEL,TRAN,SERIAL,RM,RO"],
        check=True, capture_output=True, text=True, timeout=15,
    )
    return parse_lsblk(result.stdout)
