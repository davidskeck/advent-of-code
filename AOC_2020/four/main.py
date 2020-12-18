def main():
    passportDictionary = {
        "byr": "req",
        "iyr": "req",
        "eyr": "req",
        "hgt": "req",
        "hcl": "req",
        "ecl": "req",
        "pid": "req",
        "cid": "opt"
    }

    validEyeColors = [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth"
    ]

    input_data = []
    with open("input.txt") as input:
        for line in input:
            input_data.append(line.strip())

    passports = []
    thisPassport = {}
    for line in input_data:
        if line != '':
            fields = line.split()
            for field in fields:
                key, value = field.split(':')
                thisPassport[key] = value
        else:
            passports.append(thisPassport)
            thisPassport = {}
    
    valid_passports = []
    invalid_passports = []
    for passport in passports:
        passportOK = True
        for key in passportDictionary:
            if passportDictionary[key] == "req":
                if key not in passport:
                    passportOK = False
                    break
        
        if passportOK:
            valid_passports.append(passport)
        else:
            invalid_passports.append(passport)

    print("Number of valid passports (p1): {}".format(len(valid_passports)))

    valid_passports = []
    invalid_passports = []
    for passport in passports:
        passportOK = True
        for key in passportDictionary:
            if passportDictionary[key] == "req" and passportOK:
                if key in passport:
                    valueOK = True
                    value = passport[key]
                    if key == "byr":
                        valueOK = value.isdigit() and 1920 <= int(value) <= 2002
                    elif key == "iyr":
                        valueOK = value.isdigit() and 2010 <= int(value) <= 2020
                    elif key == "eyr":
                        valueOK = value.isdigit() and 2020 <= int(value) <= 2030
                    elif key == "hgt":
                        unit = value[-2:]
                        if unit == "in":
                            valueOK = 59 <= int(value[:-2]) <= 76
                        elif unit == "cm":
                            valueOK = 150 <= int(value[:-2]) <= 193
                        else:
                            valueOK = False
                    elif key == "hcl":
                        try:
                            valueOK = value[0] == '#' and len(value[1:]) == 6 and int(value[1:], 16)
                        except ValueError:
                            valueOK = false
                    elif key == "ecl":
                        valueOK = value in validEyeColors
                    elif key == "pid":
                        valueOK = len(value) == 9 and value.isdigit()

                    if not valueOK:
                        passportOK = False
                        break
                else:
                    passportOK = False
                    break
        
        if passportOK:
            valid_passports.append(passport)
        else:
            invalid_passports.append(passport)

    print("Number of valid passports (p2): {}".format(len(valid_passports)))


if __name__ == "__main__":
    main()

