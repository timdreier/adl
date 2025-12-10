from setuptools import setup, find_packages

setup(
    name='adl',
    version='0.1.0',
    description='Download ebooks from Adobe .acsm files',
    author='Adrien Metais',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'adl=adl.cli:main',
        ],
    },
    install_requires=[
        'requests',
        'lxml',
        'cryptography>=3.1.0',
    ],
)

