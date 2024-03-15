from setuptools import find_packages, setup

with open("./README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="LLM",
    version="0.0.1",
    author="Jose Valderrama",
    author_email="jvalderr239@gmail.com",
    description="LLM Tutorial",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Source": "https://github.com/jvalderr239/LLM",
        "Bug Tracker": "https://github.com/jvalderr239/LLM/issues",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "langchain>=0.1.0",
        "openai>=1.7.2",
        "langchain-openai>=0.0.2",
        "langchain-community>=0.0.12",
        "langchainhub>=0.1.14",
        "python-dotenv"
    ],
    extras_require={
        "dev": [
            "matplotlib", 
            "pandas", 
            "jupyter",
            "ipykernel",
            "torchsummary",
            "ipywidgets",
            "widgetsnbextension",
            "pandas-profiling"
            ]
    },
    python_requires=">=3.8"
)