from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requires = f.read().splitlines()

setup(
    name='phpgadgets',
    version='0.1',
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        'console_scripts': ['phpgadgets = phpgadgets:main']
    },
)
