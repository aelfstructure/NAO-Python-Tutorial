# -*- encoding: UTF-8 -*- 

'''Torso'''

import motion #libreria movimientos cuerpos
import almath #permite calcular algunos parametros para dar estabilidad a nao
from naoqi import ALProxy #libreria posturas
import time



def main(robotIP):

    try:
        motionProxy = ALProxy("ALMotion", robotIP, 53273)
    except Exception, e:
        print "No se puede crear el proxy de ALMotion"
        print "El error fue: ", e

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 53273)
    except Exception, e:
        print "No se puede crear el proxy de ALRobotPosture"
        print "El Error fue: ", e

    # Dar inicio a la rigidez del Nao
    motionProxy.setStiffnesses("Head", 1.0) #inicio motores
    postureProxy.goToPosture("StandInit", 0.5) #posición inicial

    #inicio, interpolacion
    names      = ["Head"] # heads controla 2 angulos
    angleLists = [-1.1667,-1.1667] #Listas, con el "names" ,mueva a izquierda-derecha y hacia abajo o arriba
    timeLists  = [2.0, 2.2] #velocidad
    isAbsolute = True #angulos absolutos
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    #postureProxy.goToPosture("StandInit", 0.5)

 
    names  = ["HeadYaw","HeadPitch"] #HeadYaw lo mueve recto izquierda-Derecha, HP hacia abajo
    #la cabeza la mueve hacia arriba o abajo y de lado 

    #angleLists  = [[50.0*almath.TO_RAD, 0.0],
    #               [-30.0*almath.TO_RAD, 30.0*almath.TO_RAD, 0.0]]
    #timeLists   = [[1.0, 2.0], [ 1.0, 2.0, 3.0]]
    #isAbsolute  = True
   # motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)

    motionProxy.setStiffnesses("Head", 0.0) #apagar los motes del robot
    time.sleep(10)
    postureProxy.goToPosture("StandInit",0.5)
    motionProxy.setStiffnesses("Head", 1.0)
    postureProxy.goToPosture("StandInit", 0.5)
    names      = ["Head"]
    angleLists = [-1.8800,-1.8800]
    timeLists  = [2.0, 2.2]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    names  = ["HeadYaw","HeadPitch"]
    motionProxy.setStiffnesses("Head", 0.0)
    time.sleep(10)
    postureProxy.goToPosture("StandInit",0.5)

if __name__ == "__main__":
    robotIp = "127.0.0.1"
    main(robotIp)
