from setuptools import setup, find_packages

setup(
   name='vin_decoder_nhtsa',
   version='0.0.2',
   description='Python module for decoding VIN metadata from NHTSA API',
   author='Man Foo',
   author_email='foomail@foo.example',
   packages=['vin_decoder_nhtsa'],  #same as name
   packages=find_packages(exclude="tests")
#    install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
)