from setuptools import setup

setup(
    name="wordfreq",
    author="Greg Back",
    version='0.0.1',
    pymodules=['wordfreq'],
    entry_points={
        'console_scripts': ['wordfreq = wordfreq:main']
    }
)
