import requests
from pprint import pprint
regions = ['gb', 'it'] # Change to your country
with open('C:/Work_CV/Office_Codes/spectrum/cut.jpg', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token eea3f25dd03596bb429aab3de722fa70f83b0ef7'})
#pprint(response.json())
data = response.json()


s=(data['results'][0]['plate'])
b=str(s).upper()
print(b)
