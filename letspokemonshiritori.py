# coding: utf-8
import json

pokedex_path = 'pokedex.json'

with open(pokedex_path,encoding='utf-8') as f:
    pokedex = json.load(f)


# print(pokedex[0]['name'][0])

# https://qiita.com/tag1216/items/b2765e9e87025c01e57f
shiritori = {}
for word in pokedex:
    # これで頭文字順に追加はできる
    # shiritori.setdefault(word['name'][0],[]).append(word['name'])
    set_pokemon = {}

    lastplace = -1
    if word['name'][lastplace] == '♂' or word['name'][lastplace] == '♀':
        set_pokemon['lastword'] = 'ス'
    else:
        # https://note.nkmk.me/python-re-regex-character-type/
        # カタカナ小文字の判別
        if word['name'][lastplace] == 'ー':
            lastplace = -2
        if word['name'][lastplace] == "ァ":
            set_pokemon['lastword'] = "ア"
        elif word['name'][lastplace] == "ィ":
            set_pokemon['lastword'] = "イ"
        elif word['name'][lastplace] == "ゥ":
            set_pokemon['lastword'] = "ウ"
        elif word['name'][lastplace] == "ェ":
            set_pokemon['lastword'] = "エ"
        elif word['name'][lastplace] == "ォ":
            set_pokemon['lastword'] = "オ"
        elif word['name'][lastplace] == "ッ":
            set_pokemon['lastword'] = "ツ"
        elif word['name'][lastplace] == "ャ":
            set_pokemon['lastword'] = "ヤ"
        elif word['name'][lastplace] == "ュ":
            set_pokemon['lastword'] = "ユ"
        elif word['name'][lastplace] == "ョ":
            set_pokemon['lastword'] = "ヨ"
        elif word['name'][lastplace] == "ヮ":
            set_pokemon['lastword'] = "ワ"
        elif word['name'][lastplace] == "ヵ":
            set_pokemon['lastword'] = "カ"
        elif word['name'][lastplace] == "ヶ":
            set_pokemon['lastword'] = "ケ"
        else:
            set_pokemon['lastword'] = word['name'][lastplace]

    set_pokemon['flag'] = 0
    if word['name'][0] not in shiritori:
        shiritori[word['name'][0]] = {}
    shiritori[word['name'][0]][word['name']] = set_pokemon
    # print(shiritori[word['name'][0]][word['name']])

print(shiritori['ハ'])

