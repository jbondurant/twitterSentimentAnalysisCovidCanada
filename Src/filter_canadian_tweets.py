


#province/territory abbreviations from https://www150.statcan.gc.ca/n1/pub/92-195-x/2011001/geo/prov/tbl/tbl8-eng.htm
#things like newfoundland and labrador reduced to newfoundland
#this list of approx 1500 tweets will need to be checked manually afterwards for validity of can locations
#ie. just open tsv/csv in excel/pycharm and delete rows out of can
def get_canadian_locations():
    #pt for province/territory
    pt1 = ['newfoundland', 'newfoundland and labrador', 'terre-neuve', 'terre neuve', 'terre-neuve et labrador', 'terre neuve et labrador', 'NL', 'TNL']
    pt2 = ['nova scotia', 'nouvelle ecosse', 'nouvelle-ecosse', 'nouvelle écosse', 'nouvelle-écosse', 'NS', 'NE', 'NÉ']
    #TODO fill till pt 13
    pt3 = []
    pt4 = []
    pt5 = []
    pt6 = []
    pt7 = []
    pt8 = []
    pt9 = []
    pt10 = []
    pt11 = []
    pt12 = []
    pt13 = []

    country = ['canada', 'ca', 'can']

    all_canadian_geo = pt1 + pt2 + pt3 + pt4 + pt5 + pt6 + pt7 + pt8 + pt9 + pt10
    all_canadian_geo += pt11 + pt12 + pt13 + country;
    return all_canadian_geo


#then maybe replace non alph things with spaces from self rep. loc. and check if exact match  (i.e. for montreal,qc)


def main():
    a=1


if __name__ == '__main__':
    main()