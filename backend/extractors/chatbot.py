import json
from core.models import ParsedCV, CV, Skills, LanguageDetails, WorkExperience, Education
from utils.network import contact_api
from dataclasses import asdict, fields

# Helper per sicurezza
def safe_dataclass_from_dict(cls, data: dict):
    valid_fields = {f.name for f in fields(cls)}
    filtered_data = {k: v for k, v in data.items() if k in valid_fields}
    return cls(**filtered_data)

def build_cv_from_result(result: dict) -> CV:
    # Languages
    parsed_languages = {}
    languages_raw = result.get("languages", {})
    print("Lingue:", languages_raw)
    if isinstance(languages_raw, dict):
    # Formato già corretto
        for lang, details in languages_raw.items():
            if isinstance(details, dict):
                parsed_languages[lang.lower()] = safe_dataclass_from_dict(LanguageDetails, details)
            else:
                parsed_languages[lang.lower()] = LanguageDetails()

    elif isinstance(languages_raw, list):
        for lang in languages_raw:
            if not isinstance(lang, dict):
                print(f"⚠️ Lingua ignorata (non è un dict): {lang}")
                continue

            lang_name = lang.get("name")
            level = lang.get("level")

            if not lang_name:
                print(f"⚠️ Lingua ignorata (senza nome): {lang}")
                continue

            lang_key = lang_name.strip().lower()

            if isinstance(level, dict):
                parsed_languages[lang_key] = safe_dataclass_from_dict(LanguageDetails, level)
            elif isinstance(level, str):
                # "Mother tongue(s)" o simili
                parsed_languages[lang_key] = LanguageDetails()
            else:
                print(f"⚠️ Formato 'level' non gestito per lingua {lang_name}: {level}")
    else:
        print(f"⚠️ Formato non riconosciuto per 'languages': {type(languages_raw)}")
    # Skills
    skills_data = result.get("skills", {})
    parsed_skills = safe_dataclass_from_dict(Skills, skills_data)

    # Work Experience
    parsed_work = [
        safe_dataclass_from_dict(WorkExperience, we) for we in result.get("workExperience", [])
    ]

    # Education
    parsed_education = [
        safe_dataclass_from_dict(Education, edu) for edu in result.get("education", [])
    ]

    # CV
    print("nome;", result.get("name", ""))
    print("email;", result.get("email", ""))
    print("telefono;", result.get("phone", ""))
    print("indirizzo;", result.get("address", ""))
    print("lingue;", parsed_languages)
    print("skills;", parsed_skills)
    print("esperienza lavorativa;", parsed_work)
    print("istruzione;", parsed_education)
    return CV(
        name=result.get("name", ""),
        email=result.get("email", ""),
        phone=result.get("phone", ""),
        address=result.get("address", ""),
        languages=parsed_languages,
        skills=parsed_skills,
        workExperience=parsed_work,
        education=parsed_education
    )

def clean_json_string(text: str) -> str:
    # Rimuove eventuali ```json e ```
    if text.strip().startswith("```json"):
        text = text.strip().removeprefix("```json").strip()
    if text.strip().endswith("```"):
        text = text.strip().removesuffix("```").strip()
    return text

def chatbot_api(message):
    """
    Function to interact with the chatbot API.
    """
    result_raw = contact_api(message)
    result_raw_cleaned = clean_json_string(result_raw)
    result = json.loads(result_raw_cleaned)
    if not result:
        print("❌ Risposta API vuota o non valida")
        return None
    try:
        cv = build_cv_from_result(result)
        print("✅ CV creato correttamente:")
        return cv
    except Exception as e:
        print("❌ Errore nella creazione del CV:", e)
        return None