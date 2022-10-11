from sentence_transformers import SentenceTransformer
import scipy
import Data

model = SentenceTransformer('bert-base-nli-mean-tokens')
sentence_embeddings = model.encode(Data.sentences)

class Recom:
    def __init__(self,topic):
        self.query=topic
        self.res=[]

    def find_sim(self):
        queries = [self.query]
        query_embeddings = model.encode(queries)
        number_top_matches = 10
        for query, query_embedding in zip(queries, query_embeddings):
            distances = scipy.spatial.distance.cdist([query_embedding], sentence_embeddings, "cosine")[0]
            results = zip(range(len(distances)), distances)
            results = sorted(results, key=lambda x: x[1])
            for idx, distance in results[0:number_top_matches]:
                # print(Data.sentences[idx].strip(), "(Cosine Score: %.4f)" % (1 - distance))
                self.res.append(Data.sentences[idx].strip())
        return self.res






