#!/bin/bash

#variable
TASK_ID=3
TASK_DIR=/user/$USER/ex2/task_$TASK_ID.out
HDP_DIR=/user/$USER/data
INP_FILES=$HDP_DIR/input/ex2/logsLarge.txt
RE_INP_DIR=$HDP_DIR/input/ex2/3_task
OUT_DIR=$HDP_DIR/output
LOCAL_DIR=./

rm -R $LOCAL_DIR/output
hdfs dfs -rm -R $OUT_DIR

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -input $INP_FILES \
 -output $OUT_DIR \
 -mapper mapAggregate.py \
 -file mapAggregate.py \
 -combiner aggregate \
 -reducer aggregate \
 -jobconf mapred.job.name="Job_S1567343_ex2_task_$TASK_ID"

#Copy the output to local dir
hdfs dfs -copyToLocal $OUT_DIR $LOCAL_DIR

hdfs dfs -rm $RE_INP_DIR/*
hdfs dfs -cp $OUT_DIR/part* $RE_INP_DIR

#copy the output to task dir
#hdfs dfs -rm $TASK_DIR/*
#hdfs dfs -cp $OUT_DIR/* $TASK_DIR

echo "Done. check local output directory"

