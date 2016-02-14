#!/bin/bash

#variable
TASK_ID=3.3
TASK_DIR=/user/$USER/ex2/task_$TASK_ID.out
HDP_DIR=/user/$USER/data
INP_FILES=$HDP_DIR/input/ex2/logsLarge.txt
OUT_DIR=$HDP_DIR/output
LOCAL_DIR=./

rm -R $LOCAL_DIR/output
hdfs dfs -rm -R $OUT_DIR

#running this on a single reducer to get the final output
hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -D mapred.reduce.tasks=3 \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
 -D stream.num.map.output.key.fields=2 \
 -D num.key.fields.for.partition=1 \
 -D mapreduce.partition.keypartitioner.options=-k1,2 \
 -D mapreduce.partition.keycomparator.options="-k1,1 -k2,2n" \
 -input $INP_FILES \
 -output $OUT_DIR \
 -mapper mapReqTime.py \
 -file mapReqTime.py \
 -reducer reduceReqTime.py \
 -file reduceReqTime.py \
 -jobconf mapred.job.name="Job_S1567343_ex2_task_$TASK_ID" \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

#Copy the output to local dir
hdfs dfs -copyToLocal $OUT_DIR $LOCAL_DIR

#hdfs dfs -rm $RE_INP_DIR/*
#hdfs dfs -cp $OUT_DIR/part* $RE_INP_DIR

#copy the output to task dir
hdfs dfs -rm $TASK_DIR/*
hdfs dfs -cp $OUT_DIR/* $TASK_DIR

echo "Done. check local output directory"

