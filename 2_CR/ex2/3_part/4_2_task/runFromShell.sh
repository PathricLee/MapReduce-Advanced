#!/bin/bash

#variable
TASK_ID=4.2
TASK_DIR=/user/$USER/ex2/task_$TASK_ID.out
HDP_DIR=/user/$USER/data
INP_FILES=$HDP_DIR/input/ex2/4_task/
OUT_DIR=$HDP_DIR/output
LOCAL_DIR=./

rm -R $LOCAL_DIR/output
hdfs dfs -rm -R $OUT_DIR

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -D mapred.reduce.tasks=1 \
 -input $INP_FILES \
 -output $OUT_DIR \
 -mapper mapMostAnswers.py \
 -file mapMostAnswers.py \
 -reducer reduceMostAnswers.py \
 -file reduceMostAnswers.py \
 -jobconf mapred.job.name="Job_S1567343_ex2_task_$TASK_ID"

#Copy the output to local dir
hdfs dfs -copyToLocal $OUT_DIR $LOCAL_DIR

#copy the output to task dir
hdfs dfs -rm $TASK_DIR/*
hdfs dfs -cp $OUT_DIR/* $TASK_DIR

echo "Done. check local output directory"

