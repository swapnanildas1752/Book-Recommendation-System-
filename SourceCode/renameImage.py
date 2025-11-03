import pandas as pd
import os
import shutil

# === 配置 ===
csv_path = "data/keywords_last_with_images.csv"
original_image_dir = "generated_covers"
new_image_dir = "cover"
output_csv = "data/keywords_last_with_renamed_images.csv"

# 创建新目录
os.makedirs(new_image_dir, exist_ok=True)

# 读取 CSV
df = pd.read_csv(csv_path)

# 确保 image_path 存在
if "image_path" not in df.columns:
    raise ValueError("CSV 文件中缺少 'image_path' 列。")

# 遍历每一行，重命名并移动图片
for idx, row in df.iterrows():
    img_path = str(row["image_path"])
    row_id = row["Id"] if "Id" in row else idx  # 如果没有id列，就用行号

    # 只处理 image_path 指向 generated_covers 中的图
    if img_path.startswith(original_image_dir) and os.path.exists(img_path):
        new_filename = f"{row_id}.jpg"
        new_path = os.path.join(new_image_dir, new_filename)

        try:
            shutil.move(img_path, new_path)
            df.at[idx, "image_path"] = new_path
            print(f"✅ 移动并重命名: {img_path} → {new_path}")
        except Exception as e:
            print(f"❌ 处理失败 [{img_path}]: {e}")
    else:
        print(f"⚠️ 跳过未找到或非 generated_covers 文件: {img_path}")

# 保存更新后的 CSV
df.to_csv(output_csv, index=False)
print(f"\n✅ 更新后的 CSV 已保存为: {output_csv}")
