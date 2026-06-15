from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import resume

app = FastAPI()

# ✅ VERY IMPORTANT (fix frontend connection error)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later you can restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(resume.router)

@app.get("/")
def root():
    return {"message": "Resume Screener API is running 🚀"}