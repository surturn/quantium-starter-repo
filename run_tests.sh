#!/bin/bash

#Activate venv
#use 'source venv/bin/activate' for MacOS/Linux
#use 'source venv/Scripts/activate' for Windows

source soulfoods/Scripts/activate

#Run the test suite
echo 'Running tests....'
pytest

#Capture the exit code
#$? special variable that hold the exit code of the Last comman run(pytest)
TEST_EXIT_CODE=$?

#Logic to Determine if tests passed or failed
if [$TEST_EXIT_CODE -eq 0];then
    echo 'All tests passed successfully!'
    exit 0
else
    echo 'Some tests failed. Please check the details above.'
    exit 1
fi