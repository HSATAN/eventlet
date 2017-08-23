import oss2
auth =oss2.Auth('LTAIwI0B6B1159hV','W8IggVC8Kh6iv6PZ3xyqQ3Yt10IfMO')
bucuket=oss2.Bucket(auth,'oss-cn-beijing.aliyuncs.com','tupian-huangkaijie')
#bucuket.put_object_from_file('laopo.jpg','laopo.jpg')
print(bucuket.sign_url('GET','laopo.jpg',120))