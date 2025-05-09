import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors

class User():
    def __init__(self, nome, profissao, salario):
        self.nome = nome
        self.profissao = profissao
        self.salario = salario

def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []

    def salvar_nome(e):
        if input_nome.value == "":
            page.overlay.append(msg_erro)
            msg_erro.open = True
            page.update()
        else:
            obj_user = User(
                nome=input_nome.value,
                profissao=input_profissao.value,
                salario=input_salario.value,
            )
            lista.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON_2_OUTLINED),
                    title=nome,
                    subtitle=input_profissao.value,
                    trailing=input_salario.value,
                )
            )
            input_nome.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()



    def exibir_lista(e):
        lv_nome.controls.clear()
        for user in lista:
            lv_nome.controls.append(
                ft.Text(value=f"{user.nome}, {user.profissao}, {user.salario}"),
            )
            page.update()

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PINK),
                    input_nome,
                    input_profissao,
                    input_salario,
                    ft.Button(text="Salvar",
                              on_click=lambda _: salvar_nome(e)
                              ),
                    ft.Button(text="Exibir",
                              on_click=lambda _: page.go("/exibir"))
                ],
            )
        )

        if page.route == "/exibir":
            exibir_lista(e)
            page.views.append(
                View(
                    "/exibir",
                    [
                        AppBar(title=Text("Exibir listas"), bgcolor=Colors.PINK),
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
    input_nome = ft.TextField(label="Nome")
    input_profissao = ft.TextField(label="Profissão")
    input_salario = ft.TextField(label="Salário")

    msg_sucesso = ft.SnackBar(
        content=ft.Text("Salvo com sucesso"),
        bgcolor=Colors.GREEN
    )

    msg_erro = ft.SnackBar(
        content=ft.Text("Preencha todos os campos"),
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