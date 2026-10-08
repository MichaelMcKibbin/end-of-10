"""Minimal interactive (read-only) interface."""
from .devices import discover_disks
from .erasure import simulate

METHODS = {"1": "overwrite", "2": "ata-sanitize", "3": "nvme-sanitize"}


def main() -> int:
    print("\nEND OF 10 — STORAGE INVENTORY - SIMULATION ONLY\n")
    try:
        disks = discover_disks()
    except Exception as exc:
        print(f"Could not inventory disks: {exc}")
        return 1
    if not disks:
        print("No disks detected.")
        return 0
    for i, disk in enumerate(disks, 1):
        flags = ", ".join(x for x, yes in (("removable", disk.removable), ("read-only", disk.read_only)) if yes)
        print(f"{i}. {disk.path} | {disk.size} bytes | {disk.model} | {disk.transport} | "
              f"serial: {disk.serial}" + (f" | {flags}" if flags else ""))
    print("\nNo drives are excluded or approved for wiping in this prototype.")
    choice = input("Select a disk number to simulate (Enter to exit): ").strip()
    if not choice:
        return 0
    if not choice.isdecimal() or not 1 <= int(choice) <= len(disks):
        print("Invalid selection.")
        return 1
    disk = disks[int(choice) - 1]
    print("1. Overwrite  2. ATA Sanitize  3. NVMe Sanitize")
    method = METHODS.get(input("Simulation method: ").strip())
    if not method:
        print("Invalid method.")
        return 1
    print("\n" + simulate(disk, method))
    return 0
