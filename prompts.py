# prompts.py

KEYWORD_EXTRACTION_PROMPT = """
You are an ATS system.

Extract:
- Required skills
- Tools
- Experience level
- Certifications

From this job description:

{job_description}

Return in bullet format.
"""

ANALYSIS_PROMPT = """
Compare this resume with job requirements.

Resume:
{resume}

Job Requirements:
{keywords}

Tell:
1. Missing skills
2. Weak sections
3. Improvement suggestions
"""

REWRITE_PROMPT = """
Rewrite the resume professionally.
- Keep it ATS friendly
- Add missing keywords naturally
- Improve action verbs

Resume:
{resume}

Target Role:
{job_title}
"""