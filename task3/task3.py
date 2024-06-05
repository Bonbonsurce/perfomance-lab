import json
import sys


def process_tests(tests, values):
    for test in tests:
        for value in values['values']:
            if value['id'] == test['id']:
                test['value'] = value['value']

        if 'values' in test:
            process_tests(test['values'], values)


values_path = sys.argv[1]
tests_path = sys.argv[2]
report_path = sys.argv[3]

with open(values_path, 'r') as f:
    values_data = json.load(f)

with open(tests_path, 'r') as f:
    tests_data = json.load(f)

report = {"tests": tests_data['tests']}

process_tests(report['tests'], values_data)

with open(report_path, 'w') as f:
    json.dump(report, f, indent=2)
