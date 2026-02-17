import re

def extract_skills(text):
    skills = [
        "python", "java", "c++", "machine learning", "deep learning",
        "data science", "sql", "nlp", "tensorflow", "pandas",
        "numpy", "html", "css", "javascript"
    ]
    text = text.lower()
    found = [skill for skill in skills if skill in text]
    return set(found)

def analyze_resume(resume, job_desc):
    resume_skills = extract_skills(resume)
    job_skills = extract_skills(job_desc)

    matched = resume_skills.intersection(job_skills)
    missing = job_skills - resume_skills

    match_percent = int((len(matched) / max(len(job_skills), 1)) * 100)
    return match_percent, missing
  
