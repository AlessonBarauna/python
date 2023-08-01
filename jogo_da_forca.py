import tkinter as tk
import random

# Lista de palavras para o jogo
palavras = ['python', 'amor', 'Deus', 'felicidade', 'paixao', 'carater', 'Jesus', 'mente', 'futebol', 'homem', 'mulher', 'anjos', 'templo', 'igreja', 'paralelepipedo', 'bala','balão', 'baleia', 'banana', 'renovacao', 'ousadia', 'poder', 'espirito' 'programacao', 'forca', 'jogo', 'computador', 'desenvolvimento', 'beleza', 'bexiga', 'bico', 'bife', 'bigode', 'bobo', 'boca', 'boi', 'boia', 'bola', 'comida', 'comeia', 'interface', 'linguagem','algoritmo', 'dicionario', 'recursao', 'lista', 'modularizacao', 'condicional', 'estrutura', 'variavel', 'web', 'loop', 'classe', 'objeto', 'debug', 'string', 'arquivo', 'modulo', 'biblioteca']

class JogoForca:
    def __init__(self, master):
        self.master = master
        self.jogando = False
        self.palavra_secreta = ""
        self.letras_acertadas = []
        self.tentativas_restantes = 10
        self.letras_erradas = []
        self.palavra_chutada = False
        self.pontuacao = 0

        self.forca_label = tk.Label(master, text="", font=('Courier', 18))
        self.forca_label.pack()

        self.palavra_label = tk.Label(master, text="", font=('Arial', 18))
        self.palavra_label.pack()

        self.tentativas_label = tk.Label(master, text="", font=('Arial', 14))
        self.tentativas_label.pack()

        self.letras_erradas_label = tk.Label(master, text="", font=('Arial', 14))
        self.letras_erradas_label.pack()

        self.pontuacao_label = tk.Label(master, text="", font=('Arial', 14))
        self.pontuacao_label.pack()

        self.letra_entry = tk.Entry(master, font=('Arial', 16))
        self.letra_entry.pack()

        self.enviar_button = tk.Button(master, text="Enviar", font=('Arial', 16), command=self.enviar_letra)
        self.enviar_button.pack()

        self.chutar_button = tk.Button(master, text="Chutar Palavra", font=('Arial', 16), command=self.chutar_palavra, state=tk.DISABLED)
        self.chutar_button.pack()

        self.novo_jogo_button = tk.Button(master, text="Novo Jogo", font=('Arial', 16), state=tk.DISABLED, command=self.novo_jogo)
        self.novo_jogo_button.pack()

        self.novo_jogo()

    def escolher_palavra(self):
        # Escolhe aleatoriamente uma palavra da lista de palavras
        return random.choice(palavras)

    def gerar_palavra_chutada(self):
        # Escolhe uma palavra aleatória do tamanho da palavra secreta
        return random.choice(palavras)

    def mostrar_forca(self):
        # Desenha a forca com base nas tentativas restantes
        forca_imagens = [
            """
               _______
              |/      |
              |      (_)
              |      \|/
              |       |
              |      / \\
              |
             _|___
            """,
            """
               _______
              |/      |
              |      (_)
              |      \|/
              |       |
              |      /
              |
             _|___
            """,
            """
               _______
              |/      |
              |      (_)
              |      \|/
              |       |
              |
              |
             _|___
            """,
            """
               _______
              |/      |
              |      (_)
              |      \|
              |       |
              |
              |
             _|___
            """,
            """
               _______
              |/      |
              |      (_)
              |       |
              |       |
              |
              |
             _|___
            """,
            """
               _______
              |/      |
              |      (_)
              |
              |
              |
              |
             _|___
            """,
            """
               _______
              |/      |
              |
              |
              |
              |
              |
             _|___
            """,
            """
               _______
              |
              |
              |
              |
              |
              |
             _|___
            """,
        ]
        forca_atual = forca_imagens[7 - self.tentativas_restantes]
        self.forca_label.config(text=forca_atual)

    def atualizar_tela(self):
        self.palavra_label.config(text=" ".join(self.letras_acertadas))
        self.tentativas_label.config(text=f"Tentativas Restantes: {self.tentativas_restantes}")
        self.letras_erradas_label.config(text=f"Letras Erradas: {', '.join(self.letras_erradas)}")
        self.pontuacao_label.config(text=f"Pontuação: {self.pontuacao}")

    def verificar_letra(self, letra):
        if letra in self.palavra_secreta:
            for i in range(len(self.palavra_secreta)):
                if self.palavra_secreta[i] == letra:
                    self.letras_acertadas[i] = letra
                    self.pontuacao += 10
        else:
            self.letras_erradas.append(letra)
            self.tentativas_restantes -= 1
            self.pontuacao -= 2

    def enviar_letra(self):
        if not self.jogando:
            return

        letra = self.letra_entry.get().lower()
        self.letra_entry.delete(0, tk.END)

        if not self.palavra_chutada and self.palavra_secreta.count("_") <= len(self.palavra_secreta) // 2:
            self.chutar_button.config(state=tk.NORMAL)

        self.verificar_letra(letra)
        self.mostrar_forca()
        self.atualizar_tela()

        if "_" not in self.letras_acertadas:
            self.mostrar_mensagem("Parabéns! Você acertou a palavra!")
            self.palavra_chutada = True
            self.letras_acertadas = list(self.palavra_secreta)  # Completar a palavra acertada
            self.pontuacao += 100
            self.chutar_button.config(state=tk.DISABLED)
            self.novo_jogo_button.config(state=tk.NORMAL)
        elif self.tentativas_restantes == 0:
            self.mostrar_mensagem(f"Você perdeu! A palavra secreta era: {self.palavra_secreta}")
            self.palavra_chutada = True
            self.chutar_button.config(state=tk.NORMAL)
            self.novo_jogo_button.config(state=tk.NORMAL)

    def chutar_palavra(self):
        if not self.palavra_chutada:
            popup = tk.Toplevel()
            popup.title("Chute a Palavra")
            popup.geometry("300x150")
            tk.Label(popup, text="Chute a palavra:", font=('Arial', 16)).pack()
            chute_entry = tk.Entry(popup, font=('Arial', 16))
            chute_entry.pack()
            tk.Button(popup, text="Enviar", font=('Arial', 14), command=lambda: self.verificar_chute(chute_entry.get().lower(), popup)).pack()

    def verificar_chute(self, chute, popup):
        popup.destroy()
        if chute == self.palavra_secreta:
            self.mostrar_mensagem(f"Parabéns! Você acertou a palavra! A palavra secreta era: {self.palavra_secreta}")
            self.pontuacao += 100
            self.palavra_chutada = True
            self.letras_acertadas = list(self.palavra_secreta)  # Completar a palavra acertada
            self.chutar_button.config(state=tk.DISABLED)
            self.novo_jogo_button.config(state=tk.NORMAL)
        else:
            self.mostrar_mensagem(f"Chute errado! Continue tentando!")

    def novo_jogo(self):
        self.palavra_secreta = self.escolher_palavra()
        self.letras_acertadas = ['_' for _ in self.palavra_secreta]
        self.tentativas_restantes = 10
        self.letras_erradas = []
        self.palavra_chutada = False
        self.pontuacao = 0
        self.jogando = True

        self.mostrar_forca()
        self.atualizar_tela()

        self.novo_jogo_button.config(state=tk.DISABLED)
        self.chutar_button.config(state=tk.DISABLED)

    def mostrar_mensagem(self, mensagem):
        popup = tk.Toplevel()
        popup.title("Resultado")
        popup.geometry("300x100")
        tk.Label(popup, text=mensagem, font=('Arial', 16)).pack()
        tk.Button(popup, text="Fechar", command=popup.destroy, font=('Arial', 14)).pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Jogo da Forca")
    jogo_forca = JogoForca(root)
    root.mainloop()
