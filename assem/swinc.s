addiu $s3 $0 16
loop: swinc $s0 0($s0)
bne $s0 $s3 loop
lw $s1 0($0)
lw $s2 4($0)
lw $s1 8($0)
lw $s2 12($0)



