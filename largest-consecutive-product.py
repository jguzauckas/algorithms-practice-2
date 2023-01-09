# You are given a 1,000 digit number in the txt file "large-number.txt".
# If we went through every set of four adjacent (consecutive) digits
# in the number, we'd find that the set 9, 9, 8, 9 has the highest
# product, that is
#   9 * 9 * 8 * 9 = 5832
# Your task is to find the set of 13 adjacent digits with the highest
# product (that is 13 consecutive numbers that multiply together to
# get the largest value).

# Your final result must be printed as a formatted sentence exactly
# the same as my answer in the answers.txt file.

with open("large-number.txt", "r") as my_file:
    number = my_file.readline()
