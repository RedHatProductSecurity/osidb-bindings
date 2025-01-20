from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="osidb_bindings",
    version="4.6.2",
    author="Jakub Frejlach, Red Hat Product Security",
    author_email="jfrejlac@redhat.com",
    description="Python bindings for accessing OSIDB API",
    url="https://github.com/RedHatProductSecurity/osidb-bindings",
    project_urls={
        "Changelog": "https://github.com/RedHatProductSecurity/osidb-bindings/blob/master/CHANGELOG.md",
        "Documentation": "https://github.com/RedHatProductSecurity/osidb-bindings/blob/master/TUTORIAL.md",
        "Source": "https://github.com/RedHatProductSecurity/osidb-bindings",
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "aiohttp",
        "attrs",
        "requests",
        "requests-gssapi",
        "python-dateutil",
    ],
)
