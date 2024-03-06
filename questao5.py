def inverter_string(string):
    inverted_string = ""
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]
    return inverted_string

minha_string = "lanadelrey"

string_invertida = inverter_string(minha_string)

print("String original:", minha_string)
print("String invertida:", string_invertida)