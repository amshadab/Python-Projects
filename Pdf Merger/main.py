import PyPDF2
import os

def pdf_merge(pdf_list,output_pdf):
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)
    
    with open(output_pdf,'wb') as f:
        merger.write(f)
        
if __name__=='__main__':       
    num=int(input("Enter the total numbers of pdf: "))
    l=[]
    output_pdf="merged.pdf"
    for i in range(1,num+1):
        path=input(f"Enter pdf {i}: ")
        l.append(path)
    pdf_merge(l,output_pdf)
    

        


    