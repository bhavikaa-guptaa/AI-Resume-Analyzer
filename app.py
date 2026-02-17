import streamlit as st
from resume_analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer")
st.write("Upload your resume and compare it with a job description.")

resume_text = st.text_area("Paste Resume Text Here")
job_desc = st.text_area("Paste Job Description Here")

if st.button("Analyze"):
    if resume_text and job_desc:
        match, missing = analyze_resume(resume_text, job_desc)
        st.success(f"Skill Match: {match}%")
        st.write("### Missing Skills:")
        for skill in missing:
            st.write(f"- {skill}")
    else:
        st.warning("Please fill both fields.")
