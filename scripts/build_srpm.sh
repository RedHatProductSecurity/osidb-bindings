#!/bin/sh

set -e

mkdir dist
python3 setup.py clean sdist
cp dist/* ~/build/SOURCES/
rpmbuild --undefine dist -bs "osidb_bindings.spec" --clean
cp ~/build/SRPMS/* "$1"

