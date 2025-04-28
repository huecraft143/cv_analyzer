import fitz  # PyMuPDF
from core.validators import validate_pdf

def extract_text_with_pymupdf(pdf_path):
    try:
        validate_pdf(pdf_path)

        doc = fitz.open(pdf_path)
        full_text = ""

        for page_num, page in enumerate(doc, start=1):
            try:
                text = page.get_text()
                if not text.strip():
                    print(f"⚠️ Pagina {page_num} vuota o senza testo.")
                full_text += f"\n--- Pagina {page_num} ---\n{text}\n"
            except Exception as e:
                print(f"⚠️ Errore nella lettura della pagina {page_num}: {e}")
                continue

        doc.close()

        if not full_text.strip():
            print("⚠️ Nessun testo estratto. Il PDF potrebbe essere un'immagine.")
            return None

        return full_text.strip()

    except Exception as e:
        print(f"❌ Errore critico: {e}")
        return None


