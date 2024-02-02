def choque(a, b ,d):
    sua:a+b
    if d<=sua:
        print(True)
    else: 
        print (False)
        
# bola 1    


bola1=[]
bola1=input()
x,y,a=map(int, bola1.split())
rad1=a*2


bola2=[]
bola2=input()
p,q,b=map(int, bola2.split())
rad2=b*2

dis=((p-x)**2+(q-y)**2)**0.5
choque(rad1,rad2,dis)
