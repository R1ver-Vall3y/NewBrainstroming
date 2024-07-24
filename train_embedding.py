import gensim
from gensim.models import Word2Vec
from gensim.test.utils import common_texts

# 加载示例数据集（替换为你的数据集路径）
dataset = common_texts

# 训练 Word2Vec 模型
model = Word2Vec(sentences=dataset, vector_size=100, window=5, min_count=1, workers=4)

# 保存模型
model.save("word2vec.model")
