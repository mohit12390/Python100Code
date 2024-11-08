from pypdf  import PdfWriter
import os
pdf_merger = PdfWriter()

path = "E:\Python_Hindi\pythonProject\mergepdf"
list_pdf = []
list_file  = os.listdir(path)
# print(list_file)

for i in list_file:
    if i.endswith(".pdf"):
        list_pdf.append(i)

print(list_pdf)

for pdf in list_pdf:
    pdf_merger.append(pdf)

pdf_merger.write("merged.pdf")
pdf_merger.close()
