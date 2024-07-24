
import logging
import gensim.downloader as api
from gensim.models import Word2Vec

# Enable logging for gensim - this will show training progress
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Load the dataset
dataset = api.load("text8")

# Train the Word2Vec model
model = Word2Vec(dataset, vector_size=200, window=5, min_count=5, sg=1, negative=5, epochs=15)

# Save the model
model.save("word2vec_new.model")
