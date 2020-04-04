from setuptools import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name='eicmlr',
    version='0.1',
    author="Yang Zeng, Mingxuan Chen, Qixuan Zhou",
    description="Endoscopic image collection for machine learning research",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/everise/eicmlr",
    packages=['eicmlr'],
    license='Apache-2.0',
    zip_safe=False
)
