with open('arquivo.txt', 'wt') as smog:
    smog.write('smogon')

with open('arquivo.txt', 'r') as smog:
    dados1 = smog.read()

print(dados1)


import json
with open('arquivo.json', 'wt') as smog:
    var = 'smogon'
    json.dump(var, smog)
with open('arquivo.json', 'r') as smog:
    dados2 = json.load(smog)
print(dados2)
    