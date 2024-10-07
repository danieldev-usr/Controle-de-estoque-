import csv

vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
branco = '\033[37m'
reset = "033[0m"
reverso = '\033[2m'

class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Estoque:
    def __init__(self, arquivo_csv="estoque.csv"):
        self.produtos = {}
        self.arquivo_csv = arquivo_csv
        self.carregar_estoque()

    def carregar_estoque(self):
        try:
            with open(self.arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for linha in reader:
                    codigo = linha["codigo"]
                    nome = linha["nome"]
                    preco = float(linha["preco"])
                    quantidade = int(linha["quantidade"])
                    self.produtos[codigo] = Produto(codigo, nome, preco, quantidade)
            print("Estoque carregado com sucesso!")
        except FileNotFoundError:
            print("Arquivo de estoque não encontrado. Iniciando estoque vazio.")
        except Exception as e:
            print(f"Erro ao carregar estoque: {e}")

    def salvar_estoque(self):
        try:
            with open(self.arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ["codigo", "nome", "preco", "quantidade"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for produto in self.produtos.values():
                    writer.writerow({
                        "codigo": produto.codigo,
                        "nome": produto.nome,
                        "preco": produto.preco,
                        "quantidade": produto.quantidade
                    })
            print("Estoque salvo com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar estoque: {e}")

    def adicionar_produto(self, codigo, nome, preco, quantidade):
        if codigo in self.produtos:
            print(f"Produto com código {codigo} já existe!")
        else:
            novo_produto = Produto(codigo, nome, preco, quantidade)
            self.produtos[codigo] = novo_produto
            print(f"Produto {nome} adicionado com sucesso!")

    def remover_produto(self, codigo):
        if codigo in self.produtos:
            removido = self.produtos.pop(codigo)
            print(f"Produto {removido.nome} removido com sucesso!")
        else:
            print(f"Produto com código {codigo} não encontrado!")

    def atualizar_produto(self, codigo, nome=None, preco=None, quantidade=None):
        if codigo in self.produtos:
            produto = self.produtos[codigo]
            if nome:
                produto.nome = nome
            if preco:
                produto.preco = preco
            if quantidade is not None:
                produto.quantidade = quantidade
            print(f"Produto {codigo} atualizado com sucesso!")
        else:
            print(f"Produto com código {codigo} não encontrado!")

    def exibir_estoque(self):
        if not self.produtos:
            print("Estoque vazio.")
        else:
            for produto in self.produtos.values():
                print(f"Código: {produto.codigo} | Nome: {produto.nome} | Preço: R${produto.preco:.2f} | Quantidade: {produto.quantidade}")

def menu():
    print(f"\n {verde} -----Menu de Controle de Estoque-----")
    print("[1] Adicionar Produto")
    print("[2] Remover Produto")
    print("[3] Atualizar Produto")
    print("[4] Exibir Estoque")
    print("[5] Sair e Salvar")
    print("[6] SOBRE")
    print("  ")

def main():
    estoque = Estoque()
    
    while True:
        menu()
        opcao = input(f"{vermelho}SELECT>> \033[2m ")
        print(f" {branco} ")
        
        if opcao == '1':
            codigo = input("Informe o código do produto: ")
            nome = input("Informe o nome do produto: ")
            preco = float(input("Informe o preço do produto: "))
            quantidade = int(input("Informe a quantidade do produto: "))
            estoque.adicionar_produto(codigo, nome, preco, quantidade)

        elif opcao == '2':
            codigo = input("Informe o código do produto a ser removido: ")
            estoque.remover_produto(codigo)

        elif opcao == '3':
            codigo = input("Informe o código do produto a ser atualizado: ")
            nome = input("Novo nome (pressione Enter para manter o atual): ")
            preco = input("Novo preço (pressione Enter para manter o atual): ")
            quantidade = input("Nova quantidade (pressione Enter para manter a atual): ")
            
            nome = nome if nome else None
            preco = float(preco) if preco else None
            quantidade = int(quantidade) if quantidade else None
            
            estoque.atualizar_produto(codigo, nome, preco, quantidade)

        elif opcao == '4':
            estoque.exibir_estoque()

        elif opcao == '5':
            estoque.salvar_estoque()
            print("Saindo e salvando estoque...")
            break
            
        elif opcao =="6":
        	print("""
        	--- Codado por wan ---
        	--- Python 3           ---
        	--- Pydroid        ---
        	
        	
        	""")

        else:
            print("Opção inválida, tente novamente!")

if __name__ == "__main__":
    main()