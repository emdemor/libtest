from setuptools import setup
from libtest import __version__

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name="libtest",
    version=__version__,
    # url="",
    license="MIT License",
    author="Eduardo M. de Morais",
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email="emdemor415@gmail.com",
    keywords="",
    description=u"Some optimization functions",
    packages=["libtest"],
    install_requires=["numpy", "pandas", "setuptools"],
)
