


#province/territory abbreviations from https://www150.statcan.gc.ca/n1/pub/92-195-x/2011001/geo/prov/tbl/tbl8-eng.htm
#things like newfoundland and labrador reduced to newfoundland
#this list of approx 1500 tweets will need to be checked manually afterwards for validity of can locations
#ie. just open tsv/csv in excel/pycharm and delete rows out of can
#also for report, mention english can speakers aren't the best sample of can. you need both
def get_canadian_locations_exact():
    country = ['ca', 'can']
    p1 = ['nl', 'tnl']
    p2 = ['pei', 'ipe', 'pe']
    p3 = ['ns', 'ne', 'né']
    p4 = ['nb']
    p5 = ['que', 'qc']
    p6 = ['ont', 'on']
    p7 = ['man' 'mb']
    p8 = ['sask', 'sk']
    p9 = ['alta', 'alb', 'ab']
    p10 = ['bc', 'cb']
    t1 = ['yt', 'yn']
    t2 = ['nwt', 'tno', 'nt']
    t3 = ['nvt', 'nt', 'nu']
    #notice nt both in t2 and t3

    all_canadian_geo = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10
    all_canadian_geo += t1 + t2 + t3 + country
    return all_canadian_geo

#make sure - are replaced with spaces when comparing
#hmm, some tweets were cut short like Grand Falls-Windsor, Newfoundl cause of
#the 30 char limit
def get_canadian_locations_sub():
    country = ['canada']
    p1 = ['newfoundland', 'labrador', 'terre neuve', 'labrador']
    p2 = ['prince edward', 'prince édouard']
    p3 = ['nova scotia', 'nouvelle ecosse', 'nouvelle écosse']
    p4 = ['new brunswick', 'nouveau brunswick']
    p5 = ['quebec', 'québec']
    p6 = ['ontario']
    p7 = ['manitoba']
    p8 = ['saskatchewan']
    p9 = ['alberta']
    p10 = ['british columbia', 'colombie britannique']
    t1 = ['yukon']
    t2 = ['northwest territories', 'territoires du nord ouest']
    t3 = ['nunavut']

    all_canadian_geo = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10
    all_canadian_geo += t1 + t2 + t3 + country
    return all_canadian_geo

def main():
    a=1


if __name__ == '__main__':
    main()