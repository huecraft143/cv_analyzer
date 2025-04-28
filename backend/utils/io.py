import os
import json
from dataclasses import asdict
def save_text_to_file(text, original_pdf_path):
    txt_path = os.path.splitext(original_pdf_path)[0] + ".txt"
    try:
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"✅ Testo salvato in: {txt_path}")
    except Exception as e:
        print(f"❌ Errore nel salvataggio del file .txt: {e}")

def save_json_to_file(data, original_pdf_path):
    json_path = os.path.splitext(original_pdf_path)[0] + ".json"
    try:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(asdict(data), f, ensure_ascii=False, indent=2)
        print(f"✅ JSON salvato in: {json_path}")
    except Exception as e:
        print(f"❌ Errore nel salvataggio del file .json: {e}")

def save_list_to_json(data, out_path):
    try:
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(sorted(set(data)), f, indent=2, ensure_ascii=False)
        print(f"✅ {len(data)} elementi salvati in: {out_path}")
    except Exception as e:
        print(f"❌ Errore nel salvataggio JSON: {e}")
