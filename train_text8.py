import gensim.downloader as api
from gensim.models import Word2Vec

# 下载并加载 text8 数据集
print("Downloading text8 dataset...")
dataset = api.load('text8')
data = [d for d in dataset]
print("Download complete.")

# 打印前几行数据以确认下载成功
print("Sample data:", data[:5])

# 训练 Word2Vec 模型，调整 vector_size, window 和 min_count 参数
vector_size = 200  # 词向量的维度
window = 8         # 上下文窗口大小
min_count = 2      # 最小词频

print("Training Word2Vec model...")
model = Word2Vec(sentences=data, vector_size=vector_size, window=window, min_count=min_count, workers=4)
print("Model training complete.")

# 保存模型
model.save('word2vec.model')
print("Model saved as 'word2vec.model'.")
