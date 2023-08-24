import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME ="Text-summarizer-nlp"
AUTHOR_USERNAME = "shrutimary15"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL = "shrutimarymathew@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer NLP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shrutimarymathew/Text-summarizer-nlp",
    project_urls={
        "Bug Tracker": "https://github.com/shrutimarymathew/Text-summarizer-nlp/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
)