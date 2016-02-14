#!/bin/bash

#variable
TASK_ID=1
TASK_DIR=/user/$USER/ex2/task_$TASK_ID.out
HDP_DIR=/user/$USER/data
INP_FILES=$HDP_DIR/input/ex2/large/
RE_INP_DIR=$HDP_DIR/input/ex2/1_task
OUT_DIR=$HDP_DIR/output
OUT_DIR_2=$HDP_DIR/output_2
LOCAL_DIR=./

rm -R $LOCAL_DIR/output
hdfs dfs -rm -R $OUT_DIR
hdfs dfs -rm -R $OUT_DIR_2

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -input $INP_FILES \
 -output $OUT_DIR \
 -mapper mapTfIndex.py \
 -file mapTfIndex.py \
 -reducer reduceTfIndex.py \
 -file reduceTfIndex.py \
 -combiner combineTfIndex.py \
 -file combineTfIndex.py \
 -jobconf mapred.job.name="Job_S1567343_ex2_task_$TASK_ID"

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
 -D mapred.reduce.tasks=1 \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
 -D stream.num.map.output.key.fields=1 \
 -D num.key.fields.for.partition=1 \
 -D mapreduce.partition.keypartitioner.options=-k1,1 \
 -D mapreduce.partition.keycomparator.options='-k1n' \
 -input $OUT_DIR \
 -output $OUT_DIR_2 \
 -mapper cat \
 -reducer cat

#Copy the output to local dir
hdfs dfs -copyToLocal $OUT_DIR_2 $LOCAL_DIR

hdfs dfs -rm $RE_INP_DIR/*
hdfs dfs -cp $OUT_DIR_2/part* $RE_INP_DIR

#copy the output to task dir
hdfs dfs -rm $TASK_DIR/*
hdfs dfs -cp $OUT_DIR_2/* $TASK_DIR

echo "Done. check local output directory"

