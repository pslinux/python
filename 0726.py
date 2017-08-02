# -*- coding: UTF-8 -*-  
people = {
    'Alice' : {
      'phone'  : '378884295',
      'addr'  :   'yangzemin'
    },
      'Peter' :  {
      'phone' :  '378884295' ,
      'addr'  :  'duanyifei'
    },
    'Cecil' :  {
      'phone':  '378884295' ,
      'addr':   'cuijingang'
    }
}
labels ={
    'phone' : 'phone number',
    'addr' : 'address'
}
name=raw_input('Name: ');
request = raw_input('Phone number(p) or address (a)?');
if request == 'p': key='phone'
if request == 'a': key='addr'
if name in people: print "%s's %s is %s."  % (name,labels[key],people[name][key])
