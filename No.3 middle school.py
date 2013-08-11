import random


location=4
player_defense=40
player_joke=5
player_robber=15

d1=[8,1]
d2=[2,10]
d3=[3,11]
d4=[8,4]
d5=[4,11]
d6=[4,10]
d7=[5,9]
d8=[6,9]
d9=[8,9]
d10=[8,7]
d11=[10,44]
d12=[12,3]
d16=[11,16]
ck_r1=('door1')                                #from here 
ck_r2=('door1')
ck_r3=('door1')
ck_r4=('door1')
ck_r5=('door1')
ck_r6=('door1')
ck_r7=('door1')
ck_r8=('door1')
ck_r9=('door1')
ck_r10=('door1')
ck_r11=('door1')
ck_r12=('door1')
ck_r16=('door1') 
ck_r44=('door1')                               #to here, these tuple are useless,they may do something in the future , but not now.
doorname={"door1":d1,"door2":d2,"door3":d3,"door4":d4,"door5":d5,"door6":d6,"door7":d7,"door8":d8,"door9":d9,"door10":d10,"door11":d11,"door12":d12,"door16":d16}
r1={"door1":doorname["door1"],'west':d1}
r2={"door2":doorname["door2"],'north':d2}
r3={"door3":doorname["door3"],"door12":doorname["door12"],'north':d3,'south':d12}
r4={'door4':doorname["door4"],'door5':doorname["door5"],"door6":doorname["door6"],'west':d5,'north':d4,'east':d6}
r5={"door7":doorname["door7"],'north':d7}
r6={"door8":doorname["door8"],'south':d8}
r7={"door10":doorname["door10"],'south':d10}
r8={"door4":doorname["door4"],"door10":doorname["door10"],'door9':doorname['door9'],'door1':doorname['door1'],'south':d4,'west':d9,'north':d10,'east':d1}
r9={"door7":doorname["door7"],"door8":doorname["door8"],"door9":doorname["door9"],'south':d7,'north':d8,'east':d9}
r10={"door2":doorname["door2"],"door6":doorname["door6"],"door11":doorname["door11"],'west':d6,'south':d2,'east':d11}
r11={"door16":doorname["door16"],"door3":doorname["door3"],"door5":doorname["door5"],'west':d16,'south':d3,'east':d5}
r12={"door12":doorname["door12"],'north':d12}
r16={"door16":doorname["door16"],'east':d16}
r44={"door11":doorname["door11"],'west':d11}
room_door={1:r1,2:r2,3:r3,4:r4,5:r5,6:r6,7:r7,8:r8,9:r9,10:r10,11:r11,12:r12,16:r16,44:r44}
def check(location,in_put,room):
    if in_put in (room_door[location]):
        return True
    else:
        return False
def doorf(doorname,location):            #i deleted the 'in_put' and 'room=room_door'
    """doorf(doorname<room_door[location][userinput]>,location,input)"""
    if location==doorname[0]:
        return doorname[1]
    elif location==doorname[1]:
        return doorname[0]
def motion(enter,location=location):
    if check(location,enter,room_door)==True:
        return doorf(room_door[location][enter],location)       # i deleted the ',enter'
    else:
        print('input Error','-------printed by motion function : wrong input branch')
        return location
#print(motion('door4'))
#---------------------------------------------I'm Dividing Line-----------------------------------------------------------------------------------------
pocket=['coffeecup','coffeemaker']
on_off=[0,1]

stuf1=[4,0,'coffeecup']
stuf2=[8,0,'coffeemaker']

sname={'coffeecup':stuf1,'coffeemaker':stuf2}
slist=['coffeecup','coffermaker']
#----------interim item-----------------------

def pocheck(verb,noun,location):
    if verb == 'pick':
        if sname[noun][0] == location:
            return True 
        else: return False 
    elif verb == 'drop':
        if noun in pocket:
            return True 
        else: return False 
    else: return True 

def pocketf(verb,noun,location=location):
    global pocket
    global sname
    if pocheck(verb,noun,location) == True :
        global sname
        if verb == 'pick':
            sname[noun][0]=0
            pocket.append(noun)
        elif verb == 'turn on':
            sname[noun][1]=doorf(on_off,sname[noun][1])
        elif verb == 'drop':
            sname[noun][0]=location
            pocket.remove(noun)
        elif verb == 'count':
            pocki=set(pocket)
            for i in pocki:
                print(pocket.count(i),i,'-------printed by pocketf function : count branch')
    else: 
        if verb == 'pick':
            print('You cannot see any',noun,'-------printed by pocketf function : wrong input branch')
        elif verb == 'drop':
            print('You do not have a',noun,'-------printed by pocketf function : wrong input branch')
#-----------------------save-----------------------------------------------------------------            
def save(savename):
    save=open(savename+'.txt','w')
    save.write(str(location)+'\n')                      #saving location
    
    indics=0                                  #saving pocket
    for i in pocket:
        save.write(pocket[indics]+'\n')
        indics+=1

    save.close()
#def restore(savename):
    #restore=open(savename+'.txt')
    #indics=0
    #for i in pocket:
    #return ans

#-----------------------AI-------------------------------------------------------------------
# mob=[name,location,joke_chance,robber_chance,defense,turn]
ai1={'name':'brother tao','location':16,'joke_chance':5,'robber_chance':15,'defense':50,'turn':1,1:'brother tao has been defeated'}
ai2={'name':'madam p','location':44,'joke_chance':0,'robber_chance':10,'defense':20,'turn':2,1:'madam p seems been shocked by your attack,bur she is still standing',2:'now,she is lying in a pool of blood,and she is still bleeding'}

ainame={'brother tao':ai1,'madam p':ai2}
ailist=['brother tao','madam p']

def monster_check(monster_name):
    if monster_name in ailist:
        if ainame[monster_name]['location'] == location:
            return True
        else:
            print('YOU CANNOT SEE ANY',monster_name,'HERE','-------printed by function : monster_check : wrong location branch.')
            return False
    else :
        print('wrong type','-------printed by function : monster_check : wrong monster type branch.')
        return False
       

def fight(monster_name):
    dice_point=random.randint(0,(player_defense+ainame[monster_name]['defense']))
    if monster_check(monster_name):
        if dice_point > ainame[monster_name]['defense']:
            ainame[monster_name]['turn']-=1
            return 'victory'
        elif dice_point == ainame[monster_name]['defense']:
            return 'even'
        elif dice_point < ainame[monster_name]['defense']:
            return 'fail'
    else:
        monster_check(monster_name)

def joke(monster_name):
    dice_point=random.randint(0,(player_defense+ainame[monster_name]['joke_chance']))
    if monster_check(monster_name):
        if dice_point > ainame[monster_name]['joke_chance']:
            return 'funny'
        elif dice_point == ainame[monster_name]['joke_chance']:
            return 'funny'
        elif dice_point < ainame[monster_name]['joke_chance']:
            return 'badluck'
    else:
        monster_check(monster_name)
def robber(monster_name):
    dice_point=random.randint(0,(player_defense+ainame[monster_name]['robber_chance']))
    if monster_check(monster_name):
        if dice_point > ainame[monster_name]['robber_chance']:
            return 'through'
        elif dice_point == ainame[monster_name]['robber_chance']:
            return 'badluck'
        elif dice_point < ainame[monster_name]['robber_chance']:
            return 'badluck'
    else:
        monster_check(monster_name)
def monster_action(verb,name):
    if verb == 'attack':
        fight(name)
    elif verb == 'joke' :
        joke(name)
    elif verb == 'robber':
        robber(name)
    

#-----------------------others---------------------------------------------------------------
#-----------------------words----------------------------------------------------------------

perp_list=['in','on','into','onto','down']
verb_motion_list=['go','move ','head to ']
verb_pick_list=['take']
verb_switch_list=['turn on','power on','turn off','power off']
verb_drop_list=['drop','put']

perp_set=set(perp_list)
verb_motion_set=set(verb_motion_list)
verb_pick_set=set(verb_pick_list)
verb_switch_set=set(verb_switch_list)
verb_drop_set=set(verb_drop_list)

#-----------------------input analyze--------------------------------------------------------
def analyze(ip):
    ipcut=ip.split(' ')
    ip_set=set(ipcut)
    global location
    if ('go' in ip)or('move' in ip)or('head to' in ip):             #movement test
        if ('north' in ip)or('south' in ip)or('west' in ip)or('east' in ip):
            location=motion(ipcut[-1],location)
        else: print('i have no idea -------printed by analyze function : move branch')
    elif ('take' in ipcut)and(ipcut[-1] in slist):                  #pick test
        pocketf('pick',ipcut[-1], location)
        print('taken','-------printed by analyze function : pick branch')
    elif ('turn on' in ip)or('power off' in ip)or('turn off' in ip)or('power on' in ip):#switch test
        if ipcut[-1] in slist:
            pocketf('turn on',ipcut[-1],location)
            return None #interim
        else: print('i have no idea','-------printed by analyze function : turn on/off branch : wrong')
    elif ('drop ' in ip)or('put ' in ip):                        #drop test
        if 'drop ' in ip:
            pocketf('drop',ipcut[-1],location)
            return None #interim
        elif 'put ' in ip:
            pocketf('drop',ipcut[(ipcut.index(''.join(list(perp_set & ip_set))))-1],location)
    elif 'save' in ip:                                        #save/restore test
        save_file_name=input('please enter the save-file name(no extension)')
        save(save_file_name)
        print('saved','-------printed by analyze function : save branch')
    elif 'restore' in ip:
        pass

            
            
#print(pocket,'printed by final test print function')
#analyze('put the coffeecup in the coffee maker')
#print(pocket,'printed by final test print function')



















