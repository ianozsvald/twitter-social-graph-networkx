import cPickle
import os
import get_data

# output file once we've summarised the screen_names per users
ALL_NAMES = os.path.join(get_data.DATA_DIR, "all_names.pickle")


def get_names(sn):
    """Get a list of twitter followers"""
    fr_filename, fo_filename = get_data.get_filenames(screen_name)
    # load just the followers
    filename = fo_filename
    names = cPickle.load(open(filename))
    return names


if __name__ == "__main__":
    # summarise the screen_names from Twitter's JSON into a simple dictionary
    all_names = {}
    for screen_name in get_data.screen_names:
        all_names[screen_name] = set([sn.screen_name for sn in get_names(screen_name)])

    # we can get an overlapping set with something like this:
    #set(all_names['annotateio']).intersection(set(all_names['ianozsvald']))

    cPickle.dump(all_names, open(ALL_NAMES, "w"), protocol=2)
