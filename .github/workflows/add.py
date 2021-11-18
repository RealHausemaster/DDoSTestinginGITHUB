import requests
  
link = input("Enter your link: ")
url = link
r = requests.get(url, allow_redirects=True)

open('proxy.txt', 'wb').write(r.content)
print("Now Your Proxy list is Installing Done!")
print("File name is Proxy.txt")
print("If You Install wrong list or wont working run srcipt delete!")
