from dataclasses import dataclass
from typing import List

from pydantic import BaseModel, Field


@dataclass
class JobInformationFetchDeps:
    job_post_url: str


@dataclass
class JobDescriptionAgentDependecies:
    job_posting_information: str
    

class JobDescriptionAgentResult(BaseModel):
    role: str = Field(
        description="The job title or role position being described",
        default=""
    )
    company_name: str = Field(
        description="The Company which posted job",
        default=""
    )
    experience: str = Field(
        description="Required years and type of experience for the position",
        default=""
    )
    skills: List[str] = Field(
        description="List of specific technical skills required for the role",
        default_factory=list
    )
    description: str = Field(
        description="Detailed overview of the job responsibilities",
        default=""
    )
