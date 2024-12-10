from pydantic_ai import Agent, RunContext
from typing import Dict, Any
import json
import logging

from src.agent.job_description_parser_agent.model import (
    JobDescriptionAgentResult,
    JobInformationFetchDeps,
)
from src.utils import scrape_website

logger = logging.getLogger(__name__)

job_description_parser_agent = Agent(
    model="groq:llama-3.2-3b-preview",
    deps_type=JobInformationFetchDeps,
    result_type=JobDescriptionAgentResult,
    system_prompt="""You are a specialized HR assistant focused on analyzing and structuring job descriptions. Your task is to:
1. Extract job posting information using the get_job_details tool
2. Return a SINGLE structured response with these fields EXACTLY ONCE:
   - role: job title/position
   - company_name: company name
   - experience: required experience
   - skills: list of required technical skills
   - description: brief overview of responsibilities

Format your response as a clean JSON object with these fields only. Do not duplicate fields."""
)

@job_description_parser_agent.tool
def get_job_details(ctx: RunContext[JobInformationFetchDeps]) -> Dict[str, Any]:
    """
    Retrieves and extracts job posting information
    """
    try:
        job_post_url = ctx.deps.job_post_url
        job_posting_information = scrape_website(url=job_post_url)
        
        return {
            "raw_content": job_posting_information
        }
    except Exception as e:
        logger.error(f"Error in get_job_details: {str(e)}")
        return {
            "raw_content": ""
        }

def clean_llm_response(response_data: Dict[str, Any]) -> Dict[str, Any]:
    """Clean and validate LLM response data"""
    cleaned_data = {
        "role": str(response_data.get("role", "")),
        "company_name": str(response_data.get("company_name", "")),
        "experience": str(response_data.get("experience", "")),
        "skills": list(set(response_data.get("skills", []))),  # Remove duplicates
        "description": str(response_data.get("description", ""))
    }
    return cleaned_data

async def run_job_description_parser(job_posting_url: str) -> JobDescriptionAgentResult:
    """Parse job description from URL"""
    try:
        result = await job_description_parser_agent.run(
            "Please analyze the job posting and extract the required information into a single, clean JSON structure.",
            deps=JobInformationFetchDeps(job_post_url=job_posting_url),
        )
        
        if hasattr(result, 'data') and result.data:
            # Clean the response data
            if isinstance(result.data, dict):
                cleaned_data = clean_llm_response(result.data)
            elif isinstance(result.data, JobDescriptionAgentResult):
                cleaned_data = clean_llm_response(result.data.dict())
            else:
                logger.error(f"Unexpected result type: {type(result.data)}")
                return JobDescriptionAgentResult()

            return JobDescriptionAgentResult(**cleaned_data)
            
        logger.error("No data received from agent")
        return JobDescriptionAgentResult()
        
    except Exception as e:
        logger.error(f"Error in run_job_description_parser: {str(e)}")
        return JobDescriptionAgentResult()
