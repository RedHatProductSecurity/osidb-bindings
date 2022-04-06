from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="osidb-bindings",
    version="1.1.0",
    author="Jakub Frejlach, Red Hat Product Security",
    author_email="jfrejlac@redhat.com",
    description="Python bindings for accessing OSIDB API",
    url="https://github.com/RedHatProductSecurity/osidb-bindings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=["attrs", "httpx", "httpx-gssapi", "python-dateutil"],
)
