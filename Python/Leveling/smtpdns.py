#!/usr/bin/python
#
######### WORK IN PROGRESS #########
#

# Import
import sys, os, subprocess, sh

# Initialize Variables


# Script Body

# Grabs the IP supplied as a command line argument
IP1 = sys.argv[1]

# Looks up the hostname in the PTR record
IP1_PTR=sh.dig("-x", "+short", "%s"%(IP1))
print IP1_PTR


