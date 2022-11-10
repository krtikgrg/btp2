# importing required modules 
import textFromPDF
from preprocess import preprocess
from download import download
from webCheck import getSimilarArticleURLS

# download()
sentenceWiseWords = preprocess(textFromPDF.getTextFromPDF("lit.pdf"))
getSimilarArticleURLS(sentenceWiseWords)
# print(sentenceWiseWords)