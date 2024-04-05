def count_of_words(sentence):
  #Counts the occurrences of each word in a sentence.

  dict_a = {}

  # Check if the sentence is empty
  if not sentence:
      return dict_a  # Return empty dictionary for empty input

  for each_word in sentence.split():
    if each_word not in dict_a:
      dict_a[each_word] = 1
    else:
      dict_a[each_word] += 1

  return dict_a

# Example usage with empty input handling
sentence = input("Enter a sentence (or press Enter for empty input): ")
result = count_of_words(sentence)

if result:  # Print results only if the dictionary is not empty
  for key, value in result.items():
    pair = "{}: {}".format(key, value)
    print(pair)
else:
  print("Empty input. No words to count.")
