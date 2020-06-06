# Matthew Hopwood
# EDF Project
# Finding optimum Bypass ratio for max thrust - efficiencies assumed

import matplotlib.pyplot as plt
import isentropic as isn
import Turbojet as tj

# Assume Ideal Expansion
# Ambient Conditions for Sea Level
Pa = 101325
Ta = 300

# Additional Givens
M1 = 0.1711
To5 = 1500  # Tmax
hc = 45752000  # j/kg  --  of butane
y1 = 1.4  # inlet and comp
y2 = 1.35  # burner and turbine and nozzle
R = 287  # J/kgK
fst = 0.06
cp1 = R / (1 - (1 / y1))
cp2 = R / (1 - (1 / y2))

# Efficiencies/ratios
nd = 0.9
nc = 0.9
rc = 1.5
nb = 0.98
rb = 0.97
nt = 0.92
nn = 0.98

# Initialize iterators/ other variables
delta = 0.01
rc_list = [0]
I_array = [0]
TSFC_array = [0]
nth_array = [0]
np_array = [0]
no_array = [0]
AoAs_array = [0]

print("Walk Through")

while rc <= 10:
    # Reset To4 = 1500
    To5 = 1500

    # Initial Conditions
    a1 = (y1 * R * Ta) ** 0.5
    v1 = M1 * a1

    # Inlet/Diffuser
    To2 = Ta * isn.T_ratio(M1, y1)
    To2s = tj.n1(nd, To2, Ta)
    Po2 = Pa * (To2s / Ta) ** (y1 / (y1 - 1))

    # Compressor
    Po3 = rc * Po2
    To3s = To2 * (rc ** ((y1 - 1) / y1))
    To3 = ((To3s - To2) / nc) + To2
    Wc_in = cp1 * (To3 - To2)

    # Air Straightener
    To4 = To3
    Po4 = Po3

    # Burner
    # Check if fb > fst
    fb = tj.fb_test(To4, To5, hc, cp2, nb)
    if fb > fst:
        print('burner Tmax change')
        fb = fst
        To5 = tj.newTo4(To4, hc, cp2, nb, fb)
    Po5 = Po4 * rb

    # Nozzle
    T6s = To5 / ((Po5 / Pa) ** ((y2 - 1) / y2))
    T6 = To5 - nn * (To5 - T6s)
    To6 = To5

    # Exit Calculations
    ae = (y2 * R * T6) ** 0.5
    Me = (((To6 / T6) - 1) * (2 / (y2 - 1))) ** 0.5
    ve = Me * ae

    # Specific Thrust, TSFC
    I = tj.I_ie(fb, ve, v1)
    TSFC = tj.TSFC(fb, ve, v1)

    # Efficiencies
    np = tj.np(I, v1, fb, ve)
    nth = tj.nth(fb, ve, v1, hc)
    no = tj.no(np, nth)

    # A/A*
    AoAs = isn.AoAs(Me, y2)

    # Add Values to arrays
    I_array.append(I)
    rc_list.append(rc)
    TSFC_array.append(TSFC)
    nth_array.append(nth)
    np_array.append(np)
    no_array.append(no)
    AoAs_array.append(AoAs)


    rc += delta

print(ve)

# Remove initial zero values
rc_list.pop(0)
I_array.pop(0)
TSFC_array.pop(0)
nth_array.pop(0)
np_array.pop(0)
no_array.pop(0)
AoAs_array.pop(0)

# I vs rc
plt.plot(rc_list, I_array)
plt.suptitle('I vs rc')
plt.xlabel('rc')
plt.ylabel('I')
plt.show()

'''
# TSFC vs rc
plt.plot(rc_list, TSFC_array)
plt.suptitle('TSFC vs rc')
plt.xlabel('rc')
plt.ylabel('TSFC')
plt.show()
'''

'''
# np, nth, no vs rc
plt.plot(rc_list, nth_array, label='nth', linestyle='dashed', color='red')
plt.plot(rc_list, np_array, label='np', linestyle='dashed', color='green')
plt.plot(rc_list, no_array, label='no', color='blue')
plt.suptitle('nth, np, & no vs rc')
plt.xlabel('rc')
plt.ylabel('Efficiencies')
plt.legend()
plt.show()
'''

'''
# A/A* vs rc
plt.plot(rc_list, AoAs_array)
plt.suptitle('A/A* vs rc')
plt.xlabel('rc')
plt.ylabel('A/A*')
plt.show()
'''