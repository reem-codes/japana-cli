from janome.tokenizer import Tokenizer
import re


def main(text, kana, asc):
    t = Tokenizer()
    tokens = t.tokenize(text)
    print("total word count: ", len(tokens))
    kanji = r'[ぁ-ゟ]*[㐀-䶵一-鿋豈-頻][ぁ-ゟ]*'
    letters = r'[ぁ-んァ-ン一-龯]|[㐀-䶵一-鿋豈-頻]'

    words = dict()
    for token in tokens:
        word = dict()
        if words.get(token.base_form) is None and re.match(letters if kana else kanji, token.base_form):
            word["word"] = token.base_form
            word["frequency"] = 1
            words[token.base_form] = word
        elif words.get(token.base_form):
            words[token.base_form]["frequency"] += 1

    print("unique word count: ", len(words))
    words = [v for v in words.values()]
    words = sorted(words, key=lambda k: k['frequency'], reverse=not asc)
    word_count = list()
    for value in words:
        line = value["word"] + "\t" + str(value["frequency"]) + "\n"
        word_count.append(line)
    return word_count

