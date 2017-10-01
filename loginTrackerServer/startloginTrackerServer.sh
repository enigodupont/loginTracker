#!/bin/bash

if [  $(pgrep startloginTrackerServer.sh) ]
then
  echo "Another script is running, lets kill it...."
  kill $(pgrep startloginTrackerServer.sh)
  sleep 1
fi

if [[ $(pgrep -f 'runserver.*4242') ]]
then
  echo "Another server is running, lets kill it...."
  kill $(pgrep -f "runserver.*4242")
  sleep 1
fi

source ./linuxEnv/bin/activate
./manage.py runserver 0.0.0.0:4242
