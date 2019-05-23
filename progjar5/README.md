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
