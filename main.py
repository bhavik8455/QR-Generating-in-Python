import os
import requests
import json


with open('coupon.txt') as f:
    codes = json.load(f)


folder = 'images'
if not os.path.exists(folder):
    os.makedirs(folder)


for code in codes:
    print(codes.index(code))
    url = f'https://barcode.orcascan.com/?type=aztec&data={code}&fontsize=Fit&format=jpg&width=200&height=200'
    
   
    image_path = os.path.join( folder, f'{code}.jpg')

    
    if not os.path.exists(os.path.dirname(image_path)):
        os.makedirs(os.path.dirname(image_path))

   
    response = requests.get(url)
    with open(image_path, 'wb') as f:
        f.write(response.content)
