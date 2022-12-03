from webCheck import extractText
from preprocess import preprocess
import numpy as np
import distance

def getDocumentVector(list2D,mapper,ctr):
    soln = [0]*(ctr+1)
    for sent in list2D:
        for word in sent:
            soln[mapper[word]]+=1
    soln = np.array(soln)
    soln = soln/len(list2D)
    return soln

def processURL(url,suspectSentWords):
    text = "\n".join(extractText(url).split("\n"))
    text = ".".join(text.split("\n"))
    text = " ".join(text.split())
    text = text[:500]
    sourceSentWords = preprocess(text)
    
    
    ctr = 0
    mapperWords = {}
    
    for sentence in suspectSentWords:
        for word in sentence:
            if word not in mapperWords:
                mapperWords[word] = ctr                
                ctr += 1
    
    limits = 2*ctr                    
    for sentence in sourceSentWords:
        for word in sentence:
            if word not in mapperWords:
                mapperWords[word] = ctr                
                if ctr<limits:
                    ctr += 1
                else:
                    mapperWords[word] = ctr
    
    sourceVec = getDocumentVector(sourceSentWords, mapperWords, ctr)
    suspectVec = getDocumentVector(suspectSentWords, mapperWords, ctr)
    
    csim = distance.cosine_s(sourceVec, suspectVec)
    csim = csim*100
    print("Found ",csim,"% Similar with ",url)

        
    
def getSimilarity(urls, suspectSentWords):
    urls = list(urls)[:10]
    for url in urls:
        print(url)

    for url in urls:
        processURL(url,suspectSentWords)