# osidb-bindings
A client library for accessing OSIDB API

## Requirements
* gcc
* krb5-devel
* pip
* python3
* python3-devel

## Installation

```
pip install osidb-bindings
```

## Usage

```python
import osidb_bindings

# Basic auth
osidb_session = osidb_bindings.new_session(osidb_server_uri="http://localhost:8000/", username="username", password="password")
```
or
```python
# Default kerberos auth
osidb_session = osidb_bindings.new_session(osidb_server_uri="http://localhost:8000/")
```

```python
# Get status
osidb_session.status()

# Retrieve flaw
flaw = osidb_session.flaws.retrieve(id="CVE-1111-2222")

# Fields can be accessed directly via attributes
flaw.title
flaw.impact

# or the flaw can be converted into dict
flaw_dict = flaw.to_dict()
flaw_dict["title"]
flaw_dict["impact"]

# Retrieving multiple flaws
all_flaws = osidb_session.flaws.retrieve_list()

# All query params listed in OpenAPI schema can be passed as well
filtered_flaws = osidb_session.flaws.retrieve_list(impact="IMPORTANT", tracker_ids=["111111", "222222"])

# number of results
filtered_flaws.count

# list with the results
filtered_flaws.results
```

## For more details read [tutorial](TUTORIAL.md)

## For development details read [developer guide](DEVELOP.md)
