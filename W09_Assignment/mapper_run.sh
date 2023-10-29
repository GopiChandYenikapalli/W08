#!/bin/bash
/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files mapper.py,reducer.py \
-input /mapreduce/assignment/test.txt \
-output /mapreduce/assignment/output01 \
-mapper mapper.py \
-reducer reducer.py 

