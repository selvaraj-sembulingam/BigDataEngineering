# MapReduce Code to Find the WordCount

### Input
```
the quick brown fox jumped over lazy dogs quick dogs jumped jumped
```

### Expected Output
```
brown   1
dogs    2
fox     1
jumped  3
lazy    1
over    1
quick   2
the     1
```


### Creating the Required Files
1. Create a file in the local named `word_count_data.txt` using the command ```vi word_count_data.txt```  Note: ```/root/code/``` is my current directory
2. Enter the contents into the file to which we are going to apply MapReduce to find the word count.
3. Keep the Files `mapper.py` and `reducer.py` in the current working directory. 

### Copying the Files to HDFS
```
hdfs dfs -put word_count_data.txt /user/root/
```

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

`Found 2 items` <br />
`-rw-r--r--   1 root hdfs          0 2021-07-13 13:44 /user/root/wcoutput/_SUCCESS` <br />
`-rw-r--r--   1 root hdfs         58 2021-07-13 13:44 /user/root/wcoutput/part-00000` <br />


### To View the Output
```
hdfs dfs -cat  /user/root/wcoutput/part-00000
```

### Output

```
brown   1
dogs    2
fox     1
jumped  3
lazy    1
over    1
quick   2
the     1
```
