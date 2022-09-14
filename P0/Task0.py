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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_text_record = texts[0]
last_call_record = calls[-1]
print(f'First record of texts, {first_text_record[0]} texts {first_text_record[1]} at time {first_text_record[2]}')
print(f'Last record of calls, {last_call_record[0]} calls {last_call_record[1]} at time {last_call_record[2]}, lasting {last_call_record[3]} seconds')
