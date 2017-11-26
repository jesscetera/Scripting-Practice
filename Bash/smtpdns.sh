#!/bin/bash
#
# Goal:
# When passed an IP address (IP1), test whether the server passes the below DNS checks:
#    - SMTP Banner Check
#	These two things should match each other:
#        - The hostname in the PTR record for IP1
#        - The hostname in the '220' SMTP banner at IP1
#    - SMTP DNS Resolution
#	The hostname reported in the '220' SMTP banner at IP1 should resolve to an IP address (we'll call this IP2)
#    - SMTP Reverse DNS Mismatch
#	These two things should match each other:
#        - The hostname in the PTR record for IP2
#        - The hostname in the '220' SMTP banner at IP2

# The script prints a human-friendly message pointing out any problems detected with these checks.
# If all checks are successful, exit 0. If any checks are failures, exit 1.

# Test against:
#     - 146.20.53.83
#    - 162.209.114.133

IP1=$1
fail=""
IP1_success=""
IP2_success=""

# SMTP Banner checks
IP1_unparsed_PTR=`dig +short -x $IP1`
IP1_PTR=${IP1_unparsed_PTR::-1}
IP1_banner=`sleep .1 | telnet $IP1 25 2>&1 | grep ^220 | awk '{print $2}'`

if [[ "$IP1_PTR" == "$IP1_banner" ]]; then
	IP1_success=$(expr $IP1_success + 1)
else
	fail=$(expr $fail + 1)
fi

#SMTP DNS Resolution
resolve=$IP1_banner
IP2=`dig +short $resolve`

#echo $resolve" resolves to IP "$IP2
#echo "PTR record is "$IP2_PTR

# Reverse DNS checks
IP2_unparsed_PTR=`dig +short -x $IP2`
IP2_PTR=${IP2_unparsed_PTR::-1}
IP2_banner=`sleep .1 | telnet $IP2 25 2>&1 | grep ^220 | awk '{print $2}'`

if [[ "$IP2_PTR" == "$IP2_banner" ]]; then
	IP2_success=$(expr $IP2_success + 1)
else
	fail=$(expr $fail + 1)
fi

# Final output, re success or fail.
if [[ "$fail" -eq 0 ]]; then
	echo "All SMTP DNS checks successful."
	echo
else
	echo "There are mismatches between the SMTP hostname and the PTR record. Make sure these match."
	echo
	echo "SMTP Banner: "$IP1_banner
	echo "PTR Record: "$IP1_PTR
	echo
	false
fi