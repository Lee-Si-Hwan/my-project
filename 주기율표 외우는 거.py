import random



jock1 = ['H','Li','Na','K','Rb','Cs','Fr']
jock2 = ['Be','Mg','Ca','Sr','Ba','Ra']
jock3 = ['Sc','Y']
jock4 = ['Ti','Zr','Hf',]
jock5 = ['V','Nb','Ta',]
jock6 = ['Cr','Mo','W',]
jock7 = ['Mn','Tc','Re',]
jock8 = ['Fe','Ru','Os',]
jock9 = ['Co','Rh','Ir',]
jock10 = ['Ni','Pd','Pt',]
jock11 = ['Cu','Ag','Au',]
jock12 = ['Zn','Cd','Hg',]
jock13 = ['B','Al','Ga','In','Tl',]
jock14 = ['C','Si','Ge','Sn','Pb',]
jock15 = ['N','P','As','Sb','Bi']
jock16 = ['O','S','Se','Te','Po']
jock17 = ['F','Cl','Br','I','At']
jock18 = ['He','Ne','Ar','Kr','Xe','Rn']
lan = ['La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu']
ac = ['Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr']

n1 = ['수소','리튬','나트륨','칼륨','루비듐','세슘','프랑슘']
n2 = ['베릴륨','마그네슘','칼슘','스트론튬','바륨','라듐']
n3 = ['스칸듐','이트륨']
n4 = ['타이타늄','지르코늄','하프늄']
n5 = ['바나듐','나이오븀','탄탈럼']
n6 =['크로뮴', '몰리브데넘','텅스텐']
n7=['망가니즈','테크네튬','레늄']
n8=['철','루테늄','오스뮴']
n9=['코발트','로듐','이리듐']
n10=['니켈','팔라듐','백금']
n11=['구리','은','금']
n12=['아연','카드뮴','수은']
n13=['붕소','알루미늄','갈륨','인듐','탈륨']
n14=['탄소','규소','저마늄','주석','납']
n15=['질소','인','비소','안티모니','비스무트']
n16=['산소','황','셀레늄','텔루륨','폴로늄']
n17=['플루오린','염소','브로민','아이오딘','아스타틴']
n18=['헬륨','네온','아르곤','크립톤','제논','라돈']
nlan=['란타넘','세륨','프라세오디뮴','네오디뮴','프로메튬','사마륨','유로퓸','가돌리늄','터븀','디스프로슘','홀뮴','어븀','툴륨','이터븀','루테튬']
nac=['악티늄','토륨','프로트악티늄','우라늄','넵투늄','플루토늄','아메리슘','퀴륨','버클륨','캘리포늄','아인슈타이늄','페르뮴','멘델레븀','노벨륨','로렌슘']
x = 0
def start():#########시작 함수
    G = input("[원자이름]:1, [원자기호]:2, [원자번호]:3 중에서 원하는 모드를 타이핑해주세요: ")
    if G == "1":
        All()
    elif G == "2":
        jock()
    elif G == "3":
        num()
    else:
        start()

def All():#####################################################################################원소 이름 문제
    global x
    global R
    global j
    global name
    R = random.randint(1,103)
    if R == 1 or R == 3 or R == 11 or R == 19 or R == 37 or R == 55 or R == 87:
        if R == 1:
            x = 0
        if R == 3:
            x = 1
        if R == 11:
            x = 2
        if R == 19:
            x = 3
        if R == 37:
            x = 4
        if R == 55:
            x = 5
        if R == 87:
            x = 6
        j = '1'
        name = n1[x]
        print(jock1[x])
        Q()
    if R == 4 or R == 12 or R == 20 or R == 38 or R == 56 or R == 88 :
        if R == 4:
            x = 0
        elif R == 12:
            x = 1
        elif R == 20:
            x = 2
        elif R == 38:
            x = 3
        elif R == 56:
            x = 4
        elif R == 88:
            x = 5
        j = '2'
        name = n2[x]
        print(jock2[x])
        Q()
    if R == 21 or R == 39:
        if R == 21:
            x = 0
        elif R == 39:
            x = 1
        j = '3'
        name = n3[x]
        print(jock3[x])
        Q()
    if R == 22 or R == 40 or R == 72:
        if R == 22:
            x = 0
        elif R == 40:
            x = 1
        elif R == 72:
            x = 2

        j = '4'
        name = n4[x]
        print(jock4[x])
        Q()
    if R == 23 or R == 41 or R == 73:
        if R == 23:
            x = 0
        elif R == 41:
            x = 1
        elif R == 73:
            x = 2
        j = '5'
        name = n5[x]
        print(jock5[x])
        Q()
    if R == 24 or R == 42 or R == 74:
        if R == 24:
            x = 0
        elif R == 42:
            x = 1
        elif R == 74:
            x = 2
        j = '6'
        name = n6[x]
        print(jock6[x])
        Q()
    if R == 25 or R == 43 or R == 75:
        if R == 25:
            x = 0
        elif R == 43:
            x = 1
        elif R == 75:
            x = 2
        j = '7'
        name = n7[x]
        print(jock7[x])
        Q()
    if R == 26 or R == 44 or R == 76:
        if R == 26:
            x = 0
        elif R == 44:
            x = 1
        elif R == 76:
            x = 2
        j = '8'
        name = n8[x]
        print(jock8[x])
        Q()
    if R == 27 or R == 45 or R == 77:
        if R == 27:
            x = 0
        elif R == 45:
            x = 1
        elif R == 77:
            x = 2
        j = '9'
        name = n9[x]
        print(jock9[x])
        Q()
    if R == 28 or R == 46 or R == 78:
        if R == 28:
            x = 0
        elif R == 46:
            x = 1
        elif R == 78:
            x = 2
        j = '10'
        name = n10[x]
        print(jock10[x])
        Q()
    if R == 29 or R == 47 or R == 79:
        if R == 29:
            x = 0
        elif R == 47:
            x = 1
        elif R == 79:
            x = 2
        j = '11'
        name = n11[x]
        print(jock11[x])
        Q()
    if R == 30 or R == 48 or R == 80:
        if R == 30:
            x = 0
        elif R == 48:
            x = 1
        elif R == 80:
            x = 2
        j = '12'
        name = n12[x]
        print(jock12[x])
        Q()
    if R == 5 or R == 13 or R == 31 or R == 49 or R == 81:
        if R == 5:
            x = 0
        elif R == 13:
            x = 1
        elif R == 31:
            x = 2
        elif R == 49:
            x = 3
        elif R == 81:
            x = 4
        j = '13'
        name = n13[x]
        print(jock13[x])
        Q()
    if R == 6 or R == 14 or R == 32 or R == 50 or R == 82:
        if R == 6:
            x = 0
        elif R == 14:
            x = 1
        elif R == 32:
            x = 2
        elif R == 50:
            x = 3
        elif R == 82:
            x = 4
        j = '14'
        name = n14[x]
        print(jock14[x])
        Q()
    if R == 7 or R == 15 or R == 33 or R == 51 or R == 83:
        if R == 7:
            x = 0
        elif R == 15:
            x = 1
        elif R == 33:
            x = 2
        elif R == 51:
            x = 3
        elif R == 83:
            x = 4
        j = '15'
        name = n15[x]
        print(jock15[x])
        Q()
    if R == 8 or R == 16 or R == 34 or R == 52 or R == 84:
        if R == 8:
            x = 0
        elif R == 16:
            x = 1
        elif R == 34:
            x = 2
        elif R == 52:
            x = 3
        elif R == 84:
            x = 4
        j = '16'
        name = n16[x]
        print(jock16[x])
        Q()
    if R == 9 or R == 17 or R == 35 or R == 53 or R == 85:
        if R == 9:
            x = 0
        elif R == 17:
            x = 1
        elif R == 35:
            x = 2
        elif R == 53:
            x = 3
        elif R == 85:
            x = 4

        j = '17'
        name = n17[x]
        print(jock17[x])
        Q()
    if R == 2 or R == 10 or R == 18 or R == 36 or R == 54 or R == 86:
        if R == 2:
            x = 0
        elif R == 10:
            x = 1
        elif R == 18:
            x = 2
        elif R == 36:
            x = 3
        elif R == 54:
            x = 4
        elif R == 86:
            x = 5
        j = '18'
        name = n18[x]
        print(jock18[x])
        Q()
    if R >= 89 and R <= 103:
        if R == 89:
            x = 0
        elif R == 90:
            x = 1
        elif R == 91:
            x = 2
        elif R == 92:
            x = 3
        elif R == 93:
            x = 4
        elif R == 94:
            x = 5
        elif R == 95:
            x = 6
        elif R == 96:
            x = 7
        elif R == 97:
            x = 8
        elif R == 98:
            x = 9
        elif R == 99:
            x = 10
        elif R == 100:
            x = 11
        elif R == 101:
            x = 12
        elif R == 102:
            x = 13
        elif R == 103:
            x = 14

        j = '악티늄'
        name = nac[x]
        print(ac[x])
        Q()

    if R >= 57 and R <= 71:
        if R == 57:
            x = 0
        elif R == 58:
            x = 1
        elif R == 59:
            x = 2
        elif R == 60:
            x = 3
        elif R == 61:
            x = 4
        elif R == 62:
            x = 5
        elif R == 63:
            x = 6
        elif R == 64:
            x = 7
        elif R == 65:
            x = 8
        elif R == 66:
            x = 9
        elif R == 67:
            x = 10
        elif R == 68:
            x = 11
        elif R == 69:
            x = 12
        elif R == 70:
            x = 13
        elif R == 71:
            x = 14

        j = '란타넘'
        name = nlan[x]
        print(lan[x])
        Q()

def jock():########################################################################################원소 기호 문제
    global x
    global R
    global j
    global sign
    R = random.randint(1,103)
    if R == 1 or R == 3 or R == 11 or R == 19 or R == 37 or R == 55 or R == 87:
        if R == 1:
            x = 0
        if R == 3:
            x = 1
        if R == 11:
            x = 2
        if R == 19:
            x = 3
        if R == 37:
            x = 4
        if R == 55:
            x = 5
        if R == 87:
            x = 6
        j = '1'
        sign = jock1[x]
        print(n1[x])
        Q1()
    if R == 4 or R == 12 or R == 20 or R == 38 or R == 56 or R == 88 :
        if R == 4:
            x = 0
        elif R == 12:
            x = 1
        elif R == 20:
            x = 2
        elif R == 38:
            x = 3
        elif R == 56:
            x = 4
        elif R == 88:
            x = 5
        j = '2'
        sign = jock2[x]
        print(n2[x])
        Q1()
    if R == 21 or R == 39:
        if R == 21:
            x = 0
        elif R == 39:
            x = 1
        j = '3'
        sign = jock3[x]
        print(n3[x])
        Q1()
    if R == 22 or R == 40 or R == 72:
        if R == 22:
            x = 0
        elif R == 40:
            x = 1
        elif R == 72:
            x = 2

        j = '4'
        sign = jock4[x]
        print(n4[x])
        Q1()
    if R == 23 or R == 41 or R == 73:
        if R == 23:
            x = 0
        elif R == 41:
            x = 1
        elif R == 73:
            x = 2
        j = '5'
        sign = jock5[x]
        print(n5[x])
        Q1()
    if R == 24 or R == 42 or R == 74:
        if R == 24:
            x = 0
        elif R == 42:
            x = 1
        elif R == 74:
            x = 2
        j = '6'
        sign = jock6[x]
        print(n6[x])
        Q1()
    if R == 25 or R == 43 or R == 75:
        if R == 25:
            x = 0
        elif R == 43:
            x = 1
        elif R == 75:
            x = 2
        j = '7'
        sign = jock7[x]
        print(n7[x])
        Q1()
    if R == 26 or R == 44 or R == 76:
        if R == 26:
            x = 0
        elif R == 44:
            x = 1
        elif R == 76:
            x = 2
        j = '8'
        sign = jock8[x]
        print(n8[x])
        Q1()
    if R == 27 or R == 45 or R == 77:
        if R == 27:
            x = 0
        elif R == 45:
            x = 1
        elif R == 77:
            x = 2
        j = '9'
        sign = jock9[x]
        print(n9[x])
        Q1()
    if R == 28 or R == 46 or R == 78:
        if R == 28:
            x = 0
        elif R == 46:
            x = 1
        elif R == 78:
            x = 2
        j = '10'
        sign = jock10[x]
        print(n10[x])
        Q1()
    if R == 29 or R == 47 or R == 79:
        if R == 29:
            x = 0
        elif R == 47:
            x = 1
        elif R == 79:
            x = 2
        j = '11'
        sign = jock11[x]
        print(n11[x])
        Q1()
    if R == 30 or R == 48 or R == 80:
        if R == 30:
            x = 0
        elif R == 48:
            x = 1
        elif R == 80:
            x = 2
        j = '12'
        sign = jock12[x]
        print(n12[x])
        Q1()
    if R == 5 or R == 13 or R == 31 or R == 49 or R == 81:
        if R == 5:
            x = 0
        elif R == 13:
            x = 1
        elif R == 31:
            x = 2
        elif R == 49:
            x = 3
        elif R == 81:
            x = 4
        j = '13'
        sign = jock13[x]
        print(n13[x])
        Q1()
    if R == 6 or R == 14 or R == 32 or R == 50 or R == 82:
        if R == 6:
            x = 0
        elif R == 14:
            x = 1
        elif R == 32:
            x = 2
        elif R == 50:
            x = 3
        elif R == 82:
            x = 4
        j = '14'
        sign = jock14[x]
        print(n14[x])
        Q1()
    if R == 7 or R == 15 or R == 33 or R == 51 or R == 83:
        if R == 7:
            x = 0
        elif R == 15:
            x = 1
        elif R == 33:
            x = 2
        elif R == 51:
            x = 3
        elif R == 83:
            x = 4
        j = '15'
        sign = jock15[x]
        print(n15[x])
        Q1()
    if R == 8 or R == 16 or R == 34 or R == 52 or R == 84:
        if R == 8:
            x = 0
        elif R == 16:
            x = 1
        elif R == 34:
            x = 2
        elif R == 52:
            x = 3
        elif R == 84:
            x = 4
        j = '16'
        sign = jock16[x]
        print(n16[x])
        Q1()
    if R == 9 or R == 17 or R == 35 or R == 53 or R == 85:
        if R == 9:
            x = 0
        elif R == 17:
            x = 1
        elif R == 35:
            x = 2
        elif R == 53:
            x = 3
        elif R == 85:
            x = 4

        j = '17'
        sign = jock17[x]
        print(n17[x])
        Q1()
    if R == 2 or R == 10 or R == 18 or R == 36 or R == 54 or R == 86:
        if R == 2:
            x = 0
        elif R == 10:
            x = 1
        elif R == 18:
            x = 2
        elif R == 36:
            x = 3
        elif R == 54:
            x = 4
        elif R == 86:
            x = 5
        j = '18'
        sign = jock18[x]
        print(n18[x])
        Q1()
    if R >= 89 and R <= 103:
        if R == 89:
            x = 0
        elif R == 90:
            x = 1
        elif R == 91:
            x = 2
        elif R == 92:
            x = 3
        elif R == 93:
            x = 4
        elif R == 94:
            x = 5
        elif R == 95:
            x = 6
        elif R == 96:
            x = 7
        elif R == 97:
            x = 8
        elif R == 98:
            x = 9
        elif R == 99:
            x = 10
        elif R == 100:
            x = 11
        elif R == 101:
            x = 12
        elif R == 102:
            x = 13
        elif R == 103:
            x = 14

        j = '악티늄'
        sign = ac[x]
        print(nac[x])
        Q1()

    if R >= 57 and R <= 71:
        if R == 57:
            x = 0
        elif R == 58:
            x = 1
        elif R == 59:
            x = 2
        elif R == 60:
            x = 3
        elif R == 61:
            x = 4
        elif R == 62:
            x = 5
        elif R == 63:
            x = 6
        elif R == 64:
            x = 7
        elif R == 65:
            x = 8
        elif R == 66:
            x = 9
        elif R == 67:
            x = 10
        elif R == 68:
            x = 11
        elif R == 69:
            x = 12
        elif R == 70:
            x = 13
        elif R == 71:
            x = 14

        j = '란타넘'
        sign = lan[x]
        print(nlan[x])
        Q1()



def num():#####################################################################################원소 번호 문제
    global x
    global R
    global j
    global name
    global sign
    R = random.randint(1,103)
    if R == 1 or R == 3 or R == 11 or R == 19 or R == 37 or R == 55 or R == 87:
        if R == 1:
            x = 0
        if R == 3:
            x = 1
        if R == 11:
            x = 2
        if R == 19:
            x = 3
        if R == 37:
            x = 4
        if R == 55:
            x = 5
        if R == 87:
            x = 6
        j = '1'
        name = n1[x]
        sign = jock1[x]
        print(R)
        Q3()
    if R == 4 or R == 12 or R == 20 or R == 38 or R == 56 or R == 88 :
        if R == 4:
            x = 0
        elif R == 12:
            x = 1
        elif R == 20:
            x = 2
        elif R == 38:
            x = 3
        elif R == 56:
            x = 4
        elif R == 88:
            x = 5
        j = '2'
        name = n2[x]
        sign = jock2[x]
        print(R)
        Q3()
    if R == 21 or R == 39:
        if R == 21:
            x = 0
        elif R == 39:
            x = 1
        j = '3'
        name = n3[x]
        sign = jock3[x]
        print(R)
        Q3()
    if R == 22 or R == 40 or R == 72:
        if R == 22:
            x = 0
        elif R == 40:
            x = 1
        elif R == 72:
            x = 2

        j = '4'
        name = n4[x]
        sign = jock4[x]
        print(R)
        Q3()
    if R == 23 or R == 41 or R == 73:
        if R == 23:
            x = 0
        elif R == 41:
            x = 1
        elif R == 73:
            x = 2
        j = '5'
        name = n5[x]
        sign = jock5[x]
        print(R)
        Q3()
    if R == 24 or R == 42 or R == 74:
        if R == 24:
            x = 0
        elif R == 42:
            x = 1
        elif R == 74:
            x = 2
        j = '6'
        name = n6[x]
        sign = jock6[x]
        print(R)
        Q3()
    if R == 25 or R == 43 or R == 75:
        if R == 25:
            x = 0
        elif R == 43:
            x = 1
        elif R == 75:
            x = 2
        j = '7'
        name = n7[x]
        sign = jock7[x]
        print(R)
        Q3()
    if R == 26 or R == 44 or R == 76:
        if R == 26:
            x = 0
        elif R == 44:
            x = 1
        elif R == 76:
            x = 2
        j = '8'
        name = n8[x]
        sign = jock8[x]
        print(R)
        Q3()
    if R == 27 or R == 45 or R == 77:
        if R == 27:
            x = 0
        elif R == 45:
            x = 1
        elif R == 77:
            x = 2
        j = '9'
        name = n9[x]
        sign = jock9[x]
        print(R)
        Q3()
    if R == 28 or R == 46 or R == 78:
        if R == 28:
            x = 0
        elif R == 46:
            x = 1
        elif R == 78:
            x = 2
        j = '10'
        name = n10[x]
        sign = jock10[x]
        print(R)
        Q3()
    if R == 29 or R == 47 or R == 79:
        if R == 29:
            x = 0
        elif R == 47:
            x = 1
        elif R == 79:
            x = 2
        j = '11'
        name = n11[x]
        sign = jock11[x]
        print(R)
        Q3()
    if R == 30 or R == 48 or R == 80:
        if R == 30:
            x = 0
        elif R == 48:
            x = 1
        elif R == 80:
            x = 2
        j = '12'
        name = n12[x]
        sign = jock12[x]
        print(R)
        Q3()
    if R == 5 or R == 13 or R == 31 or R == 49 or R == 81:
        if R == 5:
            x = 0
        elif R == 13:
            x = 1
        elif R == 31:
            x = 2
        elif R == 49:
            x = 3
        elif R == 81:
            x = 4
        j = '13'
        name = n13[x]
        sign = jock13[x]
        print(R)
        Q3()
    if R == 6 or R == 14 or R == 32 or R == 50 or R == 82:
        if R == 6:
            x = 0
        elif R == 14:
            x = 1
        elif R == 32:
            x = 2
        elif R == 50:
            x = 3
        elif R == 82:
            x = 4
        j = '14'
        name = n14[x]
        sign = jock14[x]
        print(R)
        Q3()
    if R == 7 or R == 15 or R == 33 or R == 51 or R == 83:
        if R == 7:
            x = 0
        elif R == 15:
            x = 1
        elif R == 33:
            x = 2
        elif R == 51:
            x = 3
        elif R == 83:
            x = 4
        j = '15'
        name = n15[x]
        sign = jock15[x]
        print(R)
        Q3()
    if R == 8 or R == 16 or R == 34 or R == 52 or R == 84:
        if R == 8:
            x = 0
        elif R == 16:
            x = 1
        elif R == 34:
            x = 2
        elif R == 52:
            x = 3
        elif R == 84:
            x = 4
        j = '16'
        name = n16[x]
        sign = jock16[x]
        print(R)
        Q3()
    if R == 9 or R == 17 or R == 35 or R == 53 or R == 85:
        if R == 9:
            x = 0
        elif R == 17:
            x = 1
        elif R == 35:
            x = 2
        elif R == 53:
            x = 3
        elif R == 85:
            x = 4

        j = '17'
        name = n17[x]
        sign = jock17[x]
        print(R)
        Q3()
    if R == 2 or R == 10 or R == 18 or R == 36 or R == 54 or R == 86:
        if R == 2:
            x = 0
        elif R == 10:
            x = 1
        elif R == 18:
            x = 2
        elif R == 36:
            x = 3
        elif R == 54:
            x = 4
        elif R == 86:
            x = 5
        j = '18'
        name = n18[x]
        sign = jock18[x]
        print(R)
        Q3()
    if R >= 89 and R <= 103:
        if R == 89:
            x = 0
        elif R == 90:
            x = 1
        elif R == 91:
            x = 2
        elif R == 92:
            x = 3
        elif R == 93:
            x = 4
        elif R == 94:
            x = 5
        elif R == 95:
            x = 6
        elif R == 96:
            x = 7
        elif R == 97:
            x = 8
        elif R == 98:
            x = 9
        elif R == 99:
            x = 10
        elif R == 100:
            x = 11
        elif R == 101:
            x = 12
        elif R == 102:
            x = 13
        elif R == 103:
            x = 14

        j = '악티늄'
        name = nac[x]
        sign = ac[x]
        print(R)
        Q3()

    if R >= 57 and R <= 71:
        if R == 57:
            x = 0
        elif R == 58:
            x = 1
        elif R == 59:
            x = 2
        elif R == 60:
            x = 3
        elif R == 61:
            x = 4
        elif R == 62:
            x = 5
        elif R == 63:
            x = 6
        elif R == 64:
            x = 7
        elif R == 65:
            x = 8
        elif R == 66:
            x = 9
        elif R == 67:
            x = 10
        elif R == 68:
            x = 11
        elif R == 69:
            x = 12
        elif R == 70:
            x = 13
        elif R == 71:
            x = 14

        j = '란타넘'
        name = nlan[x]
        sign = lan[x]
        print(R)
        Q3()






def Q():###############퀴즈내는 함수
    global R
    global j
    global name
    answer = input("위 원소의 이름을 쓰시오:")
    if answer == name:
        answer = int(input("위 원소의 번호만 쓰세요.(숫자만): "))
        if answer == R:
            answer = input("위 원소의 족만 쓰세요.: ")
            if answer == j:
                print('정답입니다.')
                print()
                print()
            else:
                print('틀렸습니다. 답은 ',name,',',R,'번, ',j,'족 입니다.')
                print()
                print()
        else:
            print('틀렸습니다. 답은 ',name,',',R,'번, ',j,'족 입니다.')
            print()
            print()
    else:
        print('틀렸습니다. 답은 ',name,',',R,'번, ',j,'족 입니다.')
        print()
        print()
    answer = int(input("계속하시겠습니까?(1 or 2) : "))
    if answer == 1:
        All()
    elif answer == 2:
        start()
    else:
        All()   
            
        

def Q1():###############퀴즈내는 함수
    global R
    global j
    global sign
    answer = input("위 원소의 기호를 쓰시오:")
    if answer == sign:
        answer = int(input("위 원소의 번호만 쓰세요.(숫자만): "))
        if answer == R:
            answer = input("위 원소의 족만 쓰세요.: ")
            if answer == j:
                print('정답입니다.')
                print()
                print()
            else:
                print('틀렸습니다. 답은 ',sign,',',R,'번, ',j,'족 입니다.')
                print()
                print()
        else:
            print('틀렸습니다. 답은 ',sign,',',R,'번, ',j,'족 입니다.')
            print()
            print()
    else:
        print('틀렸습니다. 답은 ',sign,',',R,'번, ',j,'족 입니다.')
        print()
        print()
    answer = int(input("계속하시겠습니까?(1 or 2) : "))
    if answer == 1:
        jock()
    elif answer == 2:
        start()
    else:
        jock()   

def Q3():###############퀴즈내는 함수
    global name
    global j
    global sign
    answer = input("위 원소의 이름을 쓰시오:")
    if answer == name:
        answer = input("위 원소의 기호만 쓰세요.: ")
        if answer == sign:
            answer = input("위 원소의 족만 쓰세요.: ")
            if answer == j:
                print('정답입니다.')
                print()
                print()
            else:
                print('틀렸습니다. 답은 ',name,',',sign,',',j,'족 입니다.')
                print()
                print()
        else:
            print('틀렸습니다. 답은 ',name,',',sign,',',j,'족 입니다.')
            print()
            print()
    else:
        print('틀렸습니다. 답은 ',name,',',sign,',',j,'족 입니다.')
        print()
        print()
    answer = int(input("계속하시겠습니까?(1 or 2) : "))
    if answer == 1:
        num()
    elif answer == 2:
        start()
    else:
        num()   





###################main
start()


    



