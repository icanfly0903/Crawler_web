import requests

params = {'username': 'name', 'email': 'email@gmail.com'}

r = requests.post("https://httpbin.org/post", data=params)

print(r.text)




# r = requests.get("https://google.com/") 

# print(r.text)

# img = requests.get("https://unsplash.com/random/1080x1080")

# with open('random_image.jpg', 'wb') as f:
#     f.write(img.content)