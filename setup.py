import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
	requirements = f.read().splitlines()


setuptools.setup(
    name="sitemapgen",
    version="0.9.7",
    author="Nalin Angrish",
    author_email="nalin@nalinangrish.me",
    description="A package to generate Sitemaps from a URL. Also provides a CLI for non programmatical use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nalin-2005/SitemapGen",
    entry_points='''
        [console_scripts]
        sitemapgen=sitemapgen.cli:run
        smg=sitemapgen.cli:run
    ''',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires='>=3.0',
)