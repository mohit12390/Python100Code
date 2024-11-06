def translate(phrase):
    result = ""
    for word in phrase:
        if word in "AEIOUaeiou":
            result = result + "g"
        else:
            result = result + word
    return result

print(translate("dinkar"))