import requests


url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'
}


response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    photos = data.get("photos", [])

    if not photos:
        print("Can not find photos")
    else:
        for idx, photo in enumerate(photos, start=1):
            img_url = photo["img_src"]
            print(f"[INFO] Download photo {idx}: {img_url}")

            try:
                img_data = requests.get(img_url).content
                filename = f"mars_photo{idx}.jpg"

                with open(filename, 'wb') as f:
                    f.write(img_data)

                print(f"[OK] Saved: {filename}")
            except Exception as e:
                print(f"[ERROR] Can not download photo {idx}: {e}")
else:
    print(f"[ERROR] Can not get data. Response code: {response.status_code}")
