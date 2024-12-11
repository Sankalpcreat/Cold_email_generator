from pydantic_ai import Agent
import logging

from src.agent.cold_email_writer_agent.model import (
    ColdEmailWriterAgentInput,
    ColdEmailWriterAgentResponse,
)
from src.agent.job_description_parser_agent.model import JobDescriptionAgentResult

logger = logging.getLogger(__name__)

cold_email_writer_agent = Agent(
    model="groq:llama-3.2-3b-preview",
    deps_type=ColdEmailWriterAgentInput,
    result_type=ColdEmailWriterAgentResponse,
    system_prompt="""
You are Ria, a tech recruitment specialist at Turing, reaching out to hiring managers about your firm's pre-vetted engineering talent pool. Using the provided job description:

1. Analyze role requirements and highlight relevant Turing portfolio projects
2. Create concise, compelling subject lines highlighting available talent
3. Write brief, impactful email body (3-4 paragraphs max) that:
   - Opens with specific reference to company's hiring needs
   - Showcases relevant Turing portfolio projects matching required tech stack
   - Emphasizes that Turing has pre-vetted engineers ready to interview
   - Includes clear call-to-action to discuss available candidates

Keep tone professional yet conversational. Focus on Turing's talent pool and proven project experience.
""",
)

async def run_cold_email_writer(job_description: JobDescriptionAgentResult) -> dict:
    
    try:
        result = await cold_email_writer_agent.run(
            "Please write a cold email",
            deps=ColdEmailWriterAgentInput(job_description=job_description),
        )

        if hasattr(result, 'data') and result.data:
            
            return {
                "subject": result.data.subject,
                "body": result.data.body
            }
        
        logger.error("No data received from cold email writer agent")
        return {
            "subject": "",
            "body": ""
        }

    except Exception as e:
        logger.error(f"Error in cold email writer: {str(e)}")
        return {
            "subject": "",
            "body": ""
        }
