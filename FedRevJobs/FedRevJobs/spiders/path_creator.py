import os.path as path
from datetime import datetime

def crate_path(name):
	date = datetime.now().strftime('%Y%m%d')
	data_path = path.abspath(path.join(__file__, "../.."))+'/scraped_data/{}/'.format(name)
	feed_uri = '{}{}_{}.json'.format(data_path,name,date)
	return feed_uri