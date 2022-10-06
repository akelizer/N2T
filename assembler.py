class Assembler:

    # attributes shared by all objects of "assembler" class.
    def __init__(self):
        self.commandType = ''
        self.value = 0
        self.dest = '000'
        self.comp = ''
        self.jump = '000'
        self.aString = '0'
        self.headerString = '111'
        self.counter = -1
  
    # methods
    def get_commandType(self, line):
        if line.startswith('@'):
            self.commandType = 'A_COMMAND'
        else:
            self.commandType = 'C_COMMAND'
    # sets value of A command
    def get_value(self, line):
        if self.commandType == 'A_COMMAND':
            line = line.strip('@')
            self.value = line

    # parses out dest, comp, jump fields 
    def parser(self, line):
      # set dest field
      if line.find('=') != -1:
        # dest string starts [0] ends before '=' in line
          self.dest = line[0:line.find('=')]
      else:
        self.dest = 'null'
      # test print
      #print(f"destString: {self.dest}")

      # set comp field
      if self.dest != 'null':
        # compString starts after '=', ends at last index in line
        self.comp = line[line.find('=') + 1:len(line)]
      else:
        # compString starts at first index, ends at ';'
        self.comp = line[0:line.find(';')]

      # set jump field
      if line.find(';') != -1:
        # jumpString starts after ';', ends at last index in line
        self.jump = line[line.find(';') + 1:len(line)]
      else: 
        self.jump = 'null'  
      
# translates C command fields to binary
    def translator(self):
      # header bits
      headerString = '111'
      
      # dest translation
      if self.dest == 'null':
        destString = '000'
      elif self.dest == 'M':
        destString = '001'
      elif self.dest == 'D':
        destString = '010'
      elif self.dest == 'A':
        destString = '100'
      elif self.dest  == 'MD':
        destString = '011'
      elif self.dest == 'AM':
        destString = '101'
      elif self.dest == 'AD':
        destString = '110'
      elif self.dest == 'AMD':
        destString = '111'
      
      # comp translation:
      ## A/D values
      if self.comp == '0':
        compString = '101010'
      elif self.comp == 'A':
        compString = '110000'
      elif self.comp == 'D':
        compString = '001100'
      elif self.comp == 'D+A':
        compString = '000010'

      ## M values
      elif self.comp == 'M':
        compString = '110000'
      elif self.comp == 'D-M':
        compString = '010011' 
      elif self.comp == 'M-D':
        compString = '000111'
        
    # jump translation
      if self.jump == 'null':
        jumpString = '000'
      elif self.jump == 'JGT':
        jumpString = '001'
      elif self.jump == 'JMP':
        jumpString = '111'
      elif self.jump == 'JEQ':
        jumpString = '010'
      elif self.jump == 'JLT':
        jumpString = '100'
      elif self.jump == 'JNE':
        jumpString = '101'
      elif self.jump == 'JLE':
        jumpString = '110'
      elif self.jump == 'JGE':
        jumpString = '011'

      # set 'a' value
      if self.comp.find('M') != -1:
        aString = '1'
      else:
        aString = '0'

      return compString, destString, jumpString, headerString, aString
    
      



    # assigns values for predefined, labels, and variables
    def counter(self, line):
      # tracks line number in code; does not count lines with "(xxx)" 
      if line.find('(') == -1:
        self.counter += 1
      #print(f"counter: {self.counter}")
      
      
      

    # work in progress
    def symbolTable(self, line):
      symbolTable = {"R0": 0}
      if self.commandType == 'A_COMMAND':
        if self.value == 'R0':
          return 
      
      