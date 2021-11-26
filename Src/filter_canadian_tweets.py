import re


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
    #notice nt both in t2 and t3, not important unless we weight sample by provinces, which is a bit too fancy

    all_canadian_geo = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10
    all_canadian_geo += t1 + t2 + t3 + country
    return all_canadian_geo

def get_californian_cities_exact():
    cali_cities = ['san', 'santa', 'rio']
    return cali_cities

def get_californian_cities_sub():
    #I don't think i can put county here as of now. perhaps people say stuff like york county, ontario
    popular = ['hollywood']

    cities_1_10 = ['los angeles', 'fresno', 'long beach', 'oakland', 'bakersfield', 'anaheim']
    cities_11_20 = ['stockton', 'riverside', 'irvine', 'chula vista', 'fremont', 'modesto']
    cities_21_26 = ['fontana', 'oxnard', 'huntington beach', 'glendale', 'elk grove', ]
    #skipped 27 since it's ontario california lol
    cities_28_38 = ['rancho cucamonga', 'oceanside', 'lancaster', 'garden grove', 'salinas', 'hayward', 'corona', 'sunnyvale', 'pomona', 'escondido']
    cali_cities = popular + cities_1_10 + cities_11_20 + cities_21_26 + cities_28_38
    return cali_cities

#hmm, some tweets were cut short like Grand Falls-Windsor, Newfoundl cause of the 30 char limit
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

def is_tweet_canadian(tweet_loc):
    if tweet_loc == None:
        return False
    tweet_loc = tweet_loc.lower()
    clean_tweet_loc = re.sub("[^0-9a-zA-Z]+", " ", tweet_loc)#for things like terre-neuve
    tweet_loc_words = clean_tweet_loc.split()
    can_locs_sub = get_canadian_locations_sub()
    can_locs_exact = get_canadian_locations_exact()
    cali_cities_exact = get_californian_cities_exact()
    cali_cities_sub = get_californian_cities_sub()

    for cali_city_sub in cali_cities_sub:
        if cali_city_sub in clean_tweet_loc:
            return False
    for cali_cities_exact in cali_cities_exact:
        for tweet_word in tweet_loc_words:
            if cali_cities_exact == tweet_word:
                return False

    for can_loc_sub in can_locs_sub:
        if can_loc_sub in clean_tweet_loc:
            return True
    for can_loc_exact in can_locs_exact:
        for tweet_word in tweet_loc_words:
            if can_loc_exact == tweet_word:
                return True
    return False

def main():
    tweet_loc = 'London ON santa abc'
    print(is_tweet_canadian(tweet_loc))


if __name__ == '__main__':
    main()