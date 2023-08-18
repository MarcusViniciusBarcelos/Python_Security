import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter


def start(url):
    wordlist = []  # lista vazia para armazenar o conteudo do site
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')  # vai fazer a requisição dos dados e transformar em html

    # vai procurar dentro do site tudo que existe com div, classes e tudo que existe dentro para transformar em texto
    for each_text in soup.findAll('div'):
        content = each_text.text

        # pega todo conteudo, joga em caixa baixa e transforma em linhas.
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


def clean_wordlist(wordlist):  # essa função retira todos os symbols e substitui por '' (nada)
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[]}|\;:"<>?/.,'

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:  # se o número de palavras na lista for maior que zero ele limpa a lista
            clean_list.append(word)
        create_dictionary(clean_list)


def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(),   # contador das palavras mais usadas no site
                             key=operator.itemgetter(1)):
        print("% s : % s " % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)
    print(top)


if __name__ == '__main__':
    start("https://en.wikipedia.org/wiki/Python_(programming_language)")
