import numpy as np
f=open('E0=-3_frequency_data.dat',"r")
lines=f.readlines()
Iorth=[]
Ipar=[]
tropism=[]
def floatify(iterable):
    result = []
    for item in iterable:
        if isinstance(item, list):
            result.append(floatify(item))
        else:
            result.append(float(item))
    return result
for x in lines:
    Iorth.append(x.split('  ')[5])
    Ipar.append(x.split('   ')[6])
for y in range(len(Iorth)):    
    tropism.append((Iorth[y]-Ipar[y])//Iorth[y]+Ipar[y]))
f.close()
print('\n'.join([str(y), y in tropism]))
