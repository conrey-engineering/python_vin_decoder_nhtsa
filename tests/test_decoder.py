import unittest

from vin_decoder_nhtsa.decoder import Vin

WORKING_TEST_VIN = 'WBAGF8324WD*82'

class Test(unittest.TestCase):
    def test_vin_lookup(self):
        vin = Vin(WORKING_TEST_VIN)
        self.assertEqual(vin.ModelYear, "1998")
        self.assertEqual(vin.Model, "740i")
        self.assertEqual(vin.Make, "BMW")