# Nesse desafio você verificará dentro de uma lista se o item estar contido nela,
# caso verdadeiro deverá imprimir na tela essa informação,
# além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

cursos = ['SQL intro', 'Python básico', 'Programação em R', 'Algorítimos']
curso_git = 'Git básico'
curso_python = 'Python básico'
curso_r = 'Programação em R'

avaliacoes = {}

if curso_python in cursos:
  print(f'O curso {curso_python} esta no catálogo, por favor avalie o curso.')
  avaliacoes[curso_python] = int(input('Qual a nota que você da para o curso (0 a 5)? '))
if curso_git in cursos:
  print(f'O curso {curso_git} esta no catálogo, por favor avalie o curso.')
  avaliacoes[curso_git] = int(input('Qual a nota que você da para o curso (0 a 5)? '))
if curso_r in cursos:
  print(f'O curso {curso_r} esta no catálogo, por favor avalie o curso.')
  avaliacoes[curso_r] = int(input('Qual a nota que você da para o curso(0 a 5)? '))
else:
  print(f'Infelizmente o curso não compõe o nosso catálogo.')

print(f'As notas dos cursos são: {avaliacoes}')