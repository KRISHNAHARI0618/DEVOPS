#! /bin/bash

# print 1 to 100

# prime number are divided by 1 and itslef and iteself 2,5,7,
for i in {1..100}
do
  is_prime=true
  for (( i=0; i<num i++ ))
  do
    if [ $(($num%$i)) -eq 0 ]
    then
      is_prime=false
      break
    fi
  done
  if $is_prime
  then
    echo $num
  fi
done
