from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, OSIDBModel, Unset

T = TypeVar("T", bound="FlawPostMetaAttr")


@attr.s(auto_attribs=True)
class FlawPostMetaAttr(OSIDBModel):
    """ """

    acknowledgments: Union[Unset, str] = UNSET
    acks_not_needed: Union[Unset, str] = UNSET
    affects: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    bz_datascore: Union[Unset, str] = UNSET
    bz_id: Union[Unset, str] = UNSET
    checklists: Union[Unset, str] = UNSET
    classification: Union[Unset, str] = UNSET
    cvss2: Union[Unset, str] = UNSET
    cvss2_score: Union[Unset, str] = UNSET
    cvss2_vector: Union[Unset, str] = UNSET
    cvss3: Union[Unset, str] = UNSET
    cvss3_comment: Union[Unset, str] = UNSET
    cvss3_score: Union[Unset, str] = UNSET
    cvss3_vector: Union[Unset, str] = UNSET
    cwe: Union[Unset, str] = UNSET
    depends_on: Union[Unset, str] = UNSET
    impact: Union[Unset, str] = UNSET
    jira_trackers: Union[Unset, str] = UNSET
    mitigate: Union[Unset, str] = UNSET
    mitigation: Union[Unset, str] = UNSET
    public: Union[Unset, str] = UNSET
    references: Union[Unset, str] = UNSET
    related_cves: Union[Unset, str] = UNSET
    reported: Union[Unset, str] = UNSET
    resolution: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    statement: Union[Unset, str] = UNSET
    task_owner: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        acknowledgments = self.acknowledgments
        acks_not_needed = self.acks_not_needed
        affects = self.affects
        alias = self.alias
        bz_datascore = self.bz_datascore
        bz_id = self.bz_id
        checklists = self.checklists
        classification = self.classification
        cvss2 = self.cvss2
        cvss2_score = self.cvss2_score
        cvss2_vector = self.cvss2_vector
        cvss3 = self.cvss3
        cvss3_comment = self.cvss3_comment
        cvss3_score = self.cvss3_score
        cvss3_vector = self.cvss3_vector
        cwe = self.cwe
        depends_on = self.depends_on
        impact = self.impact
        jira_trackers = self.jira_trackers
        mitigate = self.mitigate
        mitigation = self.mitigation
        public = self.public
        references = self.references
        related_cves = self.related_cves
        reported = self.reported
        resolution = self.resolution
        source = self.source
        state = self.state
        statement = self.statement
        task_owner = self.task_owner

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(acknowledgments, Unset):
            field_dict["acknowledgments"] = acknowledgments
        if not isinstance(acks_not_needed, Unset):
            field_dict["acks_not_needed"] = acks_not_needed
        if not isinstance(affects, Unset):
            field_dict["affects"] = affects
        if not isinstance(alias, Unset):
            field_dict["alias"] = alias
        if not isinstance(bz_datascore, Unset):
            field_dict["bz_datascore"] = bz_datascore
        if not isinstance(bz_id, Unset):
            field_dict["bz_id"] = bz_id
        if not isinstance(checklists, Unset):
            field_dict["checklists"] = checklists
        if not isinstance(classification, Unset):
            field_dict["classification"] = classification
        if not isinstance(cvss2, Unset):
            field_dict["cvss2"] = cvss2
        if not isinstance(cvss2_score, Unset):
            field_dict["cvss2_score"] = cvss2_score
        if not isinstance(cvss2_vector, Unset):
            field_dict["cvss2_vector"] = cvss2_vector
        if not isinstance(cvss3, Unset):
            field_dict["cvss3"] = cvss3
        if not isinstance(cvss3_comment, Unset):
            field_dict["cvss3_comment"] = cvss3_comment
        if not isinstance(cvss3_score, Unset):
            field_dict["cvss3_score"] = cvss3_score
        if not isinstance(cvss3_vector, Unset):
            field_dict["cvss3_vector"] = cvss3_vector
        if not isinstance(cwe, Unset):
            field_dict["cwe"] = cwe
        if not isinstance(depends_on, Unset):
            field_dict["depends_on"] = depends_on
        if not isinstance(impact, Unset):
            field_dict["impact"] = impact
        if not isinstance(jira_trackers, Unset):
            field_dict["jira_trackers"] = jira_trackers
        if not isinstance(mitigate, Unset):
            field_dict["mitigate"] = mitigate
        if not isinstance(mitigation, Unset):
            field_dict["mitigation"] = mitigation
        if not isinstance(public, Unset):
            field_dict["public"] = public
        if not isinstance(references, Unset):
            field_dict["references"] = references
        if not isinstance(related_cves, Unset):
            field_dict["related_cves"] = related_cves
        if not isinstance(reported, Unset):
            field_dict["reported"] = reported
        if not isinstance(resolution, Unset):
            field_dict["resolution"] = resolution
        if not isinstance(source, Unset):
            field_dict["source"] = source
        if not isinstance(state, Unset):
            field_dict["state"] = state
        if not isinstance(statement, Unset):
            field_dict["statement"] = statement
        if not isinstance(task_owner, Unset):
            field_dict["task_owner"] = task_owner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        acknowledgments = d.pop("acknowledgments", UNSET)

        acks_not_needed = d.pop("acks_not_needed", UNSET)

        affects = d.pop("affects", UNSET)

        alias = d.pop("alias", UNSET)

        bz_datascore = d.pop("bz_datascore", UNSET)

        bz_id = d.pop("bz_id", UNSET)

        checklists = d.pop("checklists", UNSET)

        classification = d.pop("classification", UNSET)

        cvss2 = d.pop("cvss2", UNSET)

        cvss2_score = d.pop("cvss2_score", UNSET)

        cvss2_vector = d.pop("cvss2_vector", UNSET)

        cvss3 = d.pop("cvss3", UNSET)

        cvss3_comment = d.pop("cvss3_comment", UNSET)

        cvss3_score = d.pop("cvss3_score", UNSET)

        cvss3_vector = d.pop("cvss3_vector", UNSET)

        cwe = d.pop("cwe", UNSET)

        depends_on = d.pop("depends_on", UNSET)

        impact = d.pop("impact", UNSET)

        jira_trackers = d.pop("jira_trackers", UNSET)

        mitigate = d.pop("mitigate", UNSET)

        mitigation = d.pop("mitigation", UNSET)

        public = d.pop("public", UNSET)

        references = d.pop("references", UNSET)

        related_cves = d.pop("related_cves", UNSET)

        reported = d.pop("reported", UNSET)

        resolution = d.pop("resolution", UNSET)

        source = d.pop("source", UNSET)

        state = d.pop("state", UNSET)

        statement = d.pop("statement", UNSET)

        task_owner = d.pop("task_owner", UNSET)

        flaw_post_meta_attr = cls(
            acknowledgments=acknowledgments,
            acks_not_needed=acks_not_needed,
            affects=affects,
            alias=alias,
            bz_datascore=bz_datascore,
            bz_id=bz_id,
            checklists=checklists,
            classification=classification,
            cvss2=cvss2,
            cvss2_score=cvss2_score,
            cvss2_vector=cvss2_vector,
            cvss3=cvss3,
            cvss3_comment=cvss3_comment,
            cvss3_score=cvss3_score,
            cvss3_vector=cvss3_vector,
            cwe=cwe,
            depends_on=depends_on,
            impact=impact,
            jira_trackers=jira_trackers,
            mitigate=mitigate,
            mitigation=mitigation,
            public=public,
            references=references,
            related_cves=related_cves,
            reported=reported,
            resolution=resolution,
            source=source,
            state=state,
            statement=statement,
            task_owner=task_owner,
        )

        flaw_post_meta_attr.additional_properties = d
        return flaw_post_meta_attr

    @staticmethod
    def get_fields():
        return {
            "acknowledgments": str,
            "acks_not_needed": str,
            "affects": str,
            "alias": str,
            "bz_datascore": str,
            "bz_id": str,
            "checklists": str,
            "classification": str,
            "cvss2": str,
            "cvss2_score": str,
            "cvss2_vector": str,
            "cvss3": str,
            "cvss3_comment": str,
            "cvss3_score": str,
            "cvss3_vector": str,
            "cwe": str,
            "depends_on": str,
            "impact": str,
            "jira_trackers": str,
            "mitigate": str,
            "mitigation": str,
            "public": str,
            "references": str,
            "related_cves": str,
            "reported": str,
            "resolution": str,
            "source": str,
            "state": str,
            "statement": str,
            "task_owner": str,
        }

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
