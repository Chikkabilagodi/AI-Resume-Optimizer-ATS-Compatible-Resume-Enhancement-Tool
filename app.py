import streamlit as st
from ai_engine import extract_keywords, analyze_resume, rewrite_resume

st.title("AI Resume Optimizer")

resume = st.text_area("Paste Your Resume")
job_desc = st.text_area("Paste Job Description")
job_title = st.text_input("Target Job Title")

if st.button("Analyze & Optimize"):

    keywords = extract_keywords(job_desc)
    analysis = analyze_resume(resume, keywords)
    optimized_resume = rewrite_resume(resume, job_title)

    st.subheader("Extracted Keywords")
    st.write(keywords)

    st.subheader("Resume Analysis")
    st.write(analysis)

    st.subheader("Optimized Resume")
    st.write(optimized_resume)