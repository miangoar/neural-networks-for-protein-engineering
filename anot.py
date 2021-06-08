#!/usr/bin/env python3
import sys
import os
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

def do_ref():
    global ref_len
    ref_len = len(seq) - seq.count('-')
    j=1
    for res in seq:
        if res != '-':
            pos = j
            j+=1
        else:
            pos = '<' + str(j)
        refe.append([res,pos])

def do_seq():
    seq_len = len(seq) - seq.count('-');
    if seq_len < min_len * ref_len:
        print(f"seq #{q_id} is too short: {seq_len}", file=sys.stderr)
        return
    print(seq_name)
    j=1
    for i, res in enumerate(seq):
        if res != '-':
            pos = j
            j+=1
        else:
            pos = '<' + str(j)
        if res != refe[i][0]:
            print(f"{q_id}\t{i}\t{pos}\t{refe[i][0]}{refe[i][1]}{res}")


if __name__ == '__main__':
    min_len = 0.85
    seq=''
    seq_name =''
    refe = []
    ref_len =0
    q_id = -1
    if len(sys.argv) !=2:
        print("parse_mafft.py <fasta_alignment>", file=sys.stderr)
        exit()
    mafft = sys.argv[1]
    fh = open(mafft,'r')
    for line in fh:
        if line.startswith('>'):
            if len(seq)>0:
                if q_id == 0:
                    do_ref()
                else:
                    do_seq()
                seq = ''
                seq_name = line.rstrip()
            q_id +=1
            continue
        seq += line.rstrip()
if len(seq) >0:
    do_seq()



