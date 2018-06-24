#!/bin/sh

# ソートして重複除去して、その件数でソート
sort result.txt | uniq --count | sort --numeric-sort --reverse > "すべて.txt"

# 「する」のみ
grep "^する\s" result.txt | sort | uniq --count | sort --numeric-sort --reverse > "する.txt"

# 「見る」のみ
grep "^見る\s" result.txt | sort | uniq --count | sort --numeric-sort --reverse > "見る.txt"

# 「与える」のみ
grep "^与える\s" result.txt | sort | uniq --count | sort --numeric-sort --reverse > "与える.txt"
