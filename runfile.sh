#!/bin/bash

# Start the first process
gunicorn app:app &

# Start the second process
bash startup &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
