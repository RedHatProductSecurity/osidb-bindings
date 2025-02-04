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

## [4.7.0] - 2025-02-05

## [4.6.3] - 2025-01-24
### Fixed
- general handling of UUIDs

## [4.6.2] - 2025-01-21
### Fixed
- fixed issue with parametrized generic types (eg. list of affects)

## [4.6.1] - 2025-01-17
### Changed
- updated openapi-python-client which generates the core of the package to 0.22.0 (OSIDB-3773)
- switched black formatting to ruff (OSIDB-3773)

## [4.6.0] - 2024-12-10

## [4.5.0] - 2024-10-30

## [4.4.0] - 2024-10-16

## [4.3.0] - 2024-09-19

## [4.2.0] - 2024-09-02

## [4.1.2] - 2024-07-30
### Added
- support for `promote` operation for `flaw` (OSIDB-3201)

## [4.1.1] - 2024-07-10
### Added
- support for bulk create and bulk update for Affects (OSIDB-3124)

## [4.1.0] - 2024-07-01

## [4.0.0] - 2024-06-17
### Added
- add `.file` operation for `trackers` (OSIDB-2029)

### Fixed
- request format changed from form-data to json which
  prevents OSIDB serialization failures (OSIDB-2844)

## [3.7.0] - 2024-05-23
### Added
- Update and Create for Tracker entity
- JIRA_ACCESS_TOKEN environment variable

### Fixed
- Both Bugzilla API Key and Jira Access Token are now automatically fetched
  from environment variables and passed as a header

## [3.6.0] - 2024-01-29

## [3.5.1] - 2023-10-17
### Fixed
- add workaround for Erratum shipped_dt which is marked as non-nullable
  despite being nullable

## [3.5.0] - 2023-10-12
### Added
- add CRUD operations for Flaw CVSS scores and
  package version and for Affect CVSS scores

## [3.4.6] - 2023-09-05
### Fixed
- removed leftover debug output

## [3.4.5] - 2023-09-05
### Fixed
- fix regression in `to_dict` introduced in 3.4.4 by
  fliped condition

## [3.4.4] - 2023-09-05
### Fixed
- fix `to_dict` not being able corretly transform UNSET values
  of different instances (mainly multiprocessing issue)

## [3.4.3] - 2023-08-25
### Fixed
- fix bindings making lot a of uncessary calls when supplying max_results
  parameter for async list iterator which is much higher than actual results count
## [3.4.2] - 2023-08-24
### Changed
- fix missing aiohttp dependency in setup script
- fix aiohttp error when `BUGZILLA_API_KEY` environmental variable
  is not supplied
- fix error caused by supplying empty limit to async iterator
## [3.4.1] - 2023-08-23
### Added
- async iterator operation
- operation for results count

## [3.4.0] - 2023-08-14
### Added
- CRUD operations for Flaw Acknowledgments (create, update, retrieve, retrieve_list, delete)

## [3.3.1] - 2023-08-08
### Changed
- fix usage of query parameters with double underscore [#17](https://github.com/RedHatProductSecurity/osidb-bindings/issues/17)
- implement smarter pagination [#16](https://github.com/RedHatProductSecurity/osidb-bindings/issues/16)

## [3.3.0] - 2023-06-28
### Added
- support for nested resources (eg. Flaw references, Flaw comments)
- CRUD operations for Flaw References (create, update, retrieve, retrieve_list, delete)
- CRUD operations for Flaw Comments (create, retrieve, retrieve_list)
## [3.1.0] - 2023-04-26

## [3.0.2] - 2023-04-04

## [3.0.1] - 2023-04-03

## [3.0.0] - 2023-03-21
### Added
- add `next()`, `prev()` and `iterator()` methods for paginated
  responses to make page browsing easier
- require exported `BUGZILLA_API_KEY` environment variable for
  some session operations which are particulary unsafe (create, update, etc.)
  for authentication/authorization against Bugzilla

### Changed
- update allowed session operations for each resource

### Removed
- remove old aliases for session operations with flaws (eg. `session.retrieve()`,
  `session.retrieve_list()`, etc.) in favor of new resource operations
  (eg. `session.flaws.retrieve()`, `session.flaws.retrieve_list()`, etc.)

## [2.3.0] - 2023-02-23
### Added
- bring back `session.operation()` as an alias for flaws operations
  to prevent breaking changes

### Changed
- fix session.status call error

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
