import os
from PyPDF2 import PdfFileMerger

# 定义文件路径和文件名
files_dir = input('最下方输入绝对路径\n'+os.getcwd()+'\n直接回车则使用当前路径\n')
if files_dir == '':
    files_dir = os.getcwd()
result_filename = "merged.pdf"
result_file = f"{files_dir}/{result_filename}"

# 遍历pdf目录下所有的pdf文件
pdfs = [f for f in os.listdir(files_dir) if f.endswith('.pdf')]
pdfs.sort() # 将文件名排序以确保顺序正确

merger = PdfFileMerger()

for pdf in pdfs:
    # 打开每个pdf文件
    pdf_path = f"{files_dir}/{pdf}"
    merger.append(open(pdf_path, 'rb'))

#  将所有文档合并，并保存到指定的输出文件中
with open(result_file, "wb") as fout:
    merger.write(fout)
    print(f"\nMerged document saved to: {result_file}\n")