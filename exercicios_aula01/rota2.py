import flet as ft
from flet import AppBar, ElevatedButton, Text, View, colors
from flet.core.colors import Colors
from flet.core.textfield import TextField


def main(page: ft.Page):
    # Configuração da pagina
    page.title = "Cadastrar Livro"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Definição de funções

    def gerar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Início"), bgcolor=Colors.PRIMARY_CONTAINER),
                    titulo,
                    descricao,
                    categoria,
                    autor,
                    ElevatedButton(text="navegar", on_click=lambda _: page.go("/segunda")),
                ],
            )
        )

        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Inicio"), bgcolor=Colors.SECONDARY_CONTAINER),
                        Text(value=f'Titulo: {titulo.value}'),
                        Text(value=f'Descrição: {descricao.value}'),
                        Text(value=f'Categoria: {categoria.value}'),
                        Text(value=f'Autor: {autor.value}'),
                    ],
                )
            )
        page.update()


    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerar_rotas
    page.on_view_pop = voltar
    page.go(page.route)
    titulo = ft.TextField(label="Título", hint_text="Digite o titulo do livro")
    descricao = ft.TextField(label="Descrição", hint_text="Digite a descrição do livro")
    categoria = ft.TextField(label="Categoria", hint_text="Digite a categoria do livro")
    autor = ft.TextField(label="Autor", hint_text="Digite a autor do livro")

ft.app(main)