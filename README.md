# FinalProjectProgjar
Final Project matakuliah Pemrograman Jaringan oleh Alam, Firman dan Chendra
"Chat server"

## How To
There are 2 step to execute this programme.
run 
```bash
$py server_thread_chat.py
```
It will turn on the server and waiting for the connection. And then do
```bash
$py chat.py
```
It will turn on the client and then you can do these protocols


## Client Command Usage
### Create User ###
you can simply create user using
```bash
create_user (username) (password) (name) (nationality)
```
and the server will respond to you

### Send Message ###
simply type 
```bash
logout
```

### Group Messaging ###
simply type 
```bash
logout
```

### Logout ###
simply type 
```bash
logout
```
and then you will go logout from your current session.

### Logout ###
simply type 
```bash
logout
```
and then you will go logout from your current session.

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
  nationality | string
  password | string
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

