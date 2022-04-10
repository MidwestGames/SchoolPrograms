from math import sqrt

gamma = 1.4
#——————
# Input M and T
#——————
Min = float(input("What is the Mach Number in >> "))
Tin = float(input("What is the temperature in >> "))
#--------

machNoInSquared = Min**2

T0in = Tin * (1. + .2 * machNoInSquared)
T0star = T0in * (5.+7. * machNoInSquared)**2 / (120. * machNoInSquared + 24. * machNoInSquared * machNoInSquared) 
T0max = T0star - T0in

print("The flow will choke at T = %7.4f" %(round(T0max,1)))

#——————
# Input Del T0
#——————
deltaT0 = float(input(" ENTER Del T0 "))
temperatureRatio = (T0in + deltaT0) / T0star

b = 1. - gamma * (temperatureRatio - 1.) # b > 0
c = temperatureRatio
a = gamma**2 * (temperatureRatio - 1.) + 1. # a > 0 if Tr > 1.-1./gamma**2 

machNoExitSquaredSub = b / a - b / a * sqrt(1. - c * a / b**2)
machNoExitSub = sqrt(machNoExitSquaredSub)

if(a > 0.):
    machNoExitSquaredSup = b / a + b / a * sqrt(1. - c * a / b**2)
    machNoExitSup = sqrt(machNoExitSquaredSup)
else:
    machNoExitSup = 0. # just for printing 
    
print("Subsonic exit Mach Number = %6.4f\nSupersonic exit Mach Number = %7.4f" %(machNoExitSub, machNoExitSup))