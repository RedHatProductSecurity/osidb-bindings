import datetime
from typing import Any, Dict, List, Optional, Union

import requests

from ...client import AuthenticatedClient
from ...models.osidb_api_v1_flaws_list_impact import OsidbApiV1FlawsListImpact
from ...models.osidb_api_v1_flaws_list_resolution import OsidbApiV1FlawsListResolution
from ...models.osidb_api_v1_flaws_list_response_200 import (
    OsidbApiV1FlawsListResponse200,
)
from ...models.osidb_api_v1_flaws_list_source import OsidbApiV1FlawsListSource
from ...models.osidb_api_v1_flaws_list_state import OsidbApiV1FlawsListState
from ...models.osidb_api_v1_flaws_list_type import OsidbApiV1FlawsListType
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "bz_id": float,
    "changed_after": datetime.datetime,
    "changed_before": datetime.datetime,
    "created_dt": datetime.datetime,
    "cve_id": List[str],
    "cvss2": str,
    "cvss2_score": float,
    "cvss3": str,
    "cvss3_score": float,
    "cwe_id": str,
    "description": str,
    "embargoed": bool,
    "exclude_fields": List[str],
    "flaw_meta_type": List[str],
    "impact": OsidbApiV1FlawsListImpact,
    "include_fields": List[str],
    "include_meta_attr": List[str],
    "limit": int,
    "offset": int,
    "reported_dt": datetime.datetime,
    "resolution": OsidbApiV1FlawsListResolution,
    "search": str,
    "source": OsidbApiV1FlawsListSource,
    "state": OsidbApiV1FlawsListState,
    "statement": str,
    "summary": str,
    "title": str,
    "tracker_ids": List[str],
    "type": OsidbApiV1FlawsListType,
    "unembargo_dt": datetime.datetime,
    "updated_dt": datetime.datetime,
    "uuid": str,
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    bz_id: Union[Unset, None, float] = UNSET,
    changed_after: Union[Unset, None, datetime.datetime] = UNSET,
    changed_before: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    cve_id: Union[Unset, None, List[str]] = UNSET,
    cvss2: Union[Unset, None, str] = UNSET,
    cvss2_score: Union[Unset, None, float] = UNSET,
    cvss3: Union[Unset, None, str] = UNSET,
    cvss3_score: Union[Unset, None, float] = UNSET,
    cwe_id: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    flaw_meta_type: Union[Unset, None, List[str]] = UNSET,
    impact: Union[Unset, None, OsidbApiV1FlawsListImpact] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    resolution: Union[Unset, None, OsidbApiV1FlawsListResolution] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, OsidbApiV1FlawsListSource] = UNSET,
    state: Union[Unset, None, OsidbApiV1FlawsListState] = UNSET,
    statement: Union[Unset, None, str] = UNSET,
    summary: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    tracker_ids: Union[Unset, None, List[str]] = UNSET,
    type: Union[Unset, None, OsidbApiV1FlawsListType] = UNSET,
    unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/osidb/api/v1/flaws".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_changed_after: Union[Unset, None, str] = UNSET
    if not isinstance(changed_after, Unset):
        json_changed_after = changed_after.isoformat() if changed_after else None

    json_changed_before: Union[Unset, None, str] = UNSET
    if not isinstance(changed_before, Unset):
        json_changed_before = changed_before.isoformat() if changed_before else None

    json_created_dt: Union[Unset, None, str] = UNSET
    if not isinstance(created_dt, Unset):
        json_created_dt = created_dt.isoformat() if created_dt else None

    json_cve_id: Union[Unset, None, List[str]] = UNSET
    if not isinstance(cve_id, Unset):
        if cve_id is None:
            json_cve_id = None
        else:
            json_cve_id = cve_id

    json_exclude_fields: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        if exclude_fields is None:
            json_exclude_fields = None
        else:
            json_exclude_fields = exclude_fields

    json_flaw_meta_type: Union[Unset, None, List[str]] = UNSET
    if not isinstance(flaw_meta_type, Unset):
        if flaw_meta_type is None:
            json_flaw_meta_type = None
        else:
            json_flaw_meta_type = flaw_meta_type

    json_impact: Union[Unset, None, str] = UNSET
    if not isinstance(impact, Unset):

        json_impact = OsidbApiV1FlawsListImpact(impact).value if impact else None

    json_include_fields: Union[Unset, None, List[str]] = UNSET
    if not isinstance(include_fields, Unset):
        if include_fields is None:
            json_include_fields = None
        else:
            json_include_fields = include_fields

    json_include_meta_attr: Union[Unset, None, List[str]] = UNSET
    if not isinstance(include_meta_attr, Unset):
        if include_meta_attr is None:
            json_include_meta_attr = None
        else:
            json_include_meta_attr = include_meta_attr

    json_reported_dt: Union[Unset, None, str] = UNSET
    if not isinstance(reported_dt, Unset):
        json_reported_dt = reported_dt.isoformat() if reported_dt else None

    json_resolution: Union[Unset, None, str] = UNSET
    if not isinstance(resolution, Unset):

        json_resolution = (
            OsidbApiV1FlawsListResolution(resolution).value if resolution else None
        )

    json_source: Union[Unset, None, str] = UNSET
    if not isinstance(source, Unset):

        json_source = OsidbApiV1FlawsListSource(source).value if source else None

    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):

        json_state = OsidbApiV1FlawsListState(state).value if state else None

    json_tracker_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(tracker_ids, Unset):
        if tracker_ids is None:
            json_tracker_ids = None
        else:
            json_tracker_ids = tracker_ids

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):

        json_type = OsidbApiV1FlawsListType(type).value if type else None

    json_unembargo_dt: Union[Unset, None, str] = UNSET
    if not isinstance(unembargo_dt, Unset):
        json_unembargo_dt = unembargo_dt.isoformat() if unembargo_dt else None

    json_updated_dt: Union[Unset, None, str] = UNSET
    if not isinstance(updated_dt, Unset):
        json_updated_dt = updated_dt.isoformat() if updated_dt else None

    params: Dict[str, Any] = {
        "bz_id": bz_id,
        "changed_after": json_changed_after,
        "changed_before": json_changed_before,
        "created_dt": json_created_dt,
        "cve_id": json_cve_id,
        "cvss2": cvss2,
        "cvss2_score": cvss2_score,
        "cvss3": cvss3,
        "cvss3_score": cvss3_score,
        "cwe_id": cwe_id,
        "description": description,
        "embargoed": embargoed,
        "exclude_fields": json_exclude_fields,
        "flaw_meta_type": json_flaw_meta_type,
        "impact": json_impact,
        "include_fields": json_include_fields,
        "include_meta_attr": json_include_meta_attr,
        "limit": limit,
        "offset": offset,
        "reported_dt": json_reported_dt,
        "resolution": json_resolution,
        "search": search,
        "source": json_source,
        "state": json_state,
        "statement": statement,
        "summary": summary,
        "title": title,
        "tracker_ids": json_tracker_ids,
        "type": json_type,
        "unembargo_dt": json_unembargo_dt,
        "updated_dt": json_updated_dt,
        "uuid": uuid,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsidbApiV1FlawsListResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsidbApiV1FlawsListResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsidbApiV1FlawsListResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsidbApiV1FlawsListResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    bz_id: Union[Unset, None, float] = UNSET,
    changed_after: Union[Unset, None, datetime.datetime] = UNSET,
    changed_before: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    cve_id: Union[Unset, None, List[str]] = UNSET,
    cvss2: Union[Unset, None, str] = UNSET,
    cvss2_score: Union[Unset, None, float] = UNSET,
    cvss3: Union[Unset, None, str] = UNSET,
    cvss3_score: Union[Unset, None, float] = UNSET,
    cwe_id: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    flaw_meta_type: Union[Unset, None, List[str]] = UNSET,
    impact: Union[Unset, None, OsidbApiV1FlawsListImpact] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    resolution: Union[Unset, None, OsidbApiV1FlawsListResolution] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, OsidbApiV1FlawsListSource] = UNSET,
    state: Union[Unset, None, OsidbApiV1FlawsListState] = UNSET,
    statement: Union[Unset, None, str] = UNSET,
    summary: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    tracker_ids: Union[Unset, None, List[str]] = UNSET,
    type: Union[Unset, None, OsidbApiV1FlawsListType] = UNSET,
    unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Response[OsidbApiV1FlawsListResponse200]:
    kwargs = _get_kwargs(
        client=client,
        bz_id=bz_id,
        changed_after=changed_after,
        changed_before=changed_before,
        created_dt=created_dt,
        cve_id=cve_id,
        cvss2=cvss2,
        cvss2_score=cvss2_score,
        cvss3=cvss3,
        cvss3_score=cvss3_score,
        cwe_id=cwe_id,
        description=description,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        flaw_meta_type=flaw_meta_type,
        impact=impact,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
        limit=limit,
        offset=offset,
        reported_dt=reported_dt,
        resolution=resolution,
        search=search,
        source=source,
        state=state,
        statement=statement,
        summary=summary,
        title=title,
        tracker_ids=tracker_ids,
        type=type,
        unembargo_dt=unembargo_dt,
        updated_dt=updated_dt,
        uuid=uuid,
    )

    response = requests.get(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    bz_id: Union[Unset, None, float] = UNSET,
    changed_after: Union[Unset, None, datetime.datetime] = UNSET,
    changed_before: Union[Unset, None, datetime.datetime] = UNSET,
    created_dt: Union[Unset, None, datetime.datetime] = UNSET,
    cve_id: Union[Unset, None, List[str]] = UNSET,
    cvss2: Union[Unset, None, str] = UNSET,
    cvss2_score: Union[Unset, None, float] = UNSET,
    cvss3: Union[Unset, None, str] = UNSET,
    cvss3_score: Union[Unset, None, float] = UNSET,
    cwe_id: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    embargoed: Union[Unset, None, bool] = UNSET,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    flaw_meta_type: Union[Unset, None, List[str]] = UNSET,
    impact: Union[Unset, None, OsidbApiV1FlawsListImpact] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
    include_meta_attr: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    reported_dt: Union[Unset, None, datetime.datetime] = UNSET,
    resolution: Union[Unset, None, OsidbApiV1FlawsListResolution] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, OsidbApiV1FlawsListSource] = UNSET,
    state: Union[Unset, None, OsidbApiV1FlawsListState] = UNSET,
    statement: Union[Unset, None, str] = UNSET,
    summary: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    tracker_ids: Union[Unset, None, List[str]] = UNSET,
    type: Union[Unset, None, OsidbApiV1FlawsListType] = UNSET,
    unembargo_dt: Union[Unset, None, datetime.datetime] = UNSET,
    updated_dt: Union[Unset, None, datetime.datetime] = UNSET,
    uuid: Union[Unset, None, str] = UNSET,
) -> Optional[OsidbApiV1FlawsListResponse200]:
    """ """

    return sync_detailed(
        client=client,
        bz_id=bz_id,
        changed_after=changed_after,
        changed_before=changed_before,
        created_dt=created_dt,
        cve_id=cve_id,
        cvss2=cvss2,
        cvss2_score=cvss2_score,
        cvss3=cvss3,
        cvss3_score=cvss3_score,
        cwe_id=cwe_id,
        description=description,
        embargoed=embargoed,
        exclude_fields=exclude_fields,
        flaw_meta_type=flaw_meta_type,
        impact=impact,
        include_fields=include_fields,
        include_meta_attr=include_meta_attr,
        limit=limit,
        offset=offset,
        reported_dt=reported_dt,
        resolution=resolution,
        search=search,
        source=source,
        state=state,
        statement=statement,
        summary=summary,
        title=title,
        tracker_ids=tracker_ids,
        type=type,
        unembargo_dt=unembargo_dt,
        updated_dt=updated_dt,
        uuid=uuid,
    ).parsed
