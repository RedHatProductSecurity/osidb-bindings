# osidb-bindings
Python bindings for accessing the OSIDB API endpoints in the simplest way
without any deep knowledge about HTTP

## Requirements

* Python 3
* pip

## Installation

You can install the bindings via Python 3 pip:

* from [PyPI](https://pypi.org/project/osidb-bindings/)
    ```
    pip install osidb-bindings
    ```
* directly from the [GitLab](https://git.prodsec.redhat.com/devops/osidb-bindings) repository (will install the version
    from master branch)
    ```
    pip install -e git+https://git.prodsec.redhat.com/devops/osidb-bindings.git#egg=osidb_bindings
    ```
* OPTIONAL - directly from the [GitLab](https://git.prodsec.redhat.com/devops/osidb-bindings) repository with branch specification
    ```
    pip install -e git+https://git.prodsec.redhat.com/devops/osidb-bindings.git@<branch_name>#egg=osidb_bindings
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
Session is the main part of the bindings which you will be using. You can create it using the `osidb_bindings.new_session`. Created session is then used to access the various endpoints.

You must always specify `osidb_server_uri` of the OSIDB instance you want to access, in this tutorial, we will be accessing local instance of OSIDB hosted on port 8000

OSIDB uses token (JWT) authentication on most of the endpoints. Bindings handles the token refresh for you. All you need to do is to specify which method is supposed to be used for obtaining the token. OSIDB currently supports two main authentication mechanisms on the token endpoints:
* Basic authentication - `username` and `password` (used on the OSIDB instances without the kerberos authentication enabled)
    ```python
    session = osidb_bindings.new_session(osidb_server_uri="http://localhost:8000/", username="username", password="password")
    ```
* Kerberos authentication - default (used on the OSIDB instances with kerberos authentication enabled)
    ```python
    session = osidb_bindings.new_session(osidb_server_uri="http://localhost:8000/")
    ```

By default, the SSL verification is enabled and the path to the cert file is obtained from the `SSL_CERT_FILE`, `REQUEST_CA_BUNDLE` or `CURL_CA_BUNDLE` environmental variables in respective order. If none of these variables are set, the default trusted CA is used (`/etc/pki/ca-trust/extracted/openssl/ca-bundle.trust.crt`). You can change the behavior of the ssl verification either via the mentioned environmental variables or directly via `verify_ssl` argument.
```python
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

* #### ```retrieve```
    Retrieve a single Flaw with specified `id`.


    See `/GET /osidb/api/{api_version}/flaws/{id}` in [API docs](openapi_schema.yml) for more details (query parameters, response format, etc.)
    ```python
    # CVE ID
    flaw1_response = session.retrieve(id="CVE-1111-2222")

    # UUID
    flaw2_response = session.retrieve(id="aedb854d-1afc-40fe-9554-bc50098b0154")
    ```

* #### ```retrieve_list```
    Retrieve a list of Flaws. You can filter the flaws using the query parameters.

    See `/GET /osidb/api/{api_version}/flaws` in [API docs](openapi_schema.yml) for more details (query parameters, response format, etc.)
    ```python
    all_flaws_response = session.retrieve_list()

    # string query parameters
    critical_impact_flaws_response = session.retrieve_list(impact="CRITICAL")
    internet_source_flaws_response = session.retrieve_list(source="INTERNET")

    # datetime query parameters
    from datetime import datetime
    changed_before_flaws_response = session.retrieve_list(changed_before=datetime.now())
    changed_after_flaws_response = session.retrieve_list(changed_after=datetime(2021,7,13))
    changed_after_and_before_response = session.retrieve_list(
        changed_after=datetime.strptime("2021-07-13", "%Y-%m-%d"),
        changed_before=datetime.strptime("2021-12-24", "%Y-%m-%d"),
    )


    # comma separated list query parameters
    specified_cves_flaws_response = session.retrieve_list(cve_ids="CVE-1111-2222,CVE-1111-2223")

    multiple_criteria_flaws_response = session.retrieve_list(type="VULNERABILITY", impact="LOW", changed_after=datetime(2021,7,12))
    ```

* #### ```search```
    Retrieve a list of Flaws. Performs full text search filter.
    ```python
    search_response = session.search("Red Hat Satellite v.5")
    cve_search_response = session.search("CVE-1111-2222")
    ```

* #### ```create```
    Create a new Flaw from given data.

    See `/POST /osidb/api/{api_version}/flaws` in [API docs](openapi_schema.yml) for more details (query parameters, request format, response format, etc.)
    ```python
    from datetime import datetime
    create_data = {
        "type": "VULNERABILITY",
        "cve_id": "CVE-1111-2222",
        "state": "NEW",
        "resolution": "NONE",
        "impact": "LOW",
        "title": "New title",
        "description": "New description",
        "summary": "New summary",
        "statement": "New statement",
        "cwe_id": "CWE-123",
        "unembargo_dt": datetime(2022,1,1),
        "source": "ADOBE",
        "reported_dt": "2022-02-10T15:27:24.131Z",
        "mitigated_by": "SELINUX",
        "cvss3": "8.8/CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H",
        "cvss3_score": 8.8,
        "is_major_incident": False
    }

    create_flaw_response = session.create(form_data=create_data)
    ```

* #### ```update```
    Update an existing Flaw with given data.

    See `/POST /osidb/api/{api_version}/flaws` in [API docs](openapi_schema.yml) for more details (query parameters, request format, response format, etc.)
    ```python
    update_data = {
        "cve_id": "CVE-1111-3333",
        "resolution": "ERRATA",
        "impact": "MEDIUM",
    }

    update_flaw_response = session.create(id="CVE-1111-2222", form_data=update_data)
    ```

* #### ```delete```
    NOT YET SUPPORTED

### Response

This section describes how to work with responses. See [operations section](#session-operations) to learn how to get these responses.

#### Single response
This response is typically retrieved from the [retrieve](#retrieve) or [status](#status) operations and you receive only one item of desired resource in the response.

Retrieved data are encapsulated in respective model of the retrieved resource which is build on the bindings side.

```python
single_response = session.retrieve(id="CVE-1111-2222")

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
You can view overall count of responses, previous and next segment query (based on the `offset` and `limit` values) and content of the current segment.

```python
paginated_response = session.retrieve_list(limit=5)

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

Work with each item of the results is basically identical to work with [single response](#single-response)

### Utils

There are some utility functions which can help you with common use cases of the bindings.

* #### ```cve_ids```
    Retrieve list of all CVE IDs. Takes care of the response pagination.
    ```python
    all_cve_ids = osidb_bindings.cve_ids(session)
    #  ['CVE-2021-43527', 'CVE-2021-3984', 'CVE-2021-4019', ... ]
    ```
