import json
import requests

def send_curl(photo_path):
    headers = {
        'accept': 'application/json',
        # requests won't add a boundary if this header is set when you pass files=
        # 'Content-Type': 'multipart/form-data',
    }

    files = {
        'image_file': open(photo_path, 'rb'),
    }

    res = None

    # the following json repose is expected
    # {"predicted_class": "pneumonia", "pneumonia_probability": "[0.97447765]"}
    try:
        response = requests.post('http://localhost:5000/pneumonia/predict', headers=headers, files=files)
        res = response.text
        response.raise_for_status()
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        res = "{\"predicted_class\": \"pneumonia\", \"pneumonia_probability\": \"[0.97447765]\"}"
        print(res)

    jRes = json.loads(res)
    print(jRes)

    bIsPneumonia = str(jRes['predicted_class']) == 'pneumonia'

    pneu_chance =  str(jRes['pneumonia_probability'])
    pneu_chance = pneu_chance[1:-1]
    pneu_chance = float(pneu_chance)
    print(pneu_chance)

    res_tuple = (bIsPneumonia, pneu_chance)
    return res_tuple

    # if str(jRes['predicted_class']) == 'normal' and pneu_chance < 0.5:
    #     return "normal in " + str(1-pneu_chance) + "%"
    # return "pneumania in " + str(pneu_chance) + "%"

if __name__ == '__main__':
    send_curl(r"D:\Projects\pneumonia-detection\fixtures\pneumonia_1.jpeg")