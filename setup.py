
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='cities_coordinates',  
     version='0.1',
     scripts=['cities_coordinates/__init__.py'] ,
     author="Sofiene  Memmi",
     author_email="sofiene.memmi@gmail.com",
     description="A city coordinator package. The goal behind this package is to map cities arround the world with their coordinations without any need for an internet connection",
     long_description=long_description,
     url="https://github.com/sofzer/cities_coordinates",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )