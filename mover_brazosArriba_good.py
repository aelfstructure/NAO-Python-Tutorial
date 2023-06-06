# -*- encoding: UTF-8 -*-

import sys
import math

from naoqi import ALProxy
import time

def main(robotIP):
    
    try:
        posturasProxy = ALProxy("ALRobotPosture", robotIP, 62284)
        motion_proxy = ALProxy("ALMotion", robotIP, 62284)
        posturasProxy.goToPosture("StandInit", 2.0)
        part = 'Arms'
        body_names = motion_proxy.getBodyNames(part)
        speed = float(0.1) #entre 0 a 1
        #L viene de left, R viene de right
        #motion_proxy.setAngles(#parte del cuerpo,angulos radianes, velocidad)
        #Los grados son radianes ejemplo 30 grados * pi/180

        posturasProxy.goToPosture("StandInit", 2.0)
        
        motion_proxy.moveInit()
        motion_proxy.setAngles('LShoulderPitch',  -0.6, speed)
        time.sleep(2)
        posturasProxy.goToPosture("StandInit", 2.0)
    except Exception, e:
        print "No se pudo crear conexión con el robot"
        print "El error fue: ", e
    
    posturasProxy.goToPosture("StandInit", 2.0)


if __name__ == "__main__":
    robotIp = "127.0.0.1"
    print "Programacion movimiento de python"
    main(robotIp)
    
