#!/bin/bash
function climb {
  declare -i counter
  counter=0
  if [ $# -eq 1 ]; then
    while [ $counter -lt $1 ]
      do
        ((counter++))
        cd ..
      done
    else
      cd ..
    fi
}
