import paramiko


def _connect():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect('121.048.165.191', '20000', 'zhaohongye', '66666zhy')
        print('连接成功')
        return 0
    except paramiko.AuthenticationException:
        print('认证失败，请检查用户名和密码')
        return 1
    except paramiko.SSHException as e:
        print(f"SSH连接错误： {e}")
        return 2
    except Exception as e:
        print(f"连接失败：{e}")
        return 3


if __name__ == '__main__':
    _connect()
