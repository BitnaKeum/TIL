
##### 여러 pdf 파일을 병합하여 하나의 pdf로 만드는 프로그램 #####
##### https://wikidocs.net/103937 #####


from PyPDF2 import PdfFileMerger

pdfs = ['합칠 파일 1.pdf', '합칠 파일 2.pdf', '합칠 파일 3.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("합친 파일.pdf")
merger.close()
