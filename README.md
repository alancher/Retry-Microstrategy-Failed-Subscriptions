# Retry-Microstrategy-Failed-Subscriptions

## Goal
The goal is to retry Microstrategy subscriptions that have failed

## How to use it

Make a bat or sh that has:
python Main.py

Then schedule the bat/sh every hour. The script will check on the Microstrategy log file dsserrors.log the subscriptions that failed in the last hour and try to rerun them 
