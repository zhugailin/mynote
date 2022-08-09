#!/bin/bash
for x in `seq 1 149`; do
    if [[ x -lt 10 ]]; then cp file.jpg file-00$x.jpg;
    elif [[ x -lt 100 ]]; then cp file.jpg file-0$x.jpg;
    else cp file.jpg file-$x.jpg;
    fi
done