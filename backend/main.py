from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os 

from extractors.pdf_reader import extract_text_with_pymupdf
from extractors.cv_parser import parse_cv_text
from utils.io import save_text_to_file
from utils.io import save_json_to_file
from extractors.chatbot import chatbot_api
from core.constants import CV_SAMPLE_PATH

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/upload")
async def upload_cv(file: UploadFile = File(...)):
    try:
        filename = file.filename
        contents = await file.read()

        # Salva temporaneamente il file
        tmp_path = f"temp_uploads/{filename}"
        os.makedirs("temp_uploads", exist_ok=True)
        with open(tmp_path, "wb") as f:
            f.write(contents)

        # Estrai testo, analizza, salva
        cv_text = extract_text_with_pymupdf(tmp_path)
        # cv_json = parse_cv_text(cv_text)  # opzionale, se vuoi usarlo
        result_from_model = chatbot_api(cv_text)

        # Salva (opzionale)
        save_text_to_file(cv_text, tmp_path)
        save_json_to_file(result_from_model, tmp_path)

        return result_from_model

    except Exception as e:
        print("❌ Errore:", e)
        return {"error": str(e)}
"""
# Cambia questo percorso col tuo
pdf_path = CV_SAMPLE_PATH
cv_text = extract_text_with_pymupdf(pdf_path)
cv_json = parse_cv_text(cv_text)
result_from_model = chatbot_api(cv_text)


if cv_text and cv_json and result_from_model:
    save_text_to_file(cv_text, pdf_path)
    #save_json_to_file(cv_json.to_dict(), pdf_path)
    save_json_to_file(result_from_model, pdf_path)
else:
    print("❌ Estrazione fallita")
"""