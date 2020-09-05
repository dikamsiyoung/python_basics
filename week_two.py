#  Sequences
a_string = 'is an immutable sequence'
a_list = ['is', 'a', 'mutable', 'sequence', 'and']
a_tuple = ('is', 'a', 'sequence', 'but', 'immutable')


# Iterations
to_iterate = 'within a sting use a for loop'
to_iterate_words = 'in a string use'
the_split_command = to_iterate_words.split(' ')

for char in to_iterate:
    print(char)

for word in the_split_command:
    print(word)

count_items_using_accumulator = 0

for word in range(len(a_tuple)):
    count_items_using_accumulator += 1


