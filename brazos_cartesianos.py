# -*- encoding: UTF-8 -*- 

'''Control Cartesiano'''


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
    
    StiffnessOn(motionProxy)
    postureProxy.goToPosture("StandInit", 0.5)
    #dx         =  0.03      # traslación en X (metros)
    #dy         =  0.03      # traslación en Y (metros)
    #dz         =  0.00      # traslación en Z (metros)
    #dwx        =  0.00      # rotación en X (radianes)
    #dwy        =  0.00      # rotación en Y (radianes)
    #dwz        =  0.00      # rotación en Z (radianes)

    effector   = "LArm"
    space      = motion.FRAME_ROBOT #usarla para brazos
    #space      =  motion.FRAME_WORLD usarla para torso

    # x, y, z            wx.  wy.  wz
    path       = [
     [0.0, -0.05, +0.00, 0.0, 0.0, 0.0],        # punto 1
     [0.0, +0.00, +0.04, 0.0, 0.0, 0.0],        # punto 2
     [0.0, +0.04, +0.00, 0.0, 0.0, 0.0],        # punto 3
     [0.0, +0.00, -0.02, 0.0, 0.0, 0.0],        # punto 4
     [0.0, -0.05, +0.00, 0.0, 0.0, 0.0],        # punto 5
     [0.0, +0.00, +0.00, 0.0, 0.0, 0.0]]        # punto 6
    axisMask   = almath.AXIS_MASK_VEL                             #controlar la posición
    times      = [0.5, 1.0, 2.0, 3.0, 4.0, 4.5] # segundos
    isAbsolute = False
    motionProxy.positionInterpolation(effector, space, path,
                                      axisMask, times, isAbsolute)
    postureProxy.goToPosture("StandInit", 2.0)
    
    effector   = "RArm"
    space      = motion.FRAME_ROBOT
    path       = [
     [0.0, -0.05, +0.00, 0.0, 0.0, 0.0],        # punto 1
     [0.0, +0.00, +0.04, 0.0, 0.0, 0.0],        # punto 2
     [0.0, +0.04, +0.00, 0.0, 0.0, 0.0],        # punto 3
     [0.0, +0.00, -0.02, 0.0, 0.0, 0.0],        # punto 4
     [0.0, -0.05, +0.00, 0.0, 0.0, 0.0],        # punto 5
     [0.0, +0.00, +0.00, 0.0, 0.0, 0.0]]        # punto 6
    axisMask   = almath.AXIS_MASK_VEL                             #controlar la posición
    times      = [0.5, 1.0, 2.0, 3.0, 4.0, 4.5] # segundos
    isAbsolute = False
    motionProxy.positionInterpolation(effector, space, path,
                                      axisMask, times, isAbsolute)
    
#CARMOR333@GMAIL.COM

if __name__ == "__main__":
    robotIp = "127.0.0.1"
    main(robotIp)

#mas info
    #http://doc.aldebaran.com/1-14/naoqi/motion/control-cartesian.html
