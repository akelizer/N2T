# HACK Assembler 
# author: John Kayrouz
# translates HACK HDL into binary machine language via the assembler.py module and Assembler class.
# writes translated binary into .hack file

import assembler

# opens supplied HACK HDL file, removes comments and whitespace, translates into binary
def main():
    # opens HDL file to be read
    file = open('MaxL.asm', 'r')
    # test file to see what info Assemlber reads
    newFile = open('Add.vm', 'w')
    # writes translated binary to file
    hackFile = open('Max.hack', 'w')
    # creates Assembler Object to translate file to binary
    hackAssembler = assembler.Assembler()

    # reads each line in file
    for line in file:
      # ignores emptyspace and comments
      if line.startswith('//') == False and line.isspace() == False:
        line = line.rstrip('\n')
        # writs HDL lines to test file
        newFile.write(line)

        # first pass reads file for symbols and parses command types
        hackAssembler.get_commandType(line)
        hackAssembler.symbolTable(line)

      # uses assembler class methods to translate HDL; prints results
      if hackAssembler.commandType == 'A_COMMAND':
        hackAssembler.get_value(line)
        # translates int to binary and pads result with 16 bits
        print(f"{int(hackAssembler.value):0>16b}")
        hackFile.write(f"{int(hackAssembler.value):0>16b}\n")
        
      elif hackAssembler.commandType == 'C_COMMAND':
        #initialize assembler methods 
        
        hackAssembler.parser(line)
        comp, dest, jump, header, a = hackAssembler.translator()
        
        
        print(f"{header}+{a}+{comp}+{dest}+{jump}")
        
        hackFile.write(f"{header + a + comp + dest + jump}\n")
        
        
        #hackAssembler.get_dest(line)
        #hackAssembler.get_comp(line)
        #hackAssembler.get_jump(line)

     

        # test prints
        # print(f"dest: {hackAssembler.dest}")
        # print(f"comp: {hackAssembler.comp}")
        # print(f"jump: {hackAssembler.jump}")

        #print(f"{hackAssembler.header + hackAssembler.a + hackAssembler.comp + hackAssembler.dest + hackAssembler.jump}")
        
        #hackFile.write(f"{hackAssembler.header + hackAssembler.a + hackAssembler.comp + hackAssembler.dest + hackAssembler.jump}\n")

    file.close()


main()
