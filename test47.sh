#!/bin/sh
# macだと--オプションは使えないっぽい
cut -f 1 result.txt | sort | uniq -c | sort -n -r > "predicate.txt"
cut -f 1-2 result.txt | sort | uniq -c | sort --n -r  > "predicate_Particle.txt"



