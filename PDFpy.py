# 导入读写pdf模块
from PyPDF2 import PdfFileReader, PdfFileWriter

'''
注意：
页数从0开始索引
range()是左闭右开区间
'''


def split_pdf(file_name, start_page, end_page, output_pdf):
    '''
    :param file_name:待分割的pdf文件名
    :param start_page: 执行分割的开始页数
    :param end_page: 执行分割的结束位页数
    :param output_pdf: 保存切割后的文件名
    '''
    # 读取待分割的pdf文件
    input_file = PdfFileReader(open(file_name, 'rb'))
    # 实例一个 PDF文件编写器
    output_file = PdfFileWriter()
    # 把分割的文件添加在一起
    for i in range(start_page, end_page):
        output_file.addPage(input_file.getPage(i))
    # 将分割的文件输出保存
    with open(output_pdf, 'wb') as f:
        output_file.write(f)


def merge_pdf(merge_list, output_pdf):
    """
    merge_list: 需要合并的pdf列表
    output_pdf：合并之后的pdf名
    """
    # 实例一个 PDF文件编写器
    output = PdfFileWriter()
    for ml in merge_list:
        pdf_input = PdfFileReader(open(ml, 'rb'))
        page_count = pdf_input.getNumPages()
        for i in range(page_count):
            output.addPage(pdf_input.getPage(i))

    output.write(open(output_pdf, 'wb'))


if __name__ == '__main__':
    # 分割pdf
    split_pdf("test1.pdf", 0, 3, "0-2.pdf")
    split_pdf("test2.pdf", 7, 12, "7-11.pdf")
    #split_pdf("test.pdf", 18, 23, "18-22.pdf")
    #split_pdf("test.pdf", 27, 33, "26-32.pdf")
    #split_pdf("test.pdf", 40, 44, "40-43.pdf")
    #split_pdf("test.pdf", 46, 51, "46-50.pdf")
    #split_pdf("test.pdf", 58, 66, "58-65.pdf")
    #split_pdf("test.pdf", 77, 84, "77-83.pdf")
    #split_pdf("test.pdf", 93, 97, "93-96.pdf")
    #split_pdf("test.pdf", 102, 106, "102-105.pdf")
    # 合并pdf
    # 合并的pdf列表
    pdf_list = ["0-2.pdf", "7-11.pdf"]
    merge_pdf(pdf_list, "all.pdf")