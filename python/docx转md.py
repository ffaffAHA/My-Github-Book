import subprocess
import os

def convert_docx_to_markdown(docxpath, markdownpath):
    # 检查输入文件是否存在
    if not os.path.exists(docxpath):
        print("指定的DOCX文件不存在。")
        return

    # 检查Pandoc是否已安装
    try:
        subprocess.run(['pandoc', '--version'], check=True)
    except subprocess.CalledProcessError:
        print("Pandoc未安装或不可访问。请安装Pandoc后重试。")
        return

    # 使用Pandoc将DOCX文件转换为Markdown
    try:
        subprocess.run(['pandoc', '-s', docxpath, '-o', markdownpath], check=True)
        print(f"转换完成。Markdown文件已保存为{markdownpath}")
    except subprocess.CalledProcessError:
        print("转换过程中发生错误。")

# 示例用法
docxpath = input("输入DOCX文件的路径：")
# 获取DOCX文件的父目录
docx_directory = os.path.dirname(docxpath)
# 创建或检查保存Markdown文档的子目录
markdown_directory = os.path.join(docx_directory, 'md')
if not os.path.exists(markdown_directory):
    os.makedirs(markdown_directory)
# 获取DOCX文件的基本名称
docx_basename = os.path.basename(docxpath)
# 构建Markdown文件的保存路径
markdown_basename = os.path.splitext(docx_basename)[0] + '.md'
markdownpath = os.path.join(markdown_directory, markdown_basename)

convert_docx_to_markdown(docxpath, markdownpath)
