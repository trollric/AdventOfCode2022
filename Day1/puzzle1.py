"""
    
This list represents the Calories of the food carried by five Elves:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
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