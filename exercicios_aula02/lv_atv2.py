import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors

class User():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []

    def salvar_nome(e):
        if titulo_livro.value == "":
            page.overlay.append(msg_erro)
            msg_erro.open = True
            page.update()
        else:
            obj_user = User(
                titulo=titulo_livro.value,
                autor=autor_livro.value,
            )
            lista.append(obj_user)
            titulo_livro.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()



    def exibir_lista(e):
        lv_nome.controls.clear()
        for user in lista:
            lv_nome.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            Text(f"Título: {user.titulo}"),
                            Text(f"Autor: {user.autor}"),
                        ]
                        )
                    )
                )
            )
            page.update()

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    titulo_livro,
                    autor_livro,
                    ft.Button(text="Salvar",
                              on_click=lambda _: salvar_nome(e)
                              ),
                    ft.Button(text="Exibir",
                              on_click=lambda _: page.go("/segunda"))
                ],
            )
        )

        if page.route == "/segunda":
            exibir_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Exibir lista"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_nome,

                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Componentes
    titulo_livro = ft.TextField(label="Título", hint_text="Digite o titulo do livro")
    autor_livro = ft.TextField(label="Autor", hint_text="Digite a autor do livro")

    msg_sucesso = ft.SnackBar(
        content=ft.Text("Salvo com sucesso"),
        bgcolor=Colors.GREEN
    )

    msg_erro = ft.SnackBar(
        content=ft.Text("Erro, está vazio"),
        bgcolor=Colors.RED
    )

    lv_nome = ft.ListView(
        height=500
    )

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)


# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)

#lorenaleite é demais