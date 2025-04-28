# utils/convert_occupations.py
import pandas as pd
from pathlib import Path
import json

EN_CSV_SKILLS_PATH = '/Users/mattiapalano/Documents/cv_analyzer/data/skills_en.csv'
EN_CSV_JOB_PATH = '/Users/mattiapalano/Documents/cv_analyzer/data/occupations_en.csv'
EN_CSV_LANG_PATH = '/Users/mattiapalano/Documents/cv_analyzer/data/languageSkillsCollection_en.csv'
EN_SKILLS_JSON_PATH = '/Users/mattiapalano/Documents/cv_analyzer/data/skills_en.json' 
EN_JOB_JSON_PATH = '/Users/mattiapalano/Documents/cv_analyzer/data/occupations_en.json' 
EN_LANG_JSON_PATH = '/Users/mattiapalano/Documents/cv_analyzer/data/languageSkillsCollection_en.json'

def save_list_to_json(data, out_path):
    try:
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(sorted(set(data)), f, indent=2, ensure_ascii=False)
        print(f"✅ {len(data)} elementi salvati in: {out_path}")
    except Exception as e:
        print(f"❌ Errore nel salvataggio JSON: {e}")

def build_set_from_csv(df):
    values = set(df["preferredLabel"].dropna().str.lower().str.strip())
    for alt in df.get("altLabels", pd.Series()).dropna():
        for label in alt.split("\n"):
            label = label.strip().lower()
            if label:
                values.add(label)
    return sorted(values)

def main():
    job_titles = build_set_from_csv(pd.read_csv(EN_CSV_JOB_PATH))
    skills = build_set_from_csv(pd.read_csv(EN_CSV_SKILLS_PATH))
    langs = build_set_from_csv(pd.read_csv(EN_CSV_LANG_PATH))

    save_list_to_json(job_titles, EN_JOB_JSON_PATH)
    save_list_to_json(skills, EN_SKILLS_JSON_PATH)
    save_list_to_json(langs, EN_LANG_JSON_PATH)

if __name__ == "__main__":
    main()

