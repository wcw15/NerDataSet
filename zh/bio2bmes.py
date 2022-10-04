import re
def PrintOut(charls,newlabels,F):
    for i in range(len(charls)):
        print(charls[i]+" "+newlabels[i],file=F)
    print("",file=F)

def Process(charls,labells):
    newlabels=[]
    if len(labells)==1:
        if re.search("B-",labells[0]):
            new_label=re.sub("B-","S-",labells[0])
            print("----")
            newlabels.append(new_label)
        else:
            print("------hahahah")
            newlabels.append(labells[0])
    else:
        for i in range(len(labells)):
            if re.search("B-([A-Z.]+)",labells[i]):
                if i==0:
                    if re.search("-*([A-Z.]+)$",labells[i+1]) and (re.search("-*([A-Z.]+)$",labells[i+1]).group(1) !=re.search("B-([A-Z.]+)",labells[i]).group(1)):
                        newlabel=re.sub("B-","S-",labells[i])
                        newlabels.append(newlabel)
                    else:
                        newlabels.append(labells[i])
                elif i==len(labells)-1:
                    if re.search("-*([A-Z].+)$",labells[i-1]) and (re.search("-*([A-Z.]+)$",labells[i-1]).group(1) !=re.search("B-([A-Z.]+)",labells[i]).group(1)):
                        newlabel=re.sub("B-","S-",labells[i])
                        newlabels.append(newlabel)
                    else:
                        newlabels.append(labells[i])
                else:
                    # print("first here")
                    if re.search("-*([A-Z.]+)$",labells[i-1]) and re.search("-*([A-Z.]+)$",labells[i+1]) and (re.search("-*([A-Z.]+)$",labells[i-1]).group(1) != re.search("B-([A-Z.]+)",labells[i]).group(1)) and (re.search("-*([A-Z.]+)$",labells[i+1]).group(1) != re.search("B-([A-Z.]+)",labells[i]).group(1)):
                        newlabel=re.sub("B-","S-",labells[i])
                        newlabels.append(newlabel)
                    elif labells[i]==labells[i+1]:
                        newlabel = re.sub("B-", "S-", labells[i])
                        newlabels.append(newlabel)

                    elif labells[i-1]==labells[i] and re.search("-*([A-Z.]+)$",labells[i+1]) and (re.search("-*([A-Z.]+)$",labells[i+1]).group(1) != re.search("B-([A-Z.]+)",labells[i]).group(1)):
                          # print("second come here")
                          newlabel = re.sub("B-", "S-", labells[i])
                          newlabels.append(newlabel)
                    else:
                        newlabels.append(labells[i])
            elif re.search("I-([A-Z.]+)",labells[i]):
                if i==len(labells)-1:
                    newlabel=re.sub("I-","E-",labells[i])
                    newlabels.append(newlabel)
                elif re.search("-*([A-Z.]+)$",labells[i+1]) and (re.search("-*([A-Z.]+)$",labells[i+1]).group(1) !=re.search("I-([A-Z.]+)",labells[i]).group(1)):
                    newlabel = re.sub("I-", "E-",labells[i])
                    newlabels.append(newlabel)

                elif re.search("B-",labells[i+1]):
                    newlabel = re.sub("I-", "E-", labells[i])
                    newlabels.append(newlabel)
                else:
                    newlabel = re.sub("I-", "M-", labells[i])
                    newlabels.append(newlabel)
            elif labells[i]=="O":
                newlabels.append(labells[i])
    return newlabels

def format(input_path,out_path):
    charls=[]
    labells=[]
    F = open(out_path, "w",encoding="utf-8")
    In=open(input_path,"r",encoding="utf-8")
    for line in In:
        line=line.strip()
        if line =="":
            newlabels=Process(charls,labells)
            PrintOut(charls,newlabels,F)
            charls=[]
            labells=[]
        else:
            items=line.split(" ")
            char=items[0]
            label=items[1]
            charls.append(char)
            labells.append(label)
    In.close()
    F.close()
input_path="./chinese_ner 全/WeiboNER/weiboNER_2nd_conll.train_deseg"
out_path="./chinese_ner 全/WeiboNER/weiboNER_2nd_conll.train_bmes"
format(input_path,out_path)
