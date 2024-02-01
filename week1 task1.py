def validate_weight(weight):
    try:
        weight = float(weight)
        if 20 <= weight <= 150:  # Adjust the range based on your validation rules
            return True
        else:
            print("Invalid weight! Weight should be between 20 and 150 kilograms.")
            return False
    except ValueError:
        print("Invalid input! Please enter a valid weight.")
        return False

def main():
    num_pupils = 30
    weight_threshold = 2.5

    # Initialize arrays
    names = []
    weights_first_day = []
    weights_last_day = []
    weight_differences = []

    # Input and validate data for each pupil on the first day
    print("Input weights for the first day:")
    for i in range(num_pupils):
        name = input(f"Enter the name of pupil {i + 1}: ")
        weight = input(f"Enter the weight of pupil {name} on the first day: ")

        while not validate_weight(weight):
            weight = input(f"Enter a valid weight for pupil {name} on the first day: ")

        names.append(name)
        weights_first_day.append(float(weight))

    # Input and validate data for each pupil on the last day
    print("\nInput weights for the last day:")
    for i in range(num_pupils):
        weight = input(f"Enter the weight of pupil {names[i]} on the last day: ")

        while not validate_weight(weight):
            weight = input(f"Enter a valid weight for pupil {names[i]} on the last day: ")

        weights_last_day.append(float(weight))

    # Calculate and store the difference in weight for each pupil
    for i in range(num_pupils):
        difference = weights_last_day[i] - weights_first_day[i]
        weight_differences.append(difference)

    # Output names, weights on the first day, weights on the last day, and differences
    print("\nResults:")
    for i in range(num_pupils):
        print(f"{names[i]} - First Day: {weights_first_day[i]} kg, Last Day: {weights_last_day[i]} kg, Difference: {weight_differences[i]} kg")

        if abs(weight_differences[i]) > weight_threshold:
            if weight_differences[i] > 0:
                print(f"  * Weight increase: {abs(weight_differences[i])} kg")
            else:
                print(f"  * Weight decrease: {abs(weight_differences[i])} kg")

if __name__ == "__main__":
    main()
