import os
import html2text

# 指定HTML文件所在的目录
directory_path = 'html/2024-10-20'

# 列出指定目录下的所有HTML文件
html_files = [file for file in os.listdir(directory_path) if file.endswith('.html')]

# 初始化html2text转换器
converter = html2text.HTML2Text()
converter.images_to_alt = False  # 保留图片
converter.unicode_snob = True   # 支持Unicode字符
converter.body_width = 0        # 不限制文本宽度，以保留链接
# 遍历HTML文件列表
for html_file in html_files:
    # 读取HTML文件内容
    with open(os.path.join(directory_path, html_file), 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 将HTML内容转换为Markdown
    markdown_content = converter.handle(html_content)
    
    # 构造Markdown文件的名称
    markdown_file = os.path.splitext(html_file)[0] + '.md'
    
    # 写入Markdown文件
    with open(os.path.join(directory_path, markdown_file), 'w', encoding='utf-8') as f:
        f.write(markdown_content)
