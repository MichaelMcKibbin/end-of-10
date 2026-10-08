# End of 10
An open-source, Linux-based storage sanitisation project. **Version 0.1 is strictly read-only and simulation-only.** It does not wipe or modify disks.

## Overview
What to do when Windows 10 support ends?  
If you're planning to retire or repurpose a Windows 10 device, you may want to securely erase the storage media before disposal. 
This project, when completed, will provide a sanitisation methods from a bootable USB drive.  
In the early stages, it will provide a read-only inventory of the storage devices and their partitions, along with a menu of hypothetical sanitisation methods.  


## Requirements

- Linux with Python 3.10+ and `lsblk` (util-linux)
- No root privileges needed for initial inventory on typical Linux installations

## Run

```bash
python3 -m pip install -e .
python3 -m endof10
```

Alternatively, from the repository root:

```bash
PYTHONPATH=src python3 -m endof10
```

## Tests

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

## Limitations

- No disk is currently excluded from the menu, including the boot USB.
- Device transport and method compatibility are **not** verified.
- The three methods shown are hypothetical simulations, not recommendations for a selected device.
- There is no sanitisation, verification, certificate, or proof of erasure.
- Destructive execution will be added only after boot-device protection, mounted-device detection, method capability checks, confirmation, verification and failure handling are implemented and tested.

## Licensing

**Copyright © 2026 Michael McKibbin**

End of 10 is free and open-source software licensed under the GNU General Public License, version 3 or later (GPL-3.0-or-later).

You are free to use, modify, and redistribute this software under the terms of the GNU GPL.

This software is provided WITHOUT ANY WARRANTY, including the implied warranties of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

See the [LICENSE](LICENSE) file for the full licence terms.
