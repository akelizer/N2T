// Program: Multi.asm
// Computes RAM[2] = RAM[0] + RAM[1]
// Usage: Add value (n) of RAM[0] to itself until value of (c) RAM[1] is zero. 
// if (c) = 0; jump to ZERO



	@R0
	D=M
	@n	// address 16
	M=D	// n = R0
	@R1
	D=M	// store R1 into D
	@c	// address 17
	M=D	// c = R1
	@sum
	M=0	// sum=0

(LOOP)
	@c
	D=M-1
	@c
	M=D
	@STOP
	D;JLT	// if c<0 goto STOP

	@sum
	D=M
	@R0
	D=D+M	// D = sum + R0
	@sum
	M=D	// sum = sum + R0
	@LOOP
	0;JMP
	
(STOP)
	@sum
	D=M
	@R2
	M=D	// R2 = sum

(END)
	@END
	0;JMP
	
	