import re
from striprtf.striprtf import rtf_to_text
import csv

# Read RTF file. You can make an RTF from the rules document using Adobe's online converter
with open('FSAE_Rules_2022_V21.rtf', 'r') as file:
    rtf = file.read()
    
# Convert RTF to Text format
text = rtf_to_text(rtf)

# Write to text file for any debugging
with open('text.txt', 'w') as f:
    f.write(text)




with open('export.csv','w', newline='') as f:
    writer = csv.writer(f)

    for code in ["GR","AD","DR","F","V","T","VE","EV","IN"]:
        # Find all occurences of pattern that signifies a rule start
        regex = re.findall('(?!\n)('+code+'(.|\n)+?)(?=\n*'+code+'\.)',text)
        
        # Skip first one, as first occurence always is whole document
        for x in range(2,len(regex)-1):

            result = regex[x]

            # regex rule code out of line result
            ruleCode = re.search('('+code+'.+?) ', result[0])
            
            if ruleCode:
                # get text of rule code if present in result
                ruleCodeText = ruleCode.groups()[0]

                # trim off rule code from text
                length = len(ruleCode.groups()[0])
                ruleContent = result[0][length:]

                # concat row for csv and write to csv
                row = ruleCodeText, ruleContent
                writer.writerow(row)
