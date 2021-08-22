
#Gear Functions
#Part of Monkey Butler 3
#fucking gears bro on law

import arcade
import math

def gearDraw(degrees,color, x, y):
    radius = 75
    degrees = degrees
    gearColor = color

    def getTheta(degrees):
        theta = degrees * ((math.pi)/180)
        return theta
    def getX(theta, radius):
        xOut = (math.cos(theta)*radius)+x
        return xOut
    def getY(theta, radius):
        yOut = (math.sin(theta)*radius)+y
        return yOut

    xOne = getX(getTheta(degrees-15),radius)
    yOne = getY(getTheta(degrees-15),radius)
    #arcade.draw_circle_filled(xOne,yOne,2,arcade.color.RED) #ONE

    xTwo = getX(getTheta(degrees+15),radius)
    yTwo = getY(getTheta(degrees+15),radius)
    #arcade.draw_circle_filled(xTwo,yTwo,2,arcade.color.PURPLE)#TWO

    xThree = getX(getTheta(degrees-12),radius+15)
    yThree = getY(getTheta(degrees-12),radius+15)
    #arcade.draw_circle_filled(xThree,yThree,2,arcade.color.WHITE)#THREE

    xFour = getX(getTheta(degrees+12),radius+15)
    yFour = getY(getTheta(degrees+12),radius+15)
    #arcade.draw_circle_filled(xFour,yFour,2,arcade.color.ORANGE)#FOUR

    point_list = ((xOne, yOne),
              (xTwo, yTwo),
              (xFour, yFour),
              (xThree, yThree))
    arcade.draw_polygon_filled(point_list, gearColor)


def gearPlace(degrees, gearColor, x,y):
    gearDraw(degrees,gearColor,x,y)
    gearDraw(degrees-45,gearColor,x,y)
    gearDraw(degrees-90,gearColor,x,y)
    gearDraw(degrees-135,gearColor,x,y)
    gearDraw(degrees-180,gearColor,x,y)
    gearDraw(degrees-225,gearColor,x,y)
    gearDraw(degrees-270,gearColor,x,y)
    gearDraw(degrees-315,gearColor,x,y)