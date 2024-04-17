def stampaDizionario(dizionario):
    for key,value in dizionario.items():
        for key,value in dizionario.items():
            print("La chiave è ..."+key)
            print("Il valore è ..."+str(value))

#calcolare il totale delle ore del dizionario
def totaleOre(dizionario):
    somma=0
    for key,value in dizionario.items():
        somma= somma + value
    return(str(somma))

#numero degli insegnanti con cattedra piena
def cattedraPiena(dizionario = {}):
    conta=0
    for key,value in dizionario.items():
        if(value == 18):
            conta= conta+1
    return(str(conta))

#scrivere una funzione che modifiche le ore allocate ad un insegnanate
def CambiaOre(dizionario, nome, ore):
    if nome in dizionario:
        dizionario[nome] = ore


def ScalaOre(dizionario, nome, ore):
    if nome in dizionario:
        dizionario[nome] -= ore

dizionario = {"Rossi":18, "Bianchi": 16, "Verdi":6, "Viola": 14}

stampaDizionario(dizionario)
print(cattedraPiena(dizionario))
print(totaleOre(dizionario))
CambiaOre(dizionario, "Verdi", 12)
print(dizionario)
ScalaOre(dizionario, "Viola", 4)
print(dizionario)