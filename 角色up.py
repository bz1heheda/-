from random import  *
def ifr(a,b):
  c=randint(0,b-1)
  if(c<a):
    return True
t=0
cz={1:'琴',2:"迪卢克",3:"七七",4:"莫娜",5:"刻晴"}
up="胡桃"
dbd=False
for i in range(180):#修改range后面括号中的数字以修改抽卡次数
  t=t+1
  if(t<73):
    if(ifr(5,1000)):
      if(randint(0,1) and dbd==False):
        print(5*"⭐️"," ",cz[randint(1,5)],t)
        dbd=True
      else:
        print(5*"⭐️"," ",up,t)
        dbd=False
      t=0

  else:
    r=t*55.27777-3975
    if(ifr(r,1000)):
      if(randint(0,1) and dbd==False):
        print(5*"⭐️"," ",cz[randint(1,5)],t)
        dbd=True
      else:
        print(5*"⭐️"," ",up,t)
        dbd=False
      t=0