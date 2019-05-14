# FinalProjectProgjar
Final Project matakuliah Pemrograman Jaringan oleh Alam, Firman dan Chendra
"Chat server"

# How  to Run #
Terdapat 2 tahap untuk menjalankan aplikasi ini.
run 
```bash
$py server.py
```
Hal ini akan menyalakan Server dan menunggu koneksi dari client. Lalu jalankan
```bash
$py chat.py
```
Hal ini akan menyalakan client dan mengkoneksikan kepada Server.


# Client Command Usage
### Register ###
Command `register` untuk mendaftarkan akun.
> #### Parameter ####
```bash
Username :
Password :
Name :
Nationality :
```
> #### Example ###
```bash
register
Username : alam
Password : password
Name : alamcahya
Nationality : Indonesia
```
> Server Respond
```bash
User berhasil dibuat
```

### Autentikasi ###
Command `login` untuk melakukan autentikasi.
> #### Parameter ####
```bash
Username :
Password :
```
> #### Example ###
```bash
register
Username : alam
Password : password
```
> Server Respond
```bash
Login [$username] telah berhasil
```

### Send Message ###
Command `chat` untuk mengirim pesan kepada user lain.
> #### Parameter ####
```bash
Recipient username:
Message:
```
> #### Example ###
```bash
send
Recipient username: alam
Message: halo testing
```
> Server Respond
```bash
Message sent to user [$username].
```

### List File ###
Command `list file` untuk melakukan listing file yang tersedia untuk user download.

### Inbox ###
Command `inbox` untuk melihat apakah ada pesan masuk atau tidak.
> Server Respond
```bash
$count message incoming.
from $username : $message
```

### Download ###
Command `get file` untuk melakukan unduh pada file yang ada.
> #### Parameter ####
```bash
File Name: 
Recipient Username:
```
> #### Example ###
```bash
send file
File Name: $nama_file
Recipient Username: a
```
> Server Respond
```bash
Berhasil mengirim file ! $nama_file telah dikirim.
```

### Upload ###
Command `send file` untuk mengirim file kepada user lain.
> #### Parameter ####
```bash
File Name: 
Recipient Username:
```
> #### Example ###
```bash
send file
File Name: $nama_file
Recipient Username: a
```
> Server Respond
```bash
Berhasil mengirim file ! $nama_file telah dikirim.
```

### Logout ###
Command `logout` untuk keluar dari akun saat ini.
> Server Respond
```bash
Bye bye !
```

# Server
Semua data dikirimkan dalam bentuk urlencoded data, lihatlah contoh jika bingung. Semua perintah dikirim dalam bentuk `command` `payload`
## Autentikasi User
Command `auth`

Payload :
  username | string
  password | string

Example :
```
  Input : 
    auth usernam=pass&password=pass
  Output :
    status : `OK` atau `ERROR`
    message : String
```

## Register
Command `register`
Payload :
```
  username | string
  password | string
  nationality | string
  name | string
```

Example:
```
  Input:
    register username=aa&nationality=aa&password=aa&name=alam
  Output:
    status: `OK` atau `ERROR`
    message: String
```

## Inbox
Command `inbox`
Payload :
```
  session | string
```

Example :
```
Input:
  inbox session=0949r433394tr94ug5gu45t
Output:
  session: String
```

## Logout
Command `logout`
Payload:
```
  session | string
```

Example:
```
  Input:
  logout session=0949r433394tr94ug5gu45t
  Output:
  session:String
```

## File List
Command `file_list`
Payload:
```
  session | string
```
Example:
```
  Input:
  list_file session=0949r433394tr94ug5gu45t
  Output:
  session:String
  message:String
```

