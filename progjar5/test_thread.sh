ab -n 100 -c 1 localhost:8887/testing.txt > 100_1_thread.txt
ab -n 1000 -c 1 localhost:8887/testing.txt > 1000_1_thread.txt
ab -n 10000 -c 1 localhost:8887/testing.txt > 10000_1_thread.txt

ab -n 100 -c 10 localhost:8887/testing.txt > 100_10_thread.txt
ab -n 1000 -c 10 localhost:8887/testing.txt > 1000_10_thread.txt
ab -n 10000 -c 10 localhost:8887/testing.txt > 10000_10_thread.txt

ab -n 100 -c 100 localhost:8887/testing.txt > 100_100_thread.txt
ab -n 1000 -c 100 localhost:8887/testing.txt > 1000_100_thread.txt
ab -n 10000 -c 100 localhost:8887/testing.txt > 10000_100_thread.txt