from supabase import create_client
from time import localtime

def hora():
    return {"mes": localtime().tm_mon, "dia": localtime().tm_mday, "hora": localtime().tm_hour, "minuto": localtime().tm_min}

url = "https://yurkilcutxjmzhbiojkf.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl1cmtpbGN1dHhqbXpoYmlvamtmIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyNzgwNjM0OSwiZXhwIjoyMDQzMzgyMzQ5fQ.MqPS9cCgjrCYZACY9zQZuQsBPV98ZZCo6488Sh_wZgk"

supabase = create_client(url, key)


nome: str = str(input("Digite seu nome: "))

while True:

    hora_atual = hora()
    response = supabase.table('Mensagens').select('*').execute()
    for _ in response.data:
        if data["dia"] != hora_atual["dia"]:
            print(f'{_["data"]["mes"]}/{_["data"]["dia"]} {_["data"]["hora"]}:{_["data"]["minuto"]}-{_["nome"]} -{_["msg"]}')
        else:
            print(f'{_["data"]["hora"]}:{_["data"]["minuto"]}-{_["nome"]} -{_["msg"]}')



    msg = str(input("Digite uma mensagem: "))


    data = {
        "data": hora_atual, 
        "nome": nome, 
        "msg": msg}
        
    if msg == "a":
        pass
    else:
        data_add = supabase.table('Mensagens').insert(data).execute()





