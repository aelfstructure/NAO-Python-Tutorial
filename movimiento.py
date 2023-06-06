# -*- encoding: UTF-8 -*-

import sys
import math

from naoqi import ALProxy


def main(robotIP):
    try:
        posturasProxy = ALProxy("ALRobotPosture", robotIP, 50564)
        motion_proxy = ALProxy("ALMotion", robotIP, 50564)

        part = 'Body'
        body_names = motion_proxy.getBodyNames(part)
        speed = float(0.5) #entre 0 a 1
        #L viene de left, R viene de right
        #motion_proxy.setAngles(#parte del cuerpo,angulos radianes, velocidad)
        #Los grados son radianes ejemplo 30 grados * pi/180

        posturasProxy.goToPosture("StandInit", 2.0)
        motion_proxy.moveInit()
        motion_proxy.setAngles('HeadYaw',         -0.6, speed)
        motion_proxy.setAngles('HeadPitch',       -0.6, speed)
        motion_proxy.setAngles('LShoulderPitch',  1.4, speed)
        motion_proxy.setAngles('RShoulderRoll',   0.0, speed)
        motion_proxy.setAngles('LElbowYaw',       0.0, speed)
        motion_proxy.setAngles('LElbowRoll',      0.0, speed)
        motion_proxy.setAngles('RHipRoll',         0.0, speed)
        motion_proxy.setAngles('RHipPitch',        0.0, speed)
        motion_proxy.setAngles('RKneePitch',       -0.2, speed)
        motion_proxy.setAngles('RShoulderPitch',  1.4, speed)
        motion_proxy.setAngles('RShoulderRoll',   0.0, speed)
        motion_proxy.setAngles('RElbowYaw',       1.5, speed)
        motion_proxy.setAngles('RElbowRoll',      0.0, speed)
        posturasProxy.goToPosture("StandInit", 2.0)
        
        
    except Exception, e:
        print "No se pudo crear conexión con el robot"
        print "El error fue: ", e




if __name__ == "__main__":
    robotIp = "127.0.0.1"
    print "Programacion movimiento de python"
    main(robotIp)
