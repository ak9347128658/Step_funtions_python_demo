

def lambda_handler(event, context):
       print("event: ", event)
       status = event.get('status')
       print("status: ", status)
       id = event.get('id')
       print("id: ", id)
       print("i am step function two executed ...")

