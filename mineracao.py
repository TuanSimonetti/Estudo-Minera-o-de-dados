# coding: utf-8
import nltk

#nltk.download()

base = [('eu sou admirada por muitos','alegria'),
        ('me sinto completamente amado','alegria'),
        ('amar e maravilhoso','alegria'),
        ('estou me sentindo muito animado novamente','alegria'),
        ('eu estou muito bem hoje','alegria'),
        ('que belo dia para dirigir um carro novo','alegria'),
        ('o dia está muito bonito','alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
        ('o amor e lindo','alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]

#print(base[1])

basetreinamento = [

('você e abominável','desgosto'),
('abomino a maneira como você age','desgosto'),
('estou adoentado','desgosto'),
('meu pai esta adoentado','desgosto'),
('estamos todos doentes','desgosto'),
('essa situação e muito amarga','desgosto'),
('disse adeus amargamente','desgosto'),
('tenho antipatia por aquela pessoa','desgosto'),
('como pode ser tão antipática!','desgosto'),
('que horrível seu asqueroso','desgosto'),
('tenho aversão agente como você','desgosto'),
('isso tudo e só chateação','desgosto'),
('estou muito chateada com suas mentiras','desgosto'),
('tão desagradável','desgosto'),
('isso me desagrada completamente','desgosto'),
('te desagrada isso','desgosto'),
('estou com enjôos terríveis','desgosto'),
('todos estão enfermos','desgosto'),
('foi uma enfermidade terrível','desgosto'),
('isso e muito grave','desgosto'),
('não seja tão grosseiro','desgosto'),
('você fez uma manobra ilegal','desgosto'),
('sua indecente, não tem vergonha?','desgosto'),
('você e malvado com as crianças','desgosto'),
('que comentário maldoso','desgosto'),
('sem escrúpulos você manipula a tudo','desgosto'),
('sinto repulsa por você','desgosto'),
('e repulsivo a maneira como olha para as pessoas','desgosto'),
('estou indisposta','desgosto'),
('a indisposição me atacou hoje','desgosto'),
('acho que vou vomitar','desgosto'),
('tem muito vomito lá','desgosto'),
('que incomodo essa dor','desgosto'),
('não me incomode nunca mais','desgosto'),
('suas bobagens estão nos incomodando','desgosto'),
('que nojo olha toda essa sujeira','desgosto'),
('como isso está sujo','desgosto'),
('tenho náuseas só de lembrar','desgosto'),
('me sinto nauseada com o cheiro desta comida','desgosto'),
('você esta obstruindo a passagem de ar','desgosto'),
('você esta terrivelmente doente','desgosto'),
('olhe que feia esta roupa','desgosto'),
('que atitude deplorável','desgosto'),
('nossa como você e feio','desgosto'),
('muito mau tudo isso','desgosto'),
('estou desgostoso com você','desgosto'),
('você cortou o meu assunto','desgosto'),
('para que tanta chateação?','desgosto'),
('esse perfume e enjoativo','desgosto'),
('ser perigoso não nada bom','desgosto'),
('você e perigoso demais para minha filhas','desgosto'),
('que fetido este esgoto','desgosto'),
('que fedido você esta','desgosto'),
('que cachorro malcheiroso','desgosto'),
('hora que ultraje','desgosto'),
('e ultrajante da sua parte','desgosto'),
('situação desagradável essa','desgosto'),
('você só me da desgosto','desgosto'),
('tenho aversão a pessoas assim','desgosto'),
('antipatia e um mal da sociedade','desgosto'),
('que criatura abominável','desgosto'),
('e depressiva a maneira como você vê o mundo','desgosto'),
('me desagrada sua presença na festa','desgosto'),
('sinto asco dessa coisa','desgosto'),
('que hediondo!','desgosto'),
('vou golfar o cafe fora','desgosto'),
('hora que garota detestável!','desgosto'),
('estou nauseada','desgosto'),
('isso que você disse foi muito grave','desgosto'),
('não seja obsceno na frente das crianças','desgosto'),
('não seja rude com as visitas','desgosto'),
('esse assunto me da repulsa','desgosto'),
('que criança terrivelmente travessa','desgosto'),
('que criança mal educada','desgosto'),
('estou indisposta te dar o divorcio','desgosto'),
('tão patetico, não tem nada mais rude para dizer?','desgosto'),
('por motivo torpe, com emprego de meio cruel e com impossibilidade de defesa para a vítima','desgosto'),
('a inveja e tão vil e vergonhosa que ninguem se atreve a confessá-la','desgosto'),
('o miserável receio de ser sentimental e o mais vil de todos os receios modernos','desgosto'),
('travesso gato quando fica com saudades do dono mija no sapato','desgosto'),
('isso e um ato detestável e covarde','desgosto'),
('revelam apenas o que e destrutivo e detestável para o povo','desgosto'),
('não sei como e a vida de um patife, mais a de um homem honesto e abominável','desgosto'),
('há coisas que temos que suportar para não acharmos a vida insuportável','desgosto'),
('as injurias do tempo e as injustiças do homem','desgosto'),
('odioso e desumano','desgosto'),
('você não publicará conteúdo odiento, pornográfico ou ameaçador','desgosto'),
('rancoroso e reprimido','desgosto'),
('não há animal mais degradante, estúpido, covarde, lamentável, egoísta, rancoroso e invejoso do que o homem','desgosto'),
('o virulento debate ente políticos','desgosto'),

('por favor não me abandone','tristeza'),
('não quero ficar sozinha','tristeza'),
('não me deixe sozinha','tristeza'),
('estou abatida','tristeza'),
('ele esta todo abatido','tristeza'),
('tão triste suas palavras','tristeza'),
('seu amor não e mais meu','tristeza'),
('estou aborrecida','tristeza'),
('isso vai me aborrecer','tristeza'),
('estou com muita aflição','tristeza'),
('me aflige o modo como fala','tristeza'),
('estou em agonia com meu intimo','tristeza'),
('não quero fazer nada','tristeza'),
('me sinto ansiosa e tensa','tristeza'),
('não consigo parar de chorar','tristeza'),
('não consigo segurar as lagrimas','tristeza'),
('e muita dor perder um ente querido','tristeza'),
('estou realmente arrependida','tristeza'),
('acho que o carma volta, pois agora sou eu quem sofro','tristeza'),
('você não cumpriu suas promessas','tristeza'),
('me sinto amargurada','tristeza'),
('coitado esta tão triste','tristeza'),
('já e tarde de mais','tristeza'),
('nosso amor acabou','tristeza'),
('essa noite machuca só para mim','tristeza'),
('eu não estou mais no seu coração','tristeza'),
('você mudou comigo','tristeza'),
('quando eu penso em você realmente dói','tristeza'),
('como se fosse nada você vê minhas lagrimas','tristeza'),
('você disse cruelmente que não se arrependeu','tristeza'),
('eu nunca mais vou te ver','tristeza'),
('ela esta com depressão','tristeza'),
('a depressão aflige as pessoas','tristeza'),
('estar depressivo e muito ruim','tristeza'),
('estou derrotada e deprimida depois deste dia','tristeza'),
('e comovente te ver dessa maneira','tristeza'),
('e comovente ver o que os filhos do brasil passam','tristeza'),
('como me sinto culpada','tristeza'),
('estou abatida','tristeza'),
('a ansiedade tomou conta de mim','tristeza'),
('as pessoas não gostam do meu jeito','tristeza'),
('adeus passamos bons momentos juntos','tristeza'),
('sinto sua falta','tristeza'),
('ele não gostou da minha comida','tristeza'),
('estou sem dinheiro para a comida','tristeza'),
('queria que fosse o ultimo dia da minha vida','tristeza'),
('você está com vergonha de mim','tristeza'),
('ela não aceitou a minha proposta','tristeza'),
('era o meu ultimo centavo','tristeza'),
('reprovei de ano na faculdade','tristeza'),
('afinal você só sabe me desfazer','tristeza'),
('eu falhei em tudo nessa vida','tristeza'),
('eu fui muito humilhado','tristeza'),
('e uma história muito triste','tristeza'),
('ninguem acredita em mim','tristeza'),
('eu não sirvo para nada mesmo','tristeza'),
('droga, não faço nada direito','tristeza'),
('sofrimento em dobro na minha vida','tristeza'),
('fui demitida essa semana','tristeza'),
('as crianças sofrem ainda mais que os adultos','tristeza'),
('pra mim um dia e ruim, o outro e pior','tristeza'),
('de repente perdi o apetite','tristeza'),
('oh que dia infeliz','tristeza'),
('estamos afundados em contas','tristeza'),
('nem um milagre pode nos salvar','tristeza'),
('só me resta a esperança','tristeza'),
('pior que isso não pode ficar','tristeza'),
('meu salário e baixo','tristeza'),
('não passei no vestibular','tristeza'),
('ninguem se importa comigo','tristeza'),
('ninguem lembrou do meu aniversário','tristeza'),
('tenho tanto azar','tristeza'),
('o gosto da vingança e amargo','tristeza'),
('sou uma mulher amargurada depois de que você me deixou','tristeza'),
('estou desanimada com a vida','tristeza'),
('e um desanimo só coitadinha','tristeza'),
('a derrota e depressiva','tristeza'),
('discriminar e desumano','tristeza'),
('que desanimo','tristeza'),
('e uma desonra para o pais','tristeza'),
('a preocupação deveria nos levar a ação não a depressão','tristeza'),
('passamos ao desalento e a loucura','tristeza'),
('aquele que nunca viu a tristeza nunca reconhecerá a alegria','tristeza'),
('cuidado com a tristeza ela e um vicio','tristeza'),

('eu imploro, não me matem!','medo'),
('tem certeza que não e perigoso?','medo'),
('não tenho certeza se e seguro','medo'),
('tenho que correr pra não me pegarem','medo'),
('socorro! ele queria roubar os meus doces!','medo'),
('esse cara está me perseguindo','medo'),
('não entro lá, e um lugar muito perigoso','medo'),
('este lugar continua assustador','medo'),
('na selva tem muitos animais perigosos','medo'),
('avancem com cautela','medo'),
('este lugar está silencioso de mais, cuidado!','medo'),
('por favor, deixe-me viver!','medo'),
('vou ficar sem mesada se tirar nota baixa','medo'),
('parece que tem olhos nos vigiando','medo'),
('eu temo que a sentença do juiz possa ser negativa','medo'),
('mas essa missão e arriscada','medo'),
('salvem-se quem puder!','medo'),
('meu plano pode ser descoberto','medo'),
('não tive culpa, juro não fui eu','medo'),
('tenho que tomar cuidado com o lobisomem','medo'),
('se eu não achar, ele vai descobrir a verdade','medo'),
('meu deus, ele desapareceu!','medo'),
('tomara que eles não me vejam daqui!','medo'),
('mantenha isso em segredo, se descobrirem estaremos ferrados','medo'),
('por favor, me soltem, eu sou inocente','medo'),
('estou ouvindo passos atrás de mim','medo'),
('eu vou pedir socorro!','medo'),
('cuidado com as curvas na estrada','medo'),
('não sei não, parece perigoso','medo'),
('estou tremendo de medo!','medo'),
('socorro, eu vou cair!','medo'),
('eu não vou ate a floresta negra, e muito perigoso','medo'),
('ouço passos na minha direção','medo'),
('acho que está arriscado de mais','medo'),
('vamos voltar, e muito perigoso','medo'),
('fuja, se não acabaremos mortos','medo'),
('receio por não me livrar desta situação','medo'),
('socorro! ele está armado!','medo'),
('ei cuidado, você vai bater no poste!','medo'),
('socorro, nós estamos afundando','medo'),
('e serio, cuidado com essa arma!','medo'),
('os tubarões estão atacando!','medo'),
('sinto arrepios quando fico sozinho no escuro','medo'),
('calma, eu não estou com o dinheiro','medo'),
('eu acho que estou sendo enganado','medo'),
('ligeiro, temos que fugir depressa','medo'),
('tem um crocodilo selvagem vindo para cá','medo'),
('se ficarmos quietos eles não vão nos achar','medo'),
('fuja! o tigre parece faminto','medo'),
('estou sem saída, preciso de um milagre','medo'),
('tire isso de mim! socorro!','medo'),
('não sei nadar, vou me afogar!','medo'),
('não tenho certeza se e seguro','medo'),
('vou apanhar se meus pais verem meu boletim','medo'),
('não consigo sair daqui!','medo'),
('se sair tão tarde, poderei ser assaltada','medo'),
('não me deixe por favor!','medo'),
('espere, não pode me largar aqui sozinho','medo'),
('temo pela sua segurança','medo'),
('eu te entrego o dinheiro, por favor não me mate!','medo'),
('ele vai levar todo o meu dinheiro','medo'),
('não dirija tão rápido assim','medo'),
('me descobriram, irão me prender!','medo'),
('só espero que não me façam nenhum mal','medo'),
('vou me afogar, me ajudem a sair da água','medo'),
('não estaremos a salvo aqui','medo'),
('não quero nem pensar no que pode acontecer','medo'),
('nessa cidade e uma desgraça atrás da outra','medo'),
('alguem esta me ligando, estou assustado','medo'),
('isso não e remedio, não me matem','medo'),
('eu não confio nele, tenho que ter cautela','medo'),
('muita cautela','medo'),
('vou ser descoberto, meu deus','medo'),
('receio que terei de ir','medo'),
('a noite e muito perigosa','medo'),
('estou estremecendo com essa casa','medo'),
('olha aquela criatura se movendo monstruosamente','medo'),
('não agüento este suspense','medo'),
('afugente os cães','medo'),
('estou chocado e amedrontado com este assassinato brutal','medo'),
('e preciso afugenta com ímpeto este medo do inferno','medo'),
('seu políticos usam suas forças para afugentar e amedrontar o povo','medo'),
('o objetivo disso e apenas me amedrontar mais','medo'),
('isso me apavora','medo')]

baseteste =[
('o mundo e feio como o pecado','desgosto'),
('a coisa mais difícil de esconder e aquilo que não existe','desgosto'),
('você errou feio aquele gol','desgosto'),
('nunca vou me casar sou muito feia','desgosto'),
('os golpes da adversidade são terrivelmente amargos','desgosto'),
('os homem ficam terrivelmente chatos','desgosto'),
('abominavelmente convencido','desgosto'),
('terrivelmente irritado','desgosto'),
('as instituições publicas estão terrivelmente decadentes','desgosto'),
('a população viveu em isolamento por muito tempo','desgosto'),
('estou terrivelmente preocupada','desgosto'),
('o nacionalismo e uma doença infantil','desgosto'),
('se me es antipático a minha negação esta pronta','desgosto'),
('muitos documentários sobre esse casal antipático','desgosto'),
('sua beleza não desfaça sua antipatia','desgosto'),
('esta e uma experiência desagradável','desgosto'),
('desagradável estrago nos banheiros','desgosto'),
('o mais irritante no amor e que se trata de um crime que precisa de um cúmplice','desgosto'),
('a situação nos causa grande incomodo','desgosto'),
('estou preocupado com o incomodo na garganta','desgosto'),
('simplesmente não quero amolação da policia','desgosto'),
('você e uma criaturinha muito impertinente','desgosto'),
('o peso e a dor da vida','desgosto'),
('me arrependo amargamente de minhas ações','desgosto'),
('o destino e cruel e os homens não são dignos de compaixão','desgosto'),
('o ódio conduz ao isolamento cruel e ao desespero','desgosto'),
('encerrou com o massacre mais repudiável e asqueroso que se conhece','desgosto'),
('de mal gosto e asqueroso','desgosto'),
('tudo e inserto neste mundo hediondo','desgosto'),
('o crime de corrupção e um crime hediondo','desgosto'),
('o rio esta fetido e de cor escura','desgosto'),
('muito lixo no rio o deixa malcheiroso','desgosto'),
('existe uma laranja podre no grupo e já desconfiamos quem e','desgosto'),
('foi de repente estou machucado e me sentindo enjoado','desgosto'),
('eu fiquei enojado','desgosto'),
('daqui alguns meses vou embora deste pais que já estou nauseado','desgosto'),

('isso tudo e um erro','tristeza'),
('eu sou errada eu sou errante','tristeza'),
('tenho muito dó do cachorro','tristeza'),
('e dolorida a perda de um filho','tristeza'),
('essa tragedia vai nos abalar para sempre','tristeza'),
('perdi meus filhos','tristeza'),
('perdi meu curso','tristeza'),
('sou só uma chorona','tristeza'),
('você e um chorão','tristeza'),
('se arrependimento matasse','tristeza'),
('me sinto deslocado em sala de aula','tristeza'),
('foi uma passagem fúnebre','tristeza'),
('nossa condolências e tristeza a sua perda','tristeza'),
('desanimo, raiva, solidão ou vazies, depressão','tristeza'),
('vivo te desanimando','tristeza'),
('estou desanimado','tristeza'),
('imperador sanguinário, depravado e temeroso','tristeza'),
('meu ser esta em agonia','tristeza'),
('este atrito entre nos tem que acabar','tristeza'),
('a escuridão desola meu ser','tristeza'),
('sua falsa preocupação','tristeza'),
('sua falsidade me entristece','tristeza'),
('quem esta descontente com os outros esta descontente consigo próprio','tristeza'),
('a torcida esta descontente com a demissão do tecnico','tristeza'),
('estou bastante aborrecido com o jornal','tristeza'),
('me sinto solitário e entediado','tristeza'),
('a vida e solitária para aqueles que não são falsos','tristeza'),
('como com compulsão depois da depressão','tristeza'),
('estou me desencorajando a viver','tristeza'),
('ele desencoraja minhas vontades','tristeza'),
('isso vai deprimindo por dentro','tristeza'),
('acho que isso e defeituoso','tristeza'),
('os remedios me derrubam na cama','tristeza'),
('a depressão vai me derrubar','tristeza'),
('suas desculpas são falsas','tristeza'),
('não magoe as pessoas','tristeza'),

('que abominável esse montro!','medo'),
('vamos alarmar a todos sobre a situação','medo'),
('estou amedrontada','medo'),
('estou com muito medo da noite','medo'),
('ele esta me ameaçando a dias','medo'),
('quanta angustia','medo'),
('estou angustiada','medo'),
('angustiadamente vou sair e casa','medo'),
('isso me deixa apavorada','medo'),
('você esta me apavorando','medo'),
('estou desconfiada de você','medo'),
('não confio em você','medo'),
('ate o cachorro está apavorado','medo'),
('estou assustado com as ações do meu colega','medo'),
('agora se sente humilhado, apavorado','medo'),
('assustou a população e provocou mortes','medo'),
('estou com dificuldades para respirar e muito assustado','medo'),
('os policiais se assustaram quando o carro capotou','medo'),
('o trabalhador e assombrado pelo temor do desemprego','medo'),
('este lugar e mal assombrado','medo'),
('estou assombrado pela crise financeira','medo'),
('mesmo aterrorizado lembro de você','medo'),
('aterrorizado e suando frio','medo'),
('um grupo de elefantes selvagens tem aterrorizado vilas','medo'),
('me sinto intimidada pela sua presença','medo'),
('tenho medo de ser advertida novamente','medo'),
('estou correndo o risco de ser advertido','medo'),
('estou correndo riscos de saúde','medo'),
('os riscos são reais','medo'),
('podemos perder muito dinheiro com essa investida','medo'),
('socorro, fui intimado a depor','medo'),
('fui notificado e estou com medo de perde a guarda da minha filha','medo'),
('estou angustiada com meus filhos na rua','medo'),
('e abominável o que fazem com os animais','medo'),
('foi terrível o tigre quase o matou','medo'),
('me advertiram sobre isso','medo')]


stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

stopwordsnltk = nltk.corpus.stopwords.words('portuguese')
stopwordsnltk.append('vou')
stopwordsnltk.append('tão')
#print(stopwordsnltk)

def removestopwords(texto):
    frases = []
    for (palavras, emocao) in texto:
        semstop = [p for p in palavras.split() if p not in stopwordsnltk]
        frases.append((semstop, emocao))
    return frases

#print(removestopwords(base))

def aplicastemmer(texto):
    stemmer = nltk.stem.RSLPStemmer()
    frasessstemming = []
    for (palavras, emocao) in texto:
        comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwordsnltk]
        frasessstemming.append((comstemming, emocao))
    return frasessstemming

frasescomstemmingtreinamento = aplicastemmer(basetreinamento)
frasescomstemmingteste = aplicastemmer(baseteste)
#print(frasescomstemming)

def buscapalavras(frases):
    todaspalavras = []
    for (palavras, emocao) in frases:
        todaspalavras.extend(palavras)
    return todaspalavras

palavrastreinamento = buscapalavras(frasescomstemmingtreinamento)
palavrasteste = buscapalavras(frasescomstemmingteste)
#print(palavras)

def buscafrequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras

frequenciatreinamento = buscafrequencia(palavrastreinamento)
frequenciateste = buscafrequencia(palavrasteste)
#print(frequencia.most_common(50))

def buscapalavrasunicas(frequencia):
    freq = frequencia.keys()
    return freq

palavrasunicastreinamento = buscapalavrasunicas(frequenciatreinamento)
palavrasunicasteste = buscapalavrasunicas(frequenciateste)
#print(palavrasunicastreinamento)

#print(palavrasunicas)

def extratorpalavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavras in palavrasunicastreinamento:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas

caracteristicasfrase = extratorpalavras(['am', 'nov', 'dia'])
#print(caracteristicasfrase)

basecompletatreinamento = nltk.classify.apply_features(extratorpalavras, frasescomstemmingtreinamento)
basecompletateste = nltk.classify.apply_features(extratorpalavras, frasescomstemmingteste)
#print(basecompleta[15])

# constroi a tabela de probabilidade
classificador = nltk.NaiveBayesClassifier.train(basecompletatreinamento)
print(classificador.labels())
#print(classificador.show_most_informative_features(20))

print(nltk.classify.accuracy(classificador, basecompletateste))

erros = []
for (frase, classe) in basecompletateste:
    #print(frase)
    #print(classe)
    resultado = classificador.classify(frase)
    if resultado != classe:
        erros.append((classe, resultado, frase))
#for (classe, resultado, frase) in erros:
#    print(classe, resultado, frase)

from nltk.metrics import ConfusionMatrix
esperado = []
previsto = []
for (frase, classe) in basecompletateste:
    resultado = classificador.classify(frase)
    previsto.append(resultado)
    esperado.append(classe)

#esperado = 'alegria alegria alegria alegria medo medo surpresa surpresa'.split()
#previsto = 'alegria alegria medo surpresa medo medo medo surpresa'.split()
matriz = ConfusionMatrix(esperado, previsto)
print(matriz)

# 1. Cenário
# 2. Número de classes - 16%
# 3. ZeroRules - 21,05%

teste = 'eu sinto amor por voce'
testestemming = []
stemmer = nltk.stem.RSLPStemmer()
for (palavrastreinamento) in teste.split():
    comstem = [p for p in palavrastreinamento.split()]
    testestemming.append(str(stemmer.stem(comstem[0])))
#print(testestemming)

novo = extratorpalavras(testestemming)
#print(novo)

#print(classificador.classify(novo))
distribuicao = classificador.prob_classify(novo)
#for classe in distribuicao.samples():
#    print("%s: %f" % (classe, distribuicao.prob(classe)))










