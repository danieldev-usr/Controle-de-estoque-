# Controle de Estoque 

## Descrição

Este é um sistema simples de controle de estoque, desenvolvido em Python, que permite gerenciar produtos em um arquivo CSV. O sistema oferece funcionalidades como adicionar, remover, atualizar e exibir produtos no estoque, com a possibilidade de salvar as alterações no arquivo CSV.

## Funcionalidades

- **Carregar Estoque:** Ao iniciar o programa, ele tenta carregar o estoque a partir de um arquivo CSV. Se o arquivo não existir, um estoque vazio será criado.
- **Salvar Estoque:** As alterações feitas no estoque (adição, remoção, atualização de produtos) podem ser salvas no arquivo CSV.
- **Adicionar Produto:** Permite adicionar um novo produto ao estoque com código, nome, preço e quantidade.
- **Remover Produto:** Remove um produto do estoque com base no código.
- **Atualizar Produto:** Atualiza as informações de um produto já existente (nome, preço e quantidade).
- **Exibir Estoque:** Mostra todos os produtos atualmente no estoque, com seus respectivos códigos, nomes, preços e quantidades.
- **Menu de Navegação:** Um menu interativo em linha de comando para facilitar a interação com o programa.
- **Cores:** O programa utiliza diferentes cores para destacar opções e textos no terminal, criando uma experiência mais amigável.

## Requisitos

- Python 3.x
- Biblioteca CSV (nativa do Python)

## Como Usar

1. **Executar o Programa:**
   Execute o arquivo Python diretamente no terminal ou ambiente de execução compatível.
   Exemplo: `python nome_do_arquivo.py`

2. **Interação com o Menu:**
   Após iniciar o programa, um menu será exibido com as seguintes opções:
   - [1] Adicionar Produto
   - [2] Remover Produto
   - [3] Atualizar Produto
   - [4] Exibir Estoque
   - [5] Sair e Salvar
   - [6] Sobre

   Insira o número da opção desejada para realizar uma ação.

3. **Exemplo de Funcionamento:**
   Para adicionar um novo produto, selecione a opção 1 e insira os dados solicitados. Para remover, basta informar o código do produto correspondente. Ao finalizar o uso, escolha a opção 5 para salvar as alterações e sair do programa.

## Formato do Arquivo CSV

O arquivo de estoque é salvo no formato CSV, com os seguintes campos:

- **codigo:** Código identificador do produto.
- **nome:** Nome do produto.
- **preco:** Preço do produto.
- **quantidade:** Quantidade disponível no estoque.

### Exemplo de CSV:

```csv
codigo,nome,preco,quantidade
001,Produto A,10.50,100
002,Produto B,5.99,50
003,Produto C,20.00,200
