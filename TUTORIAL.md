# OSIDB Bindings Tutorial

A Pythonic way to talk to OSIDB without getting lost in HTTP details.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
  - [PyPI (Recommended)](#pypi-recommended)
  - [RPM Package](#rpm-package)
  - [Development Installation](#development-installation)
- [OSIDB Compatibility](#osidb-compatibility)
- [Usage](#usage)
  - [Import the Bindings](#import-the-bindings)
  - [Create a Session](#create-a-session)
  - [Required Environment Variables](#required-environment-variables)
  - [SSL Configuration](#ssl-configuration)
- [Session Operations](#session-operations)
  - [API Version Control](#api-version-control)
  - [Available Resources and Operations](#available-resources-and-operations)
  - [Basic Operations](#basic-operations)
    - [`status`](#status)
    - [`retrieve`](#retrieve)
    - [`retrieve_list`](#retrieve_list)
    - [`retrieve_list_iterator`](#retrieve_list_iterator)
    - [`retrieve_list_iterator_async`](#retrieve_list_iterator_async)
    - [`count`](#count)
    - [`search`](#search)
    - [`create`](#create)
    - [`update`](#update)
    - [`delete`](#delete)
  - [Extra Operations](#extra-operations)
- [Working with Responses](#working-with-responses)
  - [Single Resource Response](#single-resource-response)
  - [Paginated Response](#paginated-response)
- [Utility Functions](#utility-functions)
  - [`cve_ids`](#cve_ids)
- [Debugging and Error Handling](#debugging-and-error-handling)
  - [Exception Handling](#exception-handling)

---

## Requirements

- gcc
- krb5-devel
- pip
- python3
- python3-devel

## Installation

You can install the bindings using several methods:

### PyPI (Recommended)

Install from [PyPI](https://pypi.org/project/osidb-bindings/) using pip. It is highly recommended to install the package within a [virtual environment](https://docs.python.org/3/library/venv.html):

```bash
pip install osidb-bindings
```

### RPM Package

Install from [Fedora Copr](https://copr.fedorainfracloud.org/coprs/jazinner/osidb-bindings/):

```bash
dnf copr enable jazinner/osidb-bindings
dnf install osidb_bindings
```

### Development Installation

Install directly from the [GitHub repository](https://github.com/RedHatProductSecurity/osidb-bindings) (installs from master branch):

```bash
pip install -e git+https://github.com/RedHatProductSecurity/osidb-bindings.git#egg=osidb_bindings
```

To install from a specific branch:

```bash
pip install -e git+https://github.com/RedHatProductSecurity/osidb-bindings.git@<branch_name>#egg=osidb_bindings
```

## OSIDB Compatibility

Both OSIDB and the bindings use [semantic versioning](https://semver.org/) (MAJOR.MINOR.PATCH format, e.g., 1.2.3). The bindings are compatible with OSIDB when the MAJOR and MINOR versions match.

**Compatibility Examples:**
- OSIDB 1.2.0, bindings 1.2.0 → ✅ **Compatible**
- OSIDB 1.2.0, bindings 1.2.1 → ✅ **Compatible**
- OSIDB 1.2.2, bindings 1.2.1 → ✅ **Compatible**
- OSIDB 1.3.0, bindings 1.2.1 → ⚠️ **Feature incomplete**
- OSIDB 2.0.0, bindings 1.9.9 → ❌ **Incompatible**

> **Note:** This compatibility guarantee starts from version 1.1.0. Any previous version of the bindings is considered experimental and should not be used in production.

## Usage

### Import the Bindings

```python
import osidb_bindings
```

### Create a Session

The Session is the core component you'll interact with. Create a session using `osidb_bindings.new_session()`. Once created, the session serves as your gateway to access all OSIDB endpoints.

When initializing a session, you must specify the `osidb_server_uri` of the OSIDB instance you want to connect to. This tutorial uses a local OSIDB instance on port 8000 for examples.

OSIDB uses token-based (JWT) authentication for most endpoints. The bindings automatically handle token refreshing, so you only need to specify how to obtain the initial token. OSIDB supports two main authentication mechanisms:

#### Basic Authentication
Used for OSIDB instances without Kerberos authentication (typically local development instances):

```python
session = osidb_bindings.new_session(
    osidb_server_uri="http://localhost:8000/",
    username="your_username",
    password="your_password"
)
```

#### Kerberos Authentication (Default)
Used for OSIDB instances with Kerberos authentication enabled (production/staging/UAT environments):

```python
session = osidb_bindings.new_session(osidb_server_uri="https://osidb-prod.example.com/")
```

### Required Environment Variables

Certain operations (primarily those involving creating or modifying content) require additional API keys to work properly:

#### Bugzilla API Key
Required for operations that interact with Bugzilla:

```bash
export BUGZILLA_API_KEY="your_bugzilla_api_key"
```

#### Jira Access Token
Required for operations that interact with Jira:

```bash
export JIRA_ACCESS_TOKEN="your_jira_access_token"
```

### SSL Configuration

SSL verification is enabled by default. For proper functionality, set the `REQUESTS_CA_BUNDLE` environment variable to point to your system's CA bundle:

#### Common Linux Distributions
```bash
# Fedora/RHEL/CentOS
export REQUESTS_CA_BUNDLE="/etc/pki/tls/certs/ca-bundle.crt"

# Ubuntu/Debian
export REQUESTS_CA_BUNDLE="/etc/ssl/certs/ca-certificates.crt"
```

#### macOS and Other Systems
For macOS and other systems where the CA bundle might not be present or is located elsewhere, you may need to download the required certificate authority bundle from your organization or a trusted source:

```bash
# Use custom CA bundle path
export REQUESTS_CA_BUNDLE="/path/to/your/ca-bundle.crt"
```

#### SSL Configuration in Code
You can also configure SSL settings directly when creating a session:

```python
# Default behavior (verify_ssl=True is default, uses REQUESTS_CA_BUNDLE environment variable)
session = osidb_bindings.new_session(osidb_server_uri="https://osidb.example.com/")

# Explicitly enable SSL verification (same as default)
session = osidb_bindings.new_session(
    osidb_server_uri="https://osidb.example.com/",
    verify_ssl=True
)

# Use custom CA bundle path
session = osidb_bindings.new_session(
    osidb_server_uri="https://osidb.example.com/",
    verify_ssl="/path/to/custom/ca-bundle.crt"
)

# Disable SSL verification (not recommended for production)
session = osidb_bindings.new_session(
    osidb_server_uri="https://osidb.example.com/",
    verify_ssl=False
)
```

### Session operations

This section describes possible session operations. See [response section](#response) to learn how to work with obtained operation responses.

#### API Version Control

All session operations support an optional `api_version` parameter that allows you to specify which API version to use for the request. If not specified, the bindings will automatically use the latest available API version for that endpoint.

```python
# Uses the latest API version (default behavior)
flaw_response = session.flaws.retrieve(id="CVE-1111-2222")

# Explicitly specify an API version
flaw_response = session.flaws.retrieve(id="CVE-1111-2222", api_version="v1")
```

When using a non-latest API version, the bindings will emit a warning:

```
WARNING: A non-latest API version (v1) was used for flaws::retrieve. Please consider upgrading to the latest version: v2.
```

You may want to explicitly specify a version to lock your scripts to a specific API version, or you may prefer to always use the latest version by omitting the parameter.

You can discover available API versions and endpoints using the `session.endpoints` attribute:

```python
# View available endpoints and their versions
print(session.endpoints)
# Output: {'osidb_api': defaultdict(<class 'set'>, {'flaws_list': {'v1', 'v2'}, 'flaws_retrieve': {'v1', 'v2'}, ...})}

# Check which versions are available for a specific operation
available_versions = session.endpoints['osidb_api']['flaws_list']
print(available_versions)  # {'v1', 'v2'}
```

You can also view the complete API schema with version information by visiting the Swagger UI on your OSIDB instance: `https://<your-osidb-instance>/osidb/api/v1/schema/swagger-ui/`

#### Available Resources and Operations

Operations can be performed on the following resources and their subresources:

**Flaws** (`session.flaws`)
- Standard operations: retrieve, retrieve_list, create, update, search
- Subresources:
  - acknowledgments
  - comments
  - cvss_scores
  - labels
  - package_versions
  - references
- Extra operations: promote, reject

**Affects** (`session.affects`)
- Standard operations: retrieve, retrieve_list, create, update, delete, bulk_create, bulk_update
- Subresources:
  - cvss_scores

**Trackers** (`session.trackers`)
- Standard operations: retrieve, retrieve_list, create, update
- Extra operations: file

**Labels** (`session.labels`)
- Standard operations: retrieve, retrieve_list

> **Note:** The following examples demonstrate operations on the `flaws` resource. To work with different resources, simply replace `flaws` with the resource name. For subresources (e.g., flaw comments, flaw references), use dot notation: `session.flaws.comments.retrieve(...)`

#### Basic Operations

#### `status`
The most basic operation is retrieving the status to verify your session can successfully access OSIDB:

```python
status_response = session.status()
```

See `/GET /osidb/api/{api_version}/status` in the [API documentation](osidb_bindings/openapi_schema.yml) for details on response format and available parameters.

#### `retrieve`
Retrieve a single resource using its identifier (`id`).

**Examples:**
```python
# Using CVE ID
flaw_response = session.flaws.retrieve(id="CVE-1111-2222")

# Using UUID
flaw_response = session.flaws.retrieve(id="aedb854d-1afc-40fe-9554-bc50098b0154")

# Using specific API version
flaw_response = session.flaws.retrieve(id="CVE-1111-2222", api_version="v1")
```

See `/GET /osidb/api/{api_version}/flaws/{id}` in the [API documentation](osidb_bindings/openapi_schema.yml) for details on query parameters and response format.

#### `retrieve_list`
Retrieve a list of resources with optional filtering using query parameters. Results are paginated (see [paginated response section](#paginated-response)).

**Basic Usage:**
```python
# Retrieve all flaws
all_flaws = session.flaws.retrieve_list()

# Retrieve with specific API version
all_flaws = session.flaws.retrieve_list(api_version="v1")
```

**Filtering Examples:**
```python
# String query parameters
critical_flaws = session.flaws.retrieve_list(impact="CRITICAL")
internet_flaws = session.flaws.retrieve_list(source="INTERNET")

# Datetime query parameters
from datetime import datetime
recent_flaws = session.flaws.retrieve_list(changed_after=datetime(2023, 1, 1))
older_flaws = session.flaws.retrieve_list(changed_before=datetime.now())

# Date range filtering
date_range_flaws = session.flaws.retrieve_list(
    changed_after=datetime.strptime("2023-01-01", "%Y-%m-%d"),
    changed_before=datetime.strptime("2023-12-31", "%Y-%m-%d")
)

# List parameters (both formats work)
specific_cves = session.flaws.retrieve_list(cve_ids="CVE-1111-2222,CVE-1111-2223")  # comma-separated string
specific_cves = session.flaws.retrieve_list(cve_ids=["CVE-1111-2222", "CVE-1111-2223"])  # Python list

# Multiple filter conditions
filtered_flaws = session.flaws.retrieve_list(
    source="REDHAT",
    impact="CRITICAL",
    changed_after=datetime(2023, 1, 1)
)
```

See `/GET /osidb/api/{api_version}/flaws` in the [API documentation](osidb_bindings/openapi_schema.yml) for details on available query parameters and response format.

#### `retrieve_list_iterator`
Retrieve a list of resources with automatic pagination handling. Returns a generator that yields individual resource entities. Note that the API is called in a paginated way - pages are loaded sequentially (e.g., first 100 results, then next 100, etc.) but you can iterate through individual items.

**Basic Usage:**
```python
# Iterate through all flaws (handles pagination automatically)
for flaw in session.flaws.retrieve_list_iterator():
    print(f"Processing {flaw.cve_id}")
    # Pages are loaded as needed (e.g., 100 items at a time)

# With filtering
for flaw in session.flaws.retrieve_list_iterator(impact="CRITICAL"):
    print(f"Critical flaw: {flaw.cve_id}")

# With API version specification
for flaw in session.flaws.retrieve_list_iterator(api_version="v1"):
    process_flaw(flaw)
```

**Processing Large Datasets:**
```python
# Process flaws efficiently with automatic page loading
for flaw in session.flaws.retrieve_list_iterator(source="REDHAT"):
    # Iterator loads pages sequentially (not the entire dataset at once)
    # but you process each flaw individually
    analyze_flaw(flaw)
    update_database(flaw)
```

See `/GET /osidb/api/{api_version}/flaws` in the [API documentation](osidb_bindings/openapi_schema.yml) for details. All query parameters from `retrieve_list` are supported.

#### `retrieve_list_iterator_async`
Retrieve a list of resources with automatic pagination handling using asynchronous communication to significantly speed up data retrieval. Returns a generator that yields individual resource entities. Multiple pages are fetched concurrently rather than sequentially.

**Concurrency Configuration:**
By default, the system allows up to 10 concurrent connections. You can adjust this limit using the `OSIDB_BINDINGS_MAX_CONCURRENCY` environment variable. Keep the limit between 1 and 50 concurrent connections to avoid service overload.

```bash
export OSIDB_BINDINGS_MAX_CONCURRENCY=30
```

**Basic Usage:**
```python
# Fast iteration through all flaws using concurrent page requests
for flaw in session.flaws.retrieve_list_iterator_async():
    print(f"Processing {flaw.cve_id}")
    # Multiple pages are fetched concurrently for better performance

# With filtering
for flaw in session.flaws.retrieve_list_iterator_async(impact="CRITICAL"):
    print(f"Critical flaw: {flaw.cve_id}")

# Limit the number of results
for flaw in session.flaws.retrieve_list_iterator_async(max_results=200):
    process_flaw(flaw)

# With API version specification
for flaw in session.flaws.retrieve_list_iterator_async(api_version="v1"):
    analyze_flaw(flaw)
```

**Performance Considerations:**
```python
# Process large datasets efficiently with concurrent page loading
for flaw in session.flaws.retrieve_list_iterator_async(
    source="REDHAT",
    max_results=1000
):
    # Pages are loaded concurrently (e.g., multiple 100-item pages at once)
    # significantly faster than sequential loading
    update_metrics(flaw)
```

> **Warning:** Exceeding the recommended concurrency limit may lead to service overload, which could be interpreted as a Denial-of-Service attack.

See `/GET /osidb/api/{api_version}/flaws` in the [API documentation](osidb_bindings/openapi_schema.yml) for details. All query parameters from `retrieve_list` are supported.

#### `count`
Retrieve the total count of entities that would be returned by the same `retrieve_list` call. This operation accepts the same input arguments as `retrieve_list` but only returns the count, making it efficient for checking dataset sizes.

**Basic Usage:**
```python
# Count all flaws
total_flaws = session.flaws.count()

# Count with filtering
low_impact_count = session.flaws.count(impact="LOW")
critical_count = session.flaws.count(impact="CRITICAL")

# Count with multiple filters
recent_critical_count = session.flaws.count(
    impact="CRITICAL",
    changed_after=datetime(2023, 1, 1)
)

# Count with API version specification
count_v1 = session.flaws.count(api_version="v1")
```

**Use Cases:**
```python
from datetime import datetime

# Check if any critical flaws exist before processing
if session.flaws.count(impact="CRITICAL") > 0:
    process_critical_flaws()

# Monitor flaw trends
today_count = session.flaws.count(changed_after=datetime.now().replace(hour=0, minute=0))
print(f"Flaws updated today: {today_count}")
```

#### `search`
Retrieve a list of resources using full-text search. This performs a search across multiple text fields in the resource to find matches.

**Basic Usage:**
```python
# Search for flaws containing specific text
satellite_flaws = session.flaws.search("Red Hat Satellite v.5")
apache_flaws = session.flaws.search("Apache HTTP Server")

# Search for specific CVE
cve_results = session.flaws.search("CVE-1111-2222")

# Search with API version specification
search_results = session.flaws.search("buffer overflow", api_version="v1")
```

**Search Examples:**
```python
# Search for product names
product_flaws = session.flaws.search("OpenSSL")

# Search for vulnerability types
xss_flaws = session.flaws.search("cross-site scripting")

# Search for component names
kernel_flaws = session.flaws.search("kernel")
```

> **Note:** Search functionality depends on the OSIDB instance configuration and may search across different fields like titles, descriptions, and component names.

#### `create`
Create a new resource from provided data. This operation requires appropriate permissions and may need Bugzilla/Jira API keys depending on the resource type.

**Basic Usage:**
```python
from datetime import datetime

# Define the flaw data
flaw_data = {
    "cve_id": "CVE-1111-2222",
    "state": "NEW",
    "impact": "CRITICAL",
    "title": "Remote Code Execution in Example Component",
    "components": ["example-component", "core-library"],
    "cve_description": "A remote code execution vulnerability exists in the example component.",
    "comment_zero": "Initial analysis indicates this affects all versions prior to 2.1.0",
    "statement": "Red Hat is aware of this issue and is working on a fix.",
    "cwe_id": "CWE-787",
    "unembargo_dt": datetime(2024, 1, 15),
    "source": "REDHAT",
    "reported_dt": datetime(2023, 12, 1, 10, 30, 0),
    "is_major_incident": True
}

# Create the flaw
new_flaw = session.flaws.create(form_data=flaw_data)

# Create with specific API version
new_flaw = session.flaws.create(form_data=flaw_data, api_version="v1")
```

**Working with the Response:**
```python
# Access the created flaw's properties
print(f"Created flaw: {new_flaw.cve_id}")
print(f"UUID: {new_flaw.uuid}")
print(f"Impact: {new_flaw.impact}")
```

See `/POST /osidb/api/{api_version}/flaws` in the [API documentation](osidb_bindings/openapi_schema.yml) for details on required fields, request format, and response structure.

#### `update`
Update an existing resource with new data. This operation requires appropriate permissions and may need Bugzilla/Jira API keys depending on the resource type.

**Basic Usage:**
```python
# First, retrieve the existing flaw
existing_flaw = session.flaws.retrieve(id="CVE-1111-2222")

# Convert to dictionary for modification
flaw_data = existing_flaw.to_dict()

# Update specific fields
flaw_data["impact"] = "IMPORTANT"
flaw_data["title"] = "Updated vulnerability title"
flaw_data["statement"] = "Updated security statement"

# Apply the update
updated_flaw = session.flaws.update(id=existing_flaw.uuid, form_data=flaw_data)

# Update with specific API version
updated_flaw = session.flaws.update(
    id=existing_flaw.uuid,
    form_data=flaw_data,
    api_version="v1"
)
```

**Working with the Response:**
```python
# Verify the update was successful
print(f"Updated flaw: {updated_flaw.cve_id}")
print(f"New impact: {updated_flaw.impact}")
print(f"Last updated: {updated_flaw.updated_dt}")
```

See `/PUT /osidb/api/{api_version}/flaws/{id}` in the [API documentation](osidb_bindings/openapi_schema.yml) for details on required fields and request format.

#### `delete`
Delete an existing resource. This operation requires appropriate permissions.

**Basic Usage:**
```python
# Delete by CVE ID
delete_response = session.flaws.delete(id="CVE-1111-2222")

# Delete by UUID
delete_response = session.flaws.delete(id="aedb854d-1afc-40fe-9554-bc50098b0154")

# Delete with specific API version
delete_response = session.flaws.delete(id="CVE-1111-2222", api_version="v1")
```

See `/DELETE /osidb/api/{api_version}/flaws/{id}` in the [API documentation](osidb_bindings/openapi_schema.yml) for details on response format and required permissions.

#### Extra Operations

Some resources have additional operations beyond the standard CRUD operations:

**Flaws:**
- `promote` - Advance a flaw through workflow (POST `/osidb/api/v1/flaws/{flaw_id}/promote`)
- `reject` - Reject a flaw (POST `/osidb/api/v1/flaws/{flaw_id}/reject`)

**Trackers:**
- `file` - Given a list of flaws, generates a list of suggested trackers to file (POST `/trackers/api/v1/file`)

**Examples:**
```python
# Promote a flaw
promote_response = session.flaws.promote(id="CVE-1111-2222")

# Reject a flaw with rejection data
reject_data = {"reason": "duplicate"}
reject_response = session.flaws.reject(id="CVE-1111-2222", form_data=reject_data)

# File trackers
file_data = {"flaw_uuids": ["3fa85f64-5717-4562-b3fc-2c963f66afa6"]}
trackers_response = session.trackers.file(form_data=file_data)
```


## Working with Responses

This section describes how to work with responses from session operations.

### Single Resource Response

Single resource responses are typically returned from `retrieve`, `create`, `update`, or `status` operations. The retrieved data is encapsulated within the corresponding model class.

**Accessing Response Data:**
```python
flaw = session.flaws.retrieve(id="CVE-1111-2222")

# Access attributes directly
print(flaw.uuid)
print(flaw.cve_id)
print(flaw.impact)
print(flaw.title)

# Impact enum example
print(flaw.impact)  # <ImpactEnum.MODERATE: 'MODERATE'>
print(flaw.impact.value)  # "MODERATE"

# Access nested objects
if flaw.affects:
    for affect in flaw.affects:
        print(f"Affect UUID: {affect.uuid}")
        if affect.trackers:
            for tracker in affect.trackers:
                print(f"Tracker: {tracker.external_system_id}")
```

**Converting to Dictionary:**
```python
flaw_dict = flaw.to_dict()

# Access as dictionary
print(flaw_dict["uuid"])
print(flaw_dict["impact"])
print(flaw_dict["affects"])

# Useful for modifications
flaw_dict["impact"] = "CRITICAL"
updated_flaw = session.flaws.update(id=flaw.uuid, form_data=flaw_dict)
```

### Paginated Response

Paginated responses are returned from `retrieve_list` and `search` operations. They contain metadata about the total count, pagination links, and the actual results.

**Basic Paginated Response Structure:**
```python
paginated_response = session.flaws.retrieve_list(limit=5)

# Access pagination metadata
print(f"Total count: {paginated_response.count}")
print(f"Previous page: {paginated_response.previous}")
print(f"Next page: {paginated_response.next_}")

# Access the actual results
print(f"Results on this page: {len(paginated_response.results)}")
for flaw in paginated_response.results:
    print(f"CVE: {flaw.cve_id}, Impact: {flaw.impact}")
```

**Pagination Properties:**
```python
# Total number of items across all pages
total_items = paginated_response.count

# URL for the next page (None if last page)
next_page_url = paginated_response.next_

# URL for the previous page (None if first page)
previous_page_url = paginated_response.previous

# List of items on current page
current_page_items = paginated_response.results
```

**Pagination Helpers:**

Each paginated response includes helper methods for convenient navigation:

```python
# Get first page
page_1 = session.flaws.retrieve_list()

# Navigate to next page
page_2 = page_1.next()  # Returns None if no next page

# Navigate back to previous page
back_to_page_1 = page_2.prev()  # Returns None if no previous page

# Check if navigation is possible
if page_1.next_:  # Check if next page URL exists
    page_2 = page_1.next()
```

**Iterator for All Pages:**

Use the `.iterator` property to loop through all remaining pages:

```python
first_page = session.flaws.retrieve_list()

# Process all pages starting from the second page
for page in first_page.iterator:
    for flaw in page.results:
        print(f"Processing {flaw.cve_id}")

# Iterator can start from any page
some_page = session.flaws.retrieve_list(offset=100)
for page in some_page.iterator:
    for flaw in page.results:
        process_flaw(flaw)
```

> **Note:** Working with individual items in paginated results is identical to working with single resource responses.

## Utility Functions

The bindings provide utility functions for common use cases.

### `cve_ids`

Retrieve a list of all CVE IDs with automatic pagination handling.

```python
import osidb_bindings

# Get all CVE IDs
all_cve_ids = osidb_bindings.cve_ids(session)
print(all_cve_ids)
# ['CVE-2021-43527', 'CVE-2021-3984', 'CVE-2021-4019', ...]

# Use the CVE IDs for further processing
for cve_id in all_cve_ids:
    flaw = session.flaws.retrieve(id=cve_id)
    print(f"{cve_id}: {flaw.impact}")
```

This function handles pagination automatically, so you don't need to worry about managing page offsets or limits.

## Debugging and Error Handling

Since the bindings communicate with a remote OSIDB database, various errors can occur during HTTP communication. Proper error handling is essential for robust applications.

### Exception Handling

**Basic Exception Handling:**
```python
from requests import HTTPError

try:
    flaw = session.flaws.retrieve(id="CVE-1111-2222")
    print(f"Retrieved flaw: {flaw.cve_id}")
except HTTPError as exc:
    print(f"HTTP Error: {exc.response.status_code}")
    print(f"Response content: {exc.response.content}")
except Exception as exc:
    print(f"Unexpected error: {exc}")
```

**Handling Specific Error Scenarios:**
```python
try:
    # Attempt to create a flaw
    new_flaw = session.flaws.create(form_data=flaw_data)
except HTTPError as exc:
    if exc.response.status_code == 400:
        print("Bad request - check your data format")
        print(exc.response.content)
    elif exc.response.status_code == 401:
        print("Authentication failed - check your credentials")
    elif exc.response.status_code == 403:
        print("Permission denied - insufficient privileges")
    elif exc.response.status_code == 404:
        print("Resource not found")
    else:
        print(f"HTTP {exc.response.status_code}: {exc.response.content}")
```

**Common Error Sources:**
- Network connectivity issues
- Authentication failures
- Invalid request data
- Permission restrictions
- Resource not found
- Server-side errors

**Best Practices:**
- Always wrap API calls in try-except blocks
- Log error details for debugging
- Check response status codes for specific error handling
- Validate input data before sending requests
