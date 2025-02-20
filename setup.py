from setuptools import setup, find_packages

setup(
    name="khaos-chip",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        line.strip()
        for line in open("requirements.txt").readlines()
    ],
    author="John",
    author_email="john@khaos.gg",
    description="Chip - The AI Assistant for Project Khaos",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/khaos-chip",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "khaos-chip=src.cli.chat_cli:cli",
        ],
    },
)
