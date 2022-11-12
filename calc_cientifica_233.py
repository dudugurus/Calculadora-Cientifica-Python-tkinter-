# CALCULADORA Cientifica 2.33 aceita expressoes,TKINTER (18/08/2022) (05/11/2022)
# Botão mr Verde com valor positivo e magenta com valor negativo
# calcula fração Geratriz ou aproximada
# converte decimal para Hexa ou ROMANOS
from tkinter import *
from math import sin,cos,tan,asin,acos,atan
import os
janela = Tk() 
#janela.geometry("680x640+30+30") 
janela.title("Calculadora Cientifica V2.33a By Edu (05/11/2022)") 
janela.resizable(0,0) # remove so maximize
janela.attributes('-fullscreen', False)
if os.name != "posix":  # (não Android ou linux)
    janela.attributes("-toolwindow",True) # remove minimize só no Windows

janela.configure(bg="grey")
hst = StringVar()
hst.set(" ")
Hist = Label(janela,textvariable=hst,width=33,justify='right',bg="light green",font=('arial',10),bd=4)
Hist.grid(row=0,column=0, columnspan=5)
inp = StringVar() 
gr = StringVar()
gr.set("grau")
RG = Button(janela,highlightbackground="blue",highlightthickness=2, bd=4, textvariable=gr,width=2,height=1, font=("arial",8))
RG.grid(row=1,column=0, columnspan=1)
screen=Entry(janela,text=inp,width=23,justify='right',bg="light green",font=('arial',10),bd=4) 
screen.grid(row=1,column=1, columnspan=4, padx=5,pady=15, ipady=5) 
screen.config(font=("arial",11,"bold"))

key_matrix = [["sin", "cos", "tan","x²",u"\u221Ax"],  
              ["2ªf" , "Pi" , "x<>y" , "a/b" , "Hex"], 
              ["mc" , "mr" , "m+" , "m-" , "C"], 
              ["7", "8", "9", "x!" , "<--"], 
              ["4", "5", "6", "*", "/"],  
              ["1", "2", "3", "+", "-"], 
              ["0", ".","(", "1/x", "="]] 

btn_dict = {} # dicionario para montar Botoes
resp = 0 # opciona usado para respotas
mc = 0 # conteudo da memoria mr 
p="" # numero em str de parenteses abertos
last="" # ultimo conteudo do visor
last_err = ""
last_ant = [] # Historico anterior Lista
Pi = 3.1415926535897932
f2=0 # 2ª função ativada=1 , desativada=0
if os.name == "posix":  # (Android ou linux)
    w = 2  # largura dos botoes para Android
else:
    w = 4  # largura dos botoes para Windows

def R2(num):
    return num**.5

def R3(num):
    return num**(1/3)

def senx(x): # calcula seno com graus
    global Pi
    return sin(Pi*x/180)

def asenx(x): # calcula arco seno para graus
    global Pi
    return asin(x)*180/Pi

def cosx(x): # calcula cosseno com graus
    global Pi
    return cos(Pi*x/180)

def acosx(x): # calcula arco cosseno para graus
    global Pi
    return acos(x)*180/Pi

def tanx(x): # calcula tangente com graus
    global Pi
    return tan(Pi*x/180)

def atanx(x): # calcula arco tangente para graus
    global Pi
    return atan(x)*180/Pi

def TriLabc(a=0,b=0,c=0): # TriABC Triangulo de lados A , B , C
    global last
    ok=""
    if a==b==c==0 :
        ok="Sem LADOS a b c !!!"
        return ok
    elif a!=0 and b!=0 and c!=0:
        if a+b >c :
            ok = "Triâng."
            if round((a**2+b**2)**.5,4) == round((c**2)**.5,4):
                ok += " Retâng."
                if a==int(a) and b==int(b) and c==int(c):
                    ok += " Pitagórico"
            else:
                pass # angulos A B C  ???
        else:
            ok = "Triângulo não existe"
    elif c==0 and a!=0 and b!=0:
        c1 = a**2+b**2
        c = c1**.5
        if c==int(c): c=int(c)
        else: c = f"R2({c1})"
        ok= f"Triâng.Ret= {a},{b}, {c}"
    elif a==b==0 and c !=0:
        cat1 = c**2/2
        if cat1==int(cat1): cat1=int(cat1)
        a=b= (cat1)**.5
        if a==int(a): a=b=int(a)
        else: a=b= f"R2({cat1})"
        ok= f"Triâng.Ret={a},{b},{c}"
        #return ok
    elif a==0 and b!=0 and c!=0:
        a1 = c**2-b**2
        a=(a1)**.5
        if a==int(a): a=int(a)
        else: a = f"R2({a1})"
        ok= f"Triâng.Ret= {a},{b},{c}"
    elif b==0 and a!=0 and c!=0:
        b1 = c**2-a**2
        b=(b1)**.5
        if b==int(b): b=int(b)
        else: b = f"R2({b1})"
        ok= f"Triâng.Ret= {a},{b},{c}"
    last_ant.append(last)
    last = last + f" R= {(eval(str(a))+eval(str(b))-eval(str(c)))/2}"
    return ok


def f2_0(op=""): # Zera 2ª função ou Ativa
    global f2
    if op=="D": f2=1 # ativa para Desativar
    elif op=="A": f2=0 # desativa para Ativar
    codigo = u"\u221Ax"
    teclaraiz = f'btn_{codigo}'
    if f2==1: # se esta ativada desativa
        btn_dict["btn_2ªf"].configure(bg="light grey")
        btn_dict[teclaraiz].configure(text=codigo)
        btn_dict["btn_."].configure(text=f".")
        btn_dict["btn_("].configure(text=f"{p}(")
        btn_dict["btn_sin"].configure(text="sin")
        btn_dict["btn_cos"].configure(text="cos")
        btn_dict["btn_tan"].configure(text="tan")
        btn_dict["btn_Hex"].configure(text="Hex")
        btn_dict["btn_Pi"].configure(text="Pi")
        f2=0
    else: # ativa 2ª função
        btn_dict["btn_2ªf"].configure(bg="cyan")
        btn_dict[teclaraiz].configure(text=f"R2(")
        btn_dict["btn_."].configure(text=f",")
        btn_dict["btn_("].configure(text=f"{p})")
        btn_dict["btn_sin"].configure(text="asin")
        btn_dict["btn_cos"].configure(text="acos")
        btn_dict["btn_tan"].configure(text="atan")
        btn_dict["btn_Hex"].configure(text="Rom")
        btn_dict["btn_Pi"].configure(text="Tri")
        f2=1

def dizima(num):
    n_int = int(num)
    if num==n_int: return str(num)
    fs = str(num+1*(num<.0001))[str(num+1).find(".")+1:]
    for x in range(len(fs)):
        a=fs[x:(x+1+fs[x+1:].find(fs[x]))]
        rep,dizima = (fs.count(a),a)
        if len(dizima)>0 and fs.count(dizima*rep)>0 and rep>(11/len(dizima)) and a!="0" :
            break
    np = fs[:x]
    denumer = int((len(dizima)==0)*"10"+len(dizima)*"9")*10**len(np)
    numer = int(str(n_int)+np+dizima)- int(str(n_int)+np)+int(str(n_int)+fs)*(len(dizima)==0)
    return f"({numer}/{denumer})"

def a_b(num): # Função Gera Fração a/b
    sn = 1
    if num < 0 :
        sn = -1
        num = abs(num)
    n_int=int(num)
    frac = num-n_int
    if frac == 0:
        btn_dict["btn_<--"].configure(bg="green")
        return "Sem parte Decimal, ERROU"
    elif frac > 1e-6:
        frac = round(frac,15)
    lst = []
    exp = 0
    for exp2 in range(16,3,-1):
        if str(1+frac).count("0"*exp2)==1 and frac<1e-5:
            exp = exp2-1
            break
    frac *= 10**exp
    while frac > 1e-8 and len(lst)<22:
        a = 1/frac # sem arredondamento
        b = int(a)
        if len(str(b)) > 4 and len(lst)>2: # Limites
            break 
        lst.append(b)
        frac = a-b
    #print("Numeros encontrados",*lst)
    if len(lst)%2:
        impar=lst[-1] ; par=0
        lst=lst+[0,0,0]
    else:
        par=lst[-1] ; impar=0
        lst=lst+[0,0]
    numer = lst[-1]
    denumer = lst[-2]*numer+1*(lst[-1]>0)
    for i in range(3,len(lst)+1,2):
        numer = lst[-i]*denumer+1*(lst[-i+1]>0)*(lst[-i+2]==0)+numer*(lst[-i+2]>0)+par*(lst[-i+2]==0) 
        denumer = lst[-i-1]*numer+1*(lst[-i]>0)*(lst[-i+1]==0)+denumer*(lst[-i+1]>0)+impar*(lst[-i+1]==0)
    denumer *= 10**exp
    numer2 = numer+1*(lst[0]>0)*(lst[1]==0)
    numer =  (numer2 + n_int*denumer)*sn
    return f"({numer}/{denumer})"

def roman(num):
    # tabela em Dicionarios dos simbolos usados
    tab = {1:{"1":"I","4":"IV","5":"V","9":"IX"},2:{"1":"X","4":"XL","5":"L","9":"XC"},3:{"1":"C","4":"CD","5":"D","9":"CM"},4:{"1":"M","4":"iv","5":"v","9":"ix"},5:{"1":"x","4":"xl","5":"l","9":"xc"},6:{"1":"c","4":"cd","5":"d","9":"cm"}, 7:{"1":"m"}}
    ln = len(num)
    if ln  == 0: return ""
    if num.isdecimal():
        num = int(num)
        if num > 3999999: return ""
        return "".join([tab[ln-i][n] if tab[ln-i].get(n) else (tab[ln-i]["5"]+(int(n)-5)*(tab[ln-i]["1"]) if n>"5" else (int(n))*(tab[ln-i]["1"])) for i,n in enumerate(str(num))])
    else:
        letras="IVXLCDMivxlcdm "
        num= num+" "
        ok = [i for i in num if i not in letras]
        if len(ok):
            print("letras em Romano não aprovadas: ",ok)
            return ""
        tab2 = {" ":0,"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000, "i" :1000,"v":5000,"x":10000,"l":50000,"c":100000,"d":500000,"m":1000000}
        return str(sum([a if (a:=tab2[num[ln-i]])>=tab2[num[ln-i+1]] else -a  for i in range(1,ln+1) ]))

def cor_mem(): # cor do botao memoria mr
    global mc 
    if mc<0:
        btn_dict["btn_mr"].configure(bg="magenta")
    elif mc>0:
        btn_dict["btn_mr"].configure(bg="green")
    elif mc==0:
        btn_dict["btn_mr"].configure(bg="light grey")
        
def grau(self): # botao para graus ou radianos
    global gr
    if gr.get()=="rad":
        gr.set("grau")
    else:
        gr.set("rad")

def cop_yx(e):
    global inp, hst, last_ant
    inp.set(hst.get()) # atualiza 2º visor com o 1º visor
    if len(last_ant)>0: hst.set(last_ant.pop()) 

RG.bind("<Button-1>",grau) # executa função grau se clicar com botao nª1 do mouse
Hist.bind("<Button-1>",cop_yx) # executa função cop_xy
    
def Calcula(event):
    global Pi, last, mc, f2, p, hst, last_ant, last_err
    button = event.widget.cget("text") 
    global key_matrix, inp, resp
    try: 
        if button == u"\u221Ax":
            if float(eval(inp.get()))<0:
                last = inp.get() 
                inp.set("Numero Negativo, ERROU")
                btn_dict["btn_<--"].configure(bg="green")
                return
            last_ant.append(last)
            last = inp.get() 
            resp = float(eval(inp.get())**(0.5)) 
            inp.set(str(resp)) 
        elif button == "R2(":
            p = str(int("0"+p)+ 1)
            inp.set(inp.get()+"R2(")
        
        elif button == "1/x":
            last_ant.append(last)
            last = inp.get() 
            resp = 1/float(eval(inp.get()))
            inp.set(str(resp))
        elif button == "Hex":
            num = int(float(inp.get()))
            tab=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
            hex=""
            while num > 0:
                r = num%16
                hex = tab[r]+hex
                num = num//16
            last_ant.append(last)
            last=inp.get()
            inp.set(hex)
        elif button == "x²":
            last_ant.append(last)
            last = inp.get() 
            resp = float(eval(inp.get()))**2 
            inp.set(str(resp)) 
        elif button == " Pi":
            last_ant.append(last)
            last = inp.get() 
            inp.set(inp.get()+"Pi")
        elif button == "Tri":
            inp.set("TriLabc(")
            p = str(int("0"+p)+ 1)
        elif button == "x<>y":
            trc = inp.get()
            inp.set(last)
            last = trc
        elif button == "a/b":
            if "ERROU" in inp.get():
                return
            num = float(eval(inp.get()))
            last_ant.append(last)
            last = inp.get()
            hst.set(dizima(num))
            inp.set(a_b(num))
        elif button == "Rom":
            resp = roman(inp.get())
            if len(resp)>0:
                last_ant.append(last)
                last = inp.get()
                inp.set(resp)
        elif button == "2ªf":
            f2_0() # desativa f2 ou ativa
        elif button[-1] == "(" or button[-1] == ")":
            pc= int("0"+p)
            if f2==0:
                p = str(pc+ 1)
                inp.set(inp.get()+ "(")
                btn_dict["btn_("].configure(text=f"{p}(")
            else:
                if pc>0:
                    p = str(pc- 1)
                    if pc==1:
                        p=""
                    inp.set(inp.get()+ ")")
                    btn_dict["btn_("].configure(text=f"{p})")
        elif button == "C":
            if inp.get()=="": hst.set("")
            p = ""
            f2_0("D") # Desativa 2ª função
            inp.set("")
            btn_dict["btn_<--"].configure(bg="light grey")
        elif button == "x!":  
            def fact(n): return 1 if n == 0 else n*fact(n-1)
            num = fact(int(inp.get()))
            last_ant.append(last)
            last = inp.get() 
            inp.set(str(num))
        elif button == "<--":
            resp = inp.get()
            if "ERROU" in resp:
                inp.set(last_err)
                btn_dict["btn_<--"].configure(bg="light grey")
            else:
                if resp[-1] == "(":
                    p = str(int("0"+p)- 1)
                    if p == "0": p=" "
                    btn_dict["btn_("].configure(text=f"{p}{resp[-1]}")
                    f2_0("D") # Desativa 2ª função
                if resp[-1] == ")":
                    p = str(int("0"+p)+ 1)
                    btn_dict["btn_("].configure(text=f"{p}{resp[-1]}")
                    f2_0("A") # Ativa 2ª função
                inp.set(resp[:-1])
        elif button[-3:] == "sin":
            p = str(int("0"+p)+ 1)
            if gr.get()=="rad":
                if f2==0:
                    inp.set(inp.get()+"sin(")
                else:
                    inp.set(inp.get()+"asin(")
            else:
                if f2==0:
                    inp.set(inp.get()+"senx(")
                else:
                    inp.set(inp.get()+"asenx(")
            f2_0("D") # zera 2ª função
        elif button[-3:] == "cos":
            p = str(int("0"+p)+ 1)
            if gr.get()=="rad":
                if f2==0:
                    inp.set(inp.get()+"cos(")
                else:
                    inp.set(inp.get()+"acos(")
            else:
                if f2==0:
                    inp.set(inp.get()+"cosx(")
                else:
                    inp.set(inp.get()+"acosx(")
            f2_0("D") # Zera 2ª função
        elif button[-3:] == "tan":
            p = str(int("0"+p)+ 1)
            if gr.get()=="rad":
                if f2==0:
                    inp.set(inp.get()+"tan(")
                else:
                    inp.set(inp.get()+"atan(")
            else:
                if f2==0:
                    inp.set(inp.get()+"tanx(")
                else:
                    inp.set(inp.get()+"atanx(")
            f2_0("D") # zera 2ª função
        elif button == "mc":
            mc=0
            cor_mem()
        elif button == "mr":
            if inp.get()=="":
                inp.set("("+str(mc)+")")
            else:
                if inp.get()[-1] in "1234567890":
                    inp.set("("+str(mc)+")")
                else:
                    last = inp.get() 
                    inp.set(inp.get()+"("+str(mc)+")")
        elif button == "m+":
            pass
            mc += float(inp.get())
            cor_mem()
        elif button == "m-":
            pass
            mc -= float(inp.get())
            cor_mem()
        elif button == ",":
            resp=inp.get()
            if len(resp)>2 :
                inp.set(resp+",")
                
        elif button == "." :
            resp=inp.get()
            if resp=="" :
                inp.set(resp+".") 
            elif resp[-1] != "." :
                if len(resp) > 2:
                    if resp[-2] != "." :
                        inp.set(resp+".")
                else:
                    inp.set(resp+".")
        elif button == "=":
            if "ERROU" in inp.get() :
                inp.set(last_err)
                btn_dict["btn_<--"].configure(bg="light grey")
            else:
                last_ant.append(last)
                last = inp.get().split()[-1]
                while last[:2] == "00": last = last[1:]
                c0=last[last.find("."):].count("0")
                c9=last[last.find("."):].count("9")
                if c9>8 or c0>8:
                    last  = str(round(float(last),max(c0,c9)-1))
                resp = eval(last)
                if type(resp) != type("A"):
                    if resp > .1:
                        resp = str(round(resp,16))
                    else:
                        resp = str(resp)
                    if len(resp)>24: resp=str(float(resp))
                if resp == last: last=last_ant.pop()
                inp.set(resp)
                hst.set(last)
                f2_0("D") # zera 2ª função 
        else: 
            inp.set(inp.get()+str(button.strip())) 
            cor_mem()
    except:
        last_err = inp.get() 
        inp.set("ERROU")
        btn_dict["btn_<--"].configure(bg="green")

for i in range(len(key_matrix)):   
    for j in range(len(key_matrix[i])):   
        btn_dict["btn_"+str(key_matrix[i][j])] = Button( 
          janela, bd=2, text=str(key_matrix[i][j]),width=w,height=1, font=("arial",11,"bold")) 
        btn_dict["btn_"+str(key_matrix[i][j])].grid( 
          row=i+2, column=j, padx=1, pady=6, ipadx=1, ipady=3) 
        btn_dict["btn_"+str(key_matrix[i][j])].bind('<Button-1>', Calcula) 
btn_dict["btn_sin"].configure(highlightbackground="blue",highlightthickness=2, bd=3)
btn_dict["btn_cos"].configure(highlightbackground="blue",highlightthickness=2, bd=3)
btn_dict["btn_tan"].configure(highlightbackground="blue",highlightthickness=2, bd=3)

janela.mainloop()
