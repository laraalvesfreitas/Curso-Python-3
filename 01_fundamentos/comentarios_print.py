"""
COMENTÁRIOS E PRINT - ÍNDICE
1. DocString
2. Comentários (# e posicionamento)
3. print() com sep e end
4. Quebra de linha (\r\n e \n)


DOCSTRING

É usado para escrever textos
que ocupam várias linhas.

Usar para escrever suas notas.
"""

# Permite escrever um comentário

print(123)  # Comentário na frente

# Comentário abaixo
print(456)


# ==================================================
# PRINT COM SEP E END
# ==================================================

"""
sep → define o separador entre os valores impressos.
end → define o que é impresso ao final (padrão: '\n').
"""

print(12, 34, 1011, sep='', end='#')

print(56, 78, sep='-', end='\n')


# ==================================================
# QUEBRA DE LINHA
# ==================================================

"""
\r\n -> CRLF (usado no Windows)
\n   -> LF   (usado no Linux/macOS)
"""