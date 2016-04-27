import boto
from boto.mws import connection
import xml.etree.cElementTree as et
from jinja2 import Environment, PackageLoader

ACCOUNT_TYPE = "Merchant"

MWS_ACCESS_KEY = 'your_access_key'
MWS_SECRET_KEY = 'your_secret_key'
MERCHANT_ID = 'your_merchant_id'
MARKETPLACE_ID = 'ATVPDKIKX0DER' # This is the marketplace ID for the US.

r = open('file name')
f = r.read()
u = f.decode("utf-8-sig")
c = u.encode("utf-8")
feed_content = c

conn = connection.MWSConnection(aws_access_key_id=MWS_ACCESS_KEY,
            aws_secret_access_key=MWS_SECRET_KEY, Merchant=MERCHANT_ID)


feed = conn.submit_feed(
    FeedType='_POST_PRODUCT_DATA_',
    PurgeAndReplace=False,
    MarketplaceIdList=[MARKETPLACE_ID],
    content_type='text/xml',
    FeedContent=feed_content
)

feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
print 'Submitted Product Feed: ' + str(feed_info)
