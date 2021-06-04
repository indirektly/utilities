from sys import argv
# I really dont want to do lexical analysis thus this is the minimal needed
# CopyWhoCares @ someone

# !!operators need to be in order!!
def simplify_operations(file_name, operators, out_file=0):
    with open(file_name, 'r') as obfus_vba_file:
        output = []
        for line in obfus_vba_file.read().split('\n'):
            original_line = line
            try:
                for unique_operator in operators:
                    if(unique_operator in line):
                        attempt = 0
                        stuck_loop = 0
                        while((unique_operator in line) and (stuck_loop == 0)):
                            # For edge cases where stuck loop exists on line
                            attempt += 1
                            if(attempt == 500):
                                stuck_loop = 1
                            location_of_unique_operator = line.find(unique_operator)
                            location_of_open = location_of_unique_operator - line[location_of_unique_operator::-1].find("(")
                            location_of_closed = location_of_unique_operator + line[location_of_unique_operator:].find(")")
                            parsed_xor_statement = line[location_of_open+1:location_of_closed].split(" ")
                            # Cases where parsed out "numbers" are other variables or Strings
                            try:
                                line = line[:location_of_open] + str(int(parsed_xor_statement[0]) ^ int(parsed_xor_statement[2])) + line[location_of_closed+1:]
                            except:
                                continue
                output.append("Original:\t" + original_line)            
                output.append("Modified:\t" + line + "\n")
            except Exception as e: 
                print(str(e) + "\n\n")
                print(str(line) + "\n\nVariables:\n")
                print("location_of_unique_operator: " + str(location_of_unique_operator))
                print("location_of_open: " + str(location_of_open))
                print("location_of_closed: " + str(location_of_closed))
                print("parsed_xor_statement: " + str(parsed_xor_statement))
                quit()
        obfus_vba_file.close()
        if(out_file == 0):
            for item in output:
                print(item)
        else:
            with open(out_file, 'w') as the_out_file:
                for item in output:
                    the_out_file.write(item + "\n")
            the_out_file.close()


# basic startup / the stupid can figure out their own issues as far as input
if(__name__ == "__main__"):
    usage = "Usage: VB-obfus-by-oper-simplify FILE_NAME ['LIST_OF_OPERATORS_DELIMITED_BY_A_DASH'] OUT_FILE_NAME\n(the OUT_FILE is optional)"
    if(len(argv) == 1 or argv[1].lower() == "-h" or argv[1].lower() == "--help"):
        print(usage)
    else:
        try:
            simplify_operations(argv[1], argv[2].split('-'), argv[3])
        except:
            simplify_operations(argv[1], argv[2].split('-'))