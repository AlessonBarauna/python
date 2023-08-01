import string
import nltk
from nltk.corpus import stopwords
from nltk.util import ngrams
from collections import Counter
import tkinter as tk
from tkinter import scrolledtext, messagebox

nltk.download("punkt")
nltk.download("stopwords")

def analyze_text(text):
    # Remoção de pontuação e conversão para minúsculas
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator).lower()

    # Tokenização em palavras
    words = nltk.word_tokenize(text)

    # Remoção de stopwords
    stop_words = set(stopwords.words("portuguese"))
    words = [word for word in words if word not in stop_words]

    # Número de palavras, frases e parágrafos
    num_words = len(words)
    num_sentences = len(nltk.sent_tokenize(text))
    num_paragraphs = len(text.split("\n\n"))

    # Frequência de cada palavra
    word_frequency = Counter(words)

    # Frequência de cada letra
    letter_frequency = Counter(text)

    # Comprimento médio das palavras e frases
    average_word_length = sum(len(word) for word in words) / num_words
    average_sentence_length = num_words / num_sentences

    # Palavras mais frequentes
    most_common_words = word_frequency.most_common(5)

    # Frequência de bigramas e trigramas
    bigrams = list(ngrams(words, 2))
    trigrams = list(ngrams(words, 3))
    bigram_frequency = Counter(bigrams)
    trigram_frequency = Counter(trigrams)

    return (
        num_words,
        num_sentences,
        num_paragraphs,
        word_frequency,
        letter_frequency,
        average_word_length,
        average_sentence_length,
        most_common_words,
        bigram_frequency,
        trigram_frequency,
    )


def analyze_button_click():
    user_text = input_text.get("1.0", tk.END).strip()
    if user_text:
        try:
            (
                num_words,
                num_sentences,
                num_paragraphs,
                word_frequency,
                letter_frequency,
                average_word_length,
                average_sentence_length,
                most_common_words,
                bigram_frequency,
                trigram_frequency,
            ) = analyze_text(user_text)

            # Limpa a saída anterior
            output_text.delete("1.0", tk.END)

            # Formata a saída e exibe na interface
            output_text.insert(
                tk.END,
                f"Número de palavras: {num_words}\n"
                f"Número de frases: {num_sentences}\n"
                f"Número de parágrafos: {num_paragraphs}\n"
                f"Comprimento médio das palavras: {average_word_length:.2f} caracteres\n"
                f"Comprimento médio das frases: {average_sentence_length:.2f} palavras\n\n"
                "Frequência de cada palavra:\n"
            )
            for word, frequency in word_frequency.items():
                output_text.insert(tk.END, f"{word}: {frequency}\n")

            output_text.insert(tk.END, "\nFrequência de cada letra:\n")
            for letter, frequency in letter_frequency.items():
                output_text.insert(tk.END, f"{letter}: {frequency}\n")

            output_text.insert(tk.END, "\nPalavras mais frequentes:\n")
            for word, frequency in most_common_words:
                output_text.insert(tk.END, f"{word}: {frequency}\n")

            output_text.insert(tk.END, "\nFrequência de bigramas:\n")
            for bigram, frequency in bigram_frequency.items():
                output_text.insert(tk.END, f"{bigram}: {frequency}\n")

            output_text.insert(tk.END, "\nFrequência de trigramas:\n")
            for trigram, frequency in trigram_frequency.items():
                output_text.insert(tk.END, f"{trigram}: {frequency}\n")

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    else:
        messagebox.showwarning("Aviso", "Digite um texto para análise.")

# Criando a janela principal
root = tk.Tk()
root.title("Analisador de Texto")

# Criando a caixa de entrada de texto
input_text = scrolledtext.ScrolledText(root, width=60, height=10, wrap=tk.WORD)
input_text.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Criando o botão para análise
analyze_button = tk.Button(root, text="Analisar Texto", command=analyze_button_click)
analyze_button.grid(row=1, column=0, padx=10, pady=5)

# Criando a caixa de saída de texto
output_text = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD)
output_text.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

root.mainloop()
