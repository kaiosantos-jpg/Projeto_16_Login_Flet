# Initialize Reactive Jupyter | syncing, async | Stable code
import flet as ft
import csv
from login_utils import verificar_login, mostrar_tela_sucesso
def main(page: ft.Page):  ## FUNÇÃO QUE DEFINE COMO O NOSSO APP IRÁ SE COMPORTAR
    page.title = "Cadastro Login"  ## TÍTULO DO NOSSO APP
    page.theme_mode = "dark"  ## TEMA QUE ALTERA A COR DE FUNDO, TEXTOS E TÍTULOS
    page.vertical_alignment = "center"  ## CENTRALIZA OS COMPONENTES E TEXTOS
    page.horizontal_alignment = "center"  ## CENTRALIZA NA HORIZONTAL
    page.window.center()  ## COLOCA A TELA EM POSIÇÃO CENTRAL DO MONITOR
    page.window.width = 600  ## TAMANHO HORIZONTAL
    page.window.height = 800  ## TAMANHO VERTICAL

    def clique(e):  ## FUNÇÃO PARA AGIR DEPOIS DO CLIQUE EM CADASTRO!!
        valor_login = texto_login.value  ## PEGANDO VALOR DIGITADO EM VARIAVEIS
        valor_senha = texto_senha.value  ## PEGANDO VALOR DIGITADO EM VARIAVEIS

        with open("Relatorios/dados.csv", "a", newline="") as arquivo:  ## SALVANDO NO CSV
            escritor = csv.writer(arquivo)
            escritor.writerow([valor_login, valor_senha])

        page.open(ft.SnackBar(ft.Text(f"Conta cadastrada ! Bem Vindo(a) {valor_login}", color="white"), bgcolor="green", duration=1.7))
        ## AQUI IRA APARECER UMA MENSAGEM AO USUARIO INFORMANDO O CADASTRO E DANDO BOAS VINDAS
        page.update()
        
    def entrar(e):
        login = texto_login.value
        senha = texto_senha.value
        
        if verificar_login(login,senha):
            mostrar_tela_sucesso(page, login)
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text("Login ou senha incorretos!", color = "white"),
                bgcolor="red"
            )
            page.snack_bar.open = True
            page.update()
        

    titulo = ft.Text("Login", color="white", size=40)  ## TÍTULO DA PÁGINA
    texto_login = ft.TextField(  ## ENTRADA DE TEXTO(LOGIN)
                               focused_border_color="GREEN",
                               width=300,
                               autofocus=True)
    texto_senha = ft.TextField(label="senha",
                                focused_border_color="GREEN",
                                password=True,
                                can_reveal_password=True,
                               width=300,
                               )
    
    botao_cadastro = ft.ElevatedButton("Cadastro",
                                       on_click=clique,
                                       width=100,
                                       bgcolor="BLUE",
                                       color="white")
    botao_entrar = ft.ElevatedButton("Entrar",
                                     on_click=entrar,
                                    width=100,
                                    bgcolor="GREEN",
                                    color="white")
    page.add(titulo,texto_login,texto_senha, ## PAGE.ADD É RESPONSAVEL POR MOSTRAR NA TELA DO USUARIO OS ITENS
             ft.Row([botao_cadastro,botao_entrar],alignment="center")) ##FT.ROW É UMA CONFIGURAÇÃO APARTE(LINHA), ONDE USAMOS PARA COMPOR 1 OU MAIS
                               

ft.app(target=main) ##DEIXA O FLET EM LOOP, PARA QUE NÃO ABRA E FECHA
