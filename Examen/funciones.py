import pandas as pd
def recuperar():
    lista = pd.read_csv("Llistat.csv", usecols=["NAME", "NOTES"]).dropna()
    return lista

def recuperar_1():
    lista = pd.read_csv("Llistat.csv", usecols=["NAME", "GROUP", "ABSENCES", "MODULE"]).dropna()
    return lista


