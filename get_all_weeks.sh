#!/bin/bash

start=49
end=51

for j in $(seq 2023 2023); do
for i in $(seq $start $end); do
    url="https://www2.census.gov/programs-surveys/demo/tables/hhp/${j}/wk${i}/health2_week${i}.xlsx"
    wget -P data/depression/ $url
done
done

