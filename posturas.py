# -*- encoding: UTF-8 -*-

import sys

from naoqi import ALProxy
import almath


def main(robotIP):

    try:
        posturasProxy = ALProxy("ALRobotPosture", robotIP, 50564)
    except Exception, e:
        print "No se pudo crear conexión con el robot"
        print "El error fue: ", e

    posturasProxy.goToPosture("StandInit", 2.0)
    posturasProxy.goToPosture("SitRelax", 2.0)  
    posturasProxy.goToPosture("StandZero", 2.0)
    posturasProxy.goToPosture("LyingBelly", 2.0)
    posturasProxy.goToPosture("LyingBack", 2.0)
    posturasProxy.goToPosture("Stand", 2.0)
    posturasProxy.goToPosture("Crouch", 2.0)
    posturasProxy.goToPosture("Sit", 2.0)

if __name__ == "__main__":
    robotIp = "127.0.0.1"
    print "Programación posturas de python"
    main(robotIp)
