import pandas as pd
import matplotlib.pyplot as plt



try:
 
    file = open("finanzas2020[1].csv","r")
    data = pd.read_csv("finanzas2020[1].csv",sep="\t")
    meses = data.columns.values
    if(len(meses))!= 12:
        raise AssertionError("numero de meses incorrectos")

    DataMesesNum = []
    DataMesesTotal = []


    for mes in meses:
        try:
        
            DataMesesNum.append(sum(data[mes]))
            DataMesesTotal.append(sum(data[mes]))
                
        
        except TypeError:
            DataMesesTotal.append(mes)

    print(DataMesesTotal)

   
    Gastos= []
    ahorros = []

    for valor in DataMesesNum:
        if valor<0:
            Gastos.append(valor)
        else:
            ahorros.append(valor)
    print("Los gastos totales del año han sido",sum(Gastos))
    print("La media de gastos totales del año han sido",sum(Gastos)/len(Gastos))
    print("Los ingresos totales del años son", sum(ahorros)) 

except IOError:
    print("fichero no encontrado")
else: 
    plt.plot(DataMesesNum)
finally:
    file.close()


        
  
        
    