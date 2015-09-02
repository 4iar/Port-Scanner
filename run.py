from port_scanner import PortScanner, Target
import argparse
import sys



port_scanner = PortScanner()

parser = argparse.ArgumentParser(description='Port scanner')

parser.add_argument('ip', type=str)
parser.add_argument('--list-scan-techniques', action='store_true')
#parser.add_argument('-p', '--port', dest='ports', nargs='+', default=[], help='Port list separated by spaces')
parser.add_argument('ports', nargs='+', type=int)

args = parser.parse_args()

if args.list_scan_techniques:
    for s in port_scanner.scan_techniques:
        s = s(None)
        print(str.format("{}: {}", s.name, s.description))
    sys.exit()


scan_technique = port_scanner.scan_techniques['TCP Full Connect']
port_scanner.enqueue_scan(Target(args.ip, args.ports), scan_technique)
port_scanner.process_scan_queue()
print(port_scanner.scan_queue[0].results)

print(args)
