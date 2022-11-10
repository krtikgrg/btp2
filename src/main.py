# importing required modules 
import textFromPDF
from preprocess import preprocess
from download import download

# download()
sentenceWiseWords = preprocess(textFromPDF.getTextFromPDF("check.pdf"))
print(sentenceWiseWords)