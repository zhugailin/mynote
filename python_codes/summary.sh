#!/usr/bin/env bash
classes=("bjdsyc" \
"wcaqm" \
"jyz_pl" \
"gbps" \
"bj_bpps" \
"xy" \
"ywzt_yfyc" \
"bj_wkps" \
"hxq_gjtps" \
"bj_bpmh" \
"sly_dmyw" \
"xmbhyc" \
"yw_gkxfw" \
"yw_nc" \
"wcgz" \
"hxq_gjbs" \
"kgg_ybh")

dir=${1:-./raw_data}
tot=0
i=0
for c in ${classes[@]}; do
        # n=$(ls ./raw_data/ | grep $c | wc -l)
        n=$(grep "^$i " $dir/*.txt | wc -l)
        n=$((n))
        tot=$((tot+n))
        echo "$n images include $c"
        i=$((i+1))
done

echo "There are $tot 17-class defection labels"
