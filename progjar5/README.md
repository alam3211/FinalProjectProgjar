# FinalProjectProgjar
Final Project matakuliah Pemrograman Jaringan oleh Alam, Firman dan Chendra

# How to Run #
### Untuk web server tanpa load balancer ###
``` $py server_thread_http.py ``` untuk synchronous,
``` $py server_async_http.py ``` untuk asynchronous

### Untuk web server dengan python script load balancer ###
Pertama, jalankan
```
bash $py load_balancer.py
```
Kemudian untuk synchronous jalankan ```$bash run_sync_http.sh```
Sementara untuk asynchronous jalankan ```$bash run_async_http.sh```

### Untuk web server dengan nginx load balancer ###
#### Pertama, setting nginx terlebih dahulu:
Buka ```nginx.conf``` pada ```/etc/nginx```, tambahkan ini pada bagian http:
```
upstream node {
    server 127.0.0.1:9001;
    server 127.0.0.1:9002;
    server 127.0.0.1:9003;
    server 127.0.0.1:9004;
    server 127.0.0.1:9005;
}
```
Setelah  itu buka ```default``` pada ```/etc/nginx/sites-available```. Ubah bagian isi ```location /``` menjadi:
```
location / {
        proxy_pass http://node;
    }
```
Kemudian jalankan ```service nginx restart```

#### Kedua, jalankan bash script
Jalankan ```$bash run_sync_http.sh``` untuk synchronous, atau ```$bash run_async_http.sh``` untuk asynchronous.

# Hasil Apache Benchmark #
