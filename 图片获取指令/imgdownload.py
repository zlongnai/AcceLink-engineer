import os
import requests
import re

# 创建img文件夹
os.makedirs('img', exist_ok=True)

# 读取并解析txt文件
with open('images.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 使用正则表达式提取序号和URL
pattern = re.compile(r'图片(\d+)地址\s*[：:]\s*(https?://[^\s]+)')
matches = pattern.findall(content)

# 下载图片并按序号命名
for number, url in matches:
    try:
        response = requests.get(url)
        # 从URL提取文件扩展名
        file_ext = os.path.splitext(url)[1]
        if not file_ext:
            file_ext = '.png'  # 默认扩展名
        
        filename = f'{number}{file_ext}'
        with open(f'img/{filename}', 'wb') as f:
            f.write(response.content)
        print(f'下载成功: {filename}')
    except Exception as e:
        print(f'下载失败: 图片{number} - {e}')

print('所有图片下载完成！')