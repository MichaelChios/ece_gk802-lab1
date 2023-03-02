import requests
import datetime

def makeRequest():
    url = input("Enter a URL: ")
    print("\n")
    response = requests.get(url)
    return response

def showHeaders(response):
    print("Headers:")
    for header in response.headers:
        print(f"{header}: {response.headers[header]}\n")

def showServerSoftware(response):
    server = response.headers.get("Server")
    if server:
        print(f"Server software: {server}\n")
    else:
        print("Server software not found in headers.\n")
        
def showCookies(response):
    cookies = response.cookies
    if cookies:
        print("Cookies:")
        for cookie in cookies:
            if(cookie.expires != None):
                expires = datetime.datetime.fromtimestamp(cookie.expires)
                duration = expires - datetime.datetime.now()
                print(f"{cookie.name}: valid until {duration}")
            else:
                print(f"{cookie.name} doesn't have expiration date.")
    else:
        print("No cookies found in headers.")
    print("\n")

def main():
    while(True):
        print("1) Show all headers")
        print("2) Show web server software")
        print("3) Show cookies")
        choice = input("Type 1-3 to make a request or 0 to exit: ")
        if(choice == "1"):
            r = makeRequest()
            showHeaders(r)
        elif(choice == "2"):
            r = makeRequest()
            showServerSoftware(r)
        elif(choice == "3"):
            r = makeRequest()
            showCookies(r)
        else:
            break

main()
