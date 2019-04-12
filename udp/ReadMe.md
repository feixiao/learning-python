#### 使用方法

```shell
# Server 10000 端口
python3 server.py  10000 

# Client
python3 client.py localhost 10000

```

#### 内容显示

```shell
# Server
➜  udp git:(master) ✗ python3 server.py  10000
['server.py', '10000']
UDP bound on port  10000
Receive from 127.0.0.1:53606
Receive from 127.0.0.1:53606

# Client
➜  udp git:(master) ✗ python3 client.py localhost 10000
Receive from 127.0.0.1:10000
Hello tester!

Receive from 127.0.0.1:10000
Hello tester!

```