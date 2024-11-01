#!/bin/bash
for i in *get-*.sh; do
    if [[ "$i" != `basename $0` ]]; then
        "./$i"
    fi
done