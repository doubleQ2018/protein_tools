#!/usr/bin/env python

from proteinINFO import *
from matrix4sse import *

def main():
    pdbfile = "1dlw.pdb"
    fastafile = "1dlwA.fasta"
    proinfo = proteinINFO(pdbfile, fastafile)
    ss3 = proinfo.ss3seq
    dist_matrix = proinfo.dist_matrix
    angle_matrix = proinfo.angle_matrix
    
    c = matrix4sse(ss3, dist_matrix, angle_matrix)
    sse_matrix = c.sse_matrix_labeled
    sse_matrix = np.where(sse_matrix > 0, 1, 0)
    print ss3
    print "".join(c.sse_pattern)
    print c.sse_elements
    print sse_matrix

if __name__ == "__main__":
    main()

