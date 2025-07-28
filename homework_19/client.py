import requests

local_image_path = "C:\\Users\\forph\\Downloads\\fintown\FD-95\\2025-05-23_13-05-56.jpg"
filename = local_image_path.split("/")[-1]

with open(local_image_path, 'rb') as image_file:
    files = {'image': image_file}
    response = requests.post("http://127.0.0.1:8080/upload", files=files)

if response.status_code == 201:
    print("Image uploaded successfully.")
    image_url = response.json().get("image_url")
    print(f"Image URL: {image_url}")
else:
    print(f"Upload failed: {response.text}")
    exit()

get_url = f"http://127.0.0.1:8080/image/{filename}"
headers = {"Content-Type": "text/plain"}
response = requests.get(get_url, headers=headers)

if response.status_code == 200:
    print("Image URL retrieved:")
    print(response.json())
else:
    print(f"Failed to retrieve image URL: {response.text}")

# delete_url = f"http://127.0.0.1:8080/delete/{filename}"
# response = requests.delete(delete_url)

if response.status_code == 200:
    print("Image deleted successfully:")
    print(response.json())
else:
    print(f"Failed to delete image: {response.text}")
