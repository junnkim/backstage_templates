from aws_cdk import core as cdk
from aws_cdk import aws_lambda as _lambda

class MyLambdaStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        _lambda.Function(
            self, "MyFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset("lambda_function"),
        )

app = cdk.App()
MyLambdaStack(app, "MyLambdaStack")
app.synth()