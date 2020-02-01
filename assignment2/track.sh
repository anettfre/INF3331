#!/bin/bash
running=0 #running is 0 if no task is running and 1 if there is on running
function track {
  LOGFILE="LOGFILE" #this line is for if you dont export

  if [ "$1" = "start" ]
  then
    if [ $running -eq 0 ]
    then
      lable=$2
      echo "START $(date)" >> LOGFILE
      echo "LABEL This is task "$2"" >> LOGFILE
      running=1 #since one task is started the value is 1
    else #if running is 0
      echo "A task is allready running"
    fi

  elif [ "$1" = "status" ]
  then
    if [ $running -eq 1 ]
    then
      taskname=$( tail -n 1 LOGFILE | cut -d' ' -f5) #take the last line in logfile and cuts on the 5th word for taskname
      starttime=$( tail -2 LOGFILE | head -1 | cut -d' ' -f5) #take the second last line and gvie the first line of the two last and finds the first word then cuts it
      echo "A task is running, its called $taskname, and started $starttime"
    else
      echo "No task is running"
    fi

  elif [ "$1" = "stop" ]
  then
    if [ $running -eq 1 ]
    then
      echo "END $(date)\n\n" >> LOGFILE
      stoptime=$( tail -3 LOGFILE | head -2 | cut -d' ' -f5)
      running=0 #since a task is finished running is back to 0
    else
      echo "No task is running"
    fi

  elif [ "$1" = "log" ] #task 2.3
  then
    counter=0
    numberoflines=$(wc -l < LOGFILE) #finds the number of lines in logfile

    while [ $counter -lt $numberoflines ]
    do
      ((counter++))
      #sed finds the line on place counter in logile
      firstword=$( sed "${counter}q;d" LOGFILE | cut -d' ' -f1)  #finds the first word on line counter and cuts the first word

      if [ "$firstword" = "START" ] #if the first word on the counter line is start the number on the 5th place is the starttime
      then
        starttimelog=$( sed "${counter}q;d" LOGFILE | cut -d' ' -f5)

      elif [ "$firstword" = "LABEL" ] #if the first word is label then the name on the task is on the 5th place on the line
      then
        tasknamelog=$( sed "${counter}q;d" LOGFILE | cut -d' ' -f5)

      elif [ "$firstword" = "END" ] #if the first word is end then the endtime is on that line
      then
        endtime=$( sed "${counter}q;d" LOGFILE | cut -d' ' -f5)
        #take the time and make it into seconds to calculate
        SEC1=$( date +%s -d ${starttimelog})
        SEC2=$( date +%s -d ${endtime})
        #finds the time spendt on one task by finding the difference in seconds
        var3=$(( $SEC2 - $SEC1))
        echo "Task $tasknamelog:  $( date +%H:%M:%S -ud @${var3})" #print out to terminal the time spent and changing it back to hours, min and seconds
      fi
    done
  else
    echo "Wrong argument is given, write track start [label], track status or track stop"
  fi
}
