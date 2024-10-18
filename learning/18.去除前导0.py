def remove_leading_zeros(ip_address):
    # 分割IPv4地址为四组数字
    parts = ip_address.split('.')
    # 去除每组数字的前导零
    cleaned_parts = [int(part) for part in parts]  # 转换为整数自动去除前导零
    # 重新组合为一个清理后的IPv4地址字符串
    cleaned_ip = '.'.join(map(str, cleaned_parts))
    return cleaned_ip


def remove_leading_zeros_zhao(ip_address):
    ip_parts = ip_address.split('.')
    ip_parts = [int(ip_part) for ip_part in ip_parts]
    cleaned_ip = '.'.join(map(str, ip_parts))
    return cleaned_ip

# 示例使用
original_ip = "192.168.1.001"
cleaned_ip = remove_leading_zeros(original_ip)
print(f"原始IP地址: {original_ip}, 清理后的IP地址: {cleaned_ip}")
cleaned_ip_zhao = remove_leading_zeros_zhao(original_ip)
print(f"原始IP地址: {original_ip}, 清理后的IP地址: {cleaned_ip}")
