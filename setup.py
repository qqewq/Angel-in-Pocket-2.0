from setuptools import setup, find_packages

setup(
    name="angel-in-pocket-2.0",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic-settings",
        "stripe",
        "numpy",
    ],
)
