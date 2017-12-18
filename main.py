import embeddings

emb = embeddings.EmbeddingsDictionary (100000)
emb.w2neighbors ('hello')

if __name__ == '__main__':
    emb.w2neighbors('geek', 10)
    emb.