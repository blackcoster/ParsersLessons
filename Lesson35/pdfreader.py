from urllib.request import urlopen

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from io import StringIO

def readPDF(pdfFile):
    rsrcmngr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmngr,retstr,laparams=laparams)
    process_pdf(rsrcmngr,device,pdfFile)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content


pdfFile = urlopen('https://pythonscraping.com/pages/warandpeace/chapter1.pdf')
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()

