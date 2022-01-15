#! /bin/python3
import math

if __name__ == "__main__":
    AB = float(input())
    BC = float(input())
    AC = (AB**2 + BC**2)**(1/2)
    CM = AC/2
    anguloC = math.atan(AB/BC) #Está en radianes
    BM = (BC**2 + CM**2 -2*BC*CM*math.cos(anguloC))**(1/2)
    theta_r = math.asin( math.cos(anguloC)*CM/BM )
    theta = math.degrees(theta_r)
    print(theta)
    theta = round(theta)
    print(str(theta) + chr(176))