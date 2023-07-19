import os
import requests
from bs4 import BeautifulSoup

try:
    # 获取用户输入的电子教材地址
    book_url = input("请输入电子教材地址：")

    # 从电子教材地址中提取图书ID
    book_id = book_url.split('/')[-3]

    # 发送GET请求获取网页内容
    response = requests.get(book_url)

    # 使用BeautifulSoup解析HTML内容，获取网页标题
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.title.string

    # 将标题中的非法字符替换为下划线
    valid_title = "".join(c if c.isalnum() else "_" for c in title)

    # 设置保存图片的文件夹路径
    folder_path = f'./images/{valid_title}/'
    os.makedirs(folder_path, exist_ok=True)

    # 初始化页码
    page_number = 1

    while True:
        # 构造图片链接
        url = f"https://book.pep.com.cn/{book_id}/files/mobile/{page_number}.jpg"
        
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
            
            # 增加页码
            page_number += 1
        else:
            print(f"程序在第 {page_number} 页图片停止下载，已经是最后一页了，或者网络断开连接。")
            break
except Exception as e:
    print("发生错误：", e)