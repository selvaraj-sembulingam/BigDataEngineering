# Getting Started with Hadoop MapReduce in Python

### Running the MapReduce job
```
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-input /user/root/word_count_data.txt \
-output /user/root/wcoutput \
-mapper mapper.py \
-reducer reducer.py \
-file /root/code/mapper.py \
-file /root/code/reducer.py
```

### Files in the Output Folder
```
hdfs dfs -ls /user/root/wcoutput
```
`
Found 2 items
-rw-r--r--   1 root hdfs          0 2021-07-13 13:44 /user/root/wcoutputnewselva2/_SUCCESS
-rw-r--r--   1 root hdfs         58 2021-07-13 13:44 /user/root/wcoutputnewselva2/part-00000
`

### To View the Output
```
hdfs dfs -cat  /user/root/wcoutput/part-00000
```
