
cpu:
	cp alu.circ tests
	cp regfile.circ tests
	cp mem.circ tests
	cp cpu.circ tests
	cd tests && ./autograder_cpu.py -here
	mv tests/TEST_LOG TEST_LOG

alu:
	cp alu.circ tests
	cp regfile.circ tests
	cd tests && ./autograder_limited.py -here
	mv tests/TEST_LOG TEST_LOG
