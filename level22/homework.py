def str_to_int(characters):
    chars = "ABCDEFGHIKLMNOPQRSTVXYZabcdefghijklmnopqrstuvwxyz!@$%^&*()+#"
    nums = ""

    if characters[0] == "-" and len(characters) == 1:
        return "invalid input"

    for i in characters:
        if i in chars:
            return "invalid input"
        else:
            nums = nums + i

    return int(nums)

num1 = input("enter characters: ")
print(str_to_int(num1))