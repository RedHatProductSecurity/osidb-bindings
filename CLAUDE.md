# osidb-bindings

Auto-generated Python client bindings for OSIDB, generated via
[openapi-python-client](https://github.com/openapi-generators/openapi-python-client)
from the OpenAPI schema at `osidb_bindings/openapi_schema.yml`.

## Code generation

All files under `osidb_bindings/bindings/` are auto-generated.
Do not review generated code for implementation quality, style,
or type correctness. Reviews of changes touching generated files
should focus on:

- **CHANGELOG.md completeness** — DEVELOP.md requires documenting
  breaking changes that affect users
- **Version consistency** — the version string must match across
  `setup.py`, `osidb_bindings/bindings/pyproject.toml`,
  `osidb_bindings.spec`, `osidb_bindings/constants.py`, and
  `osidb_bindings/bindings_config.yml`
- **Breaking API surface changes** (removed exports, removed enum
  values, required field promotions) should be documented in
  CHANGELOG.md, not fixed in generated code

## Schema ownership

The OpenAPI schema (`osidb_bindings/openapi_schema.yml`) is owned
by the upstream OSIDB project. Schema-level issues should be
reported upstream, not fixed in this repository.

## Development

- Lint: `tox -e ruff`
- Tests: `tox -e unit-tests`
- Default branch: `master`
