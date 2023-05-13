url = "http://daum.com"
mystr =url.replace("http://","")

print(mystr)

mystr =mystr[:mystr.index(".")]
print(mystr)

password = mystr[:3]+ str(len(mystr)) + str(mystr.count("e"))+ "!"

print("{0}의 비밀번호는 {1} 입니다".format(url , password))
