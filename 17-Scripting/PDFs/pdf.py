import PyPDF2

with open('dummy.pdf', 'rb') as file:
    print(file)
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
