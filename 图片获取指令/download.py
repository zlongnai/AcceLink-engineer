import os
import requests
import re

# 创建img文件夹
os.makedirs('img', exist_ok=True)

# 读取并解析txt文件
with open('images.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 使用正则表达式提取所有URL
url_pattern = re.compile(r'https?://[^\s]+')
urls = url_pattern.findall(content)

# 下载图片
for i, url in enumerate(urls):
    try:
        response = requests.get(url)
        # 从URL提取文件名
        filename = url.split('/')[-1]
        if not filename or '.' not in filename:
            filename = f'image_{i+1}.jpg'
        
        with open(f'img/{filename}', 'wb') as f:
            f.write(response.content)
        print(f'下载成功: {filename}')
    except Exception as e:
        print(f'下载失败: {url} - {e}')

print('所有图片下载完成！')