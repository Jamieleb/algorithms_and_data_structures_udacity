"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
from functools import reduce

def extract_index_from_list_of_lists(index, records):
    return [record[index] for record in records]

def union_of_two_sets(set1, set2):
    return set1.union(set2)

def check_for_telemarketers(call_records, text_records):
    all_callers = set(extract_index_from_list_of_lists(0, call_records))
    all_called_numbers = set(extract_index_from_list_of_lists(1, call_records))
    all_text_senders = set(extract_index_from_list_of_lists(0, text_records))
    all_text_receivers = set(extract_index_from_list_of_lists(1, text_records))

    non_telemarketers = reduce(union_of_two_sets, [all_called_numbers, all_text_receivers, all_text_senders])
    return all_callers.difference(non_telemarketers)

def test():
    test_calls = [
        ['(080)1234123', '(080)1234567', 'time', 'duration'],
        ['(080)1234123', '(080)7654321', 'time', 'duration'],
        ['14012345678', '(080)7654321', 'time', 'duration'],
        ['8765 4321', '(020)78934362', 'time', 'duration'],
        ['8765 4321', '(080)7654321', 'time', 'duration'],
        ['(080)1234123', '7890 1234567', 'time', 'duration'],
    ]

    test_texts = [
        ['(080)1234123', '(080)1234567', 'time'],
        ['(080)1234123', '(080)7654321', 'time'],
        ['8765 4321', '7890 123464328', 'time'],
        ['8765 4321', '(080)7654321', 'time'],
        ['(080)1234123', '7890 1234567', 'time'],
    ]

    all_callers = set(extract_index_from_list_of_lists(0, test_calls))
    assert(all_callers == set(['(080)1234123', '14012345678', '8765 4321']))
    all_called_numbers = set(extract_index_from_list_of_lists(1, test_calls))
    assert(all_called_numbers == set(['(080)1234567', '(080)7654321', '(020)78934362', '7890 1234567']))
    all_text_senders = set(extract_index_from_list_of_lists(0, test_texts))
    all_text_receivers = set(extract_index_from_list_of_lists(1, test_texts))

    non_telemarketers = reduce(union_of_two_sets, [all_called_numbers, all_text_receivers, all_text_senders])
    assert(non_telemarketers == set([
        '(080)1234567',
        '(080)7654321',
        '(020)78934362',
        '7890 1234567',
        '7890 123464328',
        '(080)1234123',
        '8765 4321',
    ]))
    possible_telemarketers = all_callers.difference(non_telemarketers)
    assert(possible_telemarketers == set(['14012345678']))
    assert(possible_telemarketers == check_for_telemarketers(test_calls, test_texts))
    print('All Tests Successful')

# test()

possible_telemarketers = sorted(check_for_telemarketers(calls, texts))
print("These numbers could be telemarketers: ")
for number in possible_telemarketers:
    print(number)
