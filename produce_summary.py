import glob, os

# Well, this is just crying out for function-ization.
day = 0

os.chdir(".")
# Find each .txt file in the program directory
for each_file in glob.glob("um-*.txt"):
    day += 1  # Increment the day.

    # Create 3 lists to hold each 'column'
    melons = []
    counts = []
    amounts = []

    print(f"Day {day}")
    # Open and read each text file
    the_file = open(each_file)
    for line in the_file:
        line = line.rstrip()  # Chop trailing whitespace
        words = line.split('|')  # Pipe is our data separation character

        melons.append(words[0])
        counts.append(words[1])
        amounts.append(words[2])

    the_file.close()  # Good practice to close the files you use.

    longest_melon = len(max(melons, key=len))
    padding = longest_melon + 1
    max_price_length = 8
    max_count_length = 4
    for ii in range(len(melons)):
        spaces = (padding - len(melons[ii])) * " "
        right_justify_money = (max_price_length - len(amounts[ii])) * " "
        right_justify_counts = (max_count_length - len(counts[ii])) * " "
        prepared_line = (
            f"Delivered{right_justify_counts}{counts[ii]}\t{melons[ii]}s{spaces}for a total of "
            f"{right_justify_money}${str(amounts[ii])}")
        print(prepared_line)
        report_width = len(prepared_line)
    daily_total = 0
    for zz in amounts:
        daily_total += float(zz)
    total_line = f"Total for the day: ${daily_total}\n\n"
    sum_lines_up_with_money = (report_width - len(total_line) + max_count_length) * " "
    print(sum_lines_up_with_money + total_line)
