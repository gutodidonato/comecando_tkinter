from manutencao import *
usuarios = {}

print("BEM VINDO A VISTORIA DE BICICLETAS DA PORTO SEGURO!")
'''verificação de conta'''
conta = realizar_pergunta(pergunta="Você já tem conta na Porto-Seguro? Sim ou Não?", afirmacao="sim", negacao="não")
if conta == "sim":
    email, nome, endereco, nota_fiscal = fazer_login()
    '''verificar se já cadastrou a bicicleta'''
    cadastro_bicicleta = print("VERIFICAR NO SISTEMA, SELECT")
    if cadastro_bicicleta == "sim" :
        alterar_status = realizar_pergunta(pergunta="Deseja atualizar seus dados ou verificar status? Digite Status ou Alterar")
        if alterar_status == "alterar":
            print("UPDATE")
        elif alterar_status == "status":
            print("SELECT")  
    else:   
        marca_bike = corrigir_tipo_pergunta(tipo="String", pergunta="Digite a marca da sua bicicleta:") 
        modelo_bike = corrigir_tipo_pergunta(tipo="String", pergunta="Digite o modelo da sua bicicleta:") 
        bicicleta = {"marca": marca_bike, "modelo": modelo_bike}
        usuarios[email] = {"nome": nome, "bicicleta": bicicleta, "endereco": endereco, "nota_fiscal": nota_fiscal}
        '''verificar se já existe esta bicicleta'''
        print("VERIFICAR SE JA EXISTE ")
        bem_vindo(nome, bicicleta, endereco, nota_fiscal)
elif conta == "nao":
    cadastrar_cliente()
    '''ou'''
    conta_nova = realizar_pergunta(pergunta="Deseja criar uma conta nova? (Sim/Não): ", afirmacao="sim", negacao="não")
    if conta_nova == "sim":
        email, endereco, nota_fiscal, nome = criar_conta()
        marca_bike = input("Digite a marca da sua bicicleta: ")
        modelo_bike = input("Digite o modelo da sua bicicleta: ")
        bicicleta = {"marca": marca_bike, "modelo": modelo_bike}
        usuarios[email] = {"nome": email, "bicicleta": bicicleta, "endereco": endereco, "nota_fiscal": nota_fiscal}
        bem_vindo(email, bicicleta, endereco, nota_fiscal)
print("Adeus! Agradecemos o contato! Caso tenha alguma dúvida, entre em contato com a Porto Seguro pelo telefone: (11)3003-9303")
