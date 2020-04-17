import translate
import os
a=1
for file in os.listdir("forder_name"):
    print(file)
    print(a)
    a=a+1
    translate.translate('forder_name/'+file)
