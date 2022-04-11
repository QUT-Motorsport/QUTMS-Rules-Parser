import re
from striprtf.striprtf import rtf_to_text
import csv


with open('FSAE_Rules_2022_V21.rtf', 'r') as file:
    rtf = file.read()
    
text = rtf_to_text(rtf)

with open('text.txt', 'w') as f:
    f.write(text)


m = re.findall('(EV(.|\n)+?)(?=\n*EV\.)',text)


with open('export.csv','w', newline='') as f:
    writer = csv.writer(f)

    

    for x in range(2,len(m)):


        line = m[x]

        print('======')

        rule = re.search('(EV.+?) ', line[0])
        
        
        if rule:
            ruleTxt = rule.groups()[0]

            length = len(rule.groups()[0])
            ruleContent = line[0][length:]

            row = ruleTxt, ruleContent

            print(row)

            writer.writerow(row)



        


          
            

            

    

    


        