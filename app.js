document.getElementById('word-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const word = document.getElementById('word-input').value;
    const count = document.getElementById('word-count').value;

    fetch(`/generate?word=${word}&count=${count}`)
        .then(response => response.json())
        .then(data => {
            const generatedWordsDiv = document.getElementById('generated-words');
            generatedWordsDiv.innerHTML = '';
            data.words.forEach(w => {
                const wordSpan = document.createElement('span');
                wordSpan.textContent = w;
                generatedWordsDiv.appendChild(wordSpan);
            });
        });
});
