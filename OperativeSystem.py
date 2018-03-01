# -*- coding: cp1252 -*-

#UNIVERSIDAD DEL VALLE DE GUATEMALA
#HOJA DE TRABAJO NO. 5

#ALGORITMOS Y ESTRUCTURA DE DATOS
            

#ALEXANDER TRUJILLO (17189)
#CARLOS CHEW (17507)



#MODULES USED ON THIS WORKSHEET 
import random
import simpy

print ("")
print ("---OPERATIVE SYSTEM SIMULATION---")
print ("")
#FUNCTION DEFINES AS SIMULATION, WHICH CONTAINS PARAMETERS 
def simulation(processName,x,waiting,CPU):

    #VARIABLE WHICH NOT HAS BEEN DECLARED 
    global wholeProcess 

    #RETURNS A VALUE 
    yield x.timeout(waiting)
    
 
    ready = x.now


    running = random.randint(1, 200)
    print ('%s /Process %f needs %d ammount of RAM' % (processName,ready,running))
    

    with CPU.request() as CPUturn:
        yield CPUturn     
        yield x.timeout(running) 
        print ('%s /Finish the process on %f' % (processName, x.now))
        
        
    totalTime = x.now - ready
    print ('%s /It takes %f' % (processName, totalTime))
    wholeProcess = wholeProcess + totalTime
           


#IT NOW SIMULATES DE OPERATIVE SYSTEM 
x = simpy.Environment()
CPU = simpy.Resource(x,capacity = 1)
random.seed(10) 
wholeProcess = 0
for i in range(25):#RANGE 
    x.process(simulation('Process %d'%i,x,random.expovariate(1.0/10),CPU)) 

#IT RUNS THE SIMULATION UNTIL 50 VALULES 
x.run(until=50)  

print ("")
print ("")
print ("---AVERAGE PROCESS---")
print ("The average time of the process is: ", wholeProcess/25.0)
