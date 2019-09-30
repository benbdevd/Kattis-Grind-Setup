#!/bin/bash

# PROBLEM ID INPUT
PROB_ID=$1
if [ $# -eq 0 ]
  then
    printf 'Enter Problem ID: '
    read PROB_ID
fi

# GCC CONSTANTS
GCC_PATH="/usr/local/bin/g++-9"
GCC_ARGS="-g -O2 -std=gnu++17"

# PATHS AND DIRECTORIES
PROB_DIR=problems/$PROB_ID
PROG_PATH=$PROB_DIR/prog.cpp
LINK_PATH=$PROB_DIR/link.html
TEST_DIR=$PROB_DIR/tests

mkdir -p $PROB_DIR

# PROG.CPP FILE CREATION
echo '#include <bits/stdc++.h>' >> $PROG_PATH 
echo 'using namespace std;' >> $PROG_PATH 
echo >> $PROG_PATH
echo 'int main() {' >> $PROG_PATH
echo >> $PROG_PATH
echo '}' >> $PROG_PATH

# RUN.BASH FILE CREATION
echo \#!/bin/bash > $PROB_DIR/run.bash
echo $GCC_PATH $GCC_ARGS prog.cpp -o prog >> $PROB_DIR/run.bash
echo 'i=1; for TEST in ./tests/*.in; do printf "TEST CASE $i: "; ANS="${TEST%??}ans"; RESULT=$(cat $TEST | ./prog); PASS=$(echo $RESULT | diff -s - $ANS); PASS=${PASS:0:5}; if [ "$PASS" = "Files" ] ; then echo "PASS"; else echo "FAIL(P)"; fi; echo $RESULT; echo ''; ((i=$i+1)); done' >> $PROB_DIR/run.bash
chmod +x $PROB_DIR/run.bash

# LINK.HTML FILE CREATION
printf $'<html>\n<head>\n<meta http-equiv=\"refresh\" content=\"0; url=https://open.kattis.com/problems/' > $LINK_PATH
printf $PROB_ID >> $LINK_PATH
printf $'\"/>\n</head>\n</html>\n' >> $LINK_PATH

mkdir $TEST_DIR

# DOWNLOADING AND UNZIPPING TESTS
curl -s -o $PROB_DIR/samples.zip https://open.kattis.com/problems/$PROB_ID/file/statement/samples.zip
unzip -qq $PROB_DIR/samples.zip -d $TEST_DIR
rm $PROB_DIR/samples.zip
