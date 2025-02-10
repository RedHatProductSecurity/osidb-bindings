# osidb-bindings
Python bindings for seamless access to OSIDB API endpoints, requiring no in-depth understanding of HTTP.

## Requirements

* Python 3
* pip

## Installation

You can install the bindings via:

* Python 3 pip from [PyPI](https://pypi.org/project/osidb-bindings/)
    ```
    pip install osidb-bindings
    ```
* RPM from [Fedora Copr](https://copr.fedorainfracloud.org/coprs/jazinner/osidb-bindings/)
    ```
    dnf copr enable jazinner/osidb-bindings
    dnf install osidb_bindings
    ```
* Python 3 pip directly from the [GitHub](https://github.com/RedHatProductSecurity/osidb-bindings) repository (will install the version
    from master branch)
    ```
    pip install -e git+https://github.com/RedHatProductSecurity/osidb-bindings.git#egg=osidb_bindings
    ```
* OPTIONAL - Python 3 pip directly from the [GitHub](https://github.com/RedHatProductSecurity/osidb-bindings) repository with branch specification
    ```
    pip install -e git+https://github.com/RedHatProductSecurity/osidb-bindings.git@<branch_name>#egg=osidb_bindings
    ```

## OSIDB Compatibility

OSIDB and bindings both uses [semantic versioning](https://semver.org/) (eg. MAJOR.MINOR.PATCH, 1.2.3). Bindings are compatible
with OSIDB when MAJOR and MINOR version matches.

Eg.
* OSIDB 1.2.0, bindings 1.2.0 - compatible
* OSIDB 1.2.0, bindings 1.2.1 - compatible
* OSIDB 1.2.2, bindings 1.2.1 - compatible
* OSIDB 1.3.0, bindings 1.2.1 - **feature incomplete**
* OSIDB 2.0.0, bindings 1.9.9 - **incompatible**

**This compatibility starts from version 1.1.0. Any previous version of bindings is considered experimental and should not be used.**

## Usage

### Import the bindings

```python
import osidb_bindings
```

### Create a session
The Session is the core component of the bindings that you'll interact with. You can create a session using `osidb_bindings.new_session`. Once created, the session serves as the gateway to access various endpoints.

When initializing a session, you must specify the osidb_server_uri of the OSIDB instance you want to connect to. In this tutorial, we'll use a local OSIDB instance hosted on port 8000.

OSIDB relies on token-based (JWT) authentication for most endpoints. The bindings automatically handle token refreshing, so your primary task is to specify the method for obtaining the token. OSIDB currently supports two main authentication mechanisms for its token endpoints:
* Basic authentication - `username` and `password` (used for the OSIDB instances without the kerberos authentication enabled, mostly local instances)
    ```python
    session = osidb_bindings.new_session(osidb_server_uri="http://localhost:8000/", username="username", password="password")
    ```
* Kerberos authentication - default (used for the OSIDB instances with kerberos authentication enabled, production/stage/UAT)
    ```python
    session = osidb_bindings.new_session(osidb_server_uri="http://localhost:8000/")
    ```

Certain operations outlined in the [operations section](#session-operations) (primarily those involving creating or modifying content) will require Bugzilla API key or Jira Access Token to work properly.

* Valid Bugzilla API key is provided via `BUGZILLA_API_KEY` environment variable.

    ```bash
    export BUGZILLA_API_KEY="bugzilla api key"
    ```
* Valid Jira Access Token is provided via `JIRA_ACCESS_TOKEN` environment variable.

    ```bash
    export JIRA_ACCESS_TOKEN="jira access token"
    ```

SSL verification is enabled by default. To ensure proper functionality, you should set the `REQUESTS_CA_BUNDLE` environment variable to point to the location of the appropriate CA bundle. For example:

```bash
export REQUESTS_CA_BUNDLE="/etc/pki/tls/certs/ca-bundle.crt"
```

You can also pass the path to the CA bundle directly when creating the new session or you can disable the SSL verification:
```python
# default behavior, REQUESTS_CA_BUNDLE should be exported
session = osidb_bindings.new_session(osidb_server_uri="http://localhost:8000/", username="username", password="password", verify_ssl=True)

session = osidb_bindings.new_session(osidb_server_uri="http://localhost:8000/", username="username", password="password", verify_ssl="/path/to/cert")

session = osidb_bindings.new_session(osidb_server_uri="http://localhost:8000/", username="username", password="password", verify_ssl=False)
```

### Session operations

This section describes possible session operations. See [response section](#response) to learn how to work with obtained operation responses.

* #### ```status```
    Most basic operation of the session is retrieving the status. You can verify that your session can successfully access the OSIDB using this operation.

    See `/GET /osidb/api/{api_version}/status` in [API docs](openapi_schema.yml) for more details (query parameters, response format, etc.)
    ```python
    status_response = session.status()
    ```

Operations can be performed on the following resources/subresources (also some of the resources/subresources do have extra operations):
* flaws
    * acknowledgments
    * comments
    * cvss_scores
    * labels
    * packages_versions
    * references
    * extra operations
        * promote
        * reject
* affects
    * cvss_scores
* trackers
    * extra operations
        * file
* labels

Following operations are demonstrated on `flaws` resource, to work with different resource, just replace the `flaws` with the name of the resource. In case of subresources like `flaw comments`, `flaw references`, etc. you can use the dot notation like this `session.flaws.comments.retrieve(...)`.

* #### ```retrieve```
    Retrieve a single resource with specified `id`.


    See `/GET /osidb/api/{api_version}/flaws/{id}` in [API docs](openapi_schema.yml) for more details (query parameters, response format, etc.)
    ```python
    # CVE ID
    flaw1_response = session.flaws.retrieve(id="CVE-1111-2222")

    # UUID
    flaw2_response = session.flaws.retrieve(id="aedb854d-1afc-40fe-9554-bc50098b0154")
    ```

* #### ```retrieve_list```
    Retrieve a list of Flaws. You can filter the flaws using the query parameters. Results are paginated, see [paginated response section](#paginated-response).

    See `/GET /osidb/api/{api_version}/flaws` in [API docs](openapi_schema.yml) for more details (query parameters, response format, etc.)
    ```python
    all_flaws_response = session.flaws.retrieve_list()

    # string query parameters
    critical_impact_flaws_response = session.flaws.retrieve_list(impact="CRITICAL")
    internet_source_flaws_response = session.flaws.retrieve_list(source="INTERNET")

    # datetime query parameters
    from datetime import datetime
    changed_before_flaws_response = session.flaws.retrieve_list(changed_before=datetime.now())
    changed_after_flaws_response = session.flaws.retrieve_list(changed_after=datetime(2021,7,13))
    changed_after_and_before_response = session.flaws.retrieve_list(
        changed_after=datetime.strptime("2021-07-13", "%Y-%m-%d"),
        changed_before=datetime.strptime("2021-12-24", "%Y-%m-%d"),
    )

    # comma separated list query parameters
    specified_cves_flaws_response = session.flaws.retrieve_list(cve_ids="CVE-1111-2222,CVE-1111-2223")

    # multiple query parameters specifying multiple filter conditions
    multiple_criteria_flaws_response = session.flaws.retrieve_list(source="REDHAT", impact="LOW", changed_after=datetime(2021,7,12))
    ```

* #### ```retrieve_list_iterator```
    Retrieve a list of Flaws. You can filter the flaws using the query parameters. Handles the pagination and returns the generator of individual resource entities.

    See `/GET /osidb/api/{api_version}/flaws` in [API docs](openapi_schema.yml) for more details (query parameters, response format, etc.)

    ```python
    all_flaws = session.flaws.retrieve_list_iterator()
    for flaw in all_flaws:
        do_calc(flaw)

    # string query parameters
    critical_impact_flaws = session.flaws.retrieve_list_iterator(impact="CRITICAL")
    for flaw in critical_impact_flaws:
        print(flaw.impact)
    ```
    For the rest of the examples refer to the [retrieve_list](#retrieve_list)

* #### ```retrieve_list_iterator_async```
    Retrieve a list of Flaws. Handles the pagination and returns the generator of individual resource entities. Uses asynchronous communitation
    to speed up the data retrieval.

    By default, the system allows up to 10 concurrent connections. This limit can be adjusted by setting the `OSIDB_BINDINGS_MAX_CONCURRENCY` environment variable. It is highly recommended to keep the limit between 1 and 50 concurrent connections. Exceeding this limit may lead to service overload, which could be interpreted as a Denial-of-Service attack.

    ```bash
    export OSIDB_BINDINGS_MAX_CONCURRENCY=30
    ```

    Using the argument `max_results` you can limit the number of results returned.


    See `/GET /osidb/api/{api_version}/flaws` in [API docs](openapi_schema.yml) for more details (query parameters, response format, etc.)

    ```python
    all_flaws = session.flaws.retrieve_list_iterator_async()
    for flaw in all_flaws:
        do_calc(flaw)

    # string query parameters
    critical_impact_flaws = session.flaws.retrieve_list_iterator_async(impact="CRITICAL")
    for flaw in critical_impact_flaws:
        print(flaw.impact)

    # get the first 200 results
    for flaw in session.flaws.retrieve_list_iterator_async(max_results=200):
        do_calc(flaw)
    ```
    For the rest of the examples refer to the [retrieve_list](#retrieve_list)

* #### ```count```

    Retrieve the the total count number of entities which would be returned by the same `retrieve_list` call. In terms of the input arguments this operation behaves the same as `retrieve_list`.

    ```python
    low_impact_flaw_count = session.flaw.count(impact="LOW")
    ```

* #### ```search```
    Retrieve a list of Flaws. Performs full text search filter.
    ```python
    search_response = session.flaws.search("Red Hat Satellite v.5")
    cve_search_response = session.flaws.search("CVE-1111-2222")
    ```

* #### ```create```
    Create a new Flaw from given data.

    See `/POST /osidb/api/{api_version}/flaws` in [API docs](openapi_schema.yml) for more details (query parameters, request format, response format, etc.)
    ```python
    from datetime import datetime
    create_data = {
        "cve_id": "CVE-1111-2222",
        "state": "NEW",
        "impact": "LOW",
        "title": "New title",
        "components": ["component1", "component2"],
        "cve_description": "New CVE description",
        "comment_zero": "New comment zero",
        "statement": "New statement",
        "cwe_id": "CWE-123",
        "unembargo_dt": datetime(2022,1,1),
        "source": "ADOBE",
        "reported_dt": "2022-02-10T15:27:24.131Z",
        "is_major_incident": False
    }

    create_flaw_response = session.flaws.create(form_data=create_data)
    ```

* #### ```update```
    Update an existing Flaw with given data.

    See `/POST /osidb/api/{api_version}/flaws` in [API docs](openapi_schema.yml) for more details (query parameters, request format, response format, etc.)
    ```python

    flaw_response = session.flaws.retrieve(id="CVE-1111-2222")
    flaw_data = flaw_response.to_dict()
    flaw_data["cve_id"] = "CVE-1111-3333"
    flaw_data["impact"] = "MEDIUM"

    update_flaw_response = session.flaws.update(id=flaw_response.uuid, form_data=flaw_data)
    ```

* #### ```delete```
    Delete an existing Flaw

    See `/DELETE /osidb/api/{api_version}/flaws/{id}` in [API docs](openapi_schema.yml) for more details (query parameters, request format, response format, etc.)
    ```python
    delete_flaw_response = session.flaws.delete(id="CVE-1111-2222")
    ```

* #### ```extra operations```

    * Flaws
        * `promote` - advance a flaw through workflow (**POST** `/osidb/api/v1/flaws/{flaw_id}/promote` functionality)
        * `reject` - reject a flaw (**POST** `/osidb/api/v1/flaws/{flaw_id}/reject` functionality)
    * Trackers
        * `file` - Given a list of flaws, generates a list of suggested trackers to file. (**POST** `/trackers/api/v1/file` functionality)


### Response

This section describes how to work with responses. See [operations section](#session-operations) to learn how to get these responses.

#### Single response
This response is typically retrieved from the [retrieve](#retrieve) or [status](#status) operations, where you receive a single item of the requested resource. The retrieved data is encapsulated within the corresponding model of the resource, which is constructed on the bindings side.

```python
single_response = session.flaws.retrieve(id="CVE-1111-2222")

single_response
# Flaw(uuid='4a41bafd-43e9-4255-b5cc-a554af8dbb0c', updated_dt=datetime.datetime(2021, 11, 19, 14, 19, 30, 15530, tzinfo=tzutc()), ... )
```

You can access all the model fields as attributes.

```python
single_response.uuid
# "4a41bafd-43e9-4255-b5cc-a554af8dbb0c"

single_response.impact
# <ImpactEnum.MODERATE: 'MODERATE'>

single_response.impact.value
# "MODERATE"

single_response.affects
# [Affect(uuid='6afed665-e62d-418f-ae8b-aab51d0fc3ef', trackers=[Tracker(uuid='4e465acc-a5ca-4c5e-a7fc-d8155aa3e944', type=<TrackerTypeEnum.BUGZILLA: 'BUGZILLA'>, external_system_id='1962596', additional_properties={})], ... ]

single_response.affects[0]
# Affect(uuid='6afed665-e62d-418f-ae8b-aab51d0fc3ef', trackers=[Tracker(uuid='4e465acc-a5ca-4c5e-a7fc-d8155aa3e944', type=<TrackerTypeEnum.BUGZILLA: 'BUGZILLA'>, external_system_id='1962596', additional_properties={})], ... )
```

Or you can convert the model to dictionary representation.

```python
single_response_dict = single_response.to_dict()

single_response_dict
# {'classification': {'workflow': 'DEFAULT', 'state': 'FIX'}, 'uuid': '4a41bafd-43e9-4255-b5cc-a554af8dbb0c','updated_dt': '2021-11-19T14:19:30.015530+00:00', 'type': 'VULNERABILITY', ... )

single_response_dict["uuid"]
# "4a41bafd-43e9-4255-b5cc-a554af8dbb0c"

single_response_dict["impact"]
# "MODERATE"

single_response_dict["affects"]
# [{'uuid': '6afed665-e62d-418f-ae8b-aab51d0fc3ef', 'trackers': [{'uuid': '4e465acc-a5ca-4c5e-a7fc-d8155aa3e944','type': 'BUGZILLA', 'external_system_id': '1962596'}], 'type': 'DEFAULT', 'state': 'AFFECTED', ... ]

single_response_dict["affects"][0]
# {'uuid': '6afed665-e62d-418f-ae8b-aab51d0fc3ef', 'trackers': [{'uuid': '4e465acc-a5ca-4c5e-a7fc-d8155aa3e944','type': 'BUGZILLA', 'external_system_id': '1962596'}], 'type': 'DEFAULT', 'state': 'AFFECTED', ... }
```

#### Paginated response
Paginated responses are typically retrieved from [retrieve_list](#retrieve_list) or [search](#search) operations.
You can view overall count of responses, previous and next page of a query (based on the `offset` and `limit` values) and content of the current page.

```python
paginated_response = session.flaws.retrieve_list(limit=5)

paginated_response
# PaginatedFlawListList(count=12, next_='http://localhost:8000/osidb/api/v1/flaws?limit=5&offset=5', previous=None, results=[FlawList(uuid='de4d4901-d489-4d23-b1e2-76e14cae206f', updated_dt=datetime.datetime(2021, 11, 19, 14, 34, 15, 724267, tzinfo=tzutc()), ... )

paginated_response.count
# 12

paginated_response.previous
# None

paginated_response.next_
# "http://localhost:8000/osidb/api/v1/flaws?limit=5&offset=5"

paginated_response.results
# [FlawList(uuid='de4d4901-d489-4d23-b1e2-76e14cae206f', updated_dt=datetime.datetime(2021, 11, 19, 14, 34, 15, 724267, tzinfo=tzutc()), ... ]

paginated_response.results[0]
# FlawList(uuid='de4d4901-d489-4d23-b1e2-76e14cae206f', updated_dt=datetime.datetime(2021, 11, 19, 14, 34, 15, 724267, tzinfo=tzutc()), ... )
```

Each paginated response comes also with pagination helpers which allows user to conveniently browse through all the pages without the need to adjust offset or limit. These methods are `.next()`, `.prev()` for basic navigation in both directions:

```python
paginated_response_page_1 = session.flaws.retrieve_list()

paginated_response_page_1
# PaginatedFlawListList(count=100, next_='http://localhost:8000/osidb/api/v1/flaws?limit=100', previous=None, results=[FlawList(uuid='de4d4901-d489-4d23-b1e2-76e14cae206f', updated_dt=datetime.datetime(2021, 11, 19, 14, 34, 15, 724267, tzinfo=tzutc()), ... )

paginated_response_page_1.prev()
# None

paginated_response_page_2 = paginated_response_page_1.next()

paginated_response_page_2
# PaginatedFlawListList(count=100, next_='http://localhost:8000/osidb/api/v1/flaws?limit=100&offset=100', previous=None, results=[FlawList(uuid='0ac7a852-c973-4f7b-8c78-978fbbb59c71', updated_dt=datetime.datetime(2021, 11, 20, 14, 45, 15, 724222, tzinfo=tzutc()), ... )

previous_response = paginated_response_page_2.prev()

previous_response
# PaginatedFlawListList(count=100, next_='http://localhost:8000/osidb/api/v1/flaws?limit=100', previous=None, results=[FlawList(uuid='de4d4901-d489-4d23-b1e2-76e14cae206f', updated_dt=datetime.datetime(2021, 11, 19, 14, 34, 15, 724267, tzinfo=tzutc()), ... )
# Same as paginated_response_page_1
```

and `.iterator` which returns iterable enabling looping through the rest of response pages in for loop:

```python
first_paginated_response = session.flaws.retrieve_list()
# loop through second, third, fourth, ... page
for page in paginated_response.iterator:
    for flaw in page:
        do_calc(flaw)
```

Iterator may begin from whichever page:

```python
# first response page
paginated_response_page_1 = session.flaws.retrieve_list()

# fourth response page
paginated_response_page_4 = paginated_response_page_1.next().next().next()

# iterator starting with fifth page
for response in paginated_response_page_4.iterator:
    for flaw in page:
        do_calc(flaw)
```

Working with each item of the results is basically identical to work with [single response](#single-response)

### Utils

There are some utility functions which can help you with common use cases of the bindings.

* #### ```cve_ids```
    Retrieve list of all CVE IDs. Takes care of the response pagination.
    ```python
    all_cve_ids = osidb_bindings.cve_ids(session)
    #  ['CVE-2021-43527', 'CVE-2021-3984', 'CVE-2021-4019', ... ]
    ```

### Debugging

As this package serves as a client to an existing database, most of its functionality depends on communication with that database. Consequently, errors are likely to occur during this communication, and it's crucial to handle such errors appropriately.

#### Exception handling

Exception handling is essential to ensure that your requests are properly managed, especially when HTTP communication fails due to issues such as network failure, incorrect requests, or invalid request bodies.

```python
flaw_response = session.flaws.retrieve(id="CVE-1111-2222")
flaw_data = flaw_response.to_dict()
# Invalid operation: Flaw cannot be embargoed again once unembargoed
flaw_data.embargoed = True

# Handling specific HTTPError exceptions
from requests import HTTPError
try:
    session.flaws.update(id=flaw_response.uuid, form_data=flaw_data)
except HTTPError as exc:
    print(exc.response.content)
    handle_exception(exc)

# Handling general exceptions
try:
    session.flaws.update(id=flaw_response.uuid, form_data=flaw_data)
except Exception as exc:
    handle_exception(exc)
```
