# 交大集群使用指南

## 交大集群 
> （随便选择一台登录）,账号都是hqlabadmin，密码是nb408
* CS0：主机www.tek-pi.com 端口号10180
* CS1：主机www.tek-pi.com 端口号10181
* CS2：主机www.tek-pi.com 端口号10182
* CS3：主机www.tek-pi.com 端口号10183
* CS4：主机www.tek-pi.com 端口号10184
* CSBig：主机www.tek-pi.com 端口号410
* GS0：主机www.tek-pi.com 端口号10186

## Run docker
```bash
sudo docker run \
    -v /home/lvli/Documents/incident/derenzo_trymac:/home/derenzo_trymac \
    -it -d 192.168.1.133:5000/slurm:v0.0.13

# 进入docker
$ sudo docker exec -it slurm-0.0.11 bash # 交大集群
$ sudo docker exec -it slurm-0.0.13 bash # 410集群

# 启动pygate：
$ source /after_reboot.sh

$ pygate init subdir -n 200     
$ pygate init bcast   
$ pygate submit
$ pygate clean –d     
$ squeue
$ scancel –u tb                           # 删除该用户所有运行程序
$ seq 83252 83302                         # 83252-83302所有的值
seq 83252 83302 | xargs scancel           # 把值传给scancel

# 
$ root –b result.root
$ pygate merge --target result.root --method had
$ find -name *.root | head -n 30 | tr '\n' ' ' > command.sh
$ hadd result.root                        # 实现有选择地merge30个root
```