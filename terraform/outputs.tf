output "api_gateway_url" {
  description = "API Gateway endpoint URL"
  value       = "${aws_api_gateway_rest_api.ad_generator_api.execution_arn}/${aws_api_gateway_stage.prod.stage_name}/generate"
}

output "api_gateway_invoke_url" {
  description = "API Gateway invoke URL"
  value       = "https://${aws_api_gateway_rest_api.ad_generator_api.id}.execute-api.${var.aws_region}.amazonaws.com/${aws_api_gateway_stage.prod.stage_name}/generate"
}

output "cloudfront_domain" {
  description = "CloudFront distribution domain"
  value       = aws_cloudfront_distribution.ad_generator_cdn.domain_name
}

output "cloudfront_url" {
  description = "CloudFront URL for ad generation"
  value       = "https://${aws_cloudfront_distribution.ad_generator_cdn.domain_name}/generate"
}

