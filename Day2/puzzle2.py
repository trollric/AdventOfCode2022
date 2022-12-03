"""--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""


if __name__ == '__main__':
    # Open the file
    calory_array = []
    with open('Day1/calories.txt') as file:
        # Add the lines to an array cleaning the \n from the entries.
        [calory_array.append(line.replace('\n', '')) for line in file.readlines()]

    # Step through the lines and add until a blank line is found
    max_calories = 0
    temp_calories = 0
    for line in calory_array:
        if len(line) > 0:
            # If the line is not blank add the numbers a single elf carries.
            temp_calories += int(line)
        else:
            # If the line is blank test if the current elves total calories outweighs the previous
            # Top calories.
            if temp_calories > max_calories:
                max_calories = temp_calories

            # Reset temp_calories
            temp_calories = 0

    # Finally catch the last elf's in the list and check if he carries more calories.
    if temp_calories > max_calories:
        max_calories = temp_calories

    # Print the result.
    print(max_calories)