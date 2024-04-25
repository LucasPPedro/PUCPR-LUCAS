# Listas globais para funções "INCLUIR"
estudantes = []

# Funções incluir
def incluir_estudantes():
    print("Incluir Estudantes")
    while True:
        entrada = input("Digite o código do estudante ou '0' para sair: ")
        if entrada == "0":
            break
        codigo_estudante = int(entrada)
        
        # Verificar se o código do estudante já existe na lista
        if any(estudante['codigo'] == codigo_estudante for estudante in estudantes):
            print("Já existe um estudante com este código. Por favor, escolha outro código.")
            continue  # Retorna ao início do loop para permitir que o usuário insira um novo código
        
        nome = input("Informe o nome do estudante: ")
        
        while True:
            cpf = input("Digite o número do CPF ou 's' para sair: ")
            
            if cpf.lower() == 's':
                break  # Sai do loop interno se o usuário desejar sair
            elif len(cpf) != 11 or not cpf.isdigit():
                print("CPF inválido. O CPF deve ter exatamente onze dígitos e ser composto apenas por números inteiros.")
                continue  # Continua no loop interno para solicitar outro CPF
            elif any(estudante['cpf'] == cpf for estudante in estudantes):
                print("Já existe um estudante com este CPF. Por favor, insira outro CPF ou 's' para sair.")
                continue  # Continua no loop interno para solicitar outro CPF
            else:
                break  # Sai do loop interno se o CPF for válido e único
        
        if cpf.lower() == 's':
            break  # Sai do loop externo se o usuário desejar sair
        
        estudante = {"codigo": codigo_estudante, "nome": nome, "cpf": cpf}
        estudantes.append(estudante)
        print("Estudante adicionado com sucesso.")

# Função listar
def listar_estudantes():
    print("Listar Estudantes")
    if not estudantes:
        print("Não há estudantes cadastrados.")
    else:
        print("Lista de estudantes cadastrados:")
        for estudante in estudantes:
            print(f"Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}")

# Função excluir estudante
def excluir_estudante():
    codigo = int(input("Digite o código do estudante que deseja excluir: "))
    for estudante in estudantes:
        if estudante['codigo'] == codigo:
            estudantes.remove(estudante)
            print("Estudante excluído com sucesso.")
            return
    print("Estudante não encontrado.")

# Função editar estudante
def editar_estudante():
    codigo = int(input("Digite o código do estudante que deseja editar: "))
    for estudante in estudantes:
        if estudante['codigo'] == codigo:
            novo_nome = input("Informe o novo nome do estudante: ")
            novo_cpf = input("Digite o novo número do CPF: ")
            estudante['nome'] = novo_nome
            estudante['cpf'] = novo_cpf
            print("Estudante atualizado com sucesso.")
            return
    print("Estudante não encontrado.")

# Função atualizar          
def atualizar():
    print("Atualizar")
    print("Em desenvolvimento")

# Função excluir
def excluir():
    print("Excluir")
    print("Em desenvolvimento")

# Função voltar
def voltar():
    print("Voltando ao menu principal...")

# Função sair
def sair():
    print("Saindo do programa...")
    exit(0)

# Função escolher operação
def executar_operacao(operacao):
    operacoes = {
        1: incluir_estudantes,
        2: listar_estudantes,
        3: atualizar,
        4: excluir,
        9: voltar
    }
    if operacao in operacoes:
        operacoes[operacao]()
    elif operacao == 9:
        operacoes[9]()
    else:
        print("Opção inválida. Por favor, tente novamente.")

# Função exibição opções do menu de operações
def menu_operacoes():
    while True:
        print("\nEscolha a operação:")
        print("(1) Incluir Estudante")
        print("(2) Listar Estudantes")
        print("(3) Editar Estudante")
        print("(4) Excluir Estudante")
        print("(9) Voltar ao Menu Principal")
        escolha_operacao = int(input("Selecione a operação desejada: "))
        if escolha_operacao == 1:
            incluir_estudantes()
        elif escolha_operacao == 2:
            listar_estudantes()
        elif escolha_operacao == 3:
            editar_estudante()
        elif escolha_operacao == 4:
            excluir_estudante()
        elif escolha_operacao == 9:
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função exibição opções do menu principal 
def menu_principal():
    opcoesMenu = {
        1: "Estudantes",
        2: "Disciplinas",
        3: "Professores",
        4: "Turmas",
        5: "Matrículas",
        9: "Sair"
    }
    while True:
        print("\nMenu Principal:")
        for opcao, descricao in opcoesMenu.items():
            print(f"({opcao}) {descricao}")

        escolhaAluno = int(input("Informe a opção desejada: "))
        if escolhaAluno in opcoesMenu:
            if escolhaAluno == 9:
                sair()
            elif escolhaAluno == 1:
                menu_operacoes()
            elif escolhaAluno in [2, 3, 4, 5]:
                print("Funcionalidade em desenvolvimento")
            else:
                print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu_principal()
