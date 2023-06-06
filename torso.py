# -*- encoding: UTF-8 -*- 

'''Torso'''


import motion #libreria movimientos cuerpos
import almath #permite calcular algunos parametros para dar estabilidad a nao
from naoqi import ALProxy #libreria posturas

def StiffnessOn(proxy):
  #Usamos el nombre "Cuerpo" para significar la colección de todas las articulaciones, La rigidez de la articulación equivale a una limitación de par en los motores..
  pNames = "Body" 
  pStiffnessLists = 1.0
  pTimeLists = 1.0
  proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def main(robotIP):

    try:
        motionProxy = ALProxy("ALMotion", robotIP, 62284)
    except Exception, e:
        print "No se puede crear el proxy de ALMotion"
        print "El error fue: ", e

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 62284)
    except Exception, e:
        print "No se puede crear el proxy de ALRobotPosture"
        print "El Error fue: ", e

    # Dar inicio a la rigidez del Nao

    StiffnessOn(motionProxy)
    postureProxy.goToPosture("StandInit", 0.5)

    effector   = "Torso"
    space      = motion.FRAME_WORLD
    axisMask   = almath.AXIS_MASK_ALL
    isAbsolute = False

    #distancia
    dx  =0.045
    dy  =0.050

    path       = [
     [+dx, 0.0, 0.0, 0.0, 0.0, 0.0],        # punto 1
     [0.0, -dy, 0.0, 0.0, 0.0, 0.0],        # punto 2
     [-dx, 0.0, 0.0, 0.0, 0.0, 0.0],        # punto 3
     [0.0, +dy, 0.0, 0.0, 0.0, 0.0],        # punto 4
     [+dx, 0.0, 0.0, 0.0, 0.0, 0.0],        # punto 5
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]        # punto 6

    times      = [1.0, 2.0, 3.0, 4.0, 5.0, 6.5]
    motionProxy.positionInterpolation(effector, space, path,
                                      axisMask, times, isAbsolute)

if __name__ == "__main__":
    robotIp = "127.0.0.1"
    main(robotIp)


     
