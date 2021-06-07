from aws_cdk import (
    core,
    aws_lambda as _lambda, #cant use lambda here because its a python element
    aws_apigateway as apigw,
)

from hitcpunter import HitCounter


class CdkworkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # the id of the construct (here lambda) must be unique within this scope
        # TODO: self?
        my_function = _lambda.Function(self,
                                    id='HelloFromHitCounter',
                                    runtime=_lambda.Runtime.PYTHON_3_7,
                                    code=_lambda.Code.asset('lambda'),  # same as dir of lambda code
                                    handler='hitcount.handler',  # filename.handlername
                                   )

        hello_from_hitcounter = HitCounter(self, id='HelloHitCounter', downstream=my_function)
        apigw.LambdaRestApi(self, id='CDKendpoint', handler=hello_from_hitcounter.handler)

        # A request will go the following way: Gateway-hello_from_hitcounter(increase_count)-my-function
