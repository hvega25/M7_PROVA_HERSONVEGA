import funciones
import matplotlib.pyplot as plt
import pandas as pd

def grafica_p1():
    prueba = funciones.recuperar()
    imprimir = prueba.groupby(by="NAME").mean()
    f = pd.DataFrame (imprimir)
    f.plot.bar()
    plt.title("MITJA NOTA ALUMNE CICLE")
    plt.ylabel("NOTES")
    plt.xlabel("ALUMNE")
    plt.show()


def grafica_p2():
    prueba = funciones.recuperar_1()
    grupo = prueba [prueba [ "GROUP"] == "DAW2"]
    print(grupo)



grafica_p2()
grafica_p1()