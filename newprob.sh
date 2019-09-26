#!/bin/sh

PROBNAME=$1
GCC_PATH="/usr/local/bin/g++-9"
GCC_ARGS="-g -O2 -std=gnu++17"

if [ $# -eq 0 ]
  then
    echo 'Enter problem code: '
    read PROBNAME
fi

PROBDIR=problems/$PROBNAME

mkdir -p $PROBDIR

echo \#include \<bits/stdc++.h\> >> $PROBDIR/prog.cpp 
echo using namespace std\; >> $PROBDIR/prog.cpp 
echo >> $PROBDIR/prog.cpp
echo int main\(\) \{ >> $PROBDIR/prog.cpp
echo >> $PROBDIR/prog.cpp
echo \} >> $PROBDIR/prog.cpp

echo \#!/bin/sh > $PROBDIR/run.sh
echo $GCC_PATH $GCC_ARGS prog.cpp -o prog >> $PROBDIR/run.sh
echo "for TEST in ./tests/*.in; do cat $TEST | ./prog; done" >> $PROBDIR/run.sh
chmod +x $PROBDIR/run.sh

echo $'<html>\n<head>\n<meta http-equiv=\"refresh\" content=\"0; url=https://open.kattis.com/problems/' > $PROBDIR/link.html
echo $PROBNAME >> $PROBDIR/link.html
echo $'\" />\n</head>\n</html>\n' >> $PROBDIR/link.html

mkdir $PROBDIR/tests

curl -o $PROBDIR/samples.zip https://open.kattis.com/problems/$PROBNAME/file/statement/samples.zip
unzip -qq $PROBDIR/samples.zip -d $PROBDIR/tests

rm $PROBDIR/samples.zip
