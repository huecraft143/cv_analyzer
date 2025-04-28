import os
def validate_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"❌ Il file {pdf_path} non esiste.")
    if os.path.getsize(pdf_path) == 0:
        raise ValueError("❌ Il file PDF è vuoto.")
    with open(pdf_path, "rb") as f:
        header = f.read(1024)
        if b"%PDF" not in header:
            raise ValueError("❌ Il file non sembra un PDF valido.")