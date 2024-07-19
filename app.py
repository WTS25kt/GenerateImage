from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# 画像のサイズを設定
width, height = 800, 600
background_color = (255, 255, 255)  # 白色の背景

# 画像を作成
image = Image.new('RGB', (width, height), background_color)
draw = ImageDraw.Draw(image)

# フォントとサイズを設定
font_size = 150
font = ImageFont.truetype("arial.ttf", font_size)

# テキストを設定
text = "test"
text_color = (0, 0, 0)  # 黒色のテキスト

# テキストのサイズを取得
text_width, text_height = draw.textsize(text, font=font)

# テキストの位置を計算
text_x = (width - text_width) / 2
text_y = (height - text_height) / 2

# テキストを画像に描画
draw.text((text_x, text_y), text, font=font, fill=text_color)

# 絶対パスを指定して画像を保存
absolute_path = Path("/Users/shigoto/仕事/GitHub/GenerateImage/Image/test_image.png")
image.save(absolute_path)