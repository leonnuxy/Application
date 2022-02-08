from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO


# Read PDF file and return its text
def read_pdf(pdf_file):
    rsrcmgr = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(rsrcmgr, retstr, laparams=layout)
    fp = open(pdf_file, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for page in PDFPage.get_pages(fp, check_extractable=True):
        interpreter.process_page(page)
    
    text = retstr.getvalue()
    words = " "
    for line in text.splitlines():
        if line.strip():
            
            print(line.decode('utf-8'))
            

    fp.close()
    device.close()
    retstr.close()
    return text



# Main function
def main():
    # # Get the path of the pdf file
    # pdf_file = sys.argv[1]
    pdf_file = "./File_Processing/Texts/resume.pdf"

    # Read and Extract the text from the pdf file
    text = read_pdf(pdf_file)

    # Get the text of the pdf file
    # print(text)


# Call the main function
if __name__ == '__main__':
    main()

