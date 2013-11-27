#!/usr/bin/python

import os, sys, time, signal, json, logging, traceback
import threading

import module_display as pB_display # Only events can manipulate the display stack
import module_audio as pB_audio # Add the audio module as it will only be manipulated from here in pyBus

# This module will read a packet, match it against the json object 'DIRECTIVES' below. 
# The packet is checked by matching the source value in packet (i.e. where the packet came from) to a key in the object if possible
# Then matching the Destination if possible
# The joining the 'data' component of the packet and matching that if possible.
# The resulting value will be the name of a function to pass the packet to for processing of sorts.

# THE MAJOR DIFFRENCE BETWEEN THIS DRIVER AND EVENT DRIVER:
# This one should manipulate the state data object and use that with
# a ticking thread to figure out what to do. So tick every .5 sec or 
# so and perform an action depending on the state data like skipping
# back or forward.

#####################################
# GLOBALS
#####################################
# directives list - maps function to src:dest:data
# first level of directives is filtering the src, so put in the integer representation of the src
# second level is destination
# third level is data : function name
DIRECTIVES = {
  '44' : {
    'BF' : {
      '7401FF' : 'd_keyOut'
    }
  },
  '80' : {
    'BF' : {
      'ALL' : 'd_custom_IKE' # Use ALL to send all data to a particular function
    }
  },
  '68' : {
    '18' : {
      '01'     : 'd_cdPollResponse',
      '380000' : 'd_cdSendStatus',
      '380100' : 'd_cdStopPlaying',
      '380300' : 'd_cdStartPlaying',
      '380A00' : 'd_cdNext',
      '380A01' : 'd_cdPrev',
      '380700' : 'd_cdScanForward',
      '380701' : 'd_cdScanBackard',
      '380601' : 'd_toggleSS', # 1 pressed
      '380602' : 'd_togglePause', # 2 pressed
      '380603' : 'd_cdChange3', # 3 pressed
      '380604' : 'd_cdChange4', # 4 pressed
      '380605' : 'd_update', # 5 pressed
      '380606' : 'd_RESET', # 6 pressed
      '380401' : 'd_cdScanForward',
      '380400' : 'd_cdScanBackard',
      '380800' : 'd_cdRandom',
      '380801' : 'd_cdRandom'
    }
  },
  '50' : {
    'C8' : {
      '01'   : 'd_RESET',
      '3B40' : 'd_RESET'
    }
  }
}


WRITER = None
LISTENER = None
STATE_DATA = {}
TICK = 0.5 # sleep interval in seconds used between iBUS reads

#####################################
# FUNCTIONS
#####################################
# Set the WRITER object (the iBus interface class) to an instance passed in from the CORE module
def init(writer):
  logging.info("In empty ticker")

# Manage the packet
def manage(packet):
  logging.info("In empty ticker")

def shutDown():
  logging.info("In empty ticker")

