import unittest
from endof10.devices import parse_lsblk


class DeviceTests(unittest.TestCase):
    def test_only_disks_and_flags(self):
        payload = '{"blockdevices":[{"path":"/dev/sda","type":"disk","size":1000,"rm":1,"ro":0},{"path":"/dev/sda1","type":"part"}]}'
        disks = parse_lsblk(payload)
        self.assertEqual(len(disks), 1)
        self.assertEqual(disks[0].path, "/dev/sda")
        self.assertTrue(disks[0].removable)
        self.assertFalse(disks[0].read_only)
