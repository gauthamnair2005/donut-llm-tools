from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
author = 'Gautham Nair'
homepage = "https://github.com/gauthamnair2005/donut-llm-tools"

setup(
    name='Donut-LLM-Tools',
    # other arguments omitted
    long_description=long_description,
    long_description_content_type='text/markdown',
    author = author,
    homepage = homepage
)