#!/bin/sh

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
echo \#include \<bits/stdc++.h\> >> $PROG_PATH 
echo using namespace std\; >> $PROG_PATH 
echo >> $PROG_PATH
echo int main\(\) \{ >> $PROG_PATH
echo >> $PROG_PATH
echo \} >> $PROG_PATH

# RUN.SH FILE CREATION
echo \#!/bin/sh > $PROB_DIR/run.sh
echo $GCC_PATH $GCC_ARGS prog.cpp -o prog >> $PROB_DIR/run.sh
echo "for TEST in ./tests/*.in; do cat \$TEST | ./prog; done" >> $PROB_DIR/run.sh
chmod +x $PROB_DIR/run.sh

# LINK.HTML FILE CREATION
echo $'<html>\n<head>\n<meta http-equiv=\"refresh\" content=\"0; url=https://open.kattis.com/problems/' > $LINK_PATH
echo $PROB_ID >> $LINK_PATH
echo $'\" />\n</head>\n</html>\n' >> $LINK_PATH

mkdir $TEST_DIR

# DOWNLOADING AND UNZIPPING TESTS
curl -s -o $PROB_DIR/samples.zip https://open.kattis.com/problems/$PROB_ID/file/statement/samples.zip
unzip -qq $PROB_DIR/samples.zip -d $TEST_DIR
rm $PROB_DIR/samples.zip
