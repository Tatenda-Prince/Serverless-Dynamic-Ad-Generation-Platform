resource "aws_api_gateway_rest_api" "ad_generator_api" {
  name = "${var.project_name}-api"
  
  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

resource "aws_api_gateway_resource" "generate" {
  rest_api_id = aws_api_gateway_rest_api.ad_generator_api.id
  parent_id   = aws_api_gateway_rest_api.ad_generator_api.root_resource_id
  path_part   = "generate"
}

resource "aws_api_gateway_method" "generate_get" {
  rest_api_id   = aws_api_gateway_rest_api.ad_generator_api.id
  resource_id   = aws_api_gateway_resource.generate.id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "lambda_integration" {
  rest_api_id = aws_api_gateway_rest_api.ad_generator_api.id
  resource_id = aws_api_gateway_resource.generate.id
  http_method = aws_api_gateway_method.generate_get.http_method

  integration_http_method = "POST"
  type                   = "AWS_PROXY"
  uri                    = aws_lambda_function.dynamic_ad_generator.invoke_arn
}

resource "aws_lambda_permission" "api_gateway_invoke" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.dynamic_ad_generator.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.ad_generator_api.execution_arn}/*/*"
}

resource "aws_api_gateway_deployment" "api_deployment" {
  depends_on = [
    aws_api_gateway_method.generate_get,
    aws_api_gateway_integration.lambda_integration,
  ]

  rest_api_id = aws_api_gateway_rest_api.ad_generator_api.id
}

resource "aws_api_gateway_stage" "prod" {
  deployment_id = aws_api_gateway_deployment.api_deployment.id
  rest_api_id   = aws_api_gateway_rest_api.ad_generator_api.id
  stage_name    = "prod"
}