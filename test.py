# -*- coding: utf-8 -*-

###文件复制和替换

img = open('D:\\net_pages\\static\\netpages\\img\\self.png','r+',
               encoding = 'utf8')
    #img = 'C:\\Users\\lenovo\\Desktop\\pic\\demo.png'

img2 = open("ka.png", 'w+')
k = 3
aa = img.read(3)
while():
    img2.write(aa)

img.close()
img2.close()