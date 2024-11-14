from flask import Flask, request, jsonify
from flask_lambda import FlaskLambda
from flask_cors import CORS
import boto3
import os
import json


app = FlaskLambda(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/start-functions', methods=['GET'])
def get_todo():
    
    state_machine_arn = os.environ.get('STATE_MACHINE_ARN')

    sfn_client = boto3.client('stepfunctions')
    input_data = {
          "name": "dev dynamo ak",
            "age": 25,
    }

    response = sfn_client.start_execution(
        stateMachineArn=state_machine_arn,
        input=json.dumps(input_data)
    )
    return jsonify({"message": "step function started..."})    




def lambda_handler(event, context):
       print("event: ", event)
       return app(event, context)