# Lambda function code for building an Amazon Canary

from datetime import datetime
from urllib2 import urlopen

SITE = 'https://www.amazon.com/' # URL of the site to check
EXPECTED = 'Black Friday'        # String expected to be on the page

def validate(res):
    '''Return False to trigger the canary

    Current this simply checks whether the EXPECTED string is present.
    However, you could modify this to perform any number of check on the
    contents of SITE.
    '''
    return EXPECTED in res

def lambda_handler(event, context):
    print('Checking {} at {}...'.format(SITE, event['time']))
    try:
        if not validate(urlopen(SITE).read()):
            raise Exception('Validation failed')
    except:
        print('Check failed!')
        raise
    else:
        print('Check passed!')
        return event['time']
    finally:
        print('Check complete at {}'.format(str(datetime.now())))

