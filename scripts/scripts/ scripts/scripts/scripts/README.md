# 🛡️ Cybersecurity Toolkit (Dolphin-Llama3 70B Backend)

A **modular Python toolkit** for network reconnaissance, password cracking, phishing detection, and cryptography, powered by **Dolphin-Llama3 70B** (uncensored) via **Ollama** and **Hugging Face Spaces**.

---

## **📌 Features**
   Module          | Description                          | Script          |
 |-----------------|--------------------------------------|-----------------|
 | Port Scanner    | Scan open ports on a target IP       | `easy.py`       |
 | Network Scanner | Discover active devices in a subnet  | `easy.py`       |
 | Password Cracker| Brute-force/dictionary attacks       | `password.py`   |
 | Link Analyzer   | Detect phishing URLs                 | `link.py`       |
 | File Encryptor  | AES/Fernet encryption for files      | `crypto.py`     |
 | PDF Decryptor   | Wordlist-based PDF password recovery | `pdf.py`        |

---

## **🚀 Deployment**
### **Option 1: Local Setup**
1. Install dependencies:
   ```bash
   pip install -r config/requirements.txt
