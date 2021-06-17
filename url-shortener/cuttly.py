import requests

API_KEY = "YOUR_API_KEY"
URL = str(input("Introduce your larger url: "))
API_URL = f"https://cutt.ly/api/api.php?key={API_KEY}&short={URL}"
DATA = requests.get(API_URL).json()["url"]

if __name__ == "__main__":
    if DATA["status"] == 7:
        shortened_url = DATA["shortLink"]
        print("Shortened URL:", shortened_url)
    else:
        print("[!] Error Shortening URL:", DATA)
