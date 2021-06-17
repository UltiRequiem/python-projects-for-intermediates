import bitly_api

BITLY_ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS = bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)
SHORT_URL = ACCESS.shorten(str(input()))

if __name__ == "__main__":
    print(f"Short URL =  {SHORT_URL['url']}")
