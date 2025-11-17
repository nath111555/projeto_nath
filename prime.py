def is_prime(n: int) -> bool:
    """Verifica se um número é primo."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    num = 5
    print("Primo!" if is_prime(num) else "Não é primo.")
    num = 7
    print("Primo!" if is_prime(num) else "Não é primo.")
