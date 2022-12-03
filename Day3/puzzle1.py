"""
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp,
which means its first compartment contains the items vJrwpWtwJgWr,
while the second compartment contains the items hcsFMMfFFhFp.
The only item type that appears in both compartments is lowercase p.

The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL.
The only item type that appears in both compartments is uppercase L.

The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.

The fourth rucksack's compartments only share item type v.

The fifth rucksack's compartments only share item type t.

The sixth rucksack's compartments only share item type s.


To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.


In the above example, the priority of the item type that appears in both compartments of each rucksack is
16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
"""


def determine_value(char : str) -> int:
    """Converts a character to a value.

    Args:
        char (str): a-z or A-Z

    Returns:
        int: an integer value 1-52
    """
    value = 0
    if 'a' <= char <= 'z':
        # Get the ascii value and transpose it to 1-26
        value = ord(char) - 96
    elif 'A' <= char <= 'Z':
        # Get the ascii value and transpose it to 27-52
        value = ord(char) - 38

    return value


if __name__ == '__main__':
    # Read the file line by line and clean \n
    backpacks = []
    with open('Day3/backpacks.txt') as file:
        [backpacks.append(line.strip()) for line in file.readlines()]

    # Go through each backpack and add the value of items found in both compartments.
    sum_of_value = 0
    for pack in backpacks:
        # Determine the middle of the pack and split it into compartments.
        split = int(len(pack) / 2)
        compartment_1, compartment_2 = pack[:split], pack[split:]

        # Go through each item in compartment_1 and check if a double can be found
        # in compartment_2. If it can add the value of the item to the sum and break.
        for char in compartment_1:
            if char in compartment_2:
                sum_of_value += determine_value(char)
                break

    print(sum_of_value)