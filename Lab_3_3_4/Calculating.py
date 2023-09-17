a = 1.5 * 10 ** -3
L = 3 * 10 ** -3
l = 1.7 * 10 ** -3
R = 1.66
I = 0.5*10**-3
e = 1.6 * 10**-19
sigma_R = 0.01
rho = R * a * l / L
sigma = 1/rho/100
U_na_B = 0.00021478263248112623
n = I/(e*a*U_na_B)/10**6
mu = sigma/(e*n)

print(mu)
