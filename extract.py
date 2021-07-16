from yahooquery import Ticker

petrobras = Ticker("PETR4.SA")
print( petrobras.history(period="max"))

''' Extraindo periodo de 60 dias com intervalo de 30 minutos'''
df = petrobras.history(period="60d",  interval = "30m")

''' Extraindo periodo de 30 minutos'''
#petrobras.history(period="60d",  interval = "30m")

''' Extraindo de um periodo pré-estabelecido'''
#petr.history(start="2005–05–01", end="2013–12–31")

'''Importação dos dados para CSV'''
compression_opts = dict(method='zip',archive_name='out.csv')

df.to_csv('out.zip', index=False,compression=compression_opts)
