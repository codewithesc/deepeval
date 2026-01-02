from setuptools import setup, find_packages

setup(
    name="deepeval_poc",
    version="1.0.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "deepeval>=3.0.0",
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
    ],
)
