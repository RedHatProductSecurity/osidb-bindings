from typing import List
from .session import Session


def cve_ids(session: Session) -> List[str]:
    """Retrieve list of all CVE IDs"""
    limit = 100
    offset = 0
    cve_ids = []
    while True:
        response = session.retrieve_list(
            include_fields="cve_id", limit=limit, offset=offset
        )
        cve_ids.extend([result.cve_id for result in response.results])

        if not response.next_:
            break
        offset += limit
    return cve_ids
