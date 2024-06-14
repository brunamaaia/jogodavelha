def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
      print((" | ").join(linha))
      print("-" * 9)

def vitoria(tabuleiro, jogador):
    for i in range(3):
      if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
        return True
      if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def jogo_da_velha(tabuleiro):
    jogador = ["X", "O"]
    atual = 0

    while True:
        mostrar_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador[atual]}, linhas: 1, 2, 3 | "))
        coluna = int(input(f"Jogador {jogador[atual]}, colunas: 1, 2, 3 | "))

        if tabuleiro[linha - 1][coluna - 1] == " ":
            tabuleiro[linha - 1][coluna - 1] = jogador[atual]
            if vitoria(tabuleiro, jogador[atual]):
                mostrar_tabuleiro(tabuleiro)
                print(f"O jogador {jogador[atual]} venceu!")
                break
            elif all(tabuleiro[i][j] != " " for i in range(3) for j in range(3)):
                mostrar_tabuleiro(tabuleiro)
                print("Deu empate!")
                break
            atual = (atual + 1) % 2
        else:
            print("Esse local já está ocupado. Tente novamente!")


tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
jogo_da_velha(tabuleiro)