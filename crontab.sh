#Crontab contents:
#Crontab created Night of Monday March 24th. Should have 12 files collected by end of day Friday march 28th.

# Edit this file to introduce tasks to be run by cron.
#
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command
31 13 * * 1-5 cd /home/ubuntu/SP25_DS5111_rmd9ev && TIMESTAMP=$(date +"\%Y\%m\%d_\%H\%M") && make wsjgainers.csv && mv wsjgainers.csv wsjgainers_$TIMESTAMP.csv && rm -f wsjgainers.csv wsjgainers.html
31 13 * * 1-5 cd /home/ubuntu/SP25_DS5111_rmd9ev && TIMESTAMP=$(date +"\%Y\%m\%d_\%H\%M") && make ygainers.csv && mv ygainers.csv ygainers_$TIMESTAMP.csv && rm -f ygainers.csv ygainers.html
30 16 * * 1-5 cd /home/ubuntu/SP25_DS5111_rmd9ev && TIMESTAMP=$(date +"\%Y\%m\%d_\%H\%M") && make wsjgainers.csv && mv wsjgainers.csv wsjgainers_$TIMESTAMP.csv && rm -f wsjgainers.csv wsjgainers.html
30 16 * * 1-5 cd /home/ubuntu/SP25_DS5111_rmd9ev && TIMESTAMP=$(date +"\%Y\%m\%d_\%H\%M") && make ygainers.csv && mv ygainers.csv ygainers_$TIMESTAMP.csv && rm -f ygainers.csv ygainers.html
01 20 * * 1-5 cd /home/ubuntu/SP25_DS5111_rmd9ev && TIMESTAMP=$(date +"\%Y\%m\%d_\%H\%M") && make wsjgainers.csv && mv wsjgainers.csv wsjgainers_$TIMESTAMP.csv && rm -f wsjgainers.csv wsjgainers.html
01 20 * * 1-5 cd /home/ubuntu/SP25_DS5111_rmd9ev && TIMESTAMP=$(date +"\%Y\%m\%d_\%H\%M") && make ygainers.csv && mv ygainers.csv ygainers_$TIMESTAMP.csv && rm -f ygainers.csv ygainers.html


