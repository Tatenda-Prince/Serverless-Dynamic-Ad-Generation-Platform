resource "aws_cloudfront_distribution" "ad_generator_cdn" {
  origin {
    domain_name = "${aws_api_gateway_rest_api.ad_generator_api.id}.execute-api.${var.aws_region}.amazonaws.com"
    origin_id   = "APIGateway-${aws_api_gateway_rest_api.ad_generator_api.id}"
    origin_path = "/prod"

    custom_origin_config {
      http_port              = 443
      https_port             = 443
      origin_protocol_policy = "https-only"
      origin_ssl_protocols   = ["TLSv1.2"]
    }
  }

  enabled = true

  default_cache_behavior {
    allowed_methods        = ["GET", "HEAD", "OPTIONS"]
    cached_methods         = ["GET", "HEAD"]
    target_origin_id       = "APIGateway-${aws_api_gateway_rest_api.ad_generator_api.id}"
    compress               = true
    viewer_protocol_policy = "redirect-to-https"

    forwarded_values {
      query_string = true
      query_string_cache_keys = ["hotel", "price", "location", "rating", "t", "view"]
      cookies {
        forward = "none"
      }
    }

    min_ttl     = 0
    default_ttl = 0
    max_ttl     = 0
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }

  tags = {
    Name        = "${var.project_name}-cdn"
    Environment = "dev"
  }
}