# -*- coding: utf-8 -*-
import scrapy

from FedRevJobs.items import FedrevjobsItem
from scrapy.spiders import CrawlSpider
from datetime import datetime
import logging
import urllib.request
import json
import math
from .path_creator import crate_path
import os.path as path
from datetime import datetime
from scrapy.http.request import Request
from scrapy.http import FormRequest
from scrapy.selector import Selector
import re
global job_location

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

base_url = 'https://frbog.taleo.net'
start_url= 'https://frbog.taleo.net/careersection/1/moresearch.ftl'
json_url = 'https://frbog.taleo.net/careersection/1/moresearch.ftl?lang=en&portal=101430233'
#json_url = 'https://frbog.taleo.net/careersection/1/moresearch.ajax'

class FrjNewSpider(scrapy.Spider):
    name = 'frj_new'

    details = dict()
    path = crate_path(name)

    logging.basicConfig(filename='log.txt',format='%(levelname)s: %(message)s',level=logging.INFO)

    def __init__(self, keywords=None, category=None, *args, **kwargs):
    	super(FrjNewSpider, self).__init__(*args, **kwargs)
    	self.keywords = keywords
    	self.category = category

    def start_requests(self):

	    urls = json_url
		# first thing is to show the full list of jobs. Submit the button until shows
		# get initial list of urls
	    logging.info(start_url)
	    json_dict = dict()
	    json_dict['pageNo'] = 1
	    json_post = json.dumps(json_dict)

	    logging.info('Posting Json')

	    jobsearchdata = { #'iframemode': '1',
						'ftlpageid': 'reqListAdvancedPage',
						'ftlinterfaceid': 'advancedSearchFooterInterface',
						'ftlcompid': 'SEARCH',
						'jsfCmdId': 'SEARCH',
						'ftlcompclass': 'ButtonComponent',
						'ftlcallback': 'jobsearch_processSearch',
						'ftlajaxid': 'ftlx2',
						'lang': 'en',
						'ftlhistory': '',
						'ftlPageHistory': '',
						'ftlstate': '',
						'ftlwinscr': '',
						'ftlerrors': '',
						'portal': '101430233',
						'tz': 'GMT+05:30',
						'iniurl.src': '',
						'iniurl.media_id':'',
						'iniurl.sns_id':'' ,
						'iniurl.use_up':'' ,
						'zipcodePanelErrorDrawer.state': 'false',
						'rlPager.pageLabelBeforeHidden': '' ,
						'radiusSiteListPagerId.nbDisplayPage' : '5',
						'radiusSiteListId.isEmpty': 'true',
						'siteListId':'',
						'rssLocationIconTT': 'This criteria can be used for RSS feed creation: ??Location??',
						'actOnReqReferralApplyReqList.mode': '',
						'employeeStatusMenu.selected': '',
						'radiusSiteListPagerId.currentPage': '1',
						'listEmptyIsApplicantUser': 'false',
						'radiusSiteListPagerId.listId':'', 
						'displayUrgentNeed': 'true',
						'computeSiteListAction.zipcode': '' ,
						'jobCartIcon': 'cart_black.gif',
						'initialHistory': '',
						'rlPager.pagerLabelAfterPreviousHidden': '' , 
						'rlPager.pagerLabelTT': 'Go to page {0}',
						'listCount': '' ,
						'jobTypeMenu.selected': 'jobTypeTab',
						'rlPager.pageLabelAfterHidden': '' ,
						'listLocales': '',
						'rlPager.requisitionNo': '',
						'actOnReqApplyReqList.requisitionNo':'' ,
						'udf10Menu.selected': '',
						'udf9Menu.selected': '',
						'studyLevelMenu.selected': '',
						'listLabels': '',
						'listRequisition.nbElements': '34',
						'tabLevel1.selected': 'tabJS',
						'confirmBeaconTimedOut.a': '',
						'initialHistoryOld': '',
						'hideLinkTitle': 'Hide Search Criteria',
						'actDisplayReferralProfiler.candidateNo': '',
						'mySavedSearchesPageLink.target': '',
						'rlPager.pagerLabelNext': 'Next',
						'listRequisition.hasElements': 'true',
						'radiusSiteListPagerId.pagerLabelPrevious': 'Previous',
						'rlPager.pagerLabelPreviousTT': 'Go to the previous page',
						'careerPortalFullVersionURLEnabled': 'false',
						'searchcriteria.state': 'true',
						'isExternal': 'true',
						'tabLevel2a.selected': 'tabAdvancedReqSearch',
						'udf5Menu.selected': '',
						'jobListName': 'requisitionList',
						'radiusSiteListPagerId.pagerLabelNext': 'Next',
						'rlPager.pagerLabelPrevious': 'Previous',
						'radiusSiteListPagerId.requisitionNo': '',
						'displayAsMainHeader': 'false',
						'displaymessage': 'false',
						'tabLevel2b.selected': '',
						'actOnReqReferralApplyReqList.requisitionNo': '',
						'careerPortalFullVersionURL': '',
						'distance': '0',
						'confirmOverwrite.aor': 'false',
						'udf3Menu.selected': '',
						'radiusSiteListId.size': '5',
						'hideLinkTitleTT': 'Hide the search criteria',
						'jobsPerPageCaption': 'Results per page',
						'willTravelMenu.selected': 'willTravelTab',
						'addThisRequired': 'false',
						'actOnReqReferralProfilerAgentReqList.requisitionNo': '',
						'actAddJobToCart.requisitionNo': '',
						'radiusSiteListPagerId.pagerLabelTT': 'Go to page {0}',
						'confirmBeaconTimedOut.aor': 'false',
						'actOpenRequisitionDescription.requisitionNo': '',
						'rlPager.pagerLabelNextTT': 'Go to the next page',
						'rlPager.listId': 'listRequisition',
						'ftlISWLD': 'false',
						'jobfields.count': '1',
						'rlPager.pagerLabelBeforePreviousHidden':  '',
						'udf1Menu.selected': '',
						'displayDraft': 'true',
						'listContenDescriptionTT': '',
						'mLastActiveMode': 'reqListAdvancedPage',
						'jobShiftMenu.selected': 'jobShiftTab',
						'zipcode': '',
						'canDisplayFacebookButton': 'false',
						'isInternal': 'false',
						'confirmBeaconReset.aor': 'false',
						'actOnReqApplyReqList.mode': '',
						'showLinkTitle': 'Show Search Criteria',
						'rlPager.pagerLabelCount': 'Go to page {0}',
						'udf8Menu.selected': '',
						'navigate.url': '',
						'organizations.count': '1',
						'actDisplayReferralProfiler.requisitionNo': '',
						'computeSiteListAction.siteListId': '',
						'radiusSiteListPagerId.pagerLabelBeforePreviousHidden':  '',
						'commonDescriptionForAddThis': '',
						'jobFieldMenu.selected': 'tabJobField',
						'ftlISWLDMessage': '',
						'navigate.target': '',
						'radiusSiteListId.nbElements': '0',
						'savecriteria.state': 'false',
						'postedDateMenu.selected': 'postedDateTab',
						'organizationMenu.selected': '',
						'rlPager.currentPage': '1',
						'radiusSiteListPagerId.pagerLabelNextTT': 'Go to the next page',
						'locationSiteId': '0',
						'showLinkTitleTT': 'Show the search criteria',
						'actOnReqReferralApplyReqList.candidateNo': '',
						'confirmOverwrite.a': '',
						'countryPanelErrorDrawer.state': 'false',
						'csrftoken': '8GFB4sRP1FvsbMvGxLn1gJNZvYSJlqYJnJTVXfcW/1w=',
						'radiusLocationEmpty': '',
						'isApplicantUser': 'true',
						'urgentMenu.selected': '',
						'alreadyAppliedColumnDisplayed': 'true',
						'pBeaconBeat': '300000',
						'computeSiteListAction.distance': '0',
						'computeSiteListAction.locationSiteId': '0',
						'focusOnField': '',
						'radiusSiteListPagerId.pagerLabelAfterNextHidden':  '',
						'restoreInitialHistoryOnRefresh': 'false',
						'listRequisition.size': '100',
						'calloutPageDisplayed': 'false',
						'radiusSiteListPagerId.pagerLabelCount': 'Go to page {0}',
						'requisitionno': '',
						'rlPager.pagerLabelAfterNextHidden':  '',
						'jobScheduleMenu.selected': 'jobScheduleTab',
						'radiusContryName': '',
						'mySavedSearchesPageLink.url': '',
						'udf7Menu.selected': '',
						'rlPager.nbDisplayPage': '5',
						'radiusSiteListPagerId.pagerLabelBeforeNextHidden':  '',
						'signedIn': 'false',
						'emptyListToken': '',
						'pSessionTimeout': '1200000',
						'actOnReqApplyReqList.candidateNo': '',
						'isEnabled': 'true',
						'actOnReqReferralProfilerAgentReqList.candidateNo': '',
						'jobLevelMenu.selected': '',
						'tabLocationPatch': 'true',
						'errorMessageDrawer.state': 'false',
						'jobboardListPageTitle': 'Job Search - Job Search',
						'radiusActive': 'false',
						'actOpenRequisitionDescription.openDescFrom': 'default',
						'locations.count': '1',
						'confirmBeaconReset.a': '',
						'isListEmpty': 'false',
						'udf4Menu.selected': '',
						'actOnReqReferralProfilerAgentReqList.mode': '',
						'radiusSiteListPagerId.pagerLabelPreviousTT': 'Go to the previous page',
						'serializedCriteria': '',
						'actDisplayReferralProfiler.mode': '',
						'rlPager.pagerLabelBeforeNextHidden':  '',
						'udf2Menu.selected': '',
						'radiusSiteListId.hasElements': 'false',
						'locationMenu.selected': 'tabLocation',
						'cshtstate': '12|',
						'rssJobFieldIconTT': 'This criteria can be used for RSS feed creation: ??JobField??',
						'listRequisition.isEmpty': 'false',
						'canDisplayRSSButton': 'false',
						'canDisplaySavedSearchHelp': 'false',
						'radiusSiteListDrawer.state': 'false',
						'displayCalloutInLegend': 'false',
						'initialHistoryPage': '1',
						'descriptionLogginMandatory': 'false',
						'radiusSiteListPagerId.pageLabelAfterHidden': '',
						'computeSiteListAction.unit': '0',
						'applicationCandidateNo': '',
						'radiusSiteListPagerId.pageLabelBeforeHidden':  '',
						'rssRadiusIconTT': 'This criteria can be used for RSS feed creation: Zip/Postal Code Radius',
						'displayListingsPerPage': 'true',
						'radiusSiteListPagerId.pagerLabelAfterPreviousHidden': ''  ,
						'pSessionWarning': '600000',
						'udf6Menu.selected': '',
						'interfaceIdForTimeZone': 'requisitionListInterface',
						'nameValue': '' ,
						'jobNumberSearch': '',
						'keyword': '',
						'jobfield1':'' ,
						'location1': '',
						'postedDate': '',
						'languageSelect': '',
						'jobfield1L1': '-1',
						'location1L1': '-1',
						'dropListSize': '100',
						'dropSortBy' : '10',
						}

	    if self.keywords:
	    	jobsearchdata['keyword'] = self.keywords
	    if self.category:
	    	jobsearchdata['jobfield1'] = self.category

	    yield scrapy.FormRequest(url = urls,method='POST',
								 headers = {"Content-Type":"application/x-www-form-urlencoded",
											"Referer":"https://frbog.taleo.net/careersection/1/moresearch.ajax",
											"Host":"frbog.taleo.net",
											"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'},
									 cookies = {'locale':'eng','Path':'/careersection/'},
								formdata=jobsearchdata,
								callback=self.paginate)


    def paginate(self,response):
	    json_obj = response.text
	    item = FedrevjobsItem()

# Populate Item fields

	    item['job_pageurl'] = 'https://frbog.taleo.net/careersection/1/jobdetail.ftl'
	    item['job_title'] = re.findall(r'\|!Submission for the position%5C: (.*?) - \(', json_obj)

	    item['job_id'] = re.findall(r'\(Job Number%5C: (\d+)\)!\|', json_obj)

	    item['date_posted'] = re.findall(r'!\|!false!\|!!\|!!\|!!\|!!\|!(.*?)!\|!Apply!\|!Apply for this position', json_obj)
	    #item['location_name'] = re.findall(r'!\|!(.*?)!\|!false!\|!!\|!!\|!!\|!!\|!(.*?)!\|!Apply!\|!Apply for this position', json_obj)

	    job_id1 = item['job_id']

	    for i in job_id1 :
	    	item['job_location'] = re.findall(r'\|!%s!\|!(.*?)!\|!false!\|!!\|!!\|!!\|!!\|!' %i, json_obj)

	    if self.keywords:
	    	item['job_keyword'] = self.keywords

	    if self.category:
	    	item['job_category'] = self.category

	    return item

#def close(self,reason):
#	csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
#	os.rename(csv_file,'joblist.csv')



	    