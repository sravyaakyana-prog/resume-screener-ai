# 🚀 AI Resume Screener

A full-stack AI-powered Resume Screening and ATS-style evaluation system built using FastAPI, Python, and Ollama LLM. It compares a candidate’s resume with a job description and generates intelligent analysis including match score, matched skills, missing skills, and AI feedback.

---

## 🧠 Project Overview

Users upload a resume (PDF) and enter a job description. The backend extracts text from the resume, processes it using an AI model (Ollama LLM), and returns structured results showing how well the resume matches the job.

---

## ⚙️ Features

- Upload resume (PDF)
- Enter job description
- Automatic text extraction from resume
- AI-based matching using LLM (Ollama)
- Skill comparison system
- Outputs:
  - Match Score (0–100)
  - Matched Skills
  - Missing Skills
  - AI Feedback
- Simple frontend using HTML, CSS, JavaScript
- FastAPI REST backend

---

## 🧱 Tech Stack

Backend: FastAPI, Python, Uvicorn, PyPDF, Ollama LLM  
Frontend: HTML, CSS, JavaScript (Fetch API)

---

## 📁 Project Structure

resume-screener-ai/  
├── backend/  
│   ├── app/  
│   │   ├── routers/resume.py  
│   │   ├── services/parser.py  
│   │   ├── services/matcher.py  
│   │   └── utils/  
│   ├── main.py  
│   ├── requirements.txt  
│   └── venv/ (ignored)  
├── frontend/  
│   ├── index.html  
│   ├── script.js  
│   └── style.css  

---

## 🚀 How to Run Locally

git clone https://github.com/your-username/resume-screener-ai.git  
cd resume-screener-ai/backend  

python -m venv venv  
venv\Scripts\activate  

pip install fastapi uvicorn python-multipart pypdf  

uvicorn main:app --reload  

Open: http://127.0.0.1:8000/docs  

---

## 🌐 API Endpoints

GET / → API status  

POST /analyze  
Form Data:
- file (PDF resume)
- jd (job description)

Response:
{
  "score": 85,
  "matched_skills": ["Python", "FastAPI"],
  "missing_skills": ["Docker"],
  "feedback": "Good match with minor improvements needed."
}

---

## 🌐 Live Demo

Frontend: https://resume-screener-ai-sage.vercel.app/  
Backend: https://resume-screener-backend-t6pd.onrender.com  

---

## 🧠 How It Works

Resume Upload → Text Extraction → AI Processing (Ollama) → Skill Matching → Result Output

---

## ⚠️ Important Notes

- Do NOT push venv/
- Install dependencies before running backend
- Ensure backend URL is updated in frontend
- Ollama must be running locally (if used)

---

## 🚀 Future Improvements

- Add authentication system  
- Store resume history in database  
- Improve AI scoring accuracy  
- Better UI (drag & drop upload)  
- Deploy full SaaS version  

---

## 🏆 Use Case

ATS-style resume screening system used for automatic candidate evaluation.

---

## 👨‍💻 Author

Sravya Akyana  

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub 🚀