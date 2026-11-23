---
title: "Nebius Credits"
layout: default
nav_order: 5
parent: Production AI Agents for Generative Media
has_children: false
---

# Nebius credits for course participants

Use the AI Cloud promo code from the Nebius AI Builder Program to run the course's GPU Endpoints and Jobs. The course promo code can be redeemed without a bank card. Token Factory has a separate code for LLM API usage.

## Request both codes

1. [Apply to the Nebius AI Builder Program](https://dev.nebius.com/builders). Being approved for the course does not automatically approve your Builder Program application.
2. Wait for the Builder Program welcome email. It confirms approval. The AI Cloud and Token Factory promo codes arrive in separate emails and can arrive at different times. Mikhail noted that after approval the code emails may take an additional day.
3. Look for both emails. If you already received a Token Factory code, keep it for Token Factory and wait for the separate AI Cloud email before setting up billing for GPU workloads.

<img src="{{ '/assets/images/production-ai-agents-for-generative-media/promo-code-email-subjects.png' | relative_url }}" alt="Nebius email subjects for the Builder Program welcome and a promo code" width="90%">

## Set up AI Cloud and redeem the code

1. Follow the setup instructions in the AI Cloud promo code email. Setting up your account creates a tenant and a project in the [Nebius AI Cloud console](https://console.nebius.com/).
2. Copy the code from the email that says Nebius AI Cloud. The same email shows the amount, expiry date, and a link to the redemption instructions.
3. In the AI Cloud console, go to Manage → Billing → Payments. Select Apply promo code. In the Top up balance dialog, select With promo code, paste the code, and select Apply promo code.
4. Check your balance and [Billing → Transactions](https://console.nebius.com/billing/transactions) to verify that the promo credit was added. Enter your code before it expires. Usage beyond your available credits is billed to your account.

<img src="{{ '/assets/images/production-ai-agents-for-generative-media/promo-code-email-example.png' | relative_url }}" alt="Example AI Cloud email showing where the promo code, amount, and expiry date appear. The code is masked." width="60%">

<img src="{{ '/assets/images/production-ai-agents-for-generative-media/redeem-ai-cloud-promo-code.png' | relative_url }}" alt="Nebius Billing dialog with With promo code selected and the Apply promo code button" width="50%">

These screenshots are from [Mikhail's illustrated instructions](https://datatalks-club.slack.com/archives/C0CEG1BUDKL/p1794992006015909). Your own email specifies the amount and expiry date for your code.

### What if the console asks me to add a card?

Go back to the instructions in your AI Cloud promo code email and look for With promo code in the Top up balance dialog. If the option is missing or these steps still leave you blocked, DM Mikhail with the error you see. [Mikhail's card clarification](https://datatalks-club.slack.com/archives/C0CEG1BUDKL/p1794907812515099)

### Why do I see a $25 card charge?

If you already added a card, Nebius adds the $25 it charges to your AI Cloud balance. You can check that top-up in Billing → Transactions and use it for GPU workloads. Redeeming an AI Cloud promo code adds its value to the account balance separately. The course promo code works without adding a card. [Mikhail's billing explanation](https://datatalks-club.slack.com/archives/C0CEG1BUDKL/p1795426127492729?thread_ts=1795095154.178339)

## What to do if a code is missing or fails

- Application is still under review. If you have already applied, keep the original application. If it is stuck, DM Mikhail with the email address you used and when you applied. A second application can be flagged as a duplicate.
- Welcome email arrived, but a code is missing. Count two days from the welcome email. If the AI Cloud or Token Factory code is still missing after that, DM Mikhail. Include the email address you applied with and which code is missing.
- Builder Program application was rejected, or you received credit through an earlier event. DM Mikhail with your application email and the context, so the Builder Program team can check your case.
- The code was rejected in Billing. Check which product the email names. Token Factory and AI Cloud use separate codes and separate balances. If the AI Cloud code itself fails, send the error message in your DM without sharing the code.

Mikhail has forwarded reported cases to the Builder Program team for review. [Promo code instructions and replies](https://datatalks-club.slack.com/archives/C0CEG1BUDKL/p1794992006015909) · [Latest credit update in Slack](https://datatalks-club.slack.com/archives/C0CEG1BUDKL/p1795428925030219)

## Check GPU availability and usage

If Sana's L40S option is missing, check the Capacity dashboard. Mikhail identified eu-north1 as the region offering the L40S Intel option used in the example. Check availability before starting a run. [Capacity announcement](https://datatalks-club.slack.com/archives/C0CEG1BUDKL/p1795020068322809)

Spot prices can change as often as every 15 minutes. A running Job is billed at the applicable price for each interval, so use the applicable [Nebius rates](https://nebius.com/prices) when you estimate costs. When you finish, stop or delete the Endpoints, Jobs, and DevLabs you started. Check Billing → Usage to make sure they stopped accruing charges. [Spot pricing answer](https://datatalks-club.slack.com/archives/C0CEG1BUDKL/p1795428188538789?thread_ts=1795366558.106759)

[Back to Getting Started]({{ '/courses/production-ai-agents-generative-media/getting-started/' | relative_url }})
