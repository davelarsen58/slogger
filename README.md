# slogger

slogger is a multithreaded stream logger born from the need to correlate multiple serial / ssh streams from development devices.

The tool allows specifying a list of connections to establish, the name of the log file to use, and whether to add timestamps to each line of the log file.



## usage:
```
slogger host:serial:device host:ssh:username ...
```

slogger opens a session to each host / device in the arguments and the output to a common timestamped log file.

### options:
--logname
--sessions
--timestamp | --notimestamp - default is timestamp

## Feature Development
consider using