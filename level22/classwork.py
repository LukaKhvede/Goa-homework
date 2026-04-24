def strtoint(num):
    digits = "0123456789"
    if num[0] == "-":
        if len(num) == 1:
            return "invalid Input"
    for ch in num:
        if ch not in digits:
            return "invalid Input"
    return int("-" + num) if "-" not in num else int(num)