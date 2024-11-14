

def lambda_handler(event, context):
       print("event: ", event)
       print("i am step function one executed ...")
       return {"status": "step one executed","id": '111111'}