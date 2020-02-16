# coding: utf-8
import json

pokedex_path = 'pokedex.json'

with open(pokedex_path,encoding='utf-8') as f:
    pokedex = json.load(f)


print(pokedex[0]['name'])
