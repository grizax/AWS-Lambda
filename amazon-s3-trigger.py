import json
import boto3

print('Loading function...')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    '''
    print('Received event: ' + json.dumps(event, indent=2))

    Gets the object from the event and shows its content type
    '''
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print('CONTENT TYPE: ' + response['ContentType'])
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}.'.format(key, bucket))
        raise e
