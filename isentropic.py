# Matthew Hopwood
# Isentropic.py
# Isentropic relations functions

# M = Mach number, y = gamma
def T_ratio(M, y):
    x = (1 + .5 * (y - 1) * M ** 2)
    return x


def P_ratio(M, y):
    x = (1 + .5 * (y - 1) * M ** 2) ** (y / (y - 1))
    return x


def A_ratio(M, y):
    x = (1 + .5 * (y - 1) * M ** 2)
    return x


def AoAs(M, y):
    x = 1 / M * ((2 / (y + 1)) * (1 + ((y - 1) / 2) * M ** 2)) ** ((y + 1) / (2 * (y - 1)))
    return x
