nome = input('Nome: ')

if nome == 'Gabriel' or nome == 'gabriel':
    senha = input('Senha: ') 
    senha_permitida = '123'
    if senha == senha_permitida:
        print('Welcome to new world')
        regiao =  input('Selecione a região desejada: ')
        regiao_base1 = 'Sudeste'
        regiao_base2 = 'Norte'
        regiao_base3 = 'Nordeste'
        regiao_base4 = 'Centro Oeste'
        regiao_base5 = 'Sul'

        if regiao == regiao_base1:
            print('Você selecionou o Sudeste, boa escolha.' ' Agora selecione 1 dos 3 estados.')
            estado = input('Estado: ')
            estados1 = 'São Paulo'
            estados2 = 'Minas Gerais'
            estados3 = 'Rio de Janeiro'

            if estado == estados1:
                print('Boa manoo!')
            elif estado == estados2:
                print('Uai sô trem uai')
            elif estado == estados3:
                print('Perdu turixta, passa a carteria!')    
        if regiao == regiao_base2:
            print('Você selecionou o Norte, boa escolha.' ' Agora selecione 1 dos 3 estados.')
            estado = input('Estado: ')
            estados1 = 'Amazonas'
            estados2 = 'Para'
            estados3 = 'Acre'

            if estado == estados1:
                print('Seja bem vindo Manauara!')
            elif estado == estados2:
                print('Entre, tem show do Calipso as 14:00')
            elif estado == estados3:
                print('Aaaaaaaaaaaa, cuidado com o Tiranossauro REEEEX!')

        if regiao == regiao_base3:
            print('Você selecionou o Nordeste, boa escolha.' ' Agora selecione 1 dos 3 estados.')
            estado = input('Estado: ')
            estados1 = 'Alagoas'
            estados2 = 'Bahia'
            estados3 = 'Pernambuco'

            if estado == estados1:
                print('Seja bem vindo Alagoano')
            elif estado == estados2:
                print('Seja bem vindo meu rei, quer acarajé?')
            elif estado == estados3:
                print('Seja bem vindo, vai à praia dos Carneiros')
        
        if regiao == regiao_base4:
            print('Você selecionou o Centro oeste, boa escolha.' ' Agora selecione 1 dos 3 estados.')
            estado = input('Estado: ')
            estados1 = 'Mato Grosso'
            estados2 = 'Goias'
            estados3 = 'Distrito Federal'

            if estado == estados1:
                print('Aaooo Potencia! Chega junto vaqueiro')
            elif estado == estados2:
                print('Seja bem vindo aqui no Goiás homi.')
            elif estado == estados3:
                print('Seja bem vindo, já pagou os impostos?')

        if regiao == regiao_base5:
            print('Você selecionou o Sul, boa escolha.' ' Agora selecione 1 dos 3 estados.')
            estado = input('Estado: ')
            estados1 = 'Parana'
            estados2 = 'Santa Catarina'
            estados3 = 'Rio Grande do Sul'

            if estado == estados1:
                print('Seja bem vindo, tá frio aqui né piá?')
            elif estado == estados2:
                print('Seja bem vindo! Vai um churrasco de vina?')
            elif estado == estados3:
                print('Seja bem vindo, tá fazendo o que aqui?')


elif nome == 'abriel' or 'gabrel':
     print('Usuario inválido')

     print('Tente novamente.')

