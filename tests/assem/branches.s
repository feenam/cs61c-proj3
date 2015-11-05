        beqal $s0 $s0 start       #0
badness:
        lui $s0 0xFF            #1
        beq $s0 $s0 badness     #2
label1:
        lui $s0 3               #3
        bne $s0 $s3 label2      #4

start:  lui $s0 1               #5
        beqal $s0 $s1 badness     #6
        lui $s0 2               #7
        bne $s0 $s1 label1      #8

label2: lui $s0 4               #9
end:    ori $s2 $s0 0           #10
        beq $s2 $s0 end         #11
        ori $s2 $s0 2           #12

#0, 5, 6, 7, 8, 3, 4, 9, 10, 11, 10, 11...
