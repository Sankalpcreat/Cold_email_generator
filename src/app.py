from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from src.agent.cold_email_writer_agent.agent import run_cold_email_writer
from src.agent.job_description_parser_agent.agent import run_job_description_parser
from fastapi.middleware.cors import CORSMiddleware
from src.agent.job_description_parser_agent.model import JobDescriptionAgentResult
import logging
app = FastAPI()
logging.basicConfig(level=logging.INFO)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
# Request models with validation
class JobDescriptionRequest(BaseModel):
    job_url: HttpUrl  # Validates URL format

class ColdEmailRequest(BaseModel):
    job_url: HttpUrl  # Validates URL format

@app.post("/job-description-parser")
async def parse_job_description(request: JobDescriptionRequest):
    """
    Endpoint to parse a job description from a given job posting URL.
    """
    try:
        job_description = await run_job_description_parser(job_posting_url=request.job_url)
        
        # Validate the response
        if not job_description or not any([
            job_description.role,
            job_description.company_name,
            job_description.description
        ]):
            logging.error("Invalid or empty job description received")
            raise HTTPException(
                status_code=422,
                detail="Could not extract valid job description from the provided URL"
            )
            
        return {"job_description": job_description.dict()}
        
    except Exception as e:
        logging.exception("Error parsing job description")
        raise HTTPException(
            status_code=500,
            detail=f"Error parsing job description: {str(e)}"
        )

@app.post("/cold-email-generator")
async def generate_cold_email(request: ColdEmailRequest):
    """
    Endpoint to generate a cold email based on a job posting URL.
    """
    try:
        logging.info(f"Received request for cold email generation: {request.job_url}")

        # Get job description
        job_description = await run_job_description_parser(job_posting_url=request.job_url)
        logging.info(f"Parsed job description: {job_description}")

        # Validate job description
        if not job_description or not any([
            job_description.role,
            job_description.company_name,
            job_description.description
        ]):
            logging.error("Invalid or empty job description received")
            raise HTTPException(
                status_code=422,
                detail="Could not extract valid job description from the provided URL"
            )

        # Generate cold email
        cold_email = await run_cold_email_writer(job_description=job_description)
        logging.info(f"Generated cold email: {cold_email}")

        if not cold_email or not any([cold_email.get("subject"), cold_email.get("body")]):
            logging.error("Cold email generation failed")
            raise HTTPException(
                status_code=500,
                detail="Failed to generate cold email content"
            )
        
        return {"cold_email": cold_email}
    except Exception as e:
        logging.exception(f"Error generating cold email: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error generating cold email: {str(e)}"
        )