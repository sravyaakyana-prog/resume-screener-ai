import re

# 🔥 SKILLS DATABASE (expand anytime)
SKILLS_DB = [
    "python", "java", "c++", "scala",
    "machine learning", "deep learning",
    "sql", "mongodb", "tensorflow",
    "keras", "pytorch", "javascript",
    "react", "node", "docker", "aws",
    "kafka", "gce", "play"
]

# 🔥 ALIASES
SKILL_ALIASES = {
    "ml": "machine learning",
    "dl": "deep learning",
    "js": "javascript"
}


# ✅ CLEAN TEXT
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    return text


# ✅ EXTRACT SKILLS FROM RESUME
def extract_resume_skills(text):
    text = clean_text(text)

    # safe alias replace
    for short, full in SKILL_ALIASES.items():
        text = re.sub(rf"\b{short}\b", full, text)

    found = []

    for skill in SKILLS_DB:
        if re.search(rf"\b{re.escape(skill)}\b", text):
            found.append(skill)

    return found


# ✅ EXTRACT SKILLS FROM JD (CRITICAL FIX)
def extract_jd_skills(jd_text):
    skills = [s.strip().lower() for s in jd_text.split(",") if s.strip()]
    return skills


# ✅ MAIN MATCH FUNCTION
def match_resume_with_jd(resume_text, jd_text):

    # extract skills
    resume_skills = extract_resume_skills(resume_text)
    jd_skills = extract_jd_skills(jd_text)

    print("📌 RESUME SKILLS:", resume_skills)
    print("📌 JD SKILLS:", jd_skills)

    # ✅ MATCHING (preserve JD order)
    matched_skills = [skill for skill in jd_skills if skill in resume_skills]
    missing_skills = [skill for skill in jd_skills if skill not in resume_skills]

    print("✅ MATCHED:", matched_skills)
    print("❌ MISSING:", missing_skills)

    # ✅ SCORING
    if len(jd_skills) == 0:
        skill_score = 0
    else:
        skill_score = (len(matched_skills) / len(jd_skills)) * 100

    exp_score = 70   # static for now
    edu_score = 70   # static for now

    final_score = int(0.5 * skill_score + 0.3 * exp_score + 0.2 * edu_score)

    # ✅ SUGGESTIONS
    suggestions = [f"Consider adding {skill}" for skill in missing_skills]

    # ✅ RESPONSE
    return {
        "score": final_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "reason": f"Skills: {int(skill_score)}%, Exp: {exp_score}%, Edu: {edu_score}%",
        "suggestions": suggestions
    }