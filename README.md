# Minor Delays

A simple python project which gets London Tube statuses from the tfl.gov.uk API and sends an email with the status info for specified lines of interest.

## main.py

main.py takes sysarg variables (lines for which status is wanted), parses them to a list, passes this list to the TFL() class, and sends an email to a specified email account, from a further specified email account.

## morning_tubes.sh

shell script (for cron job) which gets tube statuses for my own lines of interest
