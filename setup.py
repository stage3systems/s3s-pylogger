# setup.py
from setuptools import setup, find_packages

setup(
    name='s3s-pylogger',
    version='0.1.0',
    description='Simple logger for internal Python apps',
    author='Kamrul Khan',
    author_email='kamrul.khan@stage3systems.com',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.9',
)

