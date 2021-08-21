from datetime import datetime
import requests


seq = 1
nome_eq = "DJ XYZ"
tipo_eq = "disjuntor"
mode_eq = "modelo-a"
nome_lo = "SE XYZ"

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
            "equipamento": {
                "nome": nome_eq,
                "tipo": tipo_eq,
                "modelo": mode_eq,
                "localidade": {
                    "nome":nome_lo
                }
            },
            "inicio": str(start),
            "fim": str(end),
            "sequencia": seq
        }
        r = requests.post(url, json=data)
        print(r.status_code, r.reason)
        print(r.text[:300] + '...')

        seq += 1

except KeyboardInterrupt:
    print("Pressionado CTRL+C. Fim do programa.")
    exit()
