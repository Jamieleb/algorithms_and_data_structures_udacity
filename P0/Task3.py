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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
from re import search

def get_number_prefix(phone_number):
    if phone_number[0] == '(':
        return search("\(\w+\)", phone_number)[0]
    elif phone_number[:3] == '140':
        return '140'
    elif ' ' in phone_number:
        return phone_number[:4]

def is_bangalore_number(number):
    return get_number_prefix(number) == '(080)'

def filter_record_on_index(filter_fn, index, records):
    return list(filter(lambda record: filter_fn(record[index]), records))

def filter_calls_by_caller(filter_fn, call_records):
    return filter_record_on_index(filter_fn, 0, call_records)

def filter_calls_by_receiver(filter_fn, call_records):
    return filter_record_on_index(filter_fn, 1, call_records)

def extract_called_area_codes(call_records):
    return [get_number_prefix(record[1]) for record in call_records]

def unique_sorted(ls):
    return sorted(set(ls))

def test():
    test_calls = [
        ['(080)1234123', '(080)1234567', 'time', 'duration'],
        ['(080)1234123', '(080)7654321', 'time', 'duration'],
        ['14012345678', '(080)7654321', 'time', 'duration'],
        ['8765 4321', '14012345678', 'time', 'duration'],
        ['8765 4321', '(080)7654321', 'time', 'duration'],
        ['(080)1234123', '7890 1234567', 'time', 'duration'],
    ]

    assert(get_number_prefix('(080)1234567') == '(080)')
    assert(get_number_prefix('140123456789') == '140')
    assert(get_number_prefix('7890 1234789') == '7890')
    assert(is_bangalore_number('(080)1234567') == True)
    assert(is_bangalore_number('1401234789') == False)
    assert(unique_sorted(extract_called_area_codes(test_calls)) == ['(080)', '140', '7890'])
    calls_from_bangalore = filter_calls_by_caller(is_bangalore_number, test_calls)
    assert(len(calls_from_bangalore) == 3)
    assert(len(filter_calls_by_receiver(is_bangalore_number, test_calls)) == 4)
    assert(unique_sorted(extract_called_area_codes(calls_from_bangalore)) == ['(080)', '7890'])

    print('All Tests Passed')

# test()

calls_from_bangalore = filter_calls_by_caller(is_bangalore_number, calls)
# Task A output
print("The numbers called by people in Bangalore have codes:")
for code in unique_sorted(extract_called_area_codes(calls_from_bangalore)):
    print(code)

# Task B output
total_calls_from_bangalore = len(calls_from_bangalore)
total_internal_bangalore_calls = len(filter_calls_by_receiver(is_bangalore_number, calls_from_bangalore))
percent = total_internal_bangalore_calls / total_calls_from_bangalore * 100
output = "{percent:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
print(output.format(percent = percent))
