def library_version_number(library): #this function verifies that the input is a number
    try:
        library_number = float(library)
        return library_number
    except:
        print(f"Unvalid library version for {library}")

    return False


def compare_library_version(version_1, version_2):
    number_1 = library_version_number(version_1) 
    number_2 = library_version_number(version_2)

    if number_1 and number_2:
        if number_2 > number_1:
            print(f"{number_2} is greater than {number_1}")

        elif number_2 < number_1:
            print(f"{number_2} is less than {number_1}")

        else: 
            print(f"{number_2} and {number_1} are equal")


compare_library_version("-1.1", "1.65")
compare_library_version("2a", "3")
compare_library_version("a", "b")
compare_library_version(None, None)
