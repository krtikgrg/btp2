# importing required modules 
import textFromPDF
from preprocess import preprocess
from download import download
from webCheck import getSimilarArticleURLS
from similarity import getSimilarity

# download()
sentenceWiseWords = preprocess(textFromPDF.getTextFromPDF("Reflection.pdf"))
getSimilarity(getSimilarArticleURLS(sentenceWiseWords),sentenceWiseWords)
# print(sentenceWiseWords)