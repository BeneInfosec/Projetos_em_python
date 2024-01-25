# 1. Extração de dados em json para excel
## 1.1 Como executar o programa? 

$`python3 paises.py`

<br/><br/>

# 2. Extracao de dados de ações da Bovespa
Exportar dados para .csv de ações da Bovespa com Python

Este programa foi baseado em: https://medium.com/@rodrigobercinimartins/como-extrair-dados-da-bovespa-sem-gastar-nada-com-python-14a03454a720

## 2.1 Como executar o programa? 

$`pip install yahooquery`

$`python3 extract.py`

<br/><br/>

# 3. Cifra-de-Cesar
Criptografia de Cifra de Cesar para o programa AceleraDev da Codenation

### Criptografia de Júlio César

Segundo o Wikipedia, criptografia ou criptologia (em grego: kryptós, “escondido”, e gráphein, “escrita”) é o estudo e prática de princípios e técnicas para comunicação segura na presença de terceiros, chamados “adversários”. Mas geralmente, a criptografia refere-se à construção e análise de protocolos que impedem terceiros, ou o público, de lerem mensagens privadas. Muitos aspectos em segurança da informação, como confidencialidade, integridade de dados, autenticação e não-repúdio são centrais à criptografia moderna. Aplicações de criptografia incluem comércio eletrônico, cartões de pagamento baseados em chip, moedas digitais, senhas de computadores e comunicações militares. Das Criptografias mais curiosas na história da humanidade podemos citar a criptografia utilizada pelo grande líder militar romano Júlio César para comunicar com os seus generais. Essa criptografia se baseia na substituição da letra do alfabeto avançado um determinado número de casas. Por exemplo, considerando o número de casas = 3:

**Normal:** a ligeira raposa marrom saltou sobre o cachorro cansado

**Cifrado:** d oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr

### Regras

As mensagens serão convertidas para minúsculas tanto para a criptografia quanto para descriptografia.
No nosso caso os números e pontos serão mantidos, ou seja:
- **Normal:** 1a.a

- **Cifrado:** 1d.d

## 3.1 Como executar o programa? 

### Para criptografar a mensagem
$`python3 cripto.py`

### Para descriptografar a mensagem
$`python3 descry.py`
