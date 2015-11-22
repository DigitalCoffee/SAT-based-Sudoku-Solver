TEST=163805070008040065005007008450082039301000040700000000839050000604200590000093081
PYTHON3="python3"
CNF="_cnf"
MINISAT_OUT="_minisat"
OUTPUT="_result"
MINISAT="minisat" # Location of the binary. If it's on path this should work.


all:
	echo "${TEST}" | ${PYTHON3} CNF_converter.py > ${CNF}
	${MINISAT} ${CNF} ${MINISAT_OUT} || true
	cat ${MINISAT_OUT} | ${PYTHON3} prettyprint.py > ${OUTPUT}
