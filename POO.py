from typing import List

# 1. Classe ItemBiblioteca
class ItemBiblioteca:
    def __init__(self, titulo: str, ano_publicacao: int, disponivel: bool = True):
        if ano_publicacao <= 0:
            raise ValueError("Ano de publicação deve ser maior que 0.")
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    def emprestar(self):
        if not self.disponivel:
            raise Exception("Item já está emprestado.")
        self.disponivel = False

    def devolver(self):
        if self.disponivel:
            raise Exception("Item já está disponível.")
        self.disponivel = True

    def obter_info(self):
        return f"Título: {self.titulo}, Ano: {self.ano_publicacao}, Disponível: {'Sim' if self.disponivel else 'Não'}"


# 2. Classe ColecaoLivros
class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo: str, ano_publicacao: int):
        super().__init__(titulo, ano_publicacao)
        self.livros: List[ItemBiblioteca] = []

    def adicionar_livro(self, livro: ItemBiblioteca):
        self.livros.append(livro)

    def verificar_disponibilidade_colecao(self):
        return all(livro.disponivel for livro in self.livros)

    def obter_info(self):
        titulos = ', '.join([livro.titulo for livro in self.livros])
        return f"{super().obter_info()}, Coleção: [{titulos}]"


# 3. Classe Revista
class Revista(ItemBiblioteca):
    def __init__(self, titulo: str, ano_publicacao: int, edicao: int):
        super().__init__(titulo, ano_publicacao)
        if edicao <= 0:
            raise ValueError("Número da edição deve ser maior que 0.")
        self.edicao = edicao

    def atualizar_edicao(self, nova_edicao: int):
        if nova_edicao <= 0:
            raise ValueError("Nova edição deve ser maior que 0.")
        self.edicao = nova_edicao

    def restringir_emprestimo(self, dias_max: int):
        return dias_max <= 7 if self.ano_publicacao < 2000 else True

    def obter_info(self):
        return f"{super().obter_info()}, Edição: {self.edicao}"


# 4. Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, item: ItemBiblioteca):
        if item.titulo in self.itens:
            raise Exception("Item já existe na biblioteca.")
        self.itens[item.titulo] = item

    def remover_item(self, titulo: str):
        if titulo not in self.itens:
            raise Exception("Item não encontrado.")
        del self.itens[titulo]

    def listar_itens_disponiveis(self):
        return [titulo for titulo, item in self.itens.items() if item.disponivel]

    def contar_itens_emprestados(self):
        return sum(1 for item in self.itens.values() if not item.disponivel)


# 5. Classe RelatorioBiblioteca
class RelatorioBiblioteca:
    def __init__(self, biblioteca: Biblioteca):
        self.biblioteca = biblioteca

    def gerar_relatorio_completo(self):
        return "\n".join(item.obter_info() for item in self.biblioteca.itens.values())

    def gerar_relatorio_disponibilidade(self):
        disponiveis = self.biblioteca.listar_itens_disponiveis()
        return f"Itens disponíveis:\n{', '.join(disponiveis)}\nTotal: {len(disponiveis)}"

    def gerar_relatorio_emprestimos(self):
        total = len(self.biblioteca.itens)
        emprestados = self.biblioteca.contar_itens_emprestados()
        proporcao = emprestados / total if total > 0 else 0
        return f"Itens emprestados: {emprestados}\nProporção: {proporcao:.2%}"
