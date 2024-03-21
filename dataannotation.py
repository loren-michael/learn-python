# this function takes text from the coding_qual_input.txt file and structures it into a dict
# it then creates a list of numbers fibbonaci style to determine what keys we can to get values for
# then it pulls the values for the numbers in the list and joins them together to form a message

def decode (words):
  lines = {}
  for line in words:
    line_strip = line.strip('\n')
    lines.update(dict([line_strip.split(" ")]))
  length = len(lines)
  end_numbers = []
  i = 1
  while i <= length:
    end_numbers.append(i)
    i += (len(end_numbers) + 1)
  message_list = []
  for num in end_numbers:
    word = lines.get(str(num))
    message_list.append(word)
    message = " ".join(message_list)
  print(message)

text = open('coding_qual_input.txt', 'r')
content = text.readlines()

decode(content)

text.close()

# these are two functions that needed to create staircase lists and sublists
# task was to determine which was correct

# def create_staircase_1(nums):
#   while len(nums) != 0:
#     step = 1
#     subsets = []
#     if len(nums) >= step:
#       subsets.append(nums[0:step])
#       nums = nums[step:]
#       step += 1
#     else:
#       return False
#   return subsets

def create_staircase_2(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
  return subsets

nums = [1, 2, 3, 4, 5, 6]

# output_1 = create_staircase_1(nums)
output_2 = create_staircase_2(nums)

# print("output 1", output_1)
print("output 2", output_2)
