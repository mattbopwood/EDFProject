# Matthew Hopwood
# Turbojet.py
# Turbojet functions

# M = Mach number, y = gamma
def I(f, ve, v, Pe, Pa, ma, Ae):
    x = (1 + f) * ve - v + ((Pe - Pa) / ma) * Ae
    return x


def T(f, ve, v, Pe, Pa, ma, Ae):
    x = ma * ((1 + f) * ve - v + (Pe - Pa) * Ae)
    return x


# ideally expanded
def I_ie(f, ve, v):
    x = ((1 + f) * ve) - v
    return x


# ideally expanded
def T_ie(f, ve, v, ma):
    x = ma * ((1 + f) * ve - v)
    return x


def TSFC(f, ve, v):
    x = f / (((1 + f) * ve) - v)
    return x


# Thermal Efficiency
def nth(f, ve, v, hc):
    x = (((1 + f) * ve ** 2) - v ** 2) / (2 * f * hc)
    return x


# Propulsive Efficiency
def np(I, v, f, ve):
    x = I * v / (((1 + f) * (0.5 * ve ** 2)) - (0.5 * v ** 2))
    return x


# Total Efficiency
def no(np, nth):
    x = np * nth
    return x


# Temp efficiencies for Diffuser/Compressor (Finding To3s)
def n1(n, To3, To2):
    x = n * (To3 - To2) + To2
    return x


# Temp efficiencies for Turbine/Nozzle (Finding To5s)
def n2(n, To5, To4):
    x = To4 - ((To4 - To5) / n)
    return x


# Compare fb to fst
def fb_test(To3, To4, hc, cp, nb):
    x = ((To4 / To3) - 1) / (((nb * hc) / (cp * To3)) - (To4 / To3))
    return x


def newTo4(To3, hc, cp, nb, fb):
    x = (1 / (1 + fb)) * ((nb * hc / cp) + To3)
    return x


# f afterburner
def fab(f, To6, To5, nab, hc, cp):
    x = ((1 + f) * (To6 - To5)) / ((nab * hc / cp) - To6)
    return x
