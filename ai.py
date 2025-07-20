import openai
import base64
from PIL import Image
from io import BytesIO

# 设置你的 OpenAI API 密钥
openai.api_key = 'your_openai_api_key'

# 生成图片的提示词
prompt = "A futuristic city floating in the sky, with flying cars and neon lights"

# 调用 DALL·E 生成图像（使用 dalle-3 模型）
response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="512x512"  # 可选尺寸: 256x256, 512x512, 1024x1024
)

# 获取图片的 URL
image_url = response['data'][0]['url']
print(f"图片地址：{image_url}")
