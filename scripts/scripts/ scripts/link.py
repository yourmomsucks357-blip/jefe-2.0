import requests
from urllib.parse import urlparse
import whois
import re

def check_phishing_url(url):
    """Analyze a URL for phishing indicators."""
    results = {
        "url": url,
        "is_phishing": False,
        "reasons": []
    }

    # Check for HTTPS
    if not url.startswith("https://"):
        results["reasons"].append("⚠️ Not HTTPS (insecure)")

    # Check domain age (suspicious if < 30 days)
    try:
        domain = urlparse(url).netloc
        w = whois.whois(domain)
        if isinstance(w.creation_date, list):
            creation_date = w.creation_date[0]
        else:
            creation_date = w.creation_date
        age_days = (time.time() - creation_date.timestamp()) / 86400
        if age_days < 30:
            results["reasons"].append(f"⚠️ Domain is {age_days:.0f} days old (suspicious)")
    except:
        results["reasons"].append("⚠️ Could not fetch WHOIS data")

    # Check for IP in URL (common in phishing)
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", urlparse(url).netloc):
        results["reasons"].append("⚠️ IP address in URL (highly suspicious)")

    # Check for URL shortening services
    shorteners = ["bit.ly", "goo.gl", "tinyurl.com", "ow.ly"]
    if any(shortener in url for shortener in shorteners):
        results["reasons"].append("⚠️ URL shortener detected")

    results["is_phishing"] = len(results["reasons"]) > 0
    return results

if __name__ == "__main__":
    print("=== Phishing Link Analyzer ===")
    url = input("Enter URL to analyze: ")
    analysis = check_phishing_url(url)
    print("\nResults:")
    for reason in analysis["reasons"]:
        print(reason)
    if not analysis["is_phishing"]:
        print("✅ No phishing indicators found.")
