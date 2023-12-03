# This Converts /proc/<PID>/net/tcp into readable text
import sys

def convert_ip_port_combo(combo):
    octet1 = str(int(combo[6:8], 16))
    octet2 = str(int(combo[4:6], 16))
    octet3 = str(int(combo[2:4], 16))
    octet4 = str(int(combo[0:2], 16))
    port = str(int(combo[-2:], 16))
    return(octet1 +"."+ octet2 +"."+ octet3 +"."+ octet4 + ":" + port)

def get_content(pid):
    file_name = "/proc/" + str(pid) + "/net/tcp"
    a = open(file_name, 'r')
    b = a.readlines()
    a.close()
    for i in range(len(b)-1):
        original_line = b[i+1][3:-2]
        split_line = b[i+1][:-2].split(" ")
        local_address = convert_ip_port_combo(split_line[4])
        foreign_address = convert_ip_port_combo(split_line[5])
        uid = split_line[11]
        print(original_line)
        print("Local address: " + local_address + "\nforeign address: " + foreign_address + "\nuid: " + uid + "\n\n")

for i in range(len(sys.argv)-1):
    get_content(sys.argv[i+1])
