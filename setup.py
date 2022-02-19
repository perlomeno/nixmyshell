from setuptools import setup, find_packages

setup(
    name='nixmyshell',
    version='0.0.1',
    description='A script to create shell.nix files',
    author="Alessandro Perlo",
    license="MIT",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nixmyshell=nixmyshell.nixmyshell:main'
        ]
    }
)
