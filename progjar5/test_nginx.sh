ab -n 100 -c 1 localhost/testing.txt > 100_1_nginx.txt
ab -n 1000 -c 1 localhost/testing.txt > 1000_1_nginx.txt
ab -n 10000 -c 1 localhost/testing.txt > 10000_1_nginx.txt

ab -n 100 -c 10 localhost/testing.txt > 100_10_nginx.txt
ab -n 1000 -c 10 localhost/testing.txt > 1000_10_nginx.txt
ab -n 10000 -c 10 localhost/testing.txt > 10000_10_nginx.txt

ab -n 100 -c 100 localhost/testing.txt > 100_100_nginx.txt
ab -n 1000 -c 100 localhost/testing.txt > 1000_100_nginx.txt
ab -n 10000 -c 100 localhost/testing.txt > 10000_100_nginx.txt