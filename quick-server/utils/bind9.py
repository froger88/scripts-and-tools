#!/usr/bin/env python2.7

import sys

def configure_local_ip():
    print "enter your machine global ip:"
    ip = sys.stdin.readline().rstrip()
    return "@\tIN\tA\t%s\n" % ip

def add_dns():
    ans = "y"
    ret = ""
    
    while ans.startswith("y"):
        print "add DNS server for domain? (Y/n): "
        ans = sys.stdin.readline()
        if ans.startswith("y"):
            print "enter your DNS server >> dns1.example.com. <<: "
            dns = sys.stdin.readline().rstrip()
            print "rev-dns name for this entry: >> dns1 <<: "
            revdns = sys.stdin.readline().rstrip()
            print "rev-dns IP for this entry >> global IP for localhost <<: "
            revip = sys.stdin.readline().rstrip()
            ret += "@\tIN\tNS\t%s\n" % dns
            ret += "%s\tIN\tA\t%s\n" % (revdns, revip)
        else:
            break
    return "%s\n" % ret

def add_mx():
    ans = "y"
    ret = ""
    cntr = 10
    
    while ans.startswith("y"):
        print "add MX server for domain? (Y/n): "
        ans = sys.stdin.readline()
        if ans.startswith("y"):
            print "enter your MX server >> mail.example.com. <<: "
            mx = sys.stdin.readline().rstrip()
            ret += "@\tIN\tMX\t%d\t%s\n" % (cntr, mx)
            cntr += 10
        else:
            break
    return "%s\n" % ret
    
def configure_soa():
    print "@ IN SOA >> dns1.example.com. <<: "
    soa1 = sys.stdin.readline().rstrip()
    print "SOA root >> root.example.com. <<: "
    soa2 = sys.stdin.readline().rstrip()

    ret_str = "@ IN SOA %s %s (\n" % (soa1, soa2)
    return ret_str
    
    
def configure_serial():
     print "unique serial in YYYYMMDDVV >> 2013091101 << :"
     serial = sys.stdin.readline().rstrip()

     ret_str = "%s\t;; serial\n1H\t;; refresh\n1H\t;; retry\n7D\t;; expire\n1D\t;; TTL\n)\n" % serial
     return ret_str

def configure_ttl():
    print "enter TTL >> 86400 <<: "
    ttl = sys.stdin.readline().rstrip()
    return "$TTL %s\n" % ttl
    
def install():
    ret_file = ""
    ret_file += configure_ttl()
    ret_file += configure_soa()
    ret_file += configure_serial()
    ret_file += configure_local_ip()
    ret_file += add_dns()

    print ret_file