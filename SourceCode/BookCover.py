import pandas as pd
import requests
import base64
from PIL import Image
from io import BytesIO
import os

# 读取CSV文件
csv_path = "keywords_final.csv"
df = pd.read_csv(csv_path)

# 输出图像保存路径
output_dir = "generated_covers"
os.makedirs(output_dir, exist_ok=True)

# 请求配置
url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
headers = {"Content-Type": "application/json"}

for idx, row in df.iterrows():
    keyword = row["keywords"]
    prompt = f"A book cover titled '{keyword}', classical painting, caduceus and cross, religious medicine theme, golden lighting, intricate, detailed"
    negative_prompt = "low quality, blurry, bad anatomy, distorted text, watermark"

    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "steps": 30,
        "cfg_scale": 8,
        "width": 768,
        "height": 1152,
        "sampler_name": "DPM++ 2M Karras",
        "seed": -1
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        r = response.json()
        image_data = base64.b64decode(r['images'][0])
        image = Image.open(BytesIO(image_data))


        filename = f"{keyword.replace(' ', '_')}.png"
        filepath = os.path.join(output_dir, filename)
        image.save(filepath)

        # 更新 CSV 中的 image path
        df.at[idx, "image path"] = filepath
        print(f"✅ Generated: {filepath}")

    except Exception as e:
        print(f"❌ Failed for '{keyword}': {e}")
        df.at[idx, "image path"] = "ERROR"

# 保存新的 CSV 文件
df.to_csv("keywords_final_with_images.csv", index=False)
print("✅ 所有封面生成完毕，结果已保存为 keywords_final_with_images.csv")
