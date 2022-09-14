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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

from itertools import chain

def extract_phone_numbers_from_records(records):
    return list(chain(*[record[:2] for record in records]))

def get_unique_numbers(phone_numbers):
    return set(phone_numbers)

def test():
    test_texts = [
        ['1234', '4321', 'timestamp1'],
        ['4321', '7890', 'timestamp2'],
        ['1234', '12345678', 'timestamp3'],
    ]
    test_calls = [
        ['1234', '123456789', 'timestamp1', 'duration1'],
        ['123', '1234', 'timestamp2', 'duration2'],
        ['4321', '7890', 'timestamp3', 'duration3'],
    ]

    text_phone_numbers = extract_phone_numbers_from_records(test_texts)
    call_phone_numbers = extract_phone_numbers_from_records(test_calls)
    assert(text_phone_numbers == ['1234', '4321', '4321', '7890', '1234', '12345678'])
    assert(get_unique_numbers(text_phone_numbers) == set(['1234', '4321', '7890', '12345678']))
    assert(get_unique_numbers(call_phone_numbers) == set(['1234', '123456789', '123', '4321', '7890']))
    assert(len(get_unique_numbers(chain(text_phone_numbers, call_phone_numbers))) == 6)

    print('Tests Finished')

# test()

phone_numbers_set = get_unique_numbers(extract_phone_numbers_from_records(chain(texts, calls)))
print(f'There are {len(phone_numbers_set)} different telephone numbers in the records.')
