import html2text

# 读取HTML文件内容
with open('html/firsi.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# 创建一个HTML2Text对象，并将images_to_alt设置为True
h = html2text.HTML2Text()
h.images_to_alt = True

# 将HTML转换为Markdown
markdown_content = html2text.html2text(html_content)

# 将Markdown内容写入到新的文件中
with open('md/make2.md', 'w', encoding='utf-8') as file:
    file.write(markdown_content)

