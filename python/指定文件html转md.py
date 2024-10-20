# import html2text


# # 定义HTML文件和Markdown文件的路径
# html_file_path = '2024-10-20/firsi.html'
# markdown_file_path = 'your_markdown_file.md'

# # # 创建md目录，如果它不存在
# # if not os.path.exists('md'):
# #     os.makedirs('md')

# # 读取HTML文件内容
# with open(html_file_path, 'r', encoding='utf-8') as file:
#     html_content = file.read()

# # 创建一个HTML2Text对象，并将images_to_alt设置为True
# h = html2text.HTML2Text()
# h.images_to_alt = True

# # 将HTML转换为Markdown
# markdown_content = h.handle(html_content)

# # 将Markdown内容写入到新的文件中
# with open(markdown_file_path, 'w', encoding='utf-8') as file:
#     file.write(markdown_content)

# # 复制HTML文件同级目录下的所有文件到md目录
# for file_name in os.listdir('.'):
#     if file_name != html_file_path and not file_name.startswith('md'):
#         shutil.copy(file_name, f'md/{file_name}')
import html2text

# 读取HTML文件内容
with open('firsi.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# 创建一个HTML2Text对象，并将images_to_alt设置为True
h = html2text.HTML2Text()
# h.images_to_alt = True

# 将HTML转换为Markdown
markdown_content = h.handle(html_content)

# 将Markdown内容写入到新的文件中
with open('file.md', 'w', encoding='utf-8') as file:
    file.write(markdown_content)
