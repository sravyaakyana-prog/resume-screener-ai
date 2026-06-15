from fastapi import APIRouter, UploadFile, File, Form
from app.services.parser import extract_text_from_pdf
from app.services.matcher import match_resume_with_jd

router = APIRouter()

@router.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    jd: str = Form(...)
):
    try:
        # Save file
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Extract text
        resume_text = extract_text_from_pdf(file_path)

        # Match with JD
        result = match_resume_with_jd(resume_text, jd)

        return result

    except Exception as e:
        return {"error": str(e)}