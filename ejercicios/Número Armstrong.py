def is_armstrong(num: int) -> bool:
    digits = str(num)
    n = len(digits)
    return sum(int(d)**n for d in digits) == num