# Lambda function for dynamic ad generation

resource "aws_lambda_function" "dynamic_ad_generator" {
  function_name = "dynamic-ad-generator"
  role          = aws_iam_role.lambda_exec_role.arn

  package_type  = "Zip"
  filename      = "lambda_deployment.zip"
  handler       = "app.lambda_handler"
  runtime       = "python3.11"

  timeout       = 30
  memory_size   = 512

  # No environment variables needed

  depends_on = [aws_iam_role_policy_attachment.lambda_policy_attach]
}
