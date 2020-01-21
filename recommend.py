import pandas as pd
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import sys
data=pd.read_csv('cleaned_1.csv')
def voting_hash(tweet):
    
    model= Doc2Vec.load("d2v.model")
    best_hashes={}
    test_data = word_tokenize(tweet.lower())
    v1 = model.infer_vector(test_data)
    print("V1_infer", v1)
    similar_documents = model.docvecs.most_similar([v1], topn = 5)
    for i in similar_documents:
#         print(tweets[int(i[0])])
        if data.iloc[int(i[0])]['hash'] in best_hashes:
            best_hashes[data.iloc[int(i[0])]['hash']]+=1
        else:
            best_hashes[data.iloc[int(i[0])]['hash']]=1
    best='none'
    max1=0
    for i in best_hashes:
        if best_hashes[i]>max1:
            best=i
            max1=best_hashes[i]
    print(best_hashes)
    return best


tweet=''
args=sys.argv
print("recommended hashtag is : " + args[1])




