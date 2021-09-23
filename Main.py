import os #importei essa biblioteca para poder apagar os clientes.
from datetime import datetime #importei essa biblioteca para poder capturar o horário exato.
entrada = 10 # criei essa variável para dar condição ao meu menu para ele ficar em loop infinito.

while entrada != 0:
    print("QuemPoupaTem-Menu")
    print("1 - Novo Cliente")       # esse é o menu em loop infinito que foi exigido, enquanto a variável não for igual a 0 ele continuará aparecendo.
    print("2 - Apagar Cliente")
    print("3 - Debita")
    print("4 - Deposita")
    print("5 - Saldo")
    print("6 - Extrato")
    print("0 - Sair")
    entrada = int(input("Digite a função desejada: ")) #aqui eu consigo trocar o valor da variavel para assim conseguir parar o loop com "0" ou chamar a função na qual cada número pertence.  
    
    
    def novo_cliente(): #criei essa função para cadastrar um novo cliente, salvando os dados de cada um em um arquivo.
        nome=str(input("Digite seu Nome:")) #cadastrar o nome.
        cpf=str(input("CPF:")) #cadastrar o CPF em formato string como o professor sugeriu.
        tipo_de_conta=str(input("tipo_de_conta(salário, comum ou plus):")) #cadastrar o tipo de conta.
        valor_inicial=str(input("valor_inicial_da_conta:")) #cadastrar a quantia inicial de dinheiro da conta.
        senha_do_usuario=str(input("senha:")) #cadastrar a senha da conta.
        if len(cpf)==11:#condição para ter um limite de 11 digitos o CPF.
            if tipo_de_conta =="salário" or tipo_de_conta== "comum" or tipo_de_conta=="plus":#condição para que não seja atribuida outra string no "tipo de conta".
                if float(valor_inicial)>0:#condição para que não seja digitado números menores que zero. 
                    txt1 = open("%s.txt" % (cpf) , "a") #abri o arquivo para poder salvar os dados do cliente.
                    txt1.write("%s %s %s %s %s" % (nome,cpf,tipo_de_conta,valor_inicial,senha_do_usuario)) #enviei todos os dados cadastrados para dentro do arquivo.
                    txt1.close() #salvei o arquivo e fechei
                    contaextrato= open("contaextrato"+cpf+".txt", "w") #abri esse arquivo para facilitar na hora de printar o extrato na função final.
                    contaextrato.close() # fechei e salvei o arquivo que por enquanto está vazio.
                else:
                    print("O valor inicial tem que ser maior que 0")
            else:
                print("Tem que ser conta do tipo: salário, comum ou plus")        
        else:
            print("Digite um CPF com 11 digítos")

    def apagar_cliente():#criei essa função para apagar a conta(arquivo) do cliente.
        cpf = input("Digite o CPF do cliente para deletá-lo: ") #com esse código consegue achar o nome do arquivo com base no CPF digitado. 
        os.remove("%s.txt" % (cpf)) #esse código serve para remover o arquivo com os dados do cliente com base no CPF digitado. 
        os.remove("contaextrato"+cpf+".txt") #idem a linha anterior

    def debitar(): #criei essa função para fazer o débito na conta.
        cpf=input("Insira o CPF para realizar o débito:") #digitar o CPF para acessar os dados do cliente.
        txt1 = open(cpf +".txt" , "r") #abri o arquivo no modo leitura o para conseguir usar o readlines no loop que explicarei como funciona logo a seguir.  
        contaextrato= open("contaextrato"+cpf+".txt", "a") #abri para poder ir salvando dentro do arquivo cada débito realizado.
        pesquisar= [] #criei essa lista para que eu consiga pesquisar pelo arquivo elementos nele presente.
        
        for linha in txt1.readlines():  #esse loop serve para poder acessar e salvar na lista cada elemento dentro do arquivo aberto anteriormente dentro dessa função.
            separada = linha.split(" ") #funciona da seguinte forma: para cada linha do arquivo a variável separada se iguala a cada elemento da linha atraves do espaçamento que o split buscou.
            pesquisar.append(separada)  # com isso todos os elementos do arquivo é copiado na lista.
        txt1.close() # depois disso fecho o arquivo.
        senha_do_usuario= input("Insira a senha para realizar o débito:") #inserir a senha do usuário para poder debitar.
        
        #como todos os dados foram copiados e colados na lista da para dar condições de realizar alguma função dentro do arquivo usando elementos da lista.
        if senha_do_usuario == pesquisar[0][4]: #esse condição serve para verificar se a senha digitada esta de acordo com a informada no cadastro e se estiver correta para realizar o código seguinte.
            txt1= open(cpf+".txt", "w") #serve para abrir o arquivo para eu conseguir escrever dentro dele o valor resultante depois do débito.
            saque= float(input("Insira um valor pra debitar:")) # valor para debitar.
            if pesquisar[0][2] == "salário": #como foi dada três condições para a realização desse projeto, aqui vai uma delas, quando a conta é do tipo "salário".
                taxa=0.05 #o valor da taxa estabelecida que teve que ser posta como uma variável, porque estava dando erro.
                valor_de_taxa= saque + saque * taxa # a quantia resultante depois do débito com a taxa.
                tarifa= taxa*float(saque) #variável que serve para mostrar o quanto de tarifa teve esse débito com base no valor sacado e na taxa.
                if float(pesquisar[0][3]) > valor_de_taxa: #condição exigida no projeto: para que a quantia dentro do arquivo seja maior que a debitada para assim não ficar no negativo.
                    pesquisar[0][3]= float(pesquisar[0][3]) - valor_de_taxa #atribuição de um novo valor: agora a quantia é igual a quantia anterior menos o valor debitado com a taxa.

                    data= datetime.now().strftime("%d - %m - %Y %H:%M") #código básico para pegar o horário atual fornecido pelo computador. 
                    contaextrato.write("Data: %s - %s Tarifa: %.2f Saldo: %.2f\n" % (data,saque,float(tarifa),float(pesquisar[0][3]))) #código que escreve no arquivo do extrato todos os componentes exigidos no projeto.
                    contaextrato.close()#fecha e salva o arquivo,agora, atualizado.

                else:
                    print("Esse tipo de conta não permite que o saldo fique negativo") #caso o valor debitado seja maior do que a quantia que existia no arquivo.

            elif pesquisar[0][2] == "comum": #como foi dada três condições para a realização desse projeto, aqui vai uma delas, quando a conta é do tipo "comum".
                taxa=0.03 #taxa atribuida para esse tipo de conta.
                valor_de_taxa= saque + saque * taxa # a quantia resultante depois do débito com a taxa.
                limite= -500 #difente da conta "salário", essa tem um limite de 500 reais negativo.
                tarifa= taxa*float(saque) #variável que serve para mostrar o quanto de tarifa teve esse débito com base no valor sacado e na taxa.
                if limite < float(pesquisar[0][3]) - valor_de_taxa: #para que quantia menos o debito seja maior que o limite exigido.
                    pesquisar[0][3]= float(pesquisar[0][3]) - valor_de_taxa #idem a explicação com o tipo de conta "salário". 

                    data= datetime.now().strftime("%d - %m - %Y %H:%M")#idem a explicação com o tipo de conta "salário".
                    contaextrato.write("Data: %s - %s Tarifa: %.2f Saldo: %.2f\n" % (data,saque,float(tarifa),float(pesquisar[0][3])))#idem a explicação com o tipo de conta "salário".
                    contaextrato.close()#idem a explicação com o tipo de conta "salário".

                else:
                    print("Esse tipo de conta não permite que o saldo fique com menos que 500 reais negativo")#caso o valor a quantia menos o valor debitado seja resulte num valor menor que o do limite exigido.

            elif pesquisar[0][2] == "plus": #esse tipo de conta possui o mesmo formato do tipo de conta "comum", sendo assim a explicação de como funciona o código é a mesma. 
                taxa= 0.01
                valor_de_taxa= saque + saque * taxa
                limite= -5000
                tarifa= taxa*float(saque)
                if limite < float(pesquisar[0][3]) - valor_de_taxa:
                    pesquisar[0][3]= float(pesquisar[0][3]) - valor_de_taxa

                    data= datetime.now().strftime("%d - %m - %Y %H:%M")
                    contaextrato.write("Data: %s - %s Tarifa: %.2f Saldo: %.2f\n" % (data,saque,float(tarifa),float(pesquisar[0][3])))
                    contaextrato.close()

                else:
                    print("Esse tipo de conta não permite que o saldo fique com menos que 5000 reais negativo")
            for elementos in pesquisar:         # esse loop foi criado para "atualizar" o valor da quantia de dinheiro. 
                for valores in elementos:       # ele funciona da seguinte maneira: para cada elemento na lista, cada valor atribuido para o elemento é escrito no arquivo. 
                    txt1.write("%s "% (valores))

            txt1.close()#criado para salvar todas as informações atualizadas no arquivo.                        
        else:
            print("Senha inválida")# caso a senha digitada não esteja correta.

    def depositar(): #criei essa função para fazer o depósito na conta.
        cpf=input("Insira o CPF para realizar o depósito:") #para acessar o arquivo através dessa variável.
        txt1 = open(cpf +".txt" , "r")# explicação identica da função de debitar.
        contaextrato= open("contaextrato"+cpf+".txt", "a")
        pesquisar= []
        
        for linha in txt1.readlines(): #explicação identica da função de debitar, tem o mesmo propósito.
            separada= linha.split(" ")
            pesquisar.append(separada)
        txt1.close()

        if cpf in pesquisar[0][1]:#condição para realizar a função de depositar quantia se o CPF digitado estiver correto.
            txt1= open(cpf+".txt", "w")
            deposito= float(input("Insira um valor pra depositar:"))
            pesquisar[0][3]= float(pesquisar[0][3]) + deposito #código para atualizar o valor da quantia com base no valor da variável "deposito".
            tarifa=0.00 #para depositar não há tarifa nesse projeto.

            data= datetime.now().strftime("%d - %m - %Y %H:%M") #explicação identica ao da função de debitar, com o mesmo propósito.
            contaextrato.write("Data: %s + %s Tarifa: %s Saldo: %.2f\n" % (data,deposito,tarifa,float(pesquisar[0][3])))#explicação identica ao da função de debitar, com o mesmo propósito, com diferença no valor da tarifa e no simbolo de adição.
            contaextrato.close()

            for elementos in pesquisar: #loop com o mesmo propósito e explicação do loop feito na função "debitar".
                for valores in elementos:
                    txt1.write("%s "% (valores))
            txt1.close()                        
        else:
            print("CPF inválido") #caso o CPF digitado esteja errado, código sem muita função, porque para acessar o arquivo eu necessito do CPF digitado corretamente.

    def saldo(): #função criada para mostrar a quantia atualizada do dinheiro.
        cpf=input("Insira o CPF para consultar o seu saldo:")
        txt1 = open(cpf +".txt" , "r")
        pesquisar= []                    #basicamente essa função tem os mesmos componentes das funções anteriores, com um pequeno detalhe de diferente, essa função só mostra a quantia de dinheiro não requer nehuma operação matemática.        
        for linha in txt1.readlines():
            separada= linha.split(" ")
            pesquisar.append(separada)
        txt1.close()

        senha_do_usuario= input("Insira a senha para consultar seu saldo:")
        if senha_do_usuario == pesquisar[0][4]: #condição para verificar se a senha digitada está correta.
            print("Seu saldo é de: R$%s" % (pesquisar[0][3]))
        else:
            print("Senha inválida")

    def extrato(): #criei essa função para mostrar toda movimentação financeira da conta.
        cpf=input("Insira o CPF para consultar seu extrato completo:")
        txt1 = open(cpf +".txt" , "r")                      #como essa função é somente de leitura abri os arquivos no modo leitura.
        contaextrato= open("contaextrato"+cpf+".txt", "r")
        pesquisar= []#essa é para ler só o arquivo que esta os dados da conta.
        pesquisar2= []#criei outra matriz para que o programa leia o arquivo que esta o extrato.
        
        for linha in txt1.readlines(): #esse loop serve para poder acessar e salvar na lista cada elemento dentro do arquivo aberto anteriormente dentro dessa função.
            separada = linha.split(" ")                       #^
            pesquisar.append(separada)                        #|
        txt1.close()                                          #|
        for linha in contaextrato.readlines():#idem a anterior   só que para outra lista.
            separada = linha.split(" ")
            pesquisar2.append(separada)
        contaextrato.close()
        senha_do_usuario= input("Insira a senha para consultar seu extrato completo:") #a senha tem que ser digitada.
        

        if senha_do_usuario == pesquisar[0][4]:#condição para verificar se a senha digitada esta correta.
            print("Nome:",pesquisar[0][0])#dado exigido no extrato.
            print("CPF:",pesquisar[0][1])#dado exigido no extrato.
            print("Conta:",pesquisar[0][2])#dado exigido no extrato.

            linhas = len(pesquisar2) #variável que se iguala ao valor de linhas da lista que foi salvo dados do arquivo extrato.
            colunas = len(pesquisar2[0])#variável que se iguala ao valor de colunas da lista que foi salvo dados do arquivo extrato.

            for i in range(linhas):        #esses loops foram feitos para printar cada elemento da lista até  sobrar nada para printar. 
                for j in range(colunas):   #funciona da seguinte maneira: para cada elemento "i"(coloquei só uma letra pra não ficar estéticamente feio, no colchete) na linha, cada elemento na coluna se o elemento da coluna for igual ao da coluna mais um o loop fará printar a parte da lista que é equivalente aos índices "i" e "j", caso contrário irá printar até não haver mais nada a ser printado, ou seja, sem dados.
                    if(j == colunas + 1):
                        print("%s" %pesquisar2[i][j])
                    else:
                        print("%s" %pesquisar2[i][j], end = " ")
        else:
            print("Senha inválida") # caso a senha digitada esteja errada.



    if entrada == 1: #condição para chamar a função de criar cliente.
        novo_cliente()
    if entrada == 2: #condição para chamar a função de deletar cliente.
        apagar_cliente()
    if entrada == 3: #condição para chamar a função de debitar valores da conta.
        debitar()
    if entrada == 4: #condição para chamar a função de depositar valores na conta.
        depositar()
    if entrada == 5: #condição para chamar a função que mostra o saldo atualizado da conta.
        saldo()    
    if entrada == 6: #condição para chamar a função que mostra o extrato com todos os movimentos feitos na conta(extrato).
        extrato()           
