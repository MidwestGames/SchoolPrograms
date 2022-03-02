import scipy.optimize as spo
from math import degrees, radians, sqrt, tan, asin, sin, atan

choice = int(input(("Aer E 311 Calculator\n\
1 - Isentropic Ratio Calculator\n\
2 - Normal Shock Calculator\n\
3 - Oblique Shock Calculator\n\
What type of calculator do you need >> ")))
#Formulas

def ObliqueShock_PR(machNo, beta):
    pressureRatio = (7/6) * (machNo**2) * (sin(beta)**2) - (1/6)
    return pressureRatio
def ObliqueShock_pR(machNo, beta):
    densityRatio = ( 2.4 * (machNo**2) * (sin(beta)**2) ) / ( 0.4 * (machNo**2) * (sin(beta)**2) + 2 )
    return densityRatio
def ObliqueShock_TR(pressureRatio, densityRatio):
    temperatureRatio = pressureRatio * densityRatio
    return temperatureRatio

def Calulator(number):
    match number:
        case 1:
            return 0
        case 2:
            return 0
        case 3:
            #This part finds beta-----------------------------------

            machNo = float(input("What is the Mach number of the leading edge >> "))
            theta = radians(float(input("What is the deflection angle of the shock >> ")))

            def fb(beta):
                Mn1 = machNo * sin(beta)
                rho12 = (5 / Mn1**2 + 1) / 6
                xx = beta - atan(rho12 * tan(beta))
                return xx - theta
            beta = float(spo.fsolve(fb, asin(1./machNo)))

            print("Beta = %.3f degrees" %(degrees(beta)) )
            #This part finds the different ratios-------------------

            upstreamMachNormal = machNo * sin(beta)

            pressureRatio = ObliqueShock_PR(machNo, beta)
            densityRatio = ObliqueShock_pR(machNo, beta)
            temperatureRatio = ObliqueShock_TR(pressureRatio,1/densityRatio) 

            print("Pressure Ratio P2/P1 = %.4f" %(pressureRatio))
            print("Density Ratio p2/p1 = %.4f" %(densityRatio))
            print("Temperature Ratio T2/T1 = %.4f" %(temperatureRatio))
            #This part calculates the downstream Mach number
            
            downstreamMachNormal = sqrt( ( 1 + 0.2 * (upstreamMachNormal**2) ) / ( 1.4 * (upstreamMachNormal**2) - 0.2 ) )
            downstreamMach = downstreamMachNormal / sin(beta - theta)

            print("Downstream Mach number = %.2f" %(downstreamMach))
            return 0


Calulator(choice) 