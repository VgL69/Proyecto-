import matplotlib.pyplot as plt
from numpy import mod, true_divide

listaDeDatos = []
def leer_archivo():
    with open("Datos.csv","r",encoding="utf-8") as f:
        for i in f.readlines():
            datos = i.split(",")
            listaDeDatos.append(datos)

def listaComunasUsuario():
    comunasListadoUsuario= []
    for i in listaDeDatos:
        if i[2] != "Comuna" and len(i[9])>0:
            comunaFormato = i[2] + "(" + i[3] + ")"
            comunasListadoUsuario.append(comunaFormato)
    formato = ""
    count = 0
    for i in range(len(comunasListadoUsuario)):
        if count < 2 and i != len(comunasListadoUsuario)-1:
            formato = formato + comunasListadoUsuario[i] + "\t\t"
            count += 1
        else:
            formato = formato + comunasListadoUsuario[i] + "\t\t"
            count = 0
            print(formato)
            formato = ""

def listaComunasValidacion():
    listaParaValidacionComunas = []
    for i in listaDeDatos:
        if i[2] != "Comuna" and len(i[3])>0:
            listaParaValidacionComunas.append(i[2])
            listaParaValidacionComunas.append(i[3])
    return listaParaValidacionComunas

def filtroDatosComuna(comuna):
    for i in listaDeDatos:
        if comuna in i:
            datoFiltrado = []
            for count in range(len(i)-9,len(i)-1):
                datoFiltrado.append(int(float(i[count])))
    return datoFiltrado

def datoComunaNoAcumulado(datoFiltrado):
    listaDatoNoAcumulado = []
    for i in range(1,len(datoFiltrado)):
        operacion = datoFiltrado[i] - datoFiltrado[i-1]
        listaDatoNoAcumulado.append(int(operacion))
    return listaDatoNoAcumulado        

def listaRegionesUsuario():
    regionListadoUsuario = []
    for i in listaDeDatos:
        formato = i[0] + "[" + i[1] + "]"
        if formato not in regionListadoUsuario and i[0] != "Region":
            regionListadoUsuario.append(formato)
    for region in regionListadoUsuario:
        print(f"-{region}")

def listaRegionValidacion():
    listaParaValidacionRegion = []
    for i in listaDeDatos:
        if i[0] not in listaParaValidacionRegion and i[0] != "Region":
            listaParaValidacionRegion.append(i[0])
            listaParaValidacionRegion.append(i[1])
    return listaParaValidacionRegion

def filtroRegion(region):
    filtrada = []
    for i in listaDeDatos:
        if region in i:   # Compruebo si el datodefiltro el cual seria region esta en la lista para asi solo obtener las que coincidan
            filtrada.append(i)
    return filtrada

def datosRegionAcumulado(filtrada):
    listaDatosRegion = [0,0,0,0,0,0,0,0] # lista creada solo para ir sumando con los indices
    for comuna in filtrada:
        contador = 0 # es ocupado para obetener el indice de la lista donde estaran las sumas de todo
        for i in range(len(comuna)-9,len(comuna)-1,1):  # Este for obtiene 8 datos ya que son necesario 8 datos para obtener el no acumulado si es necesario
            listaDatosRegion[contador] = int(listaDatosRegion[contador] + float(comuna[i])) # voy sumando lo que ya estaba en la lista y el nuevo valor obtenido de la otra comuna
            contador += 1
        contador = 0 # reinicio valor para seguir con otra comuna
    return listaDatosRegion

def datosGraficoNoAcumuladoRegion(listaDatosRegion):
    listaNoAcumulada = []
    for i in range(1 , len(listaDatosRegion)): # Este for empieza en 1 ya que para obtener los casos totales de una region seria el valor anterior menos el nuevo
        listaNoAcumulada.append(listaDatosRegion[i] - listaDatosRegion[i-1]) # Aqui hago la operacion y la ingreso a una lista
    return listaNoAcumulada

def listadoRegionesAnalisis():
    listaRegionesAnalisis = []
    for i in listaDeDatos:
        if i[0] not in listaRegionesAnalisis and i[0] != "Region":
            listaRegionesAnalisis.append(i[0])
    return listaRegionesAnalisis

def tasaRegion():
    listaRegionesAnalisis = listadoRegionesAnalisis()
    tasas = []
    for region in listaRegionesAnalisis:
        poblacion = 0
        acumulado = 0
        with open("Datos.csv","r",encoding="utf-8") as f:
            for i in f.readlines():
                linea = i.split(",")
                if region in linea and len(linea[3])>0:
                    poblacion += int(float(linea[4]))
                    acumulado += int(float(linea[len(linea)-2]))
        tasa = (acumulado/poblacion) * 100000
        tasas.append(round(tasa,1))
    return tasas,listaRegionesAnalisis
    
leer_archivo()