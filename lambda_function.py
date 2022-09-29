# import json

# def lambda_handler(event, context):
#     # TODO implement
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Application under development. Search functionality will be implemented in Assignment 2')
#     }
# import json

# def lambda_handler(event, context):
#     return {
#         'statusCode': 200,
#         'headers': {
            
            
#             'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
#         },
#         'body': json.dumps('Application under development. Search functionality will be implemented in Assignment 2')
#     }
#https://6x2z34mmga.execute-api.us-east-1.amazonaws.com/first_test/chatbot

#yes
import json

def lambda_handler(event, context):
    return{
        'statusCode' : 200,
        
        'headers':{
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            
        },
        'body':{'messages':
            [{'unstructured':
                {'text':'Application under development. Search functionality will be implemented in Assignment 2.'}, 'type':'unstructured'}]}
    }