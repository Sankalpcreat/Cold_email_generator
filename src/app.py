from fastapi import FastAPI
from pydantic import BaseModel
from agent.cold_email_writer_agent.agent import run_cold_email_writer
from agent.job_description_parser_agent.agent import run_job_description_parser

app = FastAPI()

class JobDescriptionRequest(BaseModel):
    job_url: str

class ColdEmailRequest(BaseModel):
    job_url: str

@app.post("/job-description-parser")
async def parse_job_description(request: JobDescriptionRequest):
    job_description = await run_job_description_parser(job_posting_url=request.job_url)
    return job_description

@app.post("/cold-email-generator")
async def generate_cold_email(request: ColdEmailRequest):
    job_description = await run_job_description_parser(job_posting_url=request.job_url)
    cold_email = await run_cold_email_writer(job_description=job_description)
    return cold_email