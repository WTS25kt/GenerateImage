import os
from pathlib import Path
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont

# .envファイルを読み込む
load_dotenv()

# 環境変数からパスを取得
font_path = os.getenv('FONT_PATH')
save_directory = os.getenv('SAVE_DIRECTORY')

# 画像のサイズを設定
width, height = 800, 600
background_color = (255, 255, 255)  # 白色の背景

def create_image_with_text(text):
    # 画像を作成
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # フォントとサイズを設定
    font_size = 150
    font = ImageFont.truetype(font_path, font_size)

    # テキストのバウンディングボックスを取得
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # テキストの位置を計算
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2

    # テキストを画像に描画
    draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0))  # 黒色のテキスト

    # 画像を保存
    save_path = Path(save_directory) / f"{text}.jpg"
    image.save(save_path, "JPEG")
    print(f"Image saved at: {save_path}")

if __name__ == "__main__":
    user_input = input("Enter the text to be displayed on the image: ")
    create_image_with_text(user_input)