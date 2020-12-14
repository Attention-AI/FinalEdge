import csv
import boto3
from client import send_data
with open('new_user_credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]
REKOGNITION_CLIENT = boto3.client('rekognition', aws_access_key_id=access_key_id,
	                           aws_secret_access_key=secret_access_key, region_name='us-east-2')   

  
                                   
def start_face_detection() -> dict:
    return REKOGNITION_CLIENT.start_face_detection(
         Video={
        'S3Object': {
            'Bucket': 'BUCKET NAME',
            'Name': 'video.mp4',
        
        }
        },
        
    ClientRequestToken='123',
    NotificationChannel={
            "SNSTopicArn": "arn:aws:sns:",
            "RoleArn": "arn:aws:iam::"
        },
    FaceAttributes="ALL",
    JobTag='133'
) 
response = REKOGNITION_CLIENT.get_face_detection(
    JobId='String',
    MaxResults=123,

)
# send_data(response)         
#     })    
print(start_face_detection()) 
# job_id= ''
# print(response)
# result = REKOGNITION_CLIENT.get_face_detection(JobId=job_id)
# result
# result.keys()
# result['JobStatus']
# result['ResponseMetadata']
# result['VideoMetadata']

# result['Faces']
# len(result['Faces'])
# print(result)
