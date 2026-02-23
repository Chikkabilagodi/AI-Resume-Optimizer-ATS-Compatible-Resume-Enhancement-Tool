from openai import OpenAI
from prompts import KEYWORD_EXTRACTION_PROMPT, ANALYSIS_PROMPT, REWRITE_PROMPT
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_keywords(job_description):
    prompt = KEYWORD_EXTRACTION_PROMPT.format(
        job_description=job_description
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def analyze_resume(resume, keywords):
    prompt = ANALYSIS_PROMPT.format(
        resume=resume,
        keywords=keywords
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def rewrite_resume(resume, job_title):
    prompt = REWRITE_PROMPT.format(
        resume=resume,
        job_title=job_title
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content