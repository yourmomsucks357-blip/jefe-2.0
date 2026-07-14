from PyPDF2 import PdfReader
import hashlib

def decrypt_pdf(pdf_path, wordlist_path="rockyou.txt"):
    """Brute-force a password-protected PDF."""
    try:
        with open(wordlist_path, "r", errors="ignore") as f:
            for word in f:
                word = word.strip().encode()
                try:
                    reader = PdfReader(pdf_path, password=word)
                    if reader.is_encrypted:
                        reader.decrypt(word)
                    return f"✅ PDF unlocked! Password: {word.decode()}"
                except:
                    continue
    except FileNotFoundError:
        return f"Error: Wordlist '{wordlist_path}' not found."
    return "❌ Password not found in wordlist."

if __name__ == "__main__":
    print("=== PDF Decryptor ===")
    pdf_path = input("Enter PDF file path: ")
    print(decrypt_pdf(pdf_path))
