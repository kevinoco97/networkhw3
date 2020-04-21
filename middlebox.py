#!/usr/bin/env python3

from switchyard.lib.address import *
from switchyard.lib.packet import *
from switchyard.lib.userlib import *
import random
import time


def drop(percent):
    return random.randrange(100) < percent


def delay(mean, std):
    delay =random.gauss(mean, std)
    return delay if delay > 0 else 0


def switchy_main(net):

    my_intf = net.interfaces()
    mymacs = [intf.ethaddr for intf in my_intf]
    myips = [intf.ipaddr for intf in my_intf]


    # Uncomment this line after extracting random seed from params file
    # random.seed(random_seed)


    while True:
        gotpkt = True
        try:
            timestamp,dev,pkt = net.recv_packet()
            log_debug("Device is {}".format(dev))
        except NoPackets:
            log_debug("No packets available in recv_packet")
            gotpkt = False
        except Shutdown:
            log_debug("Got shutdown signal")
            break

        if gotpkt:
            log_debug("I got a packet {}".format(pkt))
            if dev == "middlebox-eth1":
                log_debug("Received from blastee")
                '''
                Received ACK
                send directly to blaster. Not dropping ACK packets!
                net.send_packet("middlebox-eth0", pkt)
                '''
            elif dev == "middlebox-eth0":
                log_debug("Received from blaster")
                """
                ## TODO 
                find if packet needs to dropped
                if not then find the delay and add the packet and other relevant details to a queue
                """
            else:
                log_debug("Oops :))")

        """
        ##TODO
        process the queue
        """

    net.shutdown()
