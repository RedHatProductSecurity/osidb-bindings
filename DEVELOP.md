# DEVELOP

Instructions how to contribute to and release osidb-bindings

## Dependencies
The following dependencies are required for development and deployment:
* make
* python3
* python3 dependencies (see [pip-tools](#using-pip-tools))
* tox

## Development

### Using pip-tools
TBD

### Feature commit

1) Create feature branch

2) Check commit is clean by running

    ```
    $ tox
    ```

3) Run tests locally

    ```
    $ tox -e unit-tests
    ```

4) Push to branch

5) confirm branch passes CI - ***do not raise an MR if CI does not pass***

6) raise MR against master ensuring good title/description and bullet point
   all significant commits

## Release

There are two main cases when this package needs to be released.

### Version policy

OSIDB bindings as well as the OSIDB itself uses [semantic versioning](https://semver.org/) (eg. MAJOR.MINOR.PATCH, 1.2.3),
however there are some extra rules for the bindings versioning to keep bindings and OSIDB in sync.

* MAJOR and MINOR versions - these versions are only incremented based on the OSIDB version and shouldn't be incremented
when some changes or fixes happens only on the side of the bindings. Whenever the MAJOR or MINOR version of OSIDB gets
released, bindings should be regenerated and accomodated for that version and then released with the same version number.
Eg. OSIDB is on version 1.2.0, bindings are on version 1.2.0 as well, OSIDB 1.3.0 gets released, necessary changes are made
on the bindings side and bindings 1.3.0 gets released as well.

* PATCH version - this version part is separated from OSIDB and it is used mainly for introducing fixes and changes only on
bindings side. Whenever there is a fix or some change in the code that needs to be released however has nothing to do with
the OSIDB itself, the PATCH version gets incremented. Eg. Bindings are on version 1.2.0, bug is found in the bindings code,
bug gets fixed and bindings 1.2.1 are released.

Based on these rules, OSIDB and OSIDB bindings are always compatible as long as the MAJOR and MINOR version matches.
* OSIDB 1.2.0, bindings 1.2.0 - compatible
* OSIDB 1.2.0, bindings 1.2.1 - compatible
* OSIDB 1.2.2, bindings 1.2.1 - compatible
* OSIDB 1.3.0, bindings 1.2.1 - **feature incomplete**
* OSIDB 2.0.0, bindings 1.9.9 - **incompatible**

### Patch release

When minor changes needs to be done on the osidb-bindings side without the actual release of the OSIDB itself
patch release is prefered.

1) Make your changes (see [how to feature commit](feature-commit))

2) Clone/update master branch

    ```
    $ git checkout master
    $ git pull
    ```

3) Create release branch with name matching the specified format (eg. v1.1.1)

    ```
    $ git checkout -b vX.X.X
    ```

4) Prepare release

    ```
    > make patch-release
    ```

    This will:
    * update the `bindings` folder in case it hasn't been updated before
    * increment the patch part of the version (eg. x.x.1 -> x.x.2)

5) raise MR against master

6) confirm CI passes

7) merge MR

8) tag new release in git - this will trigger the build and upload to PyPI
    ```
    $ git tag <release version> vX.X.X
    $ git push origin <release version> vX.X.X
    ```

### Release with OSIDB

When new OSIDB version is released, major/minor release of the osidb-bindings needs to be performed.

1) Clone/update master branch

    ```
    $ git checkout master
    $ git pull
    ```

2) Create release branch with name matching the specified format (eg. v1.1.1)

    ```
    $ git checkout -b vX.X.X
    ```

3) Download OpenAPI schema `yml` file matching the released OSIDB version and replace
   the `osidb_bindings/openapi_schema.yml` with its content

4) Prepare release

    ```
    > make release
    ```

    This will:
    * update the `bindings` folder in case it hasn't been updated before
    * parse the new version (major/minor) from `openapi_schema.yml` and use it

5) raise MR against master

6) confirm CI passes

7) merge MR

8) tag new release in git - this will trigger the build and upload to PyPI
    ```
    $ git tag <release version> vX.X.X
    $ git push origin <release version> vX.X.X
    ```
