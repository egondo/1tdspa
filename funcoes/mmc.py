def mmc(a: int, b: int) -> int:
    candidato = a
    while candidato % a != 0 or candidato % b != 0:
        candidato = candidato + 1
        
    return candidato

def mdc(a: int, b: int) -> int:
    candidato = a
    while a % candidato != 0 or b % candidato != 0:
        candidato = candidato - 1
    return candidato


a = 50
b = 24
resp = mmc(a, b)
print(f"MMC: {resp}")

resp = mdc(a, b)
print(f"MDC: {resp}")    