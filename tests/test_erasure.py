import unittest
from endof10.devices import Disk
from endof10.erasure import simulate


class ErasureTests(unittest.TestCase):
    def setUp(self):
        self.disk = Disk('/dev/sda', '1000', 'test', 'sata', 'abc', False, False)

    def test_simulation_never_claims_success(self):
        result = simulate(self.disk, 'overwrite')
        self.assertIn('SIMULATION ONLY', result)
        self.assertIn('No disk was modified', result)

    def test_rejects_unknown_method(self):
        with self.assertRaises(ValueError):
            simulate(self.disk, 'unknown')
