# 交大集群使用指南

## docker 使用
```bash
# 首次使用需要修改docker启动配置文件
# Create or modify /etc/docker/daemon.json , add:
{ "insecure-registries":["192.168.1.133:5000","192.168.1.185:5000"] }

# Restart docker daemon
sudo service docker restart

#通过下面地址，可以查询仓库中所有镜像(Do not use proxy)
http://192.168.1.133:5000/v2/_catalog
#和某个镜像的具体版本
http://192.168.1.133:5000/v2/srf_with_anaconda/tags/list
```

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
    --name slurm-0.0.13 \
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