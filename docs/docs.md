
# Architecture in Cloud

Let's discuss an API architecture and implementation in a cloud environment..

![Logo GCP](images/gcp.png)

Cloud Provider: [Google Cloud Platform](https://cloud.google.com/?hl=en)

## Content

1. [The Design of Architecture](#architecture)
2. [Used Tools](#used-tools)

## Architecture

This designed architecture project took into account the ease of implementing the API with scalability to support a growing number of requests and with high security for external consumption of the API.

![Architecture Design](images/architecture.drawio.svg)

## Used Tools

- Security Layer: [Cloud Armor](https://cloud.google.com/security/products/armor?hl=en)
    - To handle with questions about security the api from DDoS Protection, WaF Rules, secure the Load Balancer and others things. 
- Scalability: [Cloud Load Balancing](https://cloud.google.com/load-balancing?hl=en) and [Google Cloud Run](https://cloud.google.com/run?hl=pt-BR)
    - With this combination, it is possible to quickly deploy APIs using Cloud Run and perform configurations, for example, setting the minimum and maximum number of instances. With the Load Balancer, traffic will be distributed among them, increasing the scalability of the application to respond to minimum and maximum requests, in addition to other machine configurations for the instances.
- Monitoring and Alerts: [Google Cloud Monitoring](https://cloud.google.com/monitoring?hl=en)
    - With this GCP tool, it is possible for the application to generate logs for analysis, and to create monitoring and alerts using email/chat for tracking.
- CI/CD:
    - [Github](https://github.com/) to storage source code.
    - [Cloud Build](https://cloud.google.com/build?hl=en) and [Arifact Registry](https://cloud.google.com/artifact-registry) to build, host and deploy our container application in cloud run.
- Permission: [Cloud IAM](https://cloud.google.com/security/products/iam?hl=pt-br)
    - Full control in organization level of all users and services.
- Secure Secrets: [Secret Manager](https://cloud.google.com/security/products/secret-manager?hl=pt-br)
    - Manage secrets to store in vault secure to use in application.
    - Native support to cloud run.
- Billing: [Cloud Billing](https://cloud.google.com/billing/docs?hl=pt-br)
    - Monitoring the use of cloud resources.
    - Create billing limits, alerts, monitoring, others to manage charges.