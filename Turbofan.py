# Matthew Hopwood
# Turbofan.py
# Turbofan functions

def T(mac, mah, v, vec, veh, P, Pec, Peh, Aec, Aeh, f):
    x = mac * (vec - v) + mah((1 + f) * veh - v) + (Peh - P) * Aeh + (Pec - P) * Aec
    return x


def I(f, B, v, veh, vec):
    x = ((1 + f) * veh - v) + B * (vec - v)
    return x


def TSFC(f, B, v, veh, vec):
    x = f / ((1 + f) * veh - v + B * (vec - v))
    return x


# Thermal Efficiency
def nth(f, B, v, vec, veh, hc):
    x = (((1 + f) * (veh ** 2) - (v ** 2)) + (B * (vec ** 2 - v ** 2))) / (2 * f * hc)
    return x


# Propulsive Efficiency
def np(B, f, v, veh, vec):
    x = 2 * v * (((1 + f) * veh - v) + B * (vec - v)) / (((1 + f) * veh ** 2 - v) + B * (vec ** 2 - v ** 2))
    return x



# Total Efficiency
def no(np, nth):
    x = np * nth
    return x
