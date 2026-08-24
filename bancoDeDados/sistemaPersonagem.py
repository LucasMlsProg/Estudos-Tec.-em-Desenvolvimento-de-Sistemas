from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["herois_DB"]
colecao = db["colecaoHerois"]

def listarHerois():
    print(" --------------------------------------------------")
    for heroi in colecao.find():
        print(f" Nome: {heroi['nome']}\n Poder: {heroi['poder']}\n Raca: {heroi['raca']}\n -----------------------------------------")

def adicionarHeroi():
    adicionar_nome_heroi = input("Digite o nome do novo heroi a ser adicionado:")
    novo_heroi = {
        'nome': adicionar_nome_heroi,
    }
    while True:
        op_novo_heroi= int(input("Deseja adicionar mais uma caracteristica? (1 - Sim) (0 - Não)"))
        if op_novo_heroi == 1:
            novo_campo = input("Qual característica você deseja adicionar?")
            chave = novo_campo
            novo_campo = input("Qual valor dessa característica você deseja adicionar?")
            valor = novo_campo
            novo_heroi[chave] = valor
        else:
            break
    colecao.insert_one(novo_heroi)
    print(novo_heroi ,"Heroi Adicionado.")
    
def deletarHeroi():
    heroi_removido = input("Digite o nome do heroi que será removido")
    db.colecao.deleteOne({"nome" : heroi_removido})
    print("Heroi removido!")

while True:
    print("0 - Sair.")
    print("1 - Adicione um heroi.")
    print("2 - Listar herois.")
    print("3 - Deletar um heroi.")
    print("4 - Atualizar um heroi.")

    op = int(input("Digite a opção desejada:"))

    match op:
        case 0:
            break
        case 1:
            adicionarHeroi()
        case 2:
            listarHerois()
        case 3:
            deletarHeroi()
        case 4: 
            print()