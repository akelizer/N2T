// Program: Fill.asm

// Computes: puts values -1 or 0 into SCREEN[arr+i] register while checking 

// active KEYBOARD (kbd) code

// Usage: Fills SCREEN words with black pixels when kbd is pressed down, else blank 
// arr = 16384; i = 0; n = 8191; kbd = 24576

// beginning will set up the values

	@SCREEN	
	D=A
	@arr
	M=D	// arr points to an address in Screen array 

	@8191	// number or registers in Screen array
	D=A
	@n
	M=D	// n is set to 8191


(REFRESH)
	@i
	M=0

(LOOP)
// if (i=n) goto END / fill the entire Screen memory map
	@i
	D=M
	@n
	D=D-M	// when (i) is greater than (n) entire array has been accessed, reset (i) to refresh SCREEN
	@REFRESH
	D;JGT

// check KBD value to insert black or white pixel
	@KBD
	D=M
	@BLACK
	D;JGT
	@WHITE
	D;JEQ

(BLACK)
// RAM[arr+i] = -1	// fills SCREEN word with black pixels.
	@arr
	D=M
	@i
	A=D+M
	M=-1
	@COUNTER
	0;JMP

(WHITE)
// RAM[arr+i] = 0	// fills SCREEN word with white pixels. 
	@arr
	D=M
	@i
	A=D+M
	M=0
	@COUNTER
	0;JMP


(COUNTER)
// i++
	@i
	M=M+1

	@LOOP
	0;JMP



