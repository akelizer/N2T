// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/06/add/Add.asm

// To use in a Java program: prompt > java (java VM name) HackAssembler Xxx.asm (the argument)
// creates a new .hack file that can be run in the Hack CPU Emulator

// Architecture guidelines: 

// Parser : unpacks each instruction into its underlying fields
// Code : translates each field into its corresponding binary value
// SymbolTable : manages the symbol table
// Main : initializes the i/o files and drives the process

// Implementation Guidelines : 

// Develop basic assembler that translates assembly programs without symbols
// Develop an ability to handle symbols
// Morph the basic assembler into assembler that can translate any assembly program


// make sure assembler can deal with 'white space' and the 'instructions'

// Computes R0 = 2 + 3  (R0 refers to RAM[0])

@2
D=A
@3
D=D+A
@0
M=D
