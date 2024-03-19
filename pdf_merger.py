from pypdf import PdfWriter

class PDFFiles:
    def add_pdfs(self, file_paths):
        merger = PdfWriter()
        with open('MERGER_OUTPUT.pdf', 'wb') as merger_pdf:
            for pdf_file in file_paths:
                merger.append(pdf_file)
            merger.write(merger_pdf)

pdffiles = PDFFiles()
# Can add numerous files. Here, I'm adding two files.
pdffiles.add_pdfs(['YOUR_FILE_PATH1.pdf','YOUR_FILE_PATH2.pdf'])
