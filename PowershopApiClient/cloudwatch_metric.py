import boto3
from datetime import datetime
def put_metric_data_with_value(namespace="Powershop/Services", metric_name=None, value=None, dimensions=None, unit=None)
  client = boto3.client('cloudwatch')
  client.put_metric_data(
      Namespace = namespace,
      MetricData = [{
          'MetricName': metric_name,
          'Dimensions': dimensions,
          'Timestamp': datetime.now(),
          'Value': value,
          'Unit': unit
      }]
  )
  
