addiu $s3 $0 16
loop: swinc $s0 4($s0)
bne $s0 $s3 loop
lw $s1 4($0)
lw $s2 8($0)
lw $s1 12($0)
lw $s2 16($0)



