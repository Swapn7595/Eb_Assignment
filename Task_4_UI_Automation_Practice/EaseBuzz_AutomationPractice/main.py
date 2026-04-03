import os
import subprocess

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def run_tests_and_generate_allure_report():
    # Run pytest with Allure results directory
    pytest_command = [
        "pytest",
        "--alluredir=reports/allure-results",
        "-v",
        "-s"
    ]
    subprocess.run(pytest_command, check=True)

    # Generate Allure report
    allure_generate_command = [
        "allure",
        "generate",
        "reports/allure-results",
        "-o",
        "reports/allure-report",
        "--clean"
    ]
    subprocess.run(allure_generate_command, check=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_tests_and_generate_allure_report()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
