# FinalProjectProgjar
Final Project matakuliah Pemrograman Jaringan oleh Alam, Firman dan Chendra

# How to Run #
Untuk web server tanpa load balancer, jalankan
``` $py server_thread_http.py ``` untuk synchronous,
``` $py server_async_http.py ``` untuk asynchronous

Untuk web server dengan load balancer, pertama jalankan
```
bash $py load_balancer.py
```
Kemudian untuk synchronous jalankan ```$bash run_sync_http.sh```
Sementara untuk asynchronous jalankan ```$bash run_async_http.sh```

# Hasil Apache Benchmark #
### Web server tanpa load balancer synchronous ###
Jumlah request 100, concurrency 1
```
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        myserver/1.0
Server Hostname:        localhost
Server Port:            8887

Document Path:          /testing.txt
Document Length:        20 bytes

Concurrency Level:      1
Time taken for tests:   0.120 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      15600 bytes
HTML transferred:       2000 bytes
Requests per second:    833.68 [#/sec] (mean)
Time per request:       1.200 [ms] (mean)
Time per request:       1.200 [ms] (mean, across all concurrent requests)
Transfer rate:          127.01 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     1    1   1.5      1      16
Waiting:        0    1   1.5      1      16
Total:          1    1   1.5      1      16

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      1
  98%      1
  99%     16
 100%     16 (longest request)

```

