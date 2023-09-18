class Publicacao:
    def __init__(self, titulo, ano_publicacao):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
    
    def descricao(self):
        return f"Título: {self.titulo}, Ano de Publicação: {self.ano_publicacao}"

class Livro(Publicacao):
    def __init__(self, titulo, ano_publicacao, autor, numero_paginas):
        super().__init__(titulo, ano_publicacao)
        self.autor = autor
        self.numero_paginas = numero_paginas
    
    def descricao(self):
        base_descricao = super().descricao()
        return f"{base_descricao}, Autor: {self.autor}, Número de Páginas: {self.numero_paginas}"

class Revista(Publicacao):
    def __init__(self, titulo, ano_publicacao, editora, edicao):
        super().__init__(titulo, ano_publicacao)
        self.editora = editora
        self.edicao = edicao
    
    def descricao(self):
        base_descricao = super().descricao()
        return f"{base_descricao}, Editora: {self.editora}, Edição: {self.edicao}"


livro = Livro("Dom Quixote", 1605, "Miguel de Cervantes", 800)
print(livro.descricao())

revista = Revista("National Geographic", 2022, "National Geographic Society", "Agosto")
print(revista.descricao())