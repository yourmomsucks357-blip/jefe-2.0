import hashlib
import itertools
import time

def brute_force_hash(target_hash, charset="abcdefghijklmnopqrstuvwxyz0123456789", max_length=6):
    """Brute-force a hash (e.g., MD5, SHA-1)."""
    start_time = time.time()
    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempt_str = "".join(attempt)
            if hashlib.md5(attempt_str.encode()).hexdigest() == target_hash:
                return f"Found password: {attempt_str} (Time: {time.time() - start_time:.2f}s)"
    return "Password not found."

def dictionary_attack(target_hash, wordlist_path="rockyou.txt"):
    """Dictionary attack using a wordlist."""
    try:
        with open(wordlist_path, "r", errors="ignore") as f:
            for word in f:
                word = word.strip()
                if hashlib.md5(word.encode()).hexdigest() == target_hash:
                    return f"Found password: {word}"
    except FileNotFoundError:
        return f"Error: Wordlist '{wordlist_path}' not found. Download from https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"

if __name__ == "__main__":
    print("=== Password Cracker ===")
    target_hash = input("Enter target hash (MD5): ")
    print(brute_force_hash(target_hash))
    print(dictionary_attack(target_hash))
