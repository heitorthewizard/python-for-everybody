# python strings to bytes

 when we talk to an external resource lika a network socket we send
 bytes, so we need to encode python3 strings into a given character
 encoding

 when we read data from an external resource, we must decode it based
 on the character set so it is properly represented in python3 as a
 string

```python
while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    mystring = data.decode()
    print(mystring)
```
