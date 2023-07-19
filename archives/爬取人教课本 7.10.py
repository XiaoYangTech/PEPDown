#2023.7.10 20:01
import requests
import os

# 设置保存图片的文件夹路径
folder_path = './images/'
os.makedirs(folder_path, exist_ok=True)

# 遍历每一页
for page_number in range(1, 171):
    # 构造图片链接
    url = f"https://book.pep.com.cn/1311001201171/files/mobile/{page_number}.jpg?220926132151"
    
    # 发送GET请求
    response = requests.get(url)
    
    # 检查响应状态码
    if response.status_code == 200:
        # 拼接保存图片的文件路径
        file_path = os.path.join(folder_path, f"{page_number}.jpg")
        
        # 保存图片
        with open(file_path, 'wb') as file:
            file.write(response.content)
        
        print(f"第 {page_number} 页图片下载完成")
    else:
        print(f"第 {page_number} 页图片下载失败")