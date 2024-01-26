def check(mapping):
    mapVal = set()

    for value in mapping.values():
        if value in mapVal:
            return False

        mapVal.add(value)
    return True

fungsi_mapping = {
    "a" : 2,
    "b" : 1,
    "c" : 3
}

if check(fungsi_mapping):
    print("Fungsi Satu-satu")
else:
    print("Bukan fungsi satu satu")