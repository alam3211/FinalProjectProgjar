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
Buka ```nginx.conf``` pada direktori ```/etc/nginx```, tambahkan ini pada bagian http:
```
upstream node {
    server 127.0.0.1:9001;
    server 127.0.0.1:9002;
    server 127.0.0.1:9003;
    server 127.0.0.1:9004;
    server 127.0.0.1:9005;
}
```
Setelah  itu buka ```default``` pada direktori ```/etc/nginx/sites-available```. Ubah bagian isi ```location /``` menjadi:
```
location / {
        proxy_pass http://node;
    }
```
Kemudian jalankan ```service nginx restart```

#### Kedua, jalankan bash script
Jalankan ```$bash run_sync_http.sh``` untuk synchronous, atau ```$bash run_async_http.sh``` untuk asynchronous.

# Hasil Apache Benchmark #
Berikut hasil apache benchmark:

Dengan jumlah request 100:

| Metode | -c 1 Req/sec |  -c 10 Req/sec | -c 100 Req/sec | 
|---|---|---|---|
| web server, non load balancer, sync | 833.68/sec | 1545.52/sec | 1088.67/sec |
| web server, non load balancer, async | 1094.16 /sec | 1304.94/sec | 1120.99/sec |
| web server, python load balancer, sync | 541.93 /sec | 971.40/sec | 937.06/sec |
| web server, python load balancer, async | 487.78 /sec | 790.24/sec | 957.85/sec |
| web server, nginx load balancer, sync | 748.81 /sec | 2103.71/sec | 1429.06/sec |
| web server, nginx load balancer, async | 603.46 /sec | 1887.72/sec | 1483.48/sec |

Dengan jumlah request 1000:

| Metode | -c 1 Req/sec |  -c 10 Req/sec | -c 100 Req/sec | 
|---|---|---|---|
| web server, non load balancer, sync | 1034.47/sec | 2094.49/sec | 1836.41/sec |
| web server, non load balancer, async | 1212.11/sec | 2245.04/sec | 2194.80/sec |
| web server, python load balancer, sync | 508.95/sec | 925.75/sec | 921.08/sec |
| web server, python load balancer, async | 550.64/sec | 917.24/sec | 887.74/sec |
| web server, nginx load balancer, sync | 898.04/sec | 2260.58/sec | 1751.10/sec |
| web server, nginx load balancer, async | 749.47/sec | 2125.65/sec | 2641.88/sec |

Dengan jumlah request 10000:

| Metode | -c 1 Req/sec |  -c 10 Req/sec | -c 100 Req/sec | 
|---|---|---|---|
| web server, non load balancer, sync | 1101.73/sec | 2038.88/sec | 1544.71/sec |
| web server, non load balancer, async | 1084.35/sec | 2158.50/sec | 2067.53/sec |
| web server, python load balancer, sync | 557.93/sec | 970.36/sec | 857.55/sec |
| web server, python load balancer, async | 523.23/sec | 997.95/sec | 964.49/sec |
| web server, nginx load balancer, sync | 934.19/sec | 2275.77/sec | 2319.48/sec |
| web server, nginx load balancer, async | 1034.57/sec | 2550.42/sec | 2601.63/sec |
