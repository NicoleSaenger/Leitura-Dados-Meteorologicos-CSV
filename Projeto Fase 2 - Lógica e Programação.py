#Entrada de dados para a etapa A
print('ITEM A)')
print('Informe o mês e o ano inicial do período no formato MM/AAAA -> ')

mesInicio = int(input('Informe o mês inicial de 1 a 12: '))
while mesInicio<1 or mesInicio>12:
  print('Mês inválido!')
  mesInicio = int(input('-> Informe novamente o mês inicial: '))

anoInicio = int(input('Informe o ano inicial de 1961 a 2016: '))
while anoInicio<1961 or anoInicio>2016:
  print('Ano inválido!')
  anoInicio = int(input('-> Informe novamente o ano inicial: '))

print('Agora informe o mês e o ano final do período ->')
mesFinal = int(input('Informe o mês final: '))
while mesFinal<1 or mesFinal>12:
  print('Mês inválido!')
  mesFinal = int(input('-> Informe novamente o mês final: '))

anoFinal = int(input('Informe o ano final: '))
while anoFinal<1961 or anoFinal>2016:
  print('Ano inválido!')
  anoFinal = int(input('-> Informe novamente o ano final: '))

#Validação ordem meses informados pelo usuário
aux = 0

if mesInicio>mesFinal:
  mesInico = aux
  mesInicio = mesFinal
  mesFinal = aux

if anoInicio>anoFinal:
  anoInicio = aux
  anoInicio = anoFinal
  anoFinal = aux


#-------------------------------------------------------------------------------


#Visualização do índice com as opções de leitura de dados
print()
print('Sobre o período informado, indique quais dados você deseja visualizar informando um número de 1 a 4 ->')
print('1 - Todos os Dados')
print('2 - Apenas Dados de Precipitação')
print('3 - Apenas Dados de Temperatura')
print('4 - Apenas Dados de Umidade e Vento')

indice = int(input('Informe aqui o índice desejado: '))

#Validando entrada do índice
while indice<1 or indice>4:
  print('Valor informado inválido!')
  indice = int(input('-> Por favor, redigite um valor entre 1 e 4 correspondente aos índices acima: '))
print()
print(100*'=')


#-------------------------------------------------------------------------------


#Todas as funções utilizadas no código

#Função para carregar os dados
def cargaDados(nome):
  arquivo = open(nome,"r")
  dados = []
  for linha in arquivo:
    linha1 = linha[:-1]  #retira \n
    dados.append(linha1)
  arquivo.close()
  return dados



#Função para escrever lista
def escreveLista(lista):
  for item in lista:
    print(item)



#Função para transformar os dados da linha em item de lista
def transformaDados(linha):
    itens = linha.split(',')
    data = itens[0].split('/')  #Separar a data em dia, mês e ano
    data = [int(valor) for valor in data]   #Converter a data para inteiros
    itensTransformados = [data]  #Adicionar a data separada como o primeiro item
    cont = 1  #Começar a partir do segundo item após a data
    while cont < len(itens):
        itensTransformados.append(float(itens[cont]))  # Converte para float demais itens
        cont += 1
    return itensTransformados



#Transformando as linhas em item de lista
def transformaLista(lista):
  listaDeItens = []
  cont = 1     #pula o cabecalho
  while cont< len(lista):
    listaDeItens.append(transformaDados(lista[cont]))
    cont = cont + 1
  return listaDeItens



#Índice 1 para visualizar todos os dados
def visuTodosDados(lista, mesIn, anoIn, mesFim, anoFim):
    print(cabecalho)
    for item in lista:
        data = item[0]
        dia, mes, ano = data  
        if anoIn <= ano <= anoFim:
          if anoIn == anoFim:  #Verifica se estamos no mesmo ano
            if mesIn <= mes <= mesFim:  #Verifica se o mês está dentro do intervalo
              print(item)
          elif ano == anoIn:  #Verifica se estamos no ano inicial
            if mes >= mesIn:  #Verifica se o mês é maior ou igual ao mês inicial
              print(item)
          elif ano == anoFim:  #Verifica se estamos no ano final
            if mes <= mesFim:  #Verifica se o mês é menor ou igual ao mês final
              print(item)



#Índice 2 para visualizar somente dados sobre precipitação
def visuPrecipitacao(lista, mesIn, anoIn, mesFim, anoFim):
  print(cabecalho[0], '\t', '\t', cabecalho[1])
  for item in lista:
    data = item[0] 
    dia, mes, ano = data  
    precipitacao = item[1]  
    if anoIn <= ano <= anoFim:
        if anoIn == anoFim:  
            if mesIn <= mes <= mesFim:  
              print(data, '\t', precipitacao)
        elif ano == anoIn: 
            if mes >= mesIn:  
              print(data, '\t', precipitacao)
        elif ano == anoFim:  
            if mes <= mesFim:  
              print(data, '\t', precipitacao)



#Índice 3 para visualizar somente dados sobre temperatura
def visuTemperatura(lista, mesIn, anoIn, mesFim, anoFim):
  print(cabecalho[0], '\t', '\t', cabecalho[2]+ '\t' + cabecalho[3] + '\t' + cabecalho[5])
  for item in lista:
    data = item[0]
    dia, mes, ano = data
    tempMax = item[2]
    tempMin = item[3]
    tempMedia = item[5]
    if anoIn <= ano <= anoFim:
        if anoIn == anoFim:  
            if mesIn <= mes <= mesFim:  
              print(data, '\t', tempMax, '\t', tempMin, '\t', tempMedia)
        elif ano == anoIn: 
            if mes >= mesIn:  
              print(data, '\t', tempMax, '\t', tempMin, '\t', tempMedia)
        elif ano == anoFim:  
            if mes <= mesFim:  
              print(data, '\t', tempMax, '\t', tempMin, '\t', tempMedia)



#Índice 4 para visualizar somente dados sobre ummidade e vento
def visuUmidadeVento(lista, mesIn, anoIn, mesFim, anoFim):
  print(cabecalho[0], (2*'\t'), cabecalho[6], '\t', cabecalho[7])
  for item in lista:
    data = item[0]
    dia, mes, ano = data
    umidade = item[6]
    vento = item[7]
    if anoIn <= ano <= anoFim:
        if anoIn == anoFim:  
            if mesIn <= mes <= mesFim:  
              print(data, '\t', umidade, (2*'\t'), vento)
        elif ano == anoIn:  
            if mes >= mesIn:  
              print(data, '\t', umidade, (2*'\t'), vento)
        elif ano == anoFim:  
            if mes <= mesFim:  
               print(data, '\t', umidade, (2*'\t'), vento)



#Função para criar o dicionário para verificar o mês mais chuvoso
def criaDicionarioPrecipitacao(lista):
    dicionario_precipitacao = {}
    for item in lista:
        data = tuple(item[0])  #Convertendo a lista de data em uma tupla
        precipitacao = item[1]  #Obtém os dados de precipitação da lista
        dicionario_precipitacao[data] = precipitacao  #Adiciona a data e precipitação ao dicionário
    return dicionario_precipitacao



#Função para calcular a precipitação máxima
def maximaPrecipitacao(dicionario):
    maior_precipitacao = max(dicionario.values())   #Pegando o maior valor do dicionário
    for data, precipitacao in dicionario.items():
        if precipitacao == maior_precipitacao:
            return data, precipitacao



#Função para calcular a média de temperatura mínima de um determinado mês
#OBS: últimos 11 anos (2006 - 2016)
def calcular_temperatura_min_media(lista, mesUsuario):
  #Dicionário para armazenar as temperaturas mínimas médias para cada ano
  temperatura_min_media_por_ano = {}

  #Filtrar os dados para os últimos 11 anos (de 2006 a 2016)
  lista_ultimos_11_anos = [item for item in lista if item[0][2] >= 2006 and item[0][2] <= 2016]

  #Repetição para percorrer os dados filtrados
  for item in lista_ultimos_11_anos:
    data = item[0]
    ano = data[2]
    mes_item = data[1]
    temperatura_min = item[3]

  #Verifica se o mês do item corresponde ao mês informado pelo usuário
    if mes_item == mesUsuario:
      #Se o ano já estiver no dicionário, adiciona a temperatura mínima à lista correspondente
      if ano in temperatura_min_media_por_ano:
        temperatura_min_media_por_ano[ano].append(temperatura_min)
      #Se o ano não estiver no dicionário, cria uma nova entrada com uma lista contendo a temperatura mínima
      else:
        temperatura_min_media_por_ano[ano] = [temperatura_min]

  #Cria dicionário para armazenar a temperatura mínima média de cada ano
  temperatura_min_media_por_mes = {}

  #Calcula a média das temperaturas mínimas para cada ano
  for ano, temperaturas in temperatura_min_media_por_ano.items():
    temperatura_min_media_por_mes[f"{mesUsuario}/{ano}"] = sum(temperaturas) / len(temperaturas)

  return temperatura_min_media_por_mes


#-------------------------------------------------------------------------------

#Função para gerar o gráfico

#Importa a  biblioteca do matplotlib
import matplotlib.pyplot as plt


#Cria a função para gerar o gráfico
def gerar_grafico(media_temperaturas):
  #Extrair os anos e as médias de temperatura do dicionário
  anos = [int(chave.split('/')[1]) for chave in media_temperaturas.keys()]
  medias = list(media_temperaturas.values())

  #Cria o gráfico de barras
  plt.figure(figsize=(10, 6))
  plt.bar(anos, medias, color='skyblue') #Esecifica a cor

  #Adicionr título e rótulos dos eixos
  plt.title('Média de Temperatura Mínima em Agosto (2006-2016)')
  plt.xlabel('Ano')
  plt.ylabel('Temperatura Mínima Média (°C)')

  #Adicionar grade ao gráfico
  plt.grid(True, linestyle='--', alpha=0.7)

  #Mostrar o gráfico
  plt.show()


#-------------------------------------------------------------------------------


#Carregando dados do arquivo e utilizando funções para manipulá-lo
dadosBrutos = cargaDados('Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv')

cabecalho = dadosBrutos[0].split(',')

dados = transformaLista(dadosBrutos)


#------------------------------------------------------------------------------

#Verificando escolha de índice do usuário


if indice == 1:
  visuTodosDados(dados, mesInicio, anoInicio, mesFinal, anoFinal)

if indice == 2:
  visuPrecipitacao(dados, mesInicio, anoInicio, mesFinal, anoFinal)

if indice == 3:
  visuTemperatura(dados, mesInicio, anoInicio, mesFinal, anoFinal)

if indice == 4:
  visuUmidadeVento(dados, mesInicio, anoInicio, mesFinal, anoFinal)



#-------------------------------------------------------------------------------

#Item B

print()
print(100*'=')
print()
print('ITEM B')

#Cria o dicionário para verificar o mês mais chuvoso
dicionario_precipitacao = criaDicionarioPrecipitacao(dados)
data_max_precipitacao, max_precipitacao = maximaPrecipitacao(dicionario_precipitacao)
print("Data do mês mais chuvoso:", data_max_precipitacao)
print("Maior precipitação:", max_precipitacao)


#-------------------------------------------------------------------------------

#Item C

print()
print(100*'=')
print()
print('ITEM C')

#Entrada de dados mes para item c
print('Agora vamos analisar a temperatura média mínima!')
print('Serão analisados os últimos 11 anos de um mês do auge do inverno!')
mesUsuario = int(input('Para isso, informe um mês do inverno no intervalo de 6 a 9:'))
while mesUsuario<6 or mesUsuario>9:
  print('Mês informado é inválido!')
  mesUsuario = int(input('-> Por favor, redigite o mês entre um número de 6 a 9: '))
print()
media_temperaturas = calcular_temperatura_min_media(dados, mesUsuario)
print(media_temperaturas)


#-------------------------------------------------------------------------------


#Item D


print()
print(100*'=')
print()
print('ITEM D')
print()
gerar_grafico(media_temperaturas)



#-------------------------------------------------------------------------------

#Item E

print(100*'=')
print()
print('ITEM E')
print()

print('Por último, vamos analisar a temperatura média mínima de um mes qualquer!')
print('Novamente, iremos analisar sobre os últimos 11 anos!')

mesQualquer = int(input('Para isso, informe um mês no intervalo de 1 a 12:'))
while mesQualquer<1 or mesQualquer>12:
  print('Mês informado é inválido!')
  mesQualquer = int(input('-> Por favor, redigite o mês entre um número de 1 a 12: '))

print()
media_temperaturas = calcular_temperatura_min_media(dados, mesQualquer)
print(media_temperaturas)

