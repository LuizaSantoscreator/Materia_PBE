#Criar a classe Produto com s atributos: nome e preço -> privado

class Produto:
    def __init__(self, nome, preco ):
        self.nome = nome
        self.__preco = preco

    def exibir_dados(self):
        print(f'{self.nome},{self.__preco}')

    def get_preco(self):
        return self.__preco
    def set_preco(self, valor):
        if valor < 0:
            raise ValueError('O saldo não pode sewr negativo')
        self.__preco = valor


class Carrinho:
    def __init__(self):
        self.atributo_itens = []

    def adicionar_item(self, item):
        self.atributo_itens.append(item)
        print(f'Item "{item.nome}" adicionado ao carrinho.')

    def remover_item(self, item):
        if item in self.atributo_itens:
            self.atributo_itens.remove(item)
            print(f'Item "{item.nome}" removido do carrinho.')


    def todal_itens(self):
        contador = 0
        for i in self.atributo_itens:
            contador += i.get_preco()
        print(contador)

    def exibir_produtos(self):
        print("Produtos no carrinho:")
        for item in self.atributo_itens:
            item.exibir_dados()

produto1 = Produto('Camiseta', 10)
produto2 = Produto('Boné', 20)
produto3 = Produto('Calça', 30)
produto4 = Produto('Tênis', 400)

produto1.exibir_dados()
produto1.set_preco(50)
print(f"Novo preço da {produto1.nome}: R$ {produto1.get_preco():.2f}")

carrinho = Carrinho()
carrinho.adicionar_item(produto1)
carrinho.adicionar_item(produto2)
carrinho.adicionar_item(produto3)
carrinho.adicionar_item(produto4)

print()
carrinho.exibir_produtos()
print()
carrinho.todal_itens()
#carrinho.remover_item(produto1)


