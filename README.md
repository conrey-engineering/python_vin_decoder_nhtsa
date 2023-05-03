# vin_decoder_nhtsa
Python library which uses the [NHTSA Vehicle API](https://vpic.nhtsa.dot.gov/api/) to perform lookups. Attributes are dynamically populated based on API query results returned. This, theoretically, keeps this library low maintenance and requires zero updates for handling of new VIN's.

## Usage
```
>>> from vin_decoder_nhtsa.decoder import Vin
>>>
>>> vin = Vin('WBAGF8324WD*82')
>>> print(vin.Make)
BMW
>>> print(vin.Model)
740i
>>> print(vin.ModelYear)
1998
```
