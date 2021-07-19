# MapReduce Code to Find the Maximum Temperature by Year

### Input Data

The input data contains Date (dd/mm/yyyy), ID, and Temperature
```
10-01-1990,123112,10
14-02-1991,283901,11
10-04-1990,381920,15
10-01-1991,302918,22
12-02-1990,384901,9
```

### Expected Output

```
1990    15
1991    22
```

### Creating a new directory

```
mkdir maxTemp
```

### Go to the `maxTemp` Directory 
```
cd maxTemp
```

### Creating the Required Files
1. Create a file in the local named `maxTemp.txt` using the command ```vi maxTemp.txt```  Note: ```/root/code/maxTemp``` is my current directory
2. Enter the contents into the file to which we are going to apply MapReduce to find the word count.
3. Create the Files `mapper.py` and `reducer.py` in the current working directory and enter the contents.

### Copying the Files to HDFS
```
hdfs dfs -put maxTemp.txt /user/root/
```

### Running the MapReduce job
```
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
> -input /user/root/maxTemp.txt \
> -output /user/root/maxTempOutput \
> -mapper mapper.py \
> -reducer reducer.py \
> -file /root/code/maxTemp/mapper.py \
> -file /root/code/maxTemp/reducer.py
```

### Files in the Output Folder
```
hdfs dfs -ls /user/root/maxTempOutput
```

`Found 2 items`<br/>
`-rw-r--r--   1 root hdfs          0 2021-07-19 16:27 /user/root/maxTempOutput/_SUCCESS`<br/>
`-rw-r--r--   1 root hdfs         16 2021-07-19 16:27 /user/root/maxTempOutput/part-00000`<br/>

### To View the Output
```
hdfs dfs -cat /user/root/maxTempOutput/part-00000
```

### Output

```
1990    15
1991    22
```
