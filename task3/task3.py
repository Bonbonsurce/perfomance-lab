import json


def process_tests(tests, values):
    for test in tests:
        for value in values['values']:
            if value['id'] == test['id']:
                test['value'] = value['value']

        if 'values' in test:
            process_tests(test['values'], values)


values_path = input()
tests_path = input()
report_path = input()

with open(values_path, 'r') as f:
    values_data = json.load(f)

with open(tests_path, 'r') as f:
    tests_data = json.load(f)

report = {"tests": tests_data['tests']}

process_tests(report['tests'], values_data)

with open(report_path, 'w') as f:
    json.dump(report, f, indent=2)
