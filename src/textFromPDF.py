import PyPDF2 
def getTextFromPDF(filepath):
    pdfFileObj = open(filepath, 'rb') 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    fulltext = "" 
    numPages = pdfReader.numPages 
    # print(numPages)
    for i in range(numPages):        
        pageObj = pdfReader.getPage(i) 
        fulltext += pageObj.extractText() 
        fulltext += "\n"
    
    fulltext = fulltext.split('\n')
    fulltext = " ".join(fulltext)  
    fulltext = " ".join(fulltext.split())
    pdfFileObj.close() 
    return fulltext