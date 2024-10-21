import os
from spire.pdf import *

def convert_pdf_to_html(input_pdf_path: str) -> None:
    # 检查输入文件是否存在
    if not os.path.isfile(input_pdf_path):
        print(f"错误：文件 '{input_pdf_path}' 不存在。请检查路径是否正确。")
        return
    
    # 获取输入PDF文件的文件名（不带扩展名）
    pdf_filename = os.path.basename(input_pdf_path)
    pdf_basename, _ = os.path.splitext(pdf_filename)
    
    # 构造输出HTML文件的路径
    output_html_dir = 'html'  # 直接使用'html'作为子目录
    output_html_path = os.path.join(output_html_dir, f"{pdf_basename}.html")
    
    # 确保输出目录存在
    os.makedirs(output_html_dir, exist_ok=True)
    
    # 创建一个PdfDocument类的对象
    doc = PdfDocument()
    
    try:
        # 加载一个PDF文档
        doc.LoadFromFile(input_pdf_path)
        
        # 将文档转换为HTML
        doc.SaveToFile(output_html_path, FileFormat.HTML)
        print(f"PDF已成功转换为HTML. 输出路径: {output_html_path}")
    except Exception as e:
        # 如果在转换过程中发生错误，打印错误信息
        print(f"转换过程中发生错误: {e}")
    finally:
        # 关闭文档
        doc.Close()

if __name__ == "__main__":
    # 获取用户输入的PDF文件路径
    input_pdf_path = input("请输入PDF文件的路径: ")
    
    # 调用转换函数
    convert_pdf_to_html(input_pdf_path)
