import paramiko
import time

def execute_command_with_transport(hostname, port, username, password, command):
    # 创建SSH客户端
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port, username, password)

    # 打开一个新的会话并执行命令
    transport = client.get_transport()
    channel = transport.open_session()
    # channel.exec_command('cd neurosim')
    channel.exec_command(command)

    # 持续读取输出直到命令完成
    while True:
        if channel.exit_status_ready():
            break
        while channel.recv_ready():
            output = channel.recv(1024).decode('utf-8')
            print(output, end='')  # 这里可以处理输出内容，例如更新GUI
        time.sleep(1)

    # 处理残留输出
    while channel.recv_ready():
        output = channel.recv(1024).decode('utf-8')
        print(output, end='')

    channel.close()
    client.close()


def execute_command_with_shell(hostname, port, username, password, command):
    # 创建SSH客户端
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port, username, password)

    # 启动一个交互式shell会话
    shell = client.invoke_shell()
    print(f"shell:{shell}")

    # 测试send是否会开启一个新的shell窗口环境。看两个send是否有连续性，也就是ls是不是在neurosim下执行。
    shell.send('cd neurosim/' + "\n")
    shell.send('ls' + '\n')
    output = shell.recv(1024).decode('utf-8')
    print(output, end='')

    # 发送命令到shell
    shell.send(command + "\n")


    # 读取shell的输出
    while True:
        if shell.recv_ready():
            output = shell.recv(1024).decode('utf-8')
            print(output, end='')  # 这里可以处理输出内容，例如更新GUI
        if shell.exit_status_ready():
            break
        time.sleep(1)



    # 关闭连接
    client.close()

def execute_command_with_execcommand(hostname, port, username,password, command):
    # 创建SSH客户端
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port, username, password)
    stdin, stdout, stderr = client.exec_command(command)

    while True:
        line = stdout.readline()
        if not line:
            break
        print(line)

    # Optionally, handle stderr as well
    err = stderr.read()
    if err:
        print(err.decode('utf-8'))

 # 只能执行一条命令
def connect_and_execute(hostname, port, username, password, cmd):
    # 创建SSH客户端
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port, username, password)

    # 每次执行命令会返回3个对象，对应标准输入、标准输出、标准错误
    stdin, stdout, stderr = client.exec_command(cmd)
    # 从标准输出、标准错误中提取字节
    stdout_Bytes = stdout.read()
    stderr_Bytes = stderr.read()
    outputBytes = stdout_Bytes + stderr_Bytes
    # 解码为字符串
    outputStr = outputBytes.decode('utf-8')
    print(outputStr,end='')

    # 关闭ssh连接
    # self.ssh.close()
    return outputBytes.decode('utf-8')

# 示例调用
hostname = "121.48.165.191"
port = 20000
username = "zhaohongye"
password = "66666zhy"
command = "./a.out"
cmd = 'ls'
# execute_command(hostname, port, username, password, command)
# execute_command_with_shell(hostname, port, username, password, command)
# execute_command_with_execcommand(hostname, port, username, password, command)
# connect_and_execute(hostname, port, username, password, command)
execute_command_with_transport(hostname, port, username, password, cmd)