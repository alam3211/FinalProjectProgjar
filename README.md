# FinalProjectProgjar
Final Project matakuliah Pemrograman Jaringan oleh Alam, Firman dan Chendra
"Chat server"

## How To
There are 2 step to execute this programme.
run 
```bash
$py server.py
```
It will turn on the server and waiting for the connection. And then do
```bash
$py chat.py
```
It will turn on the client and then you can do these protocols


# Client Command Usage
* ### Register ###
```bash
register
```
#### Parameter ####
```bash
Username :
Password :
Name :
Nationality :
```
#### Example ###
```bash
register
Username : alam
Password : password
Name : alamcahya
Nationality : Indonesia
```
Server Respond
```bash
User berhasil dibuat
```

* ### Autentikasi ###
```bash
login
```
#### Parameter ####
```bash
Username :
Password :
```
#### Example ###
```bash
register
Username : alam
Password : password
```
Server Respond
```bash
Login [$username] telah berhasil
```

* ### Send Message ###
```bash
chat
```
#### Parameter ####
```bash
Recipient username:
Message:
```
#### Example ###
```bash
send
Recipient username: alam
Message: halo testing
```
Server Respond
```bash
Message sent to user [$username].
```

* ### List File ###
```bash
list file
```

* ### Inbox ###
```bash
inbox
```
Server Respond
```bash
$count message incoming.
from $username : $message
```

* ### Download ###
```bash
get file
```

### Upload ###
```bash
send file
```
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
Server Respond
```bash
Berhasil mengirim file ! $nama_file telah dikirim.
```

* ### Logout ###
```bash
logout
```
Server Respond
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

