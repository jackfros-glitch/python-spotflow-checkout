# Spotflow Python Library

## Introduction

The **Spotflow Python SDK** helps you or rather enables users to make payments seamlessly. It integrates smoothly into your application, providing a streamlined checkout experience.

Available Features:

- Payments - Initializing payments

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
4. [License](#license)

## Requirements

1. **A valid Spotflow API keys**
2. **python** version >= 3.12


## Installation



using uv

```
  uv add spotflow-python-sdk

```

using pipenv

 ```bash
  pipenv install spotflow-python-sdk

```

using pip
```
  pip install spotflow-python-sdk

```


## Usage

🚀 Quick Start
```
from spotflow_sdk import SpotflowApiClient

api_key = "sk_test_xxxxxxx"

api_client = SpotflowApiClient(api_key=api_key)

payment_data = {
    "amount": 2000,
    "currency": "USD",
    "local_currency": "NGN",
    "email": "customer@example.com"
}

response = api_client.checkout.initialize_payment(**payment_data)
print(response.json())

```
Usage Example
Initializing a Payment
```
from spotflow_sdk import SpotflowApiClient

api_client = SpotflowApiClient(api_key="sk_test_xxxxx", timeout=10, max_retries=3)

payment_data = {
    "amount": 5000,
    "currency": "USD",
    "local_currency": "NGN",
    "email": "demo@spotflow.com"
}

try:
    response = api_client.checkout.initialize_payment(**payment_data)
    print("Payment initialized successfully:", response.json())
except Exception as e:
    print("Payment initialization failed:", e)


```

### Parameters

Read more about our parameters and how they can be used [here](https://docs.spotflow.one/api/API%20Endpoints/Collections/initialize-collections).

| Parameter           | Required |Description     |
| ------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| secret key         | True              | Your API Secret |
| reference           | False             | Your transaction reference. This MUST be unique for every transaction  |
| amount              | True              | Amount to charge the customer. NB: For subscription payments, amount comes from the plan details. This is not required for subscription payments.   |
| currency            | True             | Currency to charge in.           |
| localCurrency       | True            | This is required when a payment is being made in USD  |
| planId   | False | This is the plan ID being paid for a particular subscription plan, this is not required for one time payments. note that you have to have created a subscription plan on the platform before this works or you will get an error here is the doc on [subscriptions](https://docs.spotflow.one/api/API%20Endpoints/Subscription%20Plans/create-single-plan)  |
| email | True | This is the Customer's Email Address |
| metadata | False | This contains other information about the product such as the product name and other additional properties. Product Name should not be passed if planId is being passed |
| callBackUrl | False | This is the URL the browser redirects to on success of a payment |

# 🎉 Spotflow Hacktoberfest 2025

Welcome to **Spotflow’s open-source repositories** — part of this year’s **Hacktoberfest Challenge** by DigitalOcean!

Spotflow is a global **Merchant of Record (MoR)** that simplifies payment processing for businesses worldwide.  
We handle everything from global payment acceptance to compliance and settlement — empowering merchants to go global effortlessly.

## 🚀 How to Participate

1. Register for Hacktoberfest at [hacktoberfest.com](https://hacktoberfest.com)
2. Fork this repository.
3. Choose an issue labeled **`hacktoberfest`** or **`good first issue`**.
4. Make your contribution (see [Contributing Guidelines](./CONTRIBUTING.md)).
5. Open a pull request (PR) and add a **`hacktoberfest-accepted`** label to your PR.
6. Once approved and merged — it counts toward your Hacktoberfest goal!

## 💡 What You Can Contribute
- Improve or add SDK functionality  
- Write or improve API documentation 
- Spot bugs/improvements and write new issues (use [Issues Template](./ISSUE_TEMPLATE.md) as a guide).
- Add new language SDKs (Python, JS, Java, etc.)  
- Fix typos, formatting, or examples  
- Write tutorials or integration guides  

## 📅 Important Dates
- **Event:** October 1 – October 31, 2025
- **Application Deadline:** October 31, 2025

## 🧠 Resources
- Docs: [https://docs.spotflow.one](https://docs.spotflow.one)
- API Playground: [https://www.spotflow.one/demo](https://www.spotflow.one/demo)
- Sign up: [Spotflow Hacktoberfest Form](https://forms.gle/5KXXiy7mR35ocahL6)


## License

By contributing to this library, you agree that your contributions will be licensed under its [MIT license](/LICENSE).

Copyright (c) Spotflow Inc.
