# Changelog
All notable changes to this project will be documented in this file.

This project is kept in version sync with the OSIDB project, see the
[version policy](TUTORIAL.md#osidb-compatibility) and thus a lot of
versions don't bring ground breaking changes and they rather update
the API endpoints. In such cases the version is listed without and
addition/changes/deletion.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## [2.1.0] - 2022-08-04

## [2.0.0] - 2022-07-16
### Changed
- add additional resources for queries (affects and trackers),
  session now works as `session.resource_name.operation()` instead of
  old `session.operation()`

### Added
- exported `REQUESTS_CA_BUNDLE` environment variable is now needed
  in order to have the kerberos authentication working for instances
  of OSIDB which are using this auth

## [1.1.1] - 2022-04-07

## [1.1.0] - 2022-04-06
### Changed
- change the authentications to token authentication where the token
  is obtained either via username/password or kerberos, bindings
  handles the token retrieval/renew for the user

## [1.0.3] - 2021-12-06

## [1.0.2] - 2021-12-02

<!-- TODO: Add links to version comparisons -->
