from flask import Flask, render_template, request, jsonify
import gensim
import random

app = Flask(__name__)

# 加载新的 Word2Vec 模型
model = gensim.models.Word2Vec.load('word2vec_new.model')

used_combinations = set()  # 用于跟踪已经使用过的词语组合
generated_words = set()  # 用于跟踪所有生成过的词语

@app.route('/')
def index():
    return render_template('index.html')

def get_related_words(word, num_words, prev_words):
    try:
        # 获取更多相似的词语
        similar_words = model.wv.most_similar(positive=[word], topn=100)
        # 过滤掉最相似的前 10 个词语以避免同义词
        filtered_words = [w[0] for w in similar_words if w[0] not in prev_words][10:]
        # 随机选择较为跳跃的词语
        random.shuffle(filtered_words)
        related_words = random.sample(filtered_words, min(num_words, len(filtered_words)))
        return related_words
    except KeyError:
        return ["Word not in vocabulary"]

@app.route('/generate', methods=['POST'])
def generate():
    word = request.form['word']
    num_words = int(request.form['num-words'])
    prev_words = request.form.get('prev-words', '').split(',')
    prev_words = set(filter(None, prev_words))  # 过滤掉空字符串
    words = get_related_words(word, num_words, prev_words)
    for w in words:
        generated_words.add(w)  # 将生成的词语添加到集合中
    return jsonify({'words': words})

@app.route('/combine', methods=['POST'])
def combine():
    word1 = request.form['word1']
    word2 = request.form['word2']
    combination_key = f'{word1}:{word2}'

    if combination_key in used_combinations:
        return jsonify({'word': "Combination already used"})

    try:
        combined_word = model.wv.most_similar(positive=[word1, word2], topn=100)
        random.shuffle(combined_word)
        for w, _ in combined_word:
            if w not in generated_words and w != word1 and w != word2:  # 确保新词语不在已生成的词语中且不同于初始词语
                used_combinations.add(combination_key)
                generated_words.add(w)  # 将新生成的词语添加到集合中
                return jsonify({'word': w})
        return jsonify({'word': "No unique combination found"})
    except KeyError:
        return jsonify({'word': "Combination not in vocabulary"})

if __name__ == '__main__':
    app.run(debug=True)
