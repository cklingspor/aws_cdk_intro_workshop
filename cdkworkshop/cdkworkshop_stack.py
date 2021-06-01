from aws_cdk import (
    core,
    aws_lambda as _lambda #cant use lambda here because its a python element

)


class CdkworkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # the id of the construct (here lambda) must be unique within this scope
        function = _lambda.Function(self,
                                    id='HelloFromCDK',
                                    runtime=_lambda.Runtime.PYTHON_3_7,
                                    code=_lambda.Code.asset('lambda'), # same as dir of lambda code
                                    handler='hello_from_cdk.handler', #filename.handlername
                                    )

