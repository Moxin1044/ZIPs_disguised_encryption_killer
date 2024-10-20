old_byte = '504B0304140000'
new_byte = '504B0304140001'

files = "test.zip"

# 将十六进制字符串转换为字节数组
old_bytes = bytes.fromhex(old_byte)
new_bytes = bytes.fromhex(new_byte)

with open(files, 'rb') as file:
    content = file.read()

content_bytes = bytearray(content)
print(content_bytes)

start = 0
while True:
    start = content_bytes.find(old_bytes, start)
    if start == -1:
        print("没有找到")
        break
    content_bytes[start:start+len(old_bytes)] = new_bytes
    print("找到了")
    start += len(old_bytes)  # 更新 start 位置

with open(files, 'wb') as file:
    file.write(content_bytes)

