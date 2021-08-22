from datetime import datetime
import requests


nome_eq = "DJ XYZ"
tipo_eq = "disjuntor"
mode_eq = "modelo-a"
nome_lo = "SE XYZ"
seq = 0

with open('sequencia.txt', 'r+') as f:
    seq = int(f.read())

try:
    while True:

        # start
        comando_inicial = ''

        while comando_inicial != "inicio":
            comando_inicial = input("Digite 'inicio': ")

        start = datetime.now()

        # end
        comando_final = ''

        while comando_final != "fim":
            comando_final = input("Digite 'fim': ")

        end = datetime.now()

        # send
        url = "http://127.0.0.1:8000/mdj/api/evento/"
        data = {
            "equipamento": nome_eq,
            "inicio": str(start),
            "fim": str(end),
            "sequencia": seq
        }
        r = requests.post(url, json=data)
        print(r.status_code, r.reason)
        print(r.text[:300] + '...')

        seq += 1

except KeyboardInterrupt:
    print("\nPressionado CTRL+C. Fim do programa.\n")

finally:
    with open('sequencia.txt', 'r+') as f:
        f.truncate(0)
        f.write(str(seq))
    exit()
