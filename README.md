# 🚀 SkyTrip.com – Serverless Dynamic Ad Generation on AWS

## 📌 Overview

SkyTrip.com company helps millions of travelers find accommodations, flights, car rentals, taxis, and experiences in more than 200 countries. SkyTrip.com connects with travelers by running dynamic ads across social media channels, and it needed a more efficient way to create and manage its content.


Traditional server-based solutions were slow, expensive, and hard to scale during peak travel seasons.

By moving to a fully serverless AWS architecture, SkyTrip.com built an in-house dynamic ad generation system that delivers:

- ✅ **99.7% cost savings**
- ⚡ **Sub-300ms global response times**
- 📈 **Infinite scalability**
- 🎨 **Complete creative control over ads**

---

## ❌ The Challenge

### 💸 **High Costs**
- $73,000/month for servers

### 🐌 **Slow Performance**
- Ads took 8–12 seconds to generate, sometimes over 30s during peak traffic

### 📊 **Scalability Issues**
- Manual provisioning took days, causing outages during booking season, 

### 📊 **Poor Visibility**
- Manual provisioning took days, causing outages during booking season, 

### 🔒 **Limited Creativity**
- Third-party tools restricted creative testing and ad personalization

---

## ✅ The Solution: Serverless-First Architecture

SkyTrip.com built a serverless ad generation platform using an AWS-based approach.

### 🏗️ **High-Level Architecture**

![image_alt](https://github.com/Tatenda-Prince/Serverless-Dynamic-Ad-Generation-Platform/blob/b52333cf0903907a55f4cbc1d7a656657532529a/img/diagram.jpg)

---

## 🚀 How It Works

### **Step-by-Step Process:**

1. **📱 Request:** A social media channel requests an ad
   ```
   https://skytrip.com/generate?hotel=CapeGrace&price=2500
   ```

2. **🌐 CloudFront:** Routes the request to the nearest AWS edge location

3. **🚪 API Gateway:** Validates the request and forwards it securely

4. **⚡ Lambda Function:**
   - Retrieves hotel image + pricing details
   - Adds overlays (logos, price tags, ratings)
   - Generates final personalized ad

5. **📤 Response:** Ad delivered back to user in <1 second

6. Supportive services like **Amazon CloudWatch** track performance and help quickly identify and fix issues.
---

## 🎉 The Outcomes

### ⚡ **Performance Gains**

Handles **1,000+ requests per second**.

Delivers images in **under 1 second**.

Maintains **99.9% availability.**

**Reduces costs by ~90%** since SkyTrip.com only pays for what’s used and no longer pays for third-party services.

Plus, **SkyTrip.com’s teams can now experiment and update ad designs instantly** no delays or vendor dependencies

### 📈 **Business Impact**
- ✅ **40% increase** in conversion rates
- 💰 **$2.1M additional revenue** from improved user experience
- 🌍 **Global expansion** to 50+ countries with zero infrastructure changes
- 👨‍💻 **300% increase** in developer productivity

---

## 🛠️ **Technical Stack**

### **Core AWS Services:**
- **⚡ AWS Lambda** - Serverless compute for ad generation
- **🌐 CloudFront** - Global CDN with 400+ edge locations
- **🚪 API Gateway** - REST API management and routing
- **📊 CloudWatch** - Monitoring and logging

### **Key Features:**
- 🎨 **Dynamic Content Generation** - Real-time personalized ads
- 🌍 **Global Performance** - Sub-300ms response times worldwide
- 📱 **Multi-Format Support** - Web, mobile, and social media ads
- 🔄 **Auto-Refresh** - New ads every 30 seconds

---

## 🚀 **Quick Start**

### **Prerequisites:**
- AWS Account
- Terraform installed
- Python 3.11+

### **Deployment:**
```bash
# 1. Clone repository
git clone https://github.com/Tatenda-Prince/Serverless-Dynamic-Ad-Generation-Platform.githttps://github.com/Tatenda-Prince/Serverless-Dynamic-Ad-Generation-Platform.git
```

### **2. Initialize Terraform**
```bash
terraform init
```
This downloads required providers and initializes the backend.

### **2. Validate Configuration**
```bash
terraform validate
```
Checks syntax and validates configuration files.


### **3. Plan Infrastructure**
```bash
terraform plan
```
Shows what resources will be created, modified, or destroyed.

### **4. Apply Infrastructure**
```bash
terraform apply
```
Creates the infrastructure. Type `yes` when prompted.

### **5. Get Outputs**
```bash
terraform output
```
Displays important URLs and resource names:

- `website_url`: CloudFront distribution URL

# 3. Test the system
```bash
curl "https://your-cloudfront-url.cloudfront.net/generate?hotel=Cape%20Grace"
```

**Live Demo:**
- **Single Ad View:** Generate personalized hotel advertisements
  
![image_alt](https://github.com/Tatenda-Prince/Serverless-Dynamic-Ad-Generation-Platform/blob/8b3f04dfb333324306a8e63fed9cf9a4f6a748d1/img/hotel%201%20.jpg)

  
- **List View:** Browse multiple African luxury hotels

![image_alt](https://github.com/Tatenda-Prince/Serverless-Dynamic-Ad-Generation-Platform/blob/99509c634c758af0f26233412b7741716c813134/img/hotel%202%20.jpg)


- **Interactive Search:** Real-time destination filtering


 🎯 **Key Takeaways**

1. **💡 Serverless = Operational Transformation** - Not just cost savings
2. **🌍 Global Architecture = Global Scale** - CloudFront was game-changing
3. **👨‍💻 Zero Maintenance = More Features** - Focus on business value
4. **⚡ Performance = Revenue** - 300ms response times drove 40% conversion increase
5. **🚀 Business Agility = Competitive Advantage** - Deploy globally in minutes



**This case study demonstrates how serverless architecture can transform business operations, reduce costs by 99.7%, and enable global scale without traditional infrastructure complexity.**
