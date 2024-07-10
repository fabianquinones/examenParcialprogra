import csv
import random
import statistics
DicTrabajadores={}
def asignarSueldos(trabajadores):
    print("********************************************")
    for trabajador in trabajadores:
        sueldo =random.randint(100000,2000000)
        DicTrabajadores[trabajador]=sueldo
    return print(DicTrabajadores)
def calificarSueldos():
    print("********************************************")
    sueldomenor800k={}
    sueldoentre800ky2m={}
    sueldomayor2m={}
    for trabajador,sueldo in DicTrabajadores.items():
        if sueldo <800000:
            sueldomenor800k[trabajador]=sueldo
        elif sueldo >= 800000 and sueldo < 2000000:
            sueldoentre800ky2m[trabajador]=sueldo
        elif sueldo >= 2000000:
            sueldomayor2m[trabajador]=sueldo
    
    print("sueldos menores a 800.000 total: ",len(sueldomenor800k))
    print("nombre   sueldo")
    for trabajador,sueldo in sueldomenor800k.items():
        print(trabajador, sueldo,"\n")
    print("sueldos entre 800.000 y 2.000.00 total: ",len(sueldoentre800ky2m))
    print("nombre   sueldo")
    for trabajador,sueldo in sueldoentre800ky2m.items():
        print(trabajador, sueldo,"\n")
    print("sueldos mayores a 2.000.000 Total: ",len(sueldomayor2m))
    for trabajador,sueldo in sueldomayor2m.items():
        print(trabajador, sueldo,"\n")


def verEstats():
    print("********************************************")
    masalto=0
    for trabajdor,sueldo in DicTrabajadores.items():
        if sueldo > masalto:
            masalto=sueldo
    print ("el sueldo mas alto es de: ",masalto)

    masbajo=10000000000
    for trabjador,sueldo in DicTrabajadores.items():
        if sueldo<masbajo:
            masbajo=sueldo
    print("el sueldo mas bajo es de: ",masbajo)

    promedio=0
    for trabajdor,sueldo in DicTrabajadores.items():
        promedio=promedio+sueldo
    promediof=promedio/len(DicTrabajadores)
    print("el promedio de sueldos es de: ",promediof)

    for trabjador,sueldo in DicTrabajadores.items():
        sueldos=[]
        sueldos.append(sueldo)
    print("la medida geometrica se de: ",str(statistics.geometric_mean(sueldos)))

        
def reportes():
    print("********************************************")
    with open ("reportes.csv","w",newline="")as archivo:
        escritor=csv.writer(archivo,delimiter=",")
        escritor.writerow(["trabajador","sueldo","descutosalud","descuentoAFP","sueldoLiquido"])
        for trabajador , sueldo in DicTrabajadores.items():
            descutosalud= sueldo*0.07
            descuentoAFP=sueldo*0.12
            sueldoLiquido=sueldo-descuentoAFP-descutosalud
            escritor.writerow([trabajador,sueldo,descutosalud,descuentoAFP,sueldoLiquido])
        print("reporte generado")



def salir():
    print("--------------------------------------------")
    print("saliendo del programa")
    print("desarrolado por Fabian Quiñones")
    print("20.689.087-8")
    
