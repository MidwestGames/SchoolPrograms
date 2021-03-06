from calendar import c
from re import M
import numpy
import scipy.optimize as spo
from math import degrees, radians, sqrt, tan, asin, sin, atan, pow

choice = int(input(("Aer E 311 Calculator\n1 - Isentropic Ratio Calculator\n2 - Normal Shock Calculator\n3 - Oblique Shock Calculator\n4 - Prandtl-Meyer Function Solver\n5 - Prandtl-Meyer Value Calculator\nWhat type of calculator do you need >> ")))
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
def Isentropic_AR(machNo):
    areaRatio = (1/machNo**2) * ( (5/6) * (1 + (1/5) * machNo**2) ) ** 6
    return areaRatio
def PMFNu(M):
    PMF = sqrt(6.) * atan(sqrt((M**2 - 1) / 6.)) - atan(sqrt(M**2 - 1.))
    return PMF

def PR2M(R):
    M = sqrt(5 * pow(R, 2/7) - 5)
    return M
def pR2M(R):
    M = sqrt(5 * pow(R, 2/5) - 5)
    return M
def TR2M(R):
    M = sqrt(5 * R - 5)
    return M

def Calulator(number):
    match number:
        case 1:
            knownRatio = float(input("1 -- Mach Number\n2 -- P0/P\n3 -- p0/p\n4 -- T0/T\n5 -- A/A*\nWhat constant number do you have >> "))

            match knownRatio:
                case 1: #Mach Number
                    machNumber = float(input("What is the Mach number >> "))

                    pressureRatio = Isentropic_PR(machNumber)
                    densityRatio = Isentropic_pR(machNumber)
                    temperatureRatio = Isentropic_TR(machNumber)
                    areaRatio = Isentropic_AR(machNumber)

                case 2: #Pressure Ratio
                    pressureRatio = 1/float(input("What is the pressure ratio >> "))

                    #Solve for Mach Number
                    machNumber = PR2M(pressureRatio)

                    #Solve for other ratios
                    densityRatio = Isentropic_pR(machNumber)
                    temperatureRatio = Isentropic_TR(machNumber)
                    areaRatio = Isentropic_AR(machNumber)

                case 3: #Density Ratio
                    densityRatio = 1/float(input("What is the density ratio >> "))

                    #Solve for Mach Number
                    machNumber = pR2M(densityRatio)

                    #Solve for other ratios
                    temperatureRatio = Isentropic_TR(machNumber)
                    areaRatio = Isentropic_AR(machNumber)
                    pressureRatio = Isentropic_PR(machNumber)

                case 4: #Temperature Ratio
                    temperatureRatio = 1/float(input("What is the temperature ratio >> "))

                    #Solve for Mach Number
                    machNumber = TR2M(temperatureRatio)
                    
                    #Solve for other ratios
                    pressureRatio = Isentropic_PR(machNumber)
                    densityRatio = Isentropic_pR(machNumber)                   
                    areaRatio = Isentropic_AR(machNumber)

                case 5: #Area Ratio
                    areaRatio = float(input("What is the area ratio >> "))

                    #TODO
                    #Solve for Mach Number
                    def A2M(machNo):
                        xx = ((5+machNo**2)**3 / (216 * machNo))
                        return xx - areaRatio
                    
                    machNumberSub = float(spo.fsolve(A2M, 0.1))
                    machNumberSup = float(spo.fsolve(A2M, 1.1))

                    #Solve for other ratios
                    pressureRatioSub = Isentropic_PR(machNumberSub)
                    densityRatioSub = Isentropic_pR(machNumberSub)
                    temperatureRatioSub = Isentropic_TR(machNumberSub)

                    pressureRatioSup = Isentropic_PR(machNumberSup)
                    densityRatioSup = Isentropic_pR(machNumberSup)
                    temperatureRatioSup = Isentropic_TR(machNumberSup)

                    print("Subsonic Conditions")
                    print("Mach Number M = %.4f" %(machNumberSub))
                    print("Pressure Ratio P0/P1 = %.4f" %(pressureRatioSub))
                    print("Density Ratio p0/p1 = %.4f" %(densityRatioSub))
                    print("Temperature Ratio T0/T1 = %.4f" %(temperatureRatioSub))
                    print("Area Ratio = %.4f\n" %(areaRatio))

                    print("Supersonic Conditions")
                    print("Mach Number M = %.4f" %(machNumberSup))
                    print("Pressure Ratio P0/P1 = %.4f" %(pressureRatioSup))
                    print("Density Ratio p0/p1 = %.4f" %(densityRatioSup))
                    print("Temperature Ratio T0/T1 = %.4f" %(temperatureRatioSup))
                    print("Area Ratio = %.4f\n" %(areaRatio))

                    return 0

            print("Mach Number M = %.4f" %(machNumber))
            print("Pressure Ratio P0/P1 = %.4f" %(pressureRatio))
            print("Density Ratio p0/p1 = %.4f" %(densityRatio))
            print("Temperature Ratio T0/T1 = %.4f" %(temperatureRatio))
            print("Area Ratio = %.4f\n" %(areaRatio))

            return 0
        case 2:
            M1 = float(input("What is the upstream Mach number >> "))
            #This calculates the Ratios given a Mach number
            pressureRatio = NormalShock_PR(M1)
            densityRatio = NormalShock_pR(M1)
            temperatureRatio = NormalShock_TR(pressureRatio, densityRatio)

            print("Pressure Ratio P2/P1 = %.4f" %(pressureRatio))
            print("Density Ratio p2/p1 = %.4f" %(densityRatio))
            print("Temperature Ratio T2/T1 = %.4f" %(temperatureRatio))

            #Calculate the downstream Mach number
            M2 = sqrt( (5 + (M1**2) ) / ( 7 * (M1**2) - 1) )

            print("Downstream Mach number = %.2f\n" %(M2))

            return 0
        case 3:

            #This part finds beta-----------------------------------
            M1 = float(input("What is the Mach number of the leading edge >> "))
            theta = radians(float(input("What is the deflection angle of the shock >> ")))

            def fb(beta):
                Mn1 = M1 * sin(beta)
                rho12 = (5 / Mn1**2 + 1) / 6
                xx = beta - atan(rho12 * tan(beta))
                return xx - theta
            beta = float(spo.fsolve(fb, asin(1./M1)))

            print("Beta = %.3f degrees" %(degrees(beta)) )

            #This part finds the different ratios-------------------
            Mn1 = M1 * sin(beta)

            pressureRatio = ObliqueShock_PR(M1, beta)
            densityRatio = ObliqueShock_pR(M1, beta)
            temperatureRatio = ObliqueShock_TR(pressureRatio,densityRatio) 

            print("Pressure Ratio P2/P1 = %.4f" %(pressureRatio))
            print("Density Ratio p2/p1 = %.4f" %(densityRatio))
            print("Temperature Ratio T2/T1 = %.4f" %(temperatureRatio))

            #This part calculates the downstream Mach number
            Mn2 = sqrt( ( 1 + 0.2 * (Mn1**2) ) / ( 1.4 * (Mn1**2) - 0.2 ) )
            M2 = Mn2 / sin(beta - theta)

            print("Downstream Mach number = %.2f\n" %(M2))
            return 0
        case 4:

            M1 = float(input("What is the Mach number of the leading edge >> "))
            theta = float(input("What is the deflection angle of the shock >> "))
            #This finds M2 from root function
            def Nu(M):
                PMF = sqrt(6.0) * atan(sqrt((M**2 - 1.0) / 6.0)) - atan(sqrt(M**2 - 1.0))
                return PMF - nu2
            nu2 = 0.0
            nu1 = Nu(M1)
            nu2 = nu1 + (theta * numpy.pi/180)

            M2 = float(spo.fsolve(Nu, M1))

            print("Nu 1 = %.4f" %(nu1))
            print("Nu 2 = %.4f\n" %(nu2))

            print("Downstream Mach Number = %.5f" %(M2))

            #This finds the ratios needed

            temperatureRatio = Isentropic_TR(M1) / Isentropic_TR(M2)
            pressureRatio = Isentropic_PR(M1) / Isentropic_PR(M2)
            pressureRatio01 = Isentropic_PR(M1)
            temperatureRatio01 = Isentropic_TR(M1)
            pressureRatio02 = Isentropic_PR(M2)
            temperatureRatio02 = Isentropic_TR(M2)

            print("Temperature Ratio T2/T1 = %.4f" %(temperatureRatio))
            print("Pressure Ratio P2/P1 = %.4f\n" %(pressureRatio))
            print("Temperature Ratio T0/T1 = %.4f" %(temperatureRatio01))
            print("Pressure Ratio P0/P1 = %.4f\n" %(pressureRatio01))
            print("Temperature Ratio T0/T2 = %.4f" %(temperatureRatio02))
            print("Pressure Ratio P0/P2 = %.4f\n" %(pressureRatio02))
            #Calculate Forward and Rearward Mach Lines

            FML = asin(1 / M1)
            RML = asin(1 / M2)

            print("Forward Mach Line = %.2f" %(degrees(FML)))
            print("Rearward Mach Line = %.2f\n" %(degrees(RML)))

            return 0
        case 5:
            M = float(input("What is the Mach Number given >> "))
            nu = PMFNu(M)
            print("Nu = %.4f rad" %(nu))
            print("Nu = %.4f deg" %(degrees(nu)))

            return 0

more = 1
while(more == 1):
    Calulator(choice)
    more = int(input("Do you wish to continue using the calculator 1-yes, else-no >> "))
    if(more == 1) :
        choice = int(input(("Aer E 311 Calculator\n\
        1 - Isentropic Ratio Calculator\n\
        2 - Normal Shock Calculator\n\
        3 - Oblique Shock Calculator\n\
        4 - Prandtl-Meyer Function Solver\n\
        5 - Prandtl-Meyer Value Calculator\n\
        What type of calculator do you need >> ")))