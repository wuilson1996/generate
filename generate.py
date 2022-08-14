import random
from time import time
import pandas as pd
from datetime import datetime
import sqlite3

class Combinate:
    def __init__(self, inicio=None, fin=None, num=None) -> None:
        self._inicio = inicio
        self._fin = fin
        self._num = num
        self._numbers = []
        self._conexion = sqlite3.connect("db2.sqlite3")
        self._cursor = self._conexion.cursor()

    def genera(self):
        print("[+] Procesando numeros...")
        t = time()
        aux_init = 1
        aux_fin = 9
        aux = 9
        for i in range(self._inicio-1):
            if i < self._inicio-2:
                aux *= 10
                aux_fin += aux
            aux_init *= 10
        aux_fin += aux_init
        print(aux_init, aux_fin)
        i = 0
        while True:
            n = random.randint(aux_init,aux_fin)
            if n not in self._numbers:
                self._numbers.append(str(n))
                for k in range(0,10,1):
                    if k != 1:
                        self._numbers.append(str(k)+str(n)[1:len(str(n))])
                i += 1
                if i >= 10000:
                    break
        print(len(self._numbers))
        numb = []
        fin = self._fin - self._inicio
        #print(fin)
        for k in range(fin):
            if self._num is None:
                if k < fin-1:
                    m = 0
                else:
                    m = 1
            else:
                m = 0
                aux = 0
                if k == fin-1:
                    #print("entro")
                    aux = 1
            for i in range(m,10,1):
                #print(i)
                for n in self._numbers:
                    if self._num is None:
                        numb.append(str(i)+str(n))
                    else:
                        if aux == 0:
                            numb.append(str(i)+str(n))
                        else:
                            #print("entro en fin")
                            numb.append((str(self._num)+str(i)+str(n),'megatron123',datetime.today(),datetime.today(),"sin operador"))
            self._numbers = numb
            del numb
            numb = []
        #print(numb)
        print(len(self._numbers))
        print(time() - t)
        print("[+] Numeros Procesados...")

    def result(self, name="combinaciones", nums=None):
        print("[+] Procesando Excel...")
        df = pd.DataFrame()
        df["numeros"] = self._numbers
        df.to_excel(str(name)+".xlsx")
        print("[+] Excel Proceso")
    
    def text(self):

        with open("combinaciones.txt", "w") as file:
            for i in self._numbers:
                file.writelines(str(i))
                file.writelines("\n")

    def insert(self): 
        print("[+] Insertando Datos...")
        sql = """INSERT INTO api_numbers 
                    (number, client, created, updated, oper) 
                    VALUES(?,?,?,?,?)"""
        self._cursor.executemany(sql, self._numbers)
        self._conexion.commit()
        print("[+] Fin de Proceso")

if __name__ == "__main__":
    inicio = input("Ingrese inicio de combinaciones: ")
    fin = input("Ingrese fin de combinaciones: ")
    run = Combinate(inicio=int(inicio), fin=int(fin), num=6)
    run.genera()
    #run.result()
    run.text()
    #run.insert()
    print("[+] Fin de Proceso...")