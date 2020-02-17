# coding: utf-8
import json

pokedex_path = 'pokedex.json'

with open(pokedex_path,encoding='utf-8') as f:
    pokedex = json.load(f)


# print(pokedex[0]['name'][0])

shiritori = {}
for word in pokedex:
    set_pokemon = {}

    # 基本的には最後の文字を使用する
    lastplace = -1

    # ニドラン♂、ニドラン♀の時
    if word['name'][lastplace] == '♂' or word['name'][lastplace] == '♀':
        set_pokemon['lastword'] = 'ス'
    # ポリゴン2の時
    elif word['name'][lastplace] == '2':
        set_pokemon['lastword'] = 'ツ'
    # ポリゴンZの時
    elif word['name'][lastplace] == 'Z':
        set_pokemon['lastword'] = 'ト'
    else:
        # 最後の文字が長音の時は、直前の文字を使用する
        if word['name'][lastplace] == 'ー':
            lastplace = -2
        # カタカナの小文字は大文字にする
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
            # それ以外の場合はそのまま使用する
            set_pokemon['lastword'] = word['name'][lastplace]
    # フラグのデフォルト値はFalse
    set_pokemon['flag'] = False

    # 頭文字の配列が無ければ連想配列として初期化
    if word['name'][0] not in shiritori:
        shiritori[word['name'][0]] = {}
    # ポケモンの名前で配列を保存
    shiritori[word['name'][0]][word['name']] = set_pokemon

# print(shiritori['ア'])

shiritori_word = "ア"
shiritori_flag = True
while shiritori_flag:
    # print(shiritori[start_word].keys)
    for word in shiritori[shiritori_word].values():
        print(word.keys)
        if not word['flag']:
            shiritori_word = word['lastword']

        print(word)
    # shiritori_flag = False

