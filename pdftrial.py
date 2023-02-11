import PyPDF2

pdffileobj = open('trial.pdf', 'rb')
pdfreader = PyPDF2.PdfReader(pdffileobj)
pageobj = pdfreader.pages[0]
text = pageobj.extract_text()
file1 = open("waiver.txt", 'w')
file1.writelines(text)