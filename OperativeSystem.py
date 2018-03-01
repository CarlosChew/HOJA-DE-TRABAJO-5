# -*- coding: cp1252 -*-
         #UNIVERSIDAD DEL VALLE DE GUATEMALA
         #HOJA DE TRABAJO NO. 5

            #ALGORITMOS Y ESTRUCTURA DE DATOS
            

                #ALEXANDER TRUJILLO (17189)
                #CARLOS CHEW (17507)



#MODULES USED ON THIS WORKSHEET 
import random 
import simpy

def Process(ProcessName, x, Waiting, CPU):

    #GLOBAL VARIABLE, DECLARED OUTISDE THE FUNCTION 
    global OperativeSystem

    #RETURN A GENERATOR 
    yield x.timeout(Waiting)

    #READY 
    Ready = x.now

    ProcessTime = random.randit(1, 10)
    print ('%s llega a las %f necesita %d para hechar gasolina' % (ProcessName,ArriveTime,ProcessTime))

    with CPU.request() as queue:

        yield queue
        yield x.timeout(ProcessTime)
        print ('%s sale de gasolinera a las %f' % (ProcessName, x.now))

    WholeProcessTime = x.now - Ready
    print ('%s se tardo %f' % (ProcessName, WholrProcessTime))
    OperativeSystem = OperativeSystem + WholeProcessTime

x = simpy.Environment()
CPU = simpy.Resource(x,capacity = 1)
random.seed(10)

OperativeSystem = 0
for i in range(5):
    x.operation(Process('carro %d'%i,x,random.expovariate(1.0/10),CPU))
    

x.run(until=50)
print ("tiempo promedio por vehículo es: ", OperativeSystem/5.0)
