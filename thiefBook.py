import requests
from StringIO import StringIO
from PIL import Image
import profile

url = 'https://files.passeidireto.com/02f452dd-5aa0-478f-be30-3c4c7ee6dbb9/bg'
png = '.png'
nome = '.jpg'
getPage = ''

counter_num = 1;
final = 0;

while counter_num <= 16:
    

    if counter_num <= 9:
        nome = str(final) + str(counter_num) + '.png'
        getPage = url + str(counter_num) + png
        print "Asking for: "
        print getPage
        counter_num = counter_num + 1;

    else:
        
        if counter_num == 10:
            nome = str(final) + str("9_1") + '.png'
            getPage = url +'a' + png
            print "Asking for: "
            print getPage
            counter_num = counter_num + 1;
    
        elif counter_num == 11:
            nome = str(final) + str("9_2") + '.png'
            getPage = url +'b' + png
            print "Asking for: "
            print getPage
            counter_num = counter_num + 1;
    
        elif counter_num == 12:
            nome = str(final) + str("9_3") + '.png'
            getPage = url +'c' + png
            print "Asking for: "
            print getPage
            counter_num = counter_num + 1;
    
        elif counter_num == 13:
            nome = str(final) + str("9_4") + '.png'
            getPage = url +'d' + png
            print "Asking for: "
            print getPage
            counter_num = counter_num + 1;
    
        elif counter_num == 14:
            nome = str(final) + str("9_5") + '.png'
            getPage = url +'e' + png
            print "Asking for: "
            print getPage
            counter_num = counter_num + 1;
    
        else:
            nome = str(final) + str("9_6") + '.png'
            getPage = url +'f' + png
            print "Asking for: "
            print getPage
            counter_num = 0;
            final = final + 1;                    

    r = requests.get(getPage)
    i = Image.open(StringIO(r.content))
    i.save(nome,"PNG")
    print "Should be saved - Cleaning URL | Name  "
    getPage = ''
    nome = ''

input("Done")