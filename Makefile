# Puzzles
DEFAULT=	163805070008040065005007008450082039301000040700000000839050000604200590000093081
HARD=		000006000059000008200008000045000000003000000006003054000325006000000000000000000
UNSOLVABLE=	111111111111111111111111111111111111111111111111111111111111111111111111111111111

PYTHON3="python3"
CNF="_cnf"
MINISAT_OUT="_minisat"
OUTPUT="_result"
MINISAT="minisat" # Location of the binary. If it's on path this should work.


all: default

default:
	echo "${DEFAULT}" | ${PYTHON3} CNF_converter.py > ${CNF}
	${MINISAT} ${CNF} ${MINISAT_OUT} || true
	cat ${MINISAT_OUT} | ${PYTHON3} prettyprint.py > ${OUTPUT}
	cat ${OUTPUT}

hard:
	echo "${HARD}" | ${PYTHON3} CNF_converter.py > ${CNF}
	${MINISAT} ${CNF} ${MINISAT_OUT} || true
	cat ${MINISAT_OUT} | ${PYTHON3} prettyprint.py > ${OUTPUT}
	cat ${OUTPUT}

unsolvable:
	echo "${UNSOLVABLE}" | ${PYTHON3} CNF_converter.py > ${CNF}
	${MINISAT} ${CNF} ${MINISAT_OUT} || true
	cat ${MINISAT_OUT} | ${PYTHON3} prettyprint.py > ${OUTPUT}
	cat ${OUTPUT}

extended:
	echo "${TEST}" | ${PYTHON3} CNF_Extended_converter.py > ${CNF}
	${MINISAT} ${CNF} ${MINISAT_OUT} || true
	cat ${MINISAT_OUT} | ${PYTHON3} prettyprint.py > ${OUTPUT}
	cat ${OUTPUT}
