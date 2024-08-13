import fitz  # PyMuPDF

def split_pdf(input_pdf, output_pdf_prefix, start_page, end_page):
    with fitz.open(input_pdf) as pdf_document:
        pdf_writer = fitz.open()

        for page_num in range(start_page, min(end_page, pdf_document.page_count)):
            pdf_writer.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

        output_pdf = f"{output_pdf_prefix}_{start_page}_{end_page}.pdf"
        pdf_writer.save(output_pdf)

def merge_pdfs(pdf_list, output_pdf):
    pdf_writer = fitz.open()

    for pdf in pdf_list:
        with fitz.open(pdf) as pdf_document:
            pdf_writer.insert_pdf(pdf_document)

    pdf_writer.save()

# 示例用法
# 拆分 PDF
split_pdf('PQ3_240119153939.pdf', 'split', 0, 39)
split_pdf('1111_240119165940.pdf', 'split', 0, 1)
split_pdf('PQ3_240119153939_1.pdf', 'split', 40, 55)

# 合并所需页数的 PDF
merge_pdfs(['split_0_39.pdf', 'split_0_1.pdf', 'split_40_55.pdf'], 'merged2.pdf')
