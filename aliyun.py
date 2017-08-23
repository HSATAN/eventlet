import oss2
auth = oss2.Auth('LTAIwI0B6B1159hV', 'W8IggVC8Kh6iv6PZ3xyqQ3Yt10IfMO')
bucuket=oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'tupian-huangkaijie')
# bucuket.put_object_from_file('c68358782b5922275a9c199563ce3b01212805.png','c68358782b5922275a9c199563ce3b01212805.png')
print(bucuket.sign_url('GET','c68358782b5922275a9c199563ce3b01212805.png',10))