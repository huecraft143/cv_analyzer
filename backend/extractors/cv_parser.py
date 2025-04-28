from core.models import ParsedCV
from core.constants import (
    EN_SKILLS_JSON_PATH,
    EN_LANG_JSON_PATH,
    EN_JOB_JSON_PATH,
    EMAIL_RE,
    PHONE_RE,
)
import spacy
import json
from pathlib import Path

# Carica spaCy English model
import en_core_web_sm
nlp = en_core_web_sm.load()


def generate_ngrams(tokens, max_n):
    """Genera n-grammi da 1 a max_n"""
    ngrams = set()
    for n in range(1, max_n + 1):
        ngrams.update(' '.join(tokens[i:i+n]) for i in range(len(tokens) - n + 1))
    return ngrams


def parse_cv_text(text: str) -> ParsedCV:
    doc = nlp(text)
    text_lower = text.lower()
    parsed = ParsedCV()

    # --- Nome (prima entità PERSON) ---
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            parsed.nome = ent.text
            break

    # --- Email ---
    match = EMAIL_RE.search(text)
    if match:
        parsed.email = match.group()

    # --- Telefono ---
    phone = PHONE_RE.search(text)
    if phone:
        parsed.telefono = phone.group()

    # --- Tokenizzazione pulita ---
    tokens = [token.text.lower() for token in doc if not token.is_punct and not token.is_space]

    # --- Skill Matching ---
    with open(EN_SKILLS_JSON_PATH, encoding='utf-8') as f:
        skills = json.load(f)
    max_skill_len = max(len(s.split()) for s in skills) #25
    ngram_phrases = generate_ngrams(tokens, max_skill_len)
    parsed.skill = [s for s in skills if s.lower() in ngram_phrases]

    # --- Lingue ---
    with open(EN_LANG_JSON_PATH, encoding='utf-8') as f:
        langs = json.load(f)
    parsed.lingue = [l for l in langs if l.lower() in text_lower]

    # --- Esperienze lavorative ---
    with open(EN_JOB_JSON_PATH, encoding='utf-8') as f:
        jobs = json.load(f)
    max_job_len = max(len(j.split()) for j in jobs)
    ngram_phrases.update(generate_ngrams(tokens, max_job_len))
    parsed.esperienze = [
        e for e in jobs if e.lower() in ngram_phrases
    ]
    parsed.esperienze = list(dict.fromkeys(parsed.esperienze)) 

    # --- Istruzione ---
    parsed.istruzione = [
        line.strip() for line in text.splitlines()
        if any(word in line.lower() for word in ["laurea", "università", "phd", "diploma", "master"])
    ]

    return parsed

