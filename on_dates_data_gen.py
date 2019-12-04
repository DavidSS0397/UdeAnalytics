from utils import layer_generator as lg
from utils import tp_auth as tp
from utils import data_parser as dp
import pandas

# set date interval of data recollection

date_0 = lg.set_date(2019,10,18,19,23,second=3)
date_f = lg.set_date(2019,10,19,14,8,second=2)

dates = (date_0, date_f)


# get users from the followers of Daniel Quintero

json_following = dp.parse_from_txt("data/data_followers.json")
users = [json_dict["user_id"] for json_dict in json_following]


# set api

api = tp.api_auth("juanpa")

tweets = lg.get_tweetOnDates(api,users[:100],dates)

tweets.to_json("data/tweets_0to100.json")