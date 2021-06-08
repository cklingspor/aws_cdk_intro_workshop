from aws_cdk import (
    core,
    aws_lambda as _lambda, #cant use lambda here because its a python element
    aws_apigateway as apigw,
)

from hitcounter import HitCounter


class CdkworkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # the id of the construct (here lambda) must be unique within this scope
        # TODO: self?
        # Defines an AWS Lambda resource
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='hello_from_cdk.handler',
        )

        hello_with_counter = HitCounter(
            self, 'HelloHitCounter',
            downstream=my_lambda,
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_with_counter.handler,
        )

        # A request will go the following way: Gateway-hello_with_counter(increase_count)-my_lambda
