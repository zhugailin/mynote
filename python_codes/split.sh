#!/usr/bin/env bash

indir=${1:-raw_data}
outdir=${2:-partitioned}
[ ! -e "$outdir"/train ] && mkdir -p "$outdir"/train
[ ! -e "$outdir"/val ] && mkdir -p "$outdir"/val

i=0
for f in "$indir"/*.jpg; do
        if [[ $((i % 10)) == 0 ]]; then
                cp "$f" "$outdir"/val
                cp "${f%.jpg}.txt" "$outdir"/val
        else
                cp "$f" "$outdir"/train
                cp "${f%.jpg}.txt" "$outdir"/train
        fi
        i=$((i+1))
done
