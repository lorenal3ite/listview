import flet as ft
from flet import AppBar, ElevatedButton, Text, View, colors
from flet.core.colors import Colors
from flet.core.textfield import TextField




def main(page: ft.Page):
    # Configuração da pagina
    page.title = "Exemplos de rota"
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
                    AppBar(title=Text("Inicio"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
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
                        Text(value=f'Bem vindo(a) {input_nome.value}')
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
    input_nome = ft.TextField(label="Nome", hint_text="Digite seu Nome")

ft.app(main)