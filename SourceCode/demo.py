import requests
import base64
from PIL import Image
from io import BytesIO



prompt = ("A vertical book cover in classical oil painting style, "
          "featuring a golden Christian cross intertwined with the caduceus symbol, "
          "Hebrew and Latin ancient scripts in the background, "
          "dramatic warm lighting, intricate detail, sacred and scholarly tone")

negative_prompt = "low quality, blurry, bad anatomy, cropped, text, watermark"

payload = {
    "prompt": prompt,
    "negative_prompt": negative_prompt,
    "steps": 30,
    "cfg_scale": 8,
    "width": 768,
    "height": 1152,
    "sampler_name": "DPM++ 2M Karras",
    "seed": -1,
}

try:
    response = requests.post("http://127.0.0.1:7860/sdapi/v1/txt2img", json=payload)
    
    # 检查 HTTP 状态码
    if response.status_code != 200:
        print(f"❌ 请求失败，状态码: {response.status_code}")
        print("返回内容:", response.text)
    else:
        try:
            r = response.json()
            image_data = base64.b64decode(r['images'][0])
            image = Image.open(BytesIO(image_data))
            image.save("judeochristian_book_cover.png")
            print("✅ 封面已保存为 judeochristian_book_cover.png")
        except requests.exceptions.JSONDecodeError:
            print("❌ 响应内容不是合法 JSON，可能服务返回了 HTML 或出错页面")
            print("返回内容:", response.text)

except requests.exceptions.RequestException as e:
    print("❌ 网络请求失败:", e)
