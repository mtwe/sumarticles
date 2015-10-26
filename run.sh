#!/bin/bash
script_loc="$CWDnyt.py"
python "$script_loc"
while read line
do
    open "$line"
done < "$HOME/.nyt_articles.txt"