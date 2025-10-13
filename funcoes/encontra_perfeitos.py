def perfeito(n: int) -> bool:
    soma = 0
    div = 1
    while div <= n // 2:
        if n % div == 0:
            soma = soma + div
        div = div + 1
    

    return soma == n


num = 1
while num <= 50_000:
    if perfeito(num):
        print(num)
    num = num + 1
