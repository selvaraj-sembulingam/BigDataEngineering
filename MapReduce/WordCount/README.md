# Getting Started with Hadoop MapReduce in Python

'''
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-input /user/root/word_count_data.txt \
-output /user/root/wcoutput \
-mapper mapper.py \
-reducer reducer.py \
-file /root/code/mapper.py \
-file /root/code/reducer.py
'''


'''
hdfs dfs -ls /user/root/wcoutput
'''

'''
hdfs dfs -cat  /user/root/wcoutput/part-00000
'''
