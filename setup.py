import os
from setuptools import setup

description = "Python cffi bridge to fontconfig's FcFontList/FcFontMatch"
if os.path.exists("README.md"):
    long_description = open("README.md").read()
else:
    long_description = description

setup(
    name="fclist-cffi",
    version="1.1.2",
    description=description,
    long_description=long_description,
    url="https://github.com/MonsieurV/python-fclist",
    download_url="https://github.com/MonsieurV/python-fclist/archive/1.1.2.tar.gz",
    author="Yoan Tournade",
    author_email="y@yoantournade.com",
    license="MIT",
    py_modules=["fclist"],
    install_requires=["cffi"],
    zip_safe=False,
)
