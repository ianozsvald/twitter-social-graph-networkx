import cPickle
import tst

#DATA_DIR = "data"
#screen_names = ['ianozsvald', 'annotateio', 'fluffyemily']


#def get_friends(sn):
#    return cPickle.load(open(os.path.join(DATA_DIR, "%s.friends.pickle" % (sn))))
#all_friends = {}
#for screen_name in screen_names:
#    all_friends[screen_name] = set([sn.screen_name for sn in get_friends(screen_name)])
#def get_followers(sn):
#   return cPickle.load(open(os.path.join(DATA_DIR, "%s.followers.pickle" % (sn))))

def get_names(sn):
    fr_filename, fo_filename = tst.get_filenames(screen_name)
    filename = fo_filename
    names = cPickle.load(open(filename))
    return names

all_names = {}
for screen_name in tst.screen_names:
    all_names[screen_name] = set([sn.screen_name for sn in get_names(screen_name)])

# we can get an overlapping set with something like this:
#set(all_friends['annotateio']).intersection(set(all_friends['ianozsvald']))

cPickle.dump(all_names, open("all_names.pickle", "w"), protocol=2)
