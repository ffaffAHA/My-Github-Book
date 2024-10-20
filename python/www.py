import os
import subprocess

def convertdocxtomarkdown(docxpath, markdownpath):
    # 检查输入文件是否存在
    if not os.path.exists(docxpath):
        print("指定的DOCX文件不存在。")
        return

    # 定义Markdown文档的保存目录
    docx_directory = os.path.dirname(docxpath)
    markdown_directory = os.path.join(docx_directory, 'md')
    
    # 创建或检查保存Markdown文档的子目录
    if not os.path.exists(markdown_directory):
        os.makedirs(markdown_directory)
    
    # 定义媒体文件保存路径为markdown_directory的相对路径
    media_dir = os.path.join(markdown_directory)
    
    # 确保路径中的反斜杠被替换为正斜杠
    media_dir = media_dir.replace('\\', '/')
    
    # 运行 Pandoc 命令
    subprocess.run([
        'pandoc', 
        '-s', 
        '-f', 'docx', 
        '-t', 'markdown', 
        '--extract-media', media_dir, 
        '-o', markdownpath, 
        docxpath
    ], check=True)

# 示例用法
docxpath = input("输入DOCX文件的路径：")


# 调用函数，注意 mediadir 参数在这里不是必需的，因为我们已经在函数内部定义了 media_dir
convertdocxtomarkdown(docxpath, markdownpath)
