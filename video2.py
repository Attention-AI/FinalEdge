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
            'Bucket': 'myawsbucket-01',
            'Name': 'video.mp4',
        
        }
        },
        
    ClientRequestToken='123',
    NotificationChannel={
            "SNSTopicArn": "arn:aws:sns:us-east-2:348980249432:eyecatch",
            "RoleArn": "arn:aws:iam::348980249432:role/eyewatch"
        },
    FaceAttributes="ALL",
    JobTag='133'
) 
response = REKOGNITION_CLIENT.get_face_detection(
    JobId='46a6a754d5cacc0cb1e6931f3110c83b782c762a781c4decbc7cd59f4ae52b2e',
    MaxResults=123,

)
# send_data(response)         
#     })    
print(start_face_detection()) 
# job_id= '46a6a754d5cacc0cb1e6931f3110c83b782c762a781c4decbc7cd59f4ae52b2e'
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