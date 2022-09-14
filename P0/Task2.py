"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
from collections import defaultdict

def create_call_length_tally(call_records):
    call_length_dict = defaultdict(lambda: 0)

    for number1, number2, _, duration in call_records:
        call_length_dict[number1] += int(duration)
        call_length_dict[number2] += int(duration)

    return call_length_dict

def get_most_time_on_calls_from_tally(call_length_tally):
    largest_sum_of_calls = 0
    most_time_on_calls_number = None

    for number, duration in call_length_tally.items():
        if duration > largest_sum_of_calls:
            largest_sum_of_calls = duration
            most_time_on_calls_number = number

    return most_time_on_calls_number, largest_sum_of_calls

def test():
    test_calls = [
        ['1234', '123456789', 'timestamp1', '100'],
        ['123', '1234', 'timestamp2', '1000'],
        ['4321', '1234', 'timestamp3', '10000'],
    ]

    call_tally = create_call_length_tally(test_calls)
    print(call_tally)
    assert(call_tally['4321'] == 10000)
    assert(get_most_time_on_calls_from_tally(call_tally) == ('1234', 11100))

    print('Tests Finished')

# test()

phone_number, duration = get_most_time_on_calls_from_tally(create_call_length_tally(calls))
print(f"{phone_number} spent the longest time, {duration} seconds, on the phone during September 2016")
