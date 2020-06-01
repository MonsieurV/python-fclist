import os
from setuptools import setup

readme_markdown = None
with open("README.md") as f:
    readme_markdown = f.read()

setup(
    name="fclist-cffi",
    version="1.1.2",
    description="Python cffi bridge to fontconfig's FcFontList/FcFontMatch",
    long_description=readme_markdown,
    long_description_content_type="text/markdown",
    url="https://github.com/MonsieurV/python-fclist",
    download_url="https://github.com/MonsieurV/python-fclist/archive/1.1.2.tar.gz",
    author="Yoan Tournade",
    author_email="y@yoantournade.com",
    license="MIT",
    py_modules=["fclist"],
    install_requires=["cffi"],
    zip_safe=False,
)
