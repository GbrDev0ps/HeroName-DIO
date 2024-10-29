print('Bem-vindo, novo jogador!')
hero_name = input('Digite o nome para seu herói: ')
xp = int(input('Diga o nivel de xp do seu personagem (entre 0 e 100000)'))

if xp < 1000:
    nivel = "Ferro"
elif xp < 2000:
    nivel = "Bronze"
elif xp < 5000:
    nivel = "Prata"
elif xp < 7000:
    nivel = "Ouro"
elif xp < 8000:
    nivel = "Platina"
elif xp < 9000:
    nivel = "Mestre"
elif xp < 10000:
    nivel = "Imortal"
elif xp > 10001:
    nivel = "Radiante"
    
print(f"O herói {hero_name} está no nivel {nivel}")