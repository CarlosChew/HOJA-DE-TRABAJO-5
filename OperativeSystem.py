# -*- coding: cp1252 -*-
         #UNIVERSIDAD DEL VALLE DE GUATEMALA
         #HOJA DE TRABAJO NO. 5

            #ALGORITMOS Y ESTRUCTURA DE DATOS
            

                #ALEXANDER TRUJILLO (17189)
                #CARLOS CHEW (17507)



#MODULES USED ON THIS WORKSHEET 
import random

import simpy

def simulation(processName,x,waiting,CPU):
    global wholeProcess 

   
    yield x.timeout(waiting)
    
 
    ready = x.now

    running = random.randint(1, 10)
    print ('%s llega a las %f necesita %d para hechar gasolina' % (processName,ready,running))
    

    with CPU.request() as CPUturn:
        yield CPUturn     
        yield x.timeout(running) 
        print ('%s sale de gasolinera a las %f' % (processName, x.now))
        
        
    totalTime = x.now - ready
    print ('%s se tardo %f' % (processName, totalTime))
    wholeProcess = wholeProcess + totalTime
           



x = simpy.Environment()
CPU = simpy.Resource(x,capacity = 1)
random.seed(10) 
wholeProcess = 0
for i in range(5):
    x.process(simulation('carro %d'%i,x,random.expovariate(1.0/10),CPU))

x.run(until=50)  

print ("tiempo promedio por vehículo es: ", wholeProcess/5.0)
