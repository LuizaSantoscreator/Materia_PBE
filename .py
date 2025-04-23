import random

itens = {
    '1': {'nome': 'Porção de força' , 'efeito': 'ataque +20', 'turn': 2},
    '2': {'nome': 'Porção de regeneração' , 'efeito': 'vida +50', 'turn': 3},
    '3': {'nome': 'Porção de fraqueza' , 'efeito': 'ataque inimigo -20', 'turn': 2}

}

efeito_jogador = {
    'efeito': '',
    'duração': 0
}

while True:
    print("----Joguinho----")
    print('1. Iniciar Game')
    print('2.Sair')
    opcao = input('Escolha: ')
    if opcao == '2':
        print('Até mais')
        break
    elif opcao == '1':
        hp = random.randint(200, 1000)
        ataque_jogador = random.randint(1,50)
        ataque_inimigo = random.randint(1,50)
        defesa_jogador = random.randint(1, ataque_inimigo)
        defesa_inimigo = random.randint(5, ataque_jogador)

        jogador = {
            "hp": hp,
            "ataque": ataque_jogador,
            "defesa": defesa_jogador
        }
        inimigo = {
            "hp": hp,
            "ataque": ataque_inimigo,
            "defesa": defesa_inimigo
        }
        while jogador['hp'] > 0 and inimigo ['hp'] > 0:
            print(f'Se o HP: {jogador['hp']} ')
            print(f'Seu ataque {jogador['ataque']}')
            print(f'Sua defesa {jogador['defesa']}')

            print(f'Se o HP: {inimigo['hp']} ')
            print(f'Seu ataque {inimigo['ataque']}')
            print(f'Sua defesa {inimigo['defesa']}')

            if efeito_jogador['efeito'] == '1':
                if efeito_jogador['duração'] > 0:
                    efeito_jogador['duração'] -= 1
                else:
                    jogador['ataque'] -= 20
                    efeito_jogador['efeito'] = ''
            if efeito_jogador['efeito'] == '2':
                if efeito_jogador['duração'] > 0:
                    efeito_jogador['duração'] -= 1
                    jogador['hp'] +=50
                else:
                    efeito_jogador['efeito'] = ''
            if efeito_jogador['efeito'] == '3':
                if efeito_jogador['duração'] > 0:
                    efeito_jogador['duração'] -= 1
                else:
                    inimigo['ataque'] += 20
                    efeito_jogador['efeito'] = ''

            escolha = input('[1] Atacar [2] Curar [3] Itens')

            if escolha == '1':
                dano = jogador['ataque'] - inimigo['defesa']
                if random.random() < 0.1:
                    dano = dano * 2
                inimigo ['hp'] = inimigo['hp'] - dano
                print(f'Você causou {dano} de dano')
                print(f'O inimigo ficou com {inimigo['hp']} de vida')
            elif escolha == '2':
                cura = 20
                if jogador['hp'] + cura > hp:
                    jogador['hp'] = hp
                else:
                    jogador['hp'] += cura
                print(f'Você ficou com {jogador['hp']} de vida')
            elif escolha == '3':
                print('Itens disponiveis')
                for chave , valor in itens.items():
                    print(f'[{chave}] {valor['nome']} - {valor['efeito']}')
                escolha_item = input('Escolha um item: ')
                if escolha_item == '1':
                    jogador['ataque'] += 20
                    efeito_jogador['efeito'] = '1'
                    efeito_jogador['duração'] = 2
                    print('Ataque auentado por dois turnos!')
                elif escolha_item == '2':
                    jogador[hp] += 50
                    efeito_jogador['efeito'] = '2'
                    efeito_jogador['duração'] = 3
                    print('cura aumentada em 50 por dois turnos!')
                elif escolha_item == '3':
                    inimigo['ataque'] -=20
                    efeito_jogador['efeito'] = '3'
                    efeito_jogador['duração'] = 2
                    print('Ataque inimigo diminuido em 20 por dois turnos!')
                else:
                    print('Opção inválida')

            else:
                print('opção inválida')

            if inimigo['hp'] <= 0:
                print('Você venceu!')
                break

            escolha = random.choice(['1','2'])
            if escolha == '1':
                dano = inimigo['ataque'] - jogador['defesa']
                if random.random() < 0.1:
                    dano = dano * 2
                jogador['hp'] -= dano
                print(f'Você causou {dano} de dano')
                print(f'O jogador ficou com {jogador['hp']} de vida')
            elif escolha == '2':
                cura = 20
                if inimigo['hp'] + cura > hp:
                    inimigo['hp'] = hp
                else:
                    inimigo['hp'] += cura
            if inimigo['hp'] <= 0:
                print('Você perdeu')
                break
