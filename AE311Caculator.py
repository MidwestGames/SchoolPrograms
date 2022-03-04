from numpy import true_divide
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
    temperatureRatio = pressureRatio * (densityRatio**-1)
    return temperatureRatio
def NormalShock_PR(machNo):
    pressureRatio = ( 7 * (machNo**2) - 1 ) / 6
    return pressureRatio
def NormalShock_pR(machNo):
    densityRatio = ( 6 * (machNo**2) ) / ( 5 + (machNo**2) )
    return densityRatio
def NormalShock_TR(pressureRatio, densityRatio):
    temperatureRatio = pressureRatio * (densityRatio**-1)
    return temperatureRatio
def Isentropic_PR(machNo):
    pressureRatio = ( 1 + 0.2 * (machNo**2) ) ** (7/2)
    return pressureRatio
def Isentropic_pR(machNo):
    densityRatio = ( 1 + 0.2 * (machNo**2) ) ** (5/2)
    return densityRatio
def Isentropic_TR(machNo):
    temperatureRatio = ( 1 + 0.2 * (machNo**2) )
    return temperatureRatio

def Calulator(number):
    match number:
        case 1:
            machNo = float(input("What is the upstream Mach number >> "))

            #This calculates the Ratios given a Mach number
            pressureRatio = Isentropic_PR(machNo)
            densityRatio = Isentropic_pR(machNo)
            temperatureRatio = Isentropic_TR(machNo)

            print("Pressure Ratio P0/P1 = %.4f" %(pressureRatio))
            print("Density Ratio p0/p1 = %.4f" %(densityRatio))
            print("Temperature Ratio T0/T1 = %.4f" %(temperatureRatio))

            return 0
        case 2:
            machNo = float(input("What is the upstream Mach number >> "))
            #This calculates the Ratios given a Mach number
            pressureRatio = NormalShock_PR(machNo)
            densityRatio = NormalShock_pR(machNo)
            temperatureRatio = NormalShock_TR(pressureRatio, densityRatio)

            print("Pressure Ratio P2/P1 = %.4f" %(pressureRatio))
            print("Density Ratio p2/p1 = %.4f" %(densityRatio))
            print("Temperature Ratio T2/T1 = %.4f" %(temperatureRatio))

            #Calculate the downstream Mach number
            downstreamMach = sqrt( (5 + (machNo**2) ) / ( 7 * (machNo**2) - 1) )

            print("Downstream Mach number = %.2f" %(downstreamMach))

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
            temperatureRatio = ObliqueShock_TR(pressureRatio,densityRatio) 

            print("Pressure Ratio P2/P1 = %.4f" %(pressureRatio))
            print("Density Ratio p2/p1 = %.4f" %(densityRatio))
            print("Temperature Ratio T2/T1 = %.4f" %(temperatureRatio))

            #This part calculates the downstream Mach number
            downstreamMachNormal = sqrt( ( 1 + 0.2 * (upstreamMachNormal**2) ) / ( 1.4 * (upstreamMachNormal**2) - 0.2 ) )
            downstreamMach = downstreamMachNormal / sin(beta - theta)

            print("Downstream Mach number = %.2f" %(downstreamMach))
            return 0

more = 1
while(more == 1):
    Calulator(choice)
    more = int(input("Do you wish to continue using the calculator 1-yes, else-no >> ")) 