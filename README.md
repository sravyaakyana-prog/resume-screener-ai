# 🚀 AI Resume Screener

A full-stack AI-powered project designed for resume screening and ATS-style evaluation using FastAPI, Python, and Ollama LLM. The system compares a candidate’s resume with a job description and generates an intelligent analysis including match score, matched skills, missing skills, and AI-based feedback.

## 🧠 Project Overview
This project automates resume screening using AI. Users upload a resume (PDF) and provide a job description. The backend extracts text from the resume, sends it to an AI model (Ollama LLM), and returns a structured evaluation report showing how well the candidate matches the job requirements.

## ⚙️ Features
- Upload resume in PDF format
- Enter job description
- Extract text from resume automatically
- AI-based comparison using LLM (Ollama)
- Skill matching system
- Generates match score (0–100), matched skills, missing skills, and AI feedback
- Simple frontend UI using HTML, CSS, JavaScript
- REST API backend using FastAPI

## 🧱 Tech Stack
Backend: FastAPI, Python, Uvicorn, PyPDF, Ollama LLM  
Frontend: HTML, CSS, JavaScript (Fetch API)

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

## 🚀 How to Run
git clone https://github.com/your-username/resume-screener-ai.git  
cd resume-screener-ai/backend  
python -m venv venv  
venv\Scripts\activate  
pip install fastapi uvicorn python-multipart pypdf  
uvicorn main:app --reload  

OR  
python -m uvicorn main:app --reload  

Open: http://127.0.0.1:8000/docs

## 🌐 API Endpoints
GET / → Returns API status  
POST /analyze → Upload resume + job description  

Example Response:
{
  "score": 85,
  "matched_skills": ["Python", "FastAPI"],
  "missing_skills": ["Docker"],
  "feedback": "Good match with minor improvements needed."
}

## 🧠 How It Works
User uploads resume → enters job description → backend extracts text using PyPDF → sends to Ollama LLM → AI compares → returns structured result.

## ⚠️ Important Notes
Do not push venv to GitHub. Install dependencies before running. Ollama must be running locally. Keep main.py inside backend root.

## 🚀 Future Improvements
Deploy on Render/AWS, add authentication, store resume history, improve AI scoring, enhance UI, add drag-and-drop upload.

## 🏆 Use Case
Simulates an ATS (Applicant Tracking System) used by companies to automatically screen and rank resumes.

## 👨‍💻 Author
Sravya Akyana

## ⭐ If you like this project
Give it a star on GitHub 🚀