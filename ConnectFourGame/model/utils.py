def get_input_from_range(lower_number, higher_number):
    if lower_number > higher_number:
        raise Exception

    while True:
        try:
            number = int(input())
        except ValueError:
            print(f"Enter valid number from range {lower_number} to {higher_number}")
        else:
            if lower_number <= number <= higher_number:
                return int(number)
            else:
                print(f"Enter valid number from range {lower_number} to {higher_number}")

