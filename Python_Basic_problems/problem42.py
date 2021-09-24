#Gravitational Force (F) = (G*m1*m2)/r**2
# G = 6.67 * 10**(-11)Nm^2
m1 = float(input("enter the mass of 1st object:"))
m2 = float(input("enter the mass of 2nd object:"))
r = float(input("enter the radius:"))
G = 6.67 *(10**-11)
force = (G * m1 * m2)/r**2
print("Gravitational Force = ",round(force,2), "N")


