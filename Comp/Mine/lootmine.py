import random

def main():
    mon_list = make_gen_list("large/monstats.txt")
    pre_list = get_presuf_list("large/MagicPrefix.txt")
    suf_list = get_presuf_list("large/MagicSuffix.txt")
    treasure = mon_list[3].replace("\n","")
    base_item = get_base_item(treasure,"large/TreasureClassEx.txt")
    base_stat = get_base_stats(base_item, "large/armor.txt")

    print "Fighting " + mon_list[0] + " (Level " + mon_list[2] + " " + mon_list[1] +")..."
    print "You have slain " + mon_list[0]
    print mon_list[0] + " dropped:\n"

    print pre_list[0] + " " + base_item + " " + suf_list[0]
    print "Defense: " + base_stat
    if pre_list[1] != "":
        print pre_list[1]
    if suf_list[1] != "":
        print suf_list[1]

def make_dict(textfile):
    dic = {}
    with open(textfile) as f:
        for line in f.readlines():
            dic[line.split(",")[0]] = line.split(",")[1:]
        f.close()
    return dic

def make_gen_list(textfile):
    with open(textfile) as f:
        file_as_text = f.readlines()
        gen_list = file_as_text[random.randint(1,len(file_as_text)-1)].split(",")
        f.close()
    return gen_list

def recursion_generator(dic,token):
    if token.strip() not in dic:
        return token.replace("\n","")
    else:
        val = dic[token]
        alt = val[random.randint(0,len(val)-1)].strip()
        return recursion_generator(dic, alt)

def get_base_item(tc,textfile):
    treasure_class_dic = make_dict(textfile)
    return recursion_generator(treasure_class_dic,tc)

def get_base_stats(base,textfile):
    armor_dic = make_dict(textfile)
    return str(random.randint(int(armor_dic[base][0]),int(armor_dic[base][1].replace("\n",""))))

def get_presuf_list(textfile):
    if random.randint(0,1) == 1:
        pre_list = make_gen_list(textfile)
        extra_stat = random.randint(int(pre_list[2]),int(pre_list[3].replace("\n","")))
        return [pre_list[0],str(extra_stat) + " " + pre_list[1]]
    else:
        return ["",""]

main()