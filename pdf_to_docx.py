from pdf2docx import Converter

pdf_file = './data/test.pdf'
docx_file = './docx/output.docx'

cv = Converter(pdf_file)

cv.convert(docx_file, start=0, end=None)

cv.close()

print(f"Successfully converted {pdf_file} to {docx_file}")
