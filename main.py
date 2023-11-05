import requests

#Insira sua ''Chave de API'' abaixo 
API_KEY = "  "

cidade = input('Qual sua cidade? ')

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&units=metric&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp']

print(f'Atualmente {descricao} e', f'{temperatura}ºC de tempertura')