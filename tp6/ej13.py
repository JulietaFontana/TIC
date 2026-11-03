import Utils

aprioriC1 = [0.14, 0.52, 0.34]
aprioriC2 = [0.25, 0.25, 0.5]
aprioriC3 = [0.12, 0.24, 0.14, 0.5]

M1 = [
    [0.50, 0.30, 0.20],
    [0.00, 0.40, 0.60],
    [0.20, 0.80, 0.00]
]

M2 = [
    [0.25, 0.25, 0.25, 0.25],
    [0.25, 0.25, 0.00, 0.50],
    [0.50, 0.00, 0.50, 0.00]
]

M3 = [
    [0.25, 0.15, 0.30, 0.30],
    [0.23, 0.27, 0.25, 0.25],
    [0.10, 0.40, 0.25, 0.25],
    [0.34, 0.26, 0.20, 0.20]
]
print("entropia A Priori",round(Utils.entropiaAPriori(aprioriC1),4))
print("entropia Posteriori",Utils.entropiasPosteriori(aprioriC1,M1))
print("entropia A Priori",round(Utils.entropiaAPriori(aprioriC2),4))
print("entropia Posteriori",Utils.entropiasPosteriori(aprioriC2,M2))
print("entropia A Priori",round(Utils.entropiaAPriori(aprioriC3),4))
print("entropia Posteriori",Utils.entropiasPosteriori(aprioriC3,M3))