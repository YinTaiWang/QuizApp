# Reference:
# https://www.gratisexam.com/vce-to-pdf/microsoft/az-900/Microsoft.selftestengine.AZ-900.v2021-05-13.by.wanggang.117q.pdf/

quiz_data = [
    {#1
        "question": (
            "You have an on-premises network that contains several servers."
            "\nYou plan to migrate all the servers to Azure."
            "\nYou need to recommend a solution to ensure that some of the servers are available if a single Azure data center goes offline for an extended period."
            
            "\n\nWhat should you include in the recommendation?"
            ),
        "options": [
            "A. fault tolerance",
            "B. elasticity",
            "C. scalability",
            "D. low latency"
        ],
        "answer": "A",
        "explanation": (
            "Fault tolerance is the ability of a system to continue to function in the event of a failure of some of its components."
            "\nIn this question, you could have servers that are replicated across datacenters."
            )
            },
    {#2
        "question": (
            "What are two characteristics of the public cloud? Each correct answer presents a complete solution."
            ),
        "options": [
            "A. dedicated hardware",
            "B. unsecured connections",
            "C. limited storage",
            "D. metered pricing",
            "E. self-service management"
        ],
        "answer": ["D", "E"],
        "explanation": (
            "With the public cloud, you get pay-as-you-go pricing -- you pay only for what you use, no CapEx costs."
            "\nWith the public cloud, you have self-service management. You are responsible for the deployment and configuration of the cloud resources such as virtual machines or web sites."
                "The underlying hardware that hosts the cloud resources is managed by the cloud provider."
            
            "\n\nIncorrect Answers:"
            "\nA: You don't have dedicated hardware. The underlying hardware is shared so you could have multiple customers using cloud resources hosted on the same physical hardware."
            "\nB: Connections to the public cloud are secure."
            "\nC: Storage is not limited. You can have as much storage as you like."
            )
            },
    {#3
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYour company plans to migrate all its data and resources to Azure."
            "\nThe company's migration plan states that only Platform as a Service (PaaS) solutions must be used in Azure."
            "\nYou need to deploy an Azure environment that meets the company migration plan."
            "\nSolution: You create an Azure App Service and Azure SQL databases."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": "Azure App Service and Azure SQL databases are examples of Azure PaaS solutions. Therefore, this solution does meet the goal."
        },
    {#4
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYour company plans to migrate all its data and resources to Azure."
            "\nThe company's migration plan states that only Platform as a Service (PaaS) solutions must be used in Azure."
            "\nYou need to deploy an Azure environment that meets the company migration plan."
            "\nSolution: You create an Azure App Service and Azure virtual machines that have Microsoft SQL Server installed."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": (
            "Azure App Service is a PaaS (Platform as a Service) service. However, Azure virtual machines are an IaaS (Infrastructure as a Service) service."
            "\nTherefore, this solution does not meet the goal."
            )
        },
    {#5
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYour company plans to migrate all its data and resources to Azure."
            "\nThe company's migration plan states that only Platform as a Service (PaaS) solutions must be used in Azure."
            "\nYou need to deploy an Azure environment that meets the company migration plan."
            "\nSolution: You create an Azure App Service and Azure Storage accounts."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": (
            "Azure App Service is a PaaS (Platform as a Service) service. However, Azure Storage accounts are a Storage as a Service (STaaS) service."
            "\nTherefore, this solution does not meet the goal."
            )
        },
    {#6
        "question": (
            "Your company hosts an accounting application named App1 that is used by all the customers of the company."
            "\nApp1 has low usage during the first three weeks of each month and very high usage during the last week of each month."
            "\nWhich benefit of Azure Cloud Services supports cost management for this type of usage pattern?"
            ),
        "options": [
            "A. high availability",
            "B. high latency",
            "C. elasticity",
            "D. load balancing"
        ],

        "answer": "C",
        "explanation": (
            "Elasticity in this case is the ability to provide additional compute resource when needed and reduce the compute resource when not needed to reduce costs."
            "\nAutoscaling is an example of elasticity."
            )
        },
    {#7
        "question": (
            "You plan to migrate a web application to Azure. The web application is accessed by external users."
            "\nYou need to recommend a cloud deployment solution to minimize the amount of administrative effort used to manage the web application."
            "\n\nWhat should you include in the recommendation?"
            ),
        "options": [
            "A. Software as a Service (SaaS)",
            "B. Platform as a Service (PaaS)",
            "C. Infrastructure as a Service (IaaS)",
            "D. Database as a Service (DaaS)"
        ],
        "answer": "B",
        "explanation": (
            "Azure App Service is a platform-as-a-service (PaaS) offering that lets you create web and mobile apps for any platform or device and connect to data anywhere, in the cloud or on-premises."
            "\nApp Service includes the web and mobile capabilities that were previously delivered separately as Azure Websites and Azure Mobile Services."
            )
        },
    {#8
        "question": (
            "You have an on-premises network that contains 100 servers."
            "\nYou need to recommend a solution that provides additional resources to your users. The solution must minimize capital and operational expenditure costs."
            "\nWhat should you include in the recommendation?"),
        "options": [
            "A. a complete migration to the public cloud",
            "B. an additional data center",
            "C. a private cloud",
            "D. a hybrid cloud"
        ],
        "answer": "D",
        "explanation": (
            "A hybrid cloud is a combination of a private cloud and a public cloud."
            "\nCapital expenditure is the spending of money up-front for infrastructure such as new servers."
            "\nWith a hybrid cloud, you can continue to use the on-premises servers while adding new servers in the public cloud (Azure for example). Adding new servers in Azure minimizes the capital expenditure costs as you are not paying for new servers as you would if you deployed new server on-premises."
            
            "\n\nIncorrect Answers:"
            "\nA: A complete migration of 100 servers to the public cloud would involve a lot of operational expenditure (the cost of migrating all the servers)."
            "\nB: An additional data center would involve a lot of capital expenditure (the cost of the new infrastructure)."
            "\nC: A private cloud is hosted on on-premises servers to this would involve a lot of capital expenditure (the cost of the new infrastructure to host the private cloud)."
            )
        },
    {#9
        "question": (
            "You plan to migrate several servers from an on-premises network to Azure."
            "\nWhat is an advantage of using a public cloud service for the servers over an on-premises network?"
            ),
        "options": [
            "A. The public cloud is owned by the public, NOT a private corporation",
            "B. The public cloud is a crowd-sourcing solution that provides corporations with the ability to enhance the cloud",
            "C. All public cloud resources can be freely accessed by every member of the public",
            "D. The public cloud is a shared entity whereby multiple corporations each use a portion of the resources in the cloud"
        ],
        "answer": "D",
        "explanation": (
            "The public cloud is a shared entity whereby multiple corporations each use a portion of the resources in the cloud. The hardware resources (servers, infrastructure etc.) are managed by the cloud provider."
            "\nMultiple companies create resources such as virtual machines and virtual networks on the hardware resources."
            
            "\n\nIncorrect Answers:"
            "\nA: The public cloud is not owned by the public. In the case of Microsoft Azure, the cloud is owned by Microsoft."
            "\nB: The public cloud is a not crowd-sourcing solution."
            "\nC: It is not true that public cloud resources can be freely accessed by every member of the public. You pay for a cloud subscription and create accounts for your users to access your cloud resources."
            "\nNo one can access your cloud resources until you create user accounts and provide the appropriate access permissions."
            )
        },
    {#10
        "question": (
            "In which type of cloud model are all the hardware resources owned by a third-party and shared between multiple tenants?"
            ),
        "options": [
            "A. private",
            "B. hybrid",
            "C. public"
        ],
        "answer": "C",
        "explanation": (
            "Microsoft Azure, Amazon Web Services and Google Cloud are three examples of public cloud services."
            "\nMicrosoft, Amazon and Google own the hardware. The tenants are the customers who use the public cloud services."
            )
        },
    {#11
        "question": (
            "You have 1,000 virtual machines hosted on the Hyper-V hosts in a data center."
            "\nYou plan to migrate all the virtual machines to an Azure pay-as-you-go subscription."
            "\nYou need to identify which expenditure model to use for the planned Azure solution."
            "\n\nWhich expenditure model should you identify?"
            ),
        "options": [
            "A. operational",
            "B. elastic",
            "C. capital",
            "D. scalable"
        ],
        "answer": "A",
        "explanation": (
            "One of the major changes that you will face when you move from on-premises cloud to the public cloud is the switch from capital expenditure (buying hardware) to operating expenditure (paying for service as you use it)."
            "\nThis switch also requires more careful management of your costs. The benefit of the cloud is that you can fundamentally and positively affect the cost of a service you use by merely shutting down or resizing it when it's not needed."
            )
    },
    {#13 (12skip)
        "question": (
            "Your company has an on-premises network that contains multiple servers."
            "\nThe company plans to reduce the following administrative responsibilities of network administrators:"
            "\n- Backing up application data"
            "\n- Replacing failed server hardware"
            "\n- Managing physical server security"
            "\n- Updating server operating systems"
            "\n- Managing permissions to shared documents"
            
            "\n\nThe company plans to migrate several servers to Azure virtual machines."
            "\nYou need to identify which administrative responsibilities will be eliminated after the planned migration."
            "\nWhich two responsibilities should you identify? Each correct answer presents a complete solution."
            ),
        "options": [
            "A. Replacing failed server hardware",
            "B. Backing up application data",
            "C. Managing physical server security",
            "D. Updating server operating systems",
            "E. Managing permissions to shared documents"
        ],
        "answer": ["A","C"],
        "explanation": (
            "Azure virtual machines run on Hyper-V physical servers. The physical servers are owned and managed by Microsoft. As an Azure customer, you have no access to the physical servers. "
            "\nMicrosoft manage the replacement of failed server hardware and the security of the physical servers so you don’t need to."
            
            "\n\nIncorrect Answers:"
            "\nB: Microsoft have no control over the applications you run on the virtual machines. Therefore, it is your responsibility to ensure that application data is backed up."
            "\nD: Microsoft do not manage the operating systems you run on the virtual machines. Therefore, it is your responsibility to ensure that the operating systems are updated."
            "\nE: Microsoft have no control over the shared folders you host on the virtual machines. Therefore, it is your responsibility to ensure that folder permissions are configured appropriately."
            )
    },
    {#14
        "question": (
            "You plan to provision Infrastructure as a Service (IaaS) resources in Azure."
            "\nWhich resource is an example of IaaS?"
            ),
        "options": [
            "A. an Azure web app",
            "B. an Azure virtual machine",
            "C. an Azure logic app",
            "D. an Azure SQL database",
        ],
        "answer": "B",
        "explanation": (
            "An Azure virtual machine is an example of Infrastructure as a Service (IaaS)."
            "\nAzure web app, Azure logic app and Azure SQL database are all examples of Platform as a Service (Paas)."
        )
    },
    {#15
        "question": (
            "To which cloud models can you deploy physical servers?"
            ),
        "options": [
            "A. private cloud and hybrid cloud only",
            "B. private cloud only",
            "C. private cloud, hybrid cloud and public cloud",
            "D. hybrid cloud only",
        ],
        "answer": "A",
        "explanation": (
            "A private cloud is on-premises so you can deploy physical servers."
            "\nA hybrid cloud is a mix of on-premise and public cloud resources. You can deploy physical servers on-premises."
        )
    },
    {#17 (skip 16)
        "question": (
            "You have 50 virtual machines hosted on-premises and 50 virtual machines hosted in Azure. The on-premises virtual machines and the Azure virtual machines connect to each other."
            "\nWhich type of cloud model is this?"
            ),
        "options": [
            "A. hybrid",
            "B. private",
            "C. public",
        ],
        "answer": "A",
        "explanation": ""
    },
    {#18
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYour company plans to migrate all its data and resources to Azure."
            "\nThe company’s migration plan states that only Platform as a Service (PaaS) solutions must be used in Azure."
            "\nYou need to deploy an Azure environment that meets the company migration plan."
            "\nSolution: You create Azure virtual machines, Azure SQL databases, and Azure Storage accounts."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": (
            "Azure Virtual Machines are an Infrastructure as a Service (IaaS) offering, and Azure Storage Accounts are not strictly categorized as Platform as a Service (PaaS), which violates the migration plan's requirements."
        )
    },
    {#19
        "question": (
            "Your company plans to deploy several custom applications to Azure. The applications will provide invoicing services to the customers of the company."
            "Each application will have several prerequisite applications and services installed."
            "\nYou need to recommend a cloud deployment solution for all the applications. What should you recommend?"
            ),
        "options": [
            "A. Software as a Service (SaaS)",
            "B. Platform as a Service (PaaS)",
            "C. Infrastructure as a Service (laaS)"
        ],
        "answer": "C",
        "explanation": (
            "C. Infrastructure as a Service (IaaS) provides full control over the virtual machines, allowing the installation of prerequisite applications and services required by the custom applications."
            
            "\n\nIncorrect Answers:"
            "\nA: SaaS (Software as a Service) is not suitable because it offers ready-to-use applications without the ability to customize underlying systems or install prerequisite applications."
            "\nB: PaaS (Platform as a Service) provides a managed environment for deploying applications but does not allow full control to install prerequisite services or manage the operating system."
            )
    },
    {#20
        "question": (
            "This question requires that you evaluate the underlined text to determine if it is correct."
            "\n\nAn Azure region \"contains one or more data centers that are connected by using a low-latency network\"."
            "\n\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that makes the statement correct."
            ),
        "options": [
            "A. No change is needed",
            "B. Is found in each country where Microsoft has a subsidiary office",
            "C. Can be found in every country in Europe and the Americas only",
            "D. Contains one or more data centers that are connected by using a high-latency network"
        ],
        "answer": "A",
        "explanation": (
            "An Azure region indeed contains one or more data centers that are connected by using a low-latency network, as stated."
            "This definition ensures fast and reliable communication between data centers within a region, which is crucial for delivering cloud services efficiently."
            )
    },
    {#21
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYou plan to deploy several Azure virtual machines."
            "\nYou need to ensure that the services running on the virtual machines are available if a single data center fails."
            "\nSolution: You deploy the virtual machines to two or more availability zones."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": (
            "Each Availability Zone has a distinct power source, network, and cooling. By architecting your solutions to use replicated VMs in zones, you can protect your apps and data from the loss of a datacenter."
            "If one zone is compromised, then replicated apps and data are instantly available in another zone."
            )
    },
    {#22
        "question": (
            "This question requires that you evaluate the underlined text to determine if it is correct."
            "\n\nOne of the benefits of Azure SQL Data Warehouse is that \"high availability\" is built into the platform."
            "\n\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that makes the statement correct."
            ),
        "options": [
            "A. No change is needed",
            "B. automatic scaling",
            "C. data compression",
            "D. versioning"
        ],
        "answer": "A",
        "explanation": (
            "Azure Data Warehouse (now known as Azure Synapse Analytics) is a PaaS offering from Microsoft. As with all PaaS services from Microsoft, SQL Data"
            "Warehouse offers an availability SLA of 99.9%. Microsoft can offer 99.9% availability because it has high availability features built into the platform."
            )
    },
    {#23
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYou plan to deploy several Azure virtual machines."
            "\nYou need to ensure that the services running on the virtual machines are available if a single data center fails."
            "\nSolution: You deploy the virtual machines to two or more regions."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": (
            "By deploying the virtual machines to two or more regions, you are effectively deploying them to multiple datacenters, as each Azure region consists of multiple datacenters. This setup ensures that if a single data center or an entire region fails, the services remain available, meeting the goal of ensuring high availability."
            )
    },
    {#24
        "question": (
            "You plan to store 20 TB of data in Azure. The data will be accessed infrequently and visualized by using Microsoft Power BI."
            "\nYou need to recommend a storage solution for the data."
            "\nWhich two solutions should you recommend? Each correct answer presents a complete solution."
            ),
        "options": [
            "A. Azure Data Lake",
            "B. Azure Cosmos DB",
            "C. Azure SQL Data Warehouse",
            "D. Azure SQL Database",
            "E. Azure Database for PostgreSQL"
        ],
        "answer": ["A","C"],
        "explanation": (
            "You can use Power BI to analyze and visualize data stored in Azure Data Lake and Azure SQL Data Warehouse."
            "\nAzure Data Lake is cost-effective for storing large amounts of structured and unstructured data that is infrequently accessed."
            "\nAzure SQL Data Warehouse (now Azure Synapse Analytics) is optimized for large-scale data storage and processing, making it ideal for querying and analyzing big datasets."
            
            "\n\nIncorrect Answers:"
            "\nB. Azure Cosmos DB: A NoSQL database optimized for high throughput and low latency, but it's not ideal for infrequently accessed large datasets."
            "\nD. Azure SQL Database: A transactional relational database not designed for managing or analyzing 20 TB of infrequently accessed data."
            "\nE. Azure Database for PostgreSQL: Suitable for relational database workloads but not optimized for large-scale analytics or infrequent access."
        )
    },
    {#25
        "question": (
            "You need to identify the type of failure for which an Azure Availability Zone can be used to protect access to Azure services."
            "\nWhat should you identify?"
            ),
        "options": [
            "A. a physical server failure",
            "B. an Azure region failure",
            "C. a storage failure",
            "D. an Azure data center failure"
        ],
        "answer": "D",
        "explanation": (
            "Azure Availability Zones are designed to protect against Azure data center failures. Each Availability Zone is a physically separate location within an Azure region, with independent power, cooling, and networking."
            "\nBy deploying resources across multiple Availability Zones, you can ensure service continuity in case of a single data center failure."
            "\nThey do not provide protection against entire region failures or specific server or storage failures."
            )
    },
    {#26
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYou plan to deploy several Azure virtual machines."
            "\nYou need to ensure that the services running on the virtual machines are available if a single data center fails."
            "\nSolution: You deploy the virtual machines to two or more resource groups."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": (
            "A resource group is a logical container for Azure resources. When you create a resource group, you specify which location to create the resource group in."
            "\nHowever, when you create a virtual machine and place it in the resource group, the virtual machine can still be in a different location (different datacenter)."
            "\nTherefore, creating multiple resource groups, even if they are in separate datacenters does not ensure that the services running on the virtual machines are available if a single data center fails."
            )
    },
    {#27
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYou plan to deploy several Azure virtual machines."
            "\nYou need to ensure that the services running on the virtual machines are available if a single data center fails."
            "\nSolution: You deploy the virtual machines to a scale set."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": (
            "Deploying the virtual machines to a scale set does not ensure availability if a single data center fails. While scale sets provide automatic scaling and manage VM distribution across fault domains within the same data center, they do not inherently distribute VMs across multiple data centers or Availability Zones."
            )
    },
    {#28
        "question": (
            "This question requires that you evaluate the underlined text to determine if it is correct."
            "\n\n\"Resource groups\" provide organizations with the ability to manage the compliance of Azure resources across multiple subscriptions."
            "\n\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that makes the statement correct."
            ),
        "options": [
            "A. No change is needed",
            "B. Management groups",
            "C. Azure policies",
            "D. Azure App Service plans"
        ],
        "answer": "C",
        "explanation": (
            "Azure policies specifically provide the ability to enforce compliance across Azure resources, whether within a single subscription or across multiple subscriptions."
            )
    },
    {#29
        "question": (
            "Your company plans to migrate to Azure. The company has several departments. All the Azure resources used by each department will be managed by a department administrator."
            
            "\n\nWhat are two possible techniques to segment Azure for the departments? Each correct answer presents a complete solution."
            ),
        "options": [
            "A. multiple subscriptions",
            "B. multiple Azure Active Directory (Azure AD) directories",
            "C. multiple regions",
            "D. multiple resource groups"
        ],
        "answer": ["A","D"],
        "explanation": (
            "Multiple subscriptions allow departments to manage resources independently with separate billing and quotas, while resource groups enable logical organization and delegated permissions for department-specific resource management."
            
            "\n\nIncorrect Answers:"
            "\nB. Multiple Azure Active Directory (Azure AD) directories: Azure AD directories are used for identity and access management, not for segmenting Azure resources by departments."
            "\nC. Multiple regions: Regions are geographic locations where Azure resources are hosted. They are not designed for organizational segmentation or department-level management."
            )  
    },
    {#30
        "question": (
            "You have an Azure environment that contains multiple Azure virtual machines."
            "\nYou plan to implement a solution that enables the client computers on your on-premises network to communicate to the Azure virtual machines."
            "\nYou need to recommend which Azure resources must be created for the planned solution."
            
            "\n\nWhich two Azure resources should you include in the recommendation? Each correct answer presents part of the solution."
            ),
        "options": [
            "A. a virtual network gateway",
            "B. a load balancer",
            "C. an application gateway",
            "D. a virtual network",
            "E. a gateway subnet"
        ],
        "answer": ["A","E"],
        "explanation": (
            "A virtual network gateway is required to establish a secure connection, such as a VPN, between your on-premises network and the Azure virtual network hosting the virtual machines."
            "A gateway subnet is needed within the virtual network to host the virtual network gateway, enabling seamless and secure communication between the two environments."
            
            "\n\nIncorrect Answers:"
            "\nB. a load balancer: A load balancer is used to distribute traffic across multiple virtual machines within a network for high availability and performance. It does not facilitate communication between on-premises networks and Azure virtual machines."
            "\nC. an application gateway: An application gateway is used for routing and managing web traffic at the application layer (HTTP/HTTPS) within Azure. It is not designed for establishing secure communication between on-premises networks and Azure."
            "\nD. a virtual network: While a virtual network is necessary to host Azure resources, the question states that the Azure environment with virtual machines already exists, so creating a new virtual network is not required for the planned solution."
            )
    },
    {#31
        "question": (
            "You attempt to create several managed Microsoft SQL Server instances in an Azure environment and receive a message that you must increase your Azure subscription limits."
            "\nWhat should you do to increase the limits?"
            ),
        "options": [
            "A. Create a service health alert",
            "B. Upgrade your support plan",
            "C. Modify an Azure policy",
            "D. Create a new support request"
        ],
        "answer": "D",
        "explanation": (
            "To increase subscription limits (quotas) in Azure, you need to create a support request."
            "\nAzure allows customers to request an increase in certain resource limits, such as the number of managed SQL Server instances, by submitting a support ticket."
            "\nThe other options are not relevant to this scenario"
        )
    },
    {#32
        "question": (
            "Your company plans to move several servers to Azure."
            "\nThe company’s compliance policy states that a server named FinServer must be on a separate network segment."
            "\nYou are evaluating which Azure services can be used to meet the compliance policy requirements."
            "\n\nWhich Azure solution should you recommend?"
            ),
        "options": [
            "A. a resource group for FinServer and another resource group for all the other servers",
            "B. a virtual network for FinServer and another virtual network for all the other servers",
            "C. a VPN for FinServer and a virtual network gateway for each other server",
            "D. one resource group for all the servers and a resource lock for FinServer"
        ],
        "answer": "B",
        "explanation": (
            "Networks in Azure are known as virtual networks.  A virtual network can have multiple IP address spaces and multiple subnets."
            "Azure automatically routes traffic between different subnets within a virtual network."
            "\nThe question states that FinServer must be on a separate network segment."
            "The only way to separate FinServer from the other servers in networking terms is to place the server in a different virtual network to the other servers."
            )
    },
    {#33
        "question": (
            "You plan to map a network drive from several computers that run Windows 10 to Azure Storage."
            "\nYou need to create a storage solution in Azure for the planned mapped drive."
            "\nWhat should you create?"
            ),
        "options": [
            "A. an Azure SQL database",
            "B. a virtual machine data disk",
            "C. a Files service in a storage account",
            "D. a Blobs service in a storage account"
        ],
        "answer": "C",
        "explanation": (
            "Azure Files provides fully managed file shares in the cloud that can be accessed via the Server Message Block (SMB) protocol, making it suitable for mapping a network drive from Windows 10 computers. It allows you to map Azure file shares just like a network drive, enabling seamless integration with your on-premises or cloud environment."
            
            "\n\nIncorrect Answers:"
            "\nA. Azure SQL database: This is used for relational database storage and is not relevant for file storage or mapping network drives."
            "\nB. Virtual machine data disk: This is for attaching disks to Azure virtual machines and isn't used for shared file access."
            "\nD. Blobs service in a storage account: Blob storage is designed for unstructured data, such as documents and media files, and cannot be mapped as a network drive via SMB."
            )
    },
    {
        "question": (
            "Your company plans to migrate all its network resources to Azure."
            "\nYou need to start the planning process by exploring Azure."
            "\nWhat should you create first?"
            ),
        "options": [
            "A. a subscription",
            "B. a resource group",
            "C. a virtual network",
            "D. a management group"
        ],
        "answer": "A",
        "explanation": (
            "The first thing you create in Azure is a subscription. You can think of an Azure subscription as an ‘Azure account’. You get billed per subscription."
        )
    },
    {#35
        "question": "Which Azure service should you use to collect events from multiple resources into a centralized repository?",
        "options": [
            "A. Azure Event Hubs",
            "B. Azure Analysis Services",
            "C. Azure Monitor",
            "D. Azure Stream Analytics"
        ],
        "answer": "A",
        "explanation": (
            "Azure Event Hubs is a scalable event streaming platform designed to collect and centralize events from multiple sources into a single repository for real-time or batch processing."
            
            "\n\nIncorrect Answers:"
            "\nB. Azure Analysis Services: Used for building analytical models and performing complex data analysis. It does not collect or centralize events."
            "\nC. Azure Monitor: Focused on monitoring Azure resources, collecting metrics, and logs. While it centralizes monitoring data, it’s not optimized for high-throughput event ingestion."
            "\nD. Azure Stream Analytics: Designed for real-time data processing and analytics on event streams but relies on services like Event Hubs for data ingestion. It does not centralize events itself."
            )
    },
    {#36
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYou plan to deploy several Azure virtual machines."
            "\nYou need to ensure that the services running on the virtual machines are available if a single data center fails."
            "\nSolution: You deploy the virtual machines to two or more scale sets."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": (
            "Deploying the virtual machines to two or more scale sets does not ensure availability in case of a single data center failure. While scale sets provide high availability and scalability within a region, they do not inherently distribute resources across multiple availability zones or regions to mitigate data center failures."
            )
    },
    {#37
        "question": (
            "You need to be notified when Microsoft plans to perform maintenance that can affect the resources deployed to an Azure subscription."
            "\nWhat should you use?"
            ),
        "options": [
            "A. Azure Monitor",
            "B. Azure Service Health",
            "C. Azure Advisor",
            "D. Microsoft Trust Center"
        ],
        "answer": "B",
        "explanation": (
            "Azure Service Health provides personalized alerts and guidance when Azure maintenance or service issues impact your resources."
            "It includes notifications for planned maintenance events that could affect your Azure subscription."
            )
    },
    {#40
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nAn Azure administrator plans to run a PowerShell script that creates Azure resources."
            "\nYou need to recommend which computer configuration to use to run the script."
            "\nSolution: Run the script from a computer that runs Windows 10 and has the Azure PowerShell module installed."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": (
            "To run a PowerShell script that creates Azure resources, you can use a computer running Windows 10 with the Azure PowerShell module installed. The Azure PowerShell module provides the necessary cmdlets to interact with Azure resources, and Windows 10 supports running PowerShell scripts natively."
            "\nIn this question, the computer has the Azure PowerShell module installed. Therefore, this solution does meet the goal."
            )
    },
    {#42
        "question": (
            "Which service provides serverless computing in Azure?"
            ),
        "options": [
            "A. Azure Virtual Machines",
            "B. Azure Functions",
            "C. Azure storage account",
            "D. Azure dedicated hosts",
        ],
        "answer": "B",
        "explanation": (
            "Azure Functions is a serverless computing service in Azure that allows you to run small pieces of code (functions) without managing the underlying infrastructure. It automatically scales based on demand and charges only for the compute resources used during execution."
            )
    },
    {#43
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYou have an Azure subscription named Subscription1. You sign in to the Azure portal and create a resource group named RG1."
            "\nFrom Azure documentation, you have the following command that creates a virtual machine named VM1."
            "\n<az vm create --resource-group RG1 --name VM1 --image UbuntuLTS --generate-ssh-keys>"
            "\nYou need to create VM1 in Subscription1 by using the command."
            "\nSolution: From the Azure portal, launch Azure Cloud Shell and select Bash. Run the command in Cloud Shell."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": (
            "Azure Cloud Shell is a browser-based shell accessible from the Azure portal, supporting both PowerShell and Bash environments. It is preconfigured with tools like Azure CLI, allowing you to run the provided command"
            )
    },
    {#44
        "question": (
            "Your company has several business units."
            "\nEach business unit requires 20 different Azure resources for daily operation. All the business units require the same type of Azure resources."
            "\nYou need to recommend a solution to automate the creation of the Azure resources."
            "\nWhat should you include in the recommendations?"
            ),
        "options": [
            "A. Azure Resource Manager templates",
            "B. virtual machine scale sets",
            "C. the Azure API Management service",
            "D. management groups"
        ],
        "answer": "A",
        "explanation": (
            "Azure Resource Manager (ARM) templates allow you to define the infrastructure and configuration of Azure resources in a JSON file."
            "\nThis enables you to automate the deployment of multiple resources consistently and repeatedly, making it ideal for creating the same set of resources across multiple business units."
            )
    },
    {#46
        "question": (
            "A team of developers at your company plans to deploy, and then remove, 50 customized virtual machines each week."
            "Thirty of the virtual machines run Windows Server 2016 and 20 of the virtual machines run Ubuntu Linux."
            "\nYou need to recommend which Azure service will minimize the administrative effort required to deploy and remove the virtual machines."
            "\nWhat should you recommend?"
            ),
        "options": [
            "A. Azure Reserved Virtual Machines (VM) Instances",
            "B. Azure virtual machine scale sets",
            "C. Azure DevTest Labs",
            "D. Microsoft Managed Desktop"
        ],
        "answer": "C",
        "explanation": (
            "Azure DevTest Labs is designed to minimize administrative effort for creating, managing, and deleting virtual machines."
            "\nIt is ideal for scenarios where developers need to frequently deploy and remove multiple VMs, as it provides automation, cost control, and streamlined management for test and development environments."
            )
    },
    {#47
        "question": (
            "A support engineer plans to perform several Azure management tasks by using the Azure CLI."
            "\nYou install the CLI on a computer."
            "\nYou need to tell the support engineer which tools to use to run the CLI."
            "\nWhich two tools should you instruct the support engineer to use? Each correct answer presents a complete solution."
            ),
        "options": [
            "A. Command Prompt",
            "B. Azure Resource Explorer",
            "C. Windows PowerShell",
            "D. Windows Defender Firewall",
            "E. Network and Sharing Center"
        ],
        "answer": ["A","C"],
        "explanation": "For Windows, the Azure CLI is installed via an MSI, which gives you access to the CLI through the Windows Command Prompt (CMD) or PowerShell."
    },
    {#48
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYou have an Azure environment. You need to create a new Azure virtual machine from a tablet that runs the Android operating system."
            "\nSolution: You use PowerShell in Azure Cloud Shell."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": (
            "Azure Cloud Shell is a browser-based shell accessible from any device, including a tablet running Android. It supports PowerShell and Azure CLI, allowing you to manage Azure resources."
            "\nUsing PowerShell in Cloud Shell, you can create an Azure virtual machine, so this solution meets the goal."
            )
    },
    {#49
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYou have an Azure environment. You need to create a new Azure virtual machine from a tablet that runs the Android operating system."
            "\nSolution: You use the PowerApps portal."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": (
            "PowerApps lets you quickly build business applications with little or no code. It is not used to create Azure virtual machines. Therefore, this solution does not meet the goal."
            )
    },
    {#50
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYou have an Azure environment. You need to create a new Azure virtual machine from a tablet that runs the Android operating system."
            "\nSolution: You use the Azure portal."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": (
            "The Azure portal is a web-based management interface that can be accessed from any device with a browser, including a tablet running Android."
            "\nYou can use the portal to create and manage Azure resources, including virtual machines. Therefore, this solution meets the goal."
            )
    },
    {#51
        "question": (
            "This question requires that you evaluate the underlined text to determine if it is correct."
            "\n\n\"Azure Databricks\" is an Apache Spark-based analytics service."
            "\n\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that makes the statement correct."
            ),
        "options": [
            "A. No change is needed",
            "B. Azure Data Factory",
            "C. Azure DevOps",
            "D. Azure HDInsight"
        ],
        "answer": "A",
        "explanation": (
            "Azure Databricks is indeed an Apache Spark-based analytics service. It provides a fast, easy, and collaborative platform for big data analytics and machine learning. No changes are needed to the statement."
            )
    },
    {#52
        "question": "Which Azure service provides a set of version control tools to manage code?",
        "options": [
            "A. Azure Repos",
            "B. Azure DevTest Labs",
            "C. Azure Storage",
            "D. Azure Cosmos DB"
        ],
        "answer": "A",
        "explanation": (
            "Azure Repos provides a set of version control tools to manage code."
            "\nIt supports both Git and Team Foundation Version Control (TFVC), enabling teams to collaborate on code development, track changes, and manage code versions efficiently."
            
            "\n\nIncorrect Answers:"
            "\nB. Azure DevTest Labs: Used to manage development and test environments, not version control."
            "\nC. Azure Storage: Provides scalable cloud storage solutions but does not offer version control tools for code."
            "\nD. Azure Cosmos DB: A globally distributed database for managing data, not code."
            )
    },
    {#53
        "question": (
            "You have a virtual machine named VM1 that runs Windows Server 2016. VM1 is in the East US Azure region."
            "\nWhich Azure service should you use from the Azure portal to view service failure notifications that can affect the availability of VM1?"
            ),
        "options": [
            "A. Azure Service Fabric",
            "B. Azure Monitor",
            "C. Azure virtual machines",
            "D. Azure Advisor"
        ],
        "answer": "B",
        "explanation": (
            "Azure Monitor allows you to view service failure notifications and analyze metrics and logs for your resources, including virtual machines."
            "\nIt provides insights into the health and availability of your Azure services and can alert you about potential issues affecting VM1's availability."
            "\nAzure Monitor -> Service Health -> Resource health."
            
            "\n\nIncorrect Answers:"
            "\nA. Azure Service Fabric: Used for building and managing microservices applications, not for monitoring VM availability or failures."
            "\nC. Azure virtual machines: This is where you manage VMs, but it does not provide service failure notifications."
            "\nD. Azure Advisor: Provides recommendations to optimize Azure resources but does not notify you about service failures."
            )
    },
    {#54
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nAn Azure administrator plans to run a PowerShell script that creates Azure resources."
            "\nYou need to recommend which computer configuration to use to run the script."
            "\nSolution: Run the script from a computer that runs macOS and has PowerShell Core 6.0 installed."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": (
            "PowerShell Core 6.0 is a cross-platform version of PowerShell that works on macOS, Linux, and Windows. It supports Azure modules, enabling users to run scripts to create Azure resources."
            "\nTherefore, running the script from a macOS computer with PowerShell Core 6.0 installed meets the goal."
            )
    },
    {#55
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nAn Azure administrator plans to run a PowerShell script that creates Azure resources."
            "\nYou need to recommend which computer configuration to use to run the script."
            "\nSolution: Run the script from a computer that runs Chrome OS and uses Azure Cloud Shell."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": (
            "Azure Cloud Shell is a browser-based shell accessible from any device, including those running Chrome OS. It provides preconfigured tools like Azure PowerShell and Azure CLI to manage Azure resources."
            "\nTherefore, running the script from Chrome OS using Azure Cloud Shell meets the goal."
            )
    },
    {#56
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nAn Azure administrator plans to run a PowerShell script that creates Azure resources."
            "\nYou need to recommend which computer configuration to use to run the script."
            "\nSolution: Run the script from a computer that runs macOS and has PowerShell Core 6.0 installed."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": (
            "PowerShell Core 6.0 is a cross-platform version of PowerShell that works on macOS, Linux, and Windows. It supports Azure modules, allowing you to run scripts for creating and managing Azure resources."
            "\nUsing a macOS computer with PowerShell Core 6.0 installed meets the goal."
            )
    },
    {#59
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYou have an Azure environment. You need to create a new Azure virtual machine from a tablet that runs the Android operating system."
            "\nSolution: You use Bash in Azure Cloud Shell."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": (
            "Azure Cloud Shell is accessible through a browser and supports Bash, allowing you to manage and create Azure resources from any device, including an Android tablet."
            "\nUsing Bash in Cloud Shell meets the goal for creating a new Azure virtual machine."
            )
    },
    {#60
        "question": (
            "You have an on-premises application that sends email notifications automatically based on a rule."
            "\nYou plan to migrate the application to Azure."
            "\nYou need to recommend a serverless computing solution for the application."
            "\nWhat should you include in the recommendation?"
            ),
        "options": [
            "A. a web app",
            "B. a server image in Azure Marketplace",
            "C. a logic app",
            "D. an API app"
        ],
        "answer": "C",
        "explanation": (
            "Azure Logic Apps is a cloud service that helps you schedule, automate, and orchestrate tasks, business processes, and workflows when you need to integrate apps, data, systems, and services across enterprises or organizations."
            "\nLogic Apps simplifies how you design and build scalable solutions for app integration, data integration, system integration, enterprise application integration (EAI), and business-to-business (B2B) communication, whether in the cloud, on premises, or both."
        )
    },
    {#61
        "question": (
            "You plan to deploy a website to Azure. The website will be accessed by users worldwide and will host large video files."
            "\nYou need to recommend which Azure feature must be used to provide the best video playback experience."
            "\nWhat should you recommend?"
            ),
        "options": [
            "A. an application gateway",
            "B. an Azure ExpressRoute circuit",
            "C. a content delivery network (CDN)",
            "D. an Azure Traffic Manager profile"
        ],
        "answer": "C",
        "explanation": (
            "An Azure Content Delivery Network (CDN) is the best solution for improving video playback performance for users worldwide. It works by caching video files at globally distributed edge servers, ensuring faster delivery and lower latency. This significantly enhances the playback experience for large video files, as users are served content from the server closest to their location."
            
            "\n\nIncorrect Answers:"
            "\nA. an application gateway: Manages HTTP traffic but does not optimize the delivery of large files or provide global caching."
            "\nB. an Azure ExpressRoute circuit: Offers private network connectivity to Azure, which is unnecessary for public video delivery."
            "\nD. an Azure Traffic Manager profile: Helps direct traffic across regions but does not cache or optimize content delivery for large files."
            )
    },
    {#62
        "question": (
            "Your company plans to deploy several million sensors that will upload data to Azure."
            "\nYou need to identify which Azure resources must be created to support the planned solution."
            "\nWhich two Azure resources should you identify? Each correct answer presents part of the solution."
            ),
        "options": [
            "A. Azure Data Lake",
            "B. Azure Queue storage",
            "C. Azure File Storage",
            "D. Azure IoT Hub",
            "E. Azure Notification Hubs"
        ],
        "answer": ["A","D"],
        "explanation": (
            "Azure IoT Hub enables communication, monitoring, and management of millions of IoT devices, making it essential for handling sensor data. "
            "\nAzure Data Lake provides scalable storage for large volumes of structured and unstructured data, ideal for storing and analyzing the data uploaded by these sensors."
            
            "\n\nIncorrect Answers:"
            "\nB. Azure Queue Storage: Useful for message queuing but not designed to handle massive data ingestion from millions of sensors or long-term storage."
            "\nC. Azure File Storage: Provides SMB-based file shares, which are not optimized for the scale and type of data produced by millions of sensors."
            "\nE. Azure Notification Hubs: Designed for sending push notifications to applications, not for managing or storing data from sensors."
        )
    },
    {#63
        "question": (
            "You have an Azure web app."
            "\nYou need to manage the settings of the web app from an iPhone."
            "\nWhat are two Azure management tools that you can use? Each correct answer presents a complete solution."
            ),
        "options": [
            "A. Azure CLI",
            "B. the Azure portal",
            "C. Azure Cloud Shell",
            "D. Windows PowerShell",
            "E. Azure Storage Explorer"
        ],
        "answer": ["B","C"],
        "explanation": (
            "The Azure portal is a web-based interface accessible from any device with a browser, including an iPhone, allowing you to manage your web app settings easily. "
            "\nAzure Cloud Shell is a browser-based command-line tool integrated with the Azure portal, providing the ability to manage resources using Bash or PowerShell from any device."
            
            "\n\nIncorrect Answers:"
            "\nA. Azure CLI: While it is a command-line tool for managing Azure resources, it requires installation and is not accessible directly from an iPhone."
            "\nD. Windows PowerShell: Requires a Windows environment and cannot be used natively on an iPhone."
            "\nE. Azure Storage Explorer: A standalone application for managing Azure storage resources, not web app settings."
        )
    },
    {#64
        "question": (
            "Your company plans to deploy an Artificial Intelligence (AI) solution in Azure."
            "\nWhat should the company use to build, test, and deploy predictive analytics solutions?"
            ),
        "options": [
            "A. Azure Logic Apps",
            "B. Azure Machine Learning Designer",
            "C. Azure Batch",
            "D. Azure Cosmos DB"
        ],
        "answer": "B",
        "explanation": (
            "Azure Machine Learning designer lets you visually connect datasets and modules on an interactive canvas to create machine learning models."
        )
    },
    {#65
        "question": (
            "What can you use to automatically send an alert if an administrator stops an Azure virtual machine?"
            ),
        "options": [
            "A. Azure Advisor",
            "B. Azure Service Health",
            "C. Azure Monitor",
            "D. Azure Network Watcher"
        ],
        "answer": "C",
        "explanation": (
            "Azure Monitor allows you to create alerts based on activity logs and metrics. You can configure an alert rule to trigger a notification if an administrator stops a virtual machine, ensuring you are automatically informed of such events."
        )
    },
    {#66
        "question": (
            "You have an Azure environment."
            "\nYou need to create a new Azure virtual machine from a tablet that runs the Android operating system."
            "\nWhat are three possible solutions? Each correct answer presents a complete solution."
            ),
        "options": [
            "A. Use Bash in Azure Cloud Shell.",
            "B. Use PowerShell in Azure Cloud Shell.",
            "C. Use the PowerApps portal.",
            "D. Use the Security & Compliance admin center.",
            "E. Use the Azure portal."
        ],
        "answer": ["A","B","E"],
        "explanation": (
            "The Android tablet device will have a web browser (Chrome). That’s enough to connect to the Azure portal."
            "\nThe Azure portal offers three ways to create a VM:"
            "\n- Using the graphical portal."
            "\n- Using the Azure Cloud Shell using Bash."
            "\n- Using the Azure Cloud Shell using PowerShell."
        )
    },
    {#67
        "question": (
            "A team of developers at your company plans to deploy, and then remove, 50 virtual machines each week. All the virtual machines are configured by using Azure Resource Manager templates."
            "\nYou need to recommend which Azure service will minimize the administrative effort required to deploy and remove the virtual machines."
            "\nWhat should you recommend?"
            ),
        "options": [
            "A. Azure Reserved Virtual Machine (VM) Instances",
            "B. Azure DevTest Labs",
            "C. Azure virtual machine scale sets",
            "D. Microsoft Managed Desktop"
        ],
        "answer": "B",
        "explanation": (
            "DevTest Labs creates labs consisting of pre-configured bases or Azure Resource Manager templates."
            "\nBy using DevTest Labs, you can test the latest versions of your applications by doing the following tasks:"
            "\n- Quickly provision Windows and Linux environments by using reusable templates and artifacts."
            "\n- Easily integrate your deployment pipeline with DevTest Labs to provision on-demand environments."
            "\n- Scale up your load testing by provisioning multiple test agents and create pre-provisioned environments for training and demos."
        )
    },
    {#68
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYou have an Azure subscription named Subscription1. You sign in to the Azure portal and create a resource group named RG1."
            "\nFrom Azure documentation, you have the following command that creates a virtual machine named VM1."
            "\n<az vm create --resource-group RG1 --name VM1 --image UbuntuLTS --generate-ssh-keys>"
            "\nYou need to create VM1 in Subscription1 by using the command."
            "\nSolution: From the Azure portal, launch Azure Cloud Shell and select PowerShell. Run the command in Cloud Shell."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": (
            "Azure Cloud Shell is a browser-based shell accessible from the Azure portal, supporting both PowerShell and Bash environments. It is preconfigured with tools like Azure CLI, allowing you to run the provided command"
            )
    },
    {#69
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYou have an Azure subscription named Subscription1. You sign in to the Azure portal and create a resource group named RG1."
            "\nFrom Azure documentation, you have the following command that creates a virtual machine named VM1."
            "\n<az vm create --resource-group RG1 --name VM1 --image UbuntuLTS --generate-ssh-keys>"
            "\nYou need to create VM1 in Subscription1 by using the command."
            "\nSolution: From a computer that runs Windows 10, install Azure CLI. From PowerShell, sign in to Azure and then run the command."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": (
            "The command can indeed be run from PowerShell or the command prompt if the Azure CLI is installed on the Windows 10 computer."
            "\nThis method requires the command to be executed locally on the Windows 10 computer, not within the Azure portal or Azure Cloud Shell. Therefore, the solution meets the goal."
            )
    },
    {#70
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYou have an Azure subscription named Subscription1. You sign in to the Azure portal and create a resource group named RG1."
            "\nFrom Azure documentation, you have the following command that creates a virtual machine named VM1."
            "\n<az vm create --resource-group RG1 --name VM1 --image UbuntuLTS --generate-ssh-keys>"
            "\nYou need to create VM1 in Subscription1 by using the command."
            "\nSolution: From a computer that runs Windows 10, install Azure CLI. From a command prompt, sign in to Azure and then run the command."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": (
            "The command can indeed be run from PowerShell or the command prompt if the Azure CLI is installed on the Windows 10 computer."
            "\nThis method requires the command to be executed locally on the Windows 10 computer, not within the Azure portal or Azure Cloud Shell. Therefore, the solution meets the goal."
            )
    },
    {#71
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYour Azure environment contains multiple Azure virtual machines."
            "\nYou need to ensure that a virtual machine named VM1 is accessible from the Internet over HTTP."
            "\nSolution: You modify an Azure firewall."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": (
            "An Azure Firewall can be configured to allow inbound HTTP (port 80) traffic to a virtual machine."
            "\nBy creating a rule in the Azure Firewall to permit HTTP traffic, you can ensure that VM1 is accessible from the Internet over HTTP. This solution meets the goal."
            "\n\nhttps://adamtheautomator.com/azure-firewall/"
            )
    },
    {#72
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYour Azure environment contains multiple Azure virtual machines."
            "\nYou need to ensure that a virtual machine named VM1 is accessible from the Internet over HTTP."
            "\nSolution: You modify an Azure Traffic Manager profile."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": (
            "Azure Traffic Manager is used for DNS-based traffic routing and load balancing across multiple endpoints or regions. It does not directly handle network-level access, such as allowing HTTP traffic to a virtual machine."
            )
    },
    {#73
        "question": (
            "Your company plans to deploy several web servers and several database servers to Azure."
            "\nYou need to recommend an Azure solution to limit the types of connections from the web servers to the database servers."
            "\nWhat should you include in the recommendation?"
            ),
        "options": [
            "A. network security groups (NSGs)",
            "B. Azure Service Bus",
            "C. a local network gateway",
            "D. a route filter"
        ],
        "answer": "A",
        "explanation": (
            "Network security groups (NSGs) are used in Azure to control inbound and outbound network traffic to and from Azure resources. They can be configured to allow or deny specific types of connections between web servers and database servers, ensuring only authorized traffic is permitted."
        )
    },
    {#74
        "question": (
            "Which service provides network traffic filtering across multiple Azure subscriptions and virtual networks?"
            ),
        "options": [
            "A. Azure Firewall",
            "B. an application security group",
            "C. Azure DDoS protection",
            "D. a network security group (NSG)"
        ],
        "answer": "A",
        "explanation": (
            "Azure Firewall is a managed, cloud-based network security service that provides network traffic filtering across multiple Azure subscriptions and virtual networks. It allows for centralized control of inbound and outbound traffic, supporting rules for application and network filtering at scale."
        )
    },
    {#75
        "question": (
            "Which Azure service should you use to store certificates?"
            ),
        "options": [
            "A. Azure Security Center",
            "B. an Azure Storage account",
            "C. Azure Key Vault",
            "D. Azure Information Protection"
        ],
        "answer": "C",
        "explanation": (
            "Azure Key Vault is a cloud service specifically designed to store and manage cryptographic keys, certificates, secrets, and other sensitive information securely. It provides secure storage and access control for certificates, making it the ideal choice."
        )
    },
    {#76
        "question": (
            "You need to configure an Azure solution that meets the following requirements:"
            "\n- Secures websites from attacks"
            "\n- Generates reports that contain details of attempted attacks"
            "\nWhat should you include in the solution?"
            ),
        "options": [
            "A. Azure Firewall"
            "B. a network security group (NSG)"
            "C. Azure Information Protection"
            "D. DDoS protection"
        ],
        "answer": "D",
        "explanation": (
            "Azure DDoS Protection protects applications by mitigating Distributed Denial of Service (DDoS) attacks. It includes monitoring and automatic mitigation for attacks targeting Azure-hosted websites. Additionally, it provides detailed reports and telemetry on attempted attacks, fulfilling the requirement for securing websites and generating attack details."
            
            "\n\nIncorrect Answers:"
            "\nA. Azure Firewall: Provides network traffic filtering and application rules but does not specialize in mitigating DDoS attacks or generating reports specific to attempted attacks."
            "\nB. Network Security Group (NSG): Filters network traffic at the subnet or NIC level but does not provide comprehensive attack protection or reporting capabilities."
            "\nC. Azure Information Protection: Focuses on classifying and protecting data, not securing websites from attacks."
        )
    },
    {#77
        "question": (
            "Your Azure environment contains multiple Azure virtual machines."
            "\nYou need to ensure that a virtual machine named VM1 is accessible from the Internet over HTTP."
            "\nWhat are two possible solutions? Each correct answer presents a complete solution."
            ),
        "options": [
            "A. Modify an Azure Traffic Manager profile"
            "B. Modify a network security group (NSG)"
            "C. Modify a DDoS protection plan"
            "D. Modify an Azure firewall"
        ],
        "answer": ["B","D"],
        "explanation": (
            "To ensure that VM1 is accessible from the Internet over HTTP (port 80), you need to allow inbound HTTP traffic. Both Network Security Groups (NSGs) and Azure Firewall can be configured to enable this access:"
            "\nB. Modify a network security group (NSG): NSGs are used to control inbound and outbound traffic to Azure resources at the subnet or NIC level. Adding a rule to allow HTTP (port 80) traffic to VM1 will enable Internet access."
            "\nD. Modify an Azure firewall: Azure Firewall can also allow HTTP traffic by defining a rule for inbound traffic on port 80. This solution is more appropriate for centralized traffic management."
            )
    },
    {#78
        "question": (
            "You have an Azure environment that contains 10 virtual networks and 100 virtual machines."
            "\nYou need to limit the amount of inbound traffic to all the Azure virtual networks."
            "\nWhat should you create?"
            ),
        "options": [
            "A. one application security group (ASG)",
            "B. 10 virtual network gateways",
            "C. 10 Azure ExpressRoute circuits",
            "D. one Azure firewall"
        ],
        "answer": "D",
        "explanation": (
            "An Azure Firewall is a centralized network security service that can control and limit inbound traffic to all Azure virtual networks."
            "\nBy deploying a single Azure Firewall and connecting it to the virtual networks, you can create rules to manage and limit traffic effectively across the environment."
            )
    },
    {#79
        "question": (
            "This question requires that you evaluate the underlined text to determine if it is correct."
            "\n\nAzure Key Vault is used to store secrets for \"Azure Active Directory (Azure AD)\" user accounts."
            "\n\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that makes the statement correct."
            ),
        "options": [
            "A. No change is needed",
            "B. Azure Active Directory (Azure AD) administrative accounts",
            "C. Personally Identifiable Information (PII)",
            "D. server applications"
        ],
        "answer": "D",
        "explanation": (
            "Azure Key Vault is primarily used to store and manage sensitive information like secrets, keys, and certificates for server applications and services. It ensures secure access to credentials, API keys, and other sensitive data required by applications, not user accounts in Azure Active Directory (Azure AD)."
            "\n\nIncorrect Answers:"
            "\nC. Personally Identifiable Information (PII): While Key Vault can secure sensitive data, it is not explicitly designed to manage PII."
            )
    },
    {#80
        "question": (
            "Your company plans to automate the deployment of servers to Azure."
            "Your manager is concerned that you may expose administrative credentials during the deployment."
            "You need to recommend an Azure solution that encrypts the administrative credentials during the deployment."
            "What should you include in the recommendation?"
            ),
        "options": [
            "A. Azure Key Vault",
            "B. Azure Information Protection",
            "C. Azure Security Center",
            "D. Azure Multi-Factor Authentication (MFA)"
        ],
        "answer": "A",
        "explanation": (
            "Azure Key Vault is the appropriate solution for securely managing and encrypting sensitive information like administrative credentials during deployment. It ensures credentials are securely stored and accessed only by authorized applications or users, preventing exposure during the deployment process."
            )
    },
    {#81
        "question": (
            "You plan to deploy several Azure virtual machines."
            "\nYou need to control the ports that devices on the Internet can use to access the virtual machines."
            "\nWhat should you use?"
            ),
        "options": [
            "A. a network security group (NSG)",
            "B. an Azure Active Directory (Azure AD) role",
            "C. an Azure Active Directory group",
            "D. an Azure key vault"
        ],
        "answer": "A",
        "explanation": (
            "A Network Security Group (NSG) is used to control inbound and outbound network traffic to and from Azure resources, such as virtual machines. NSGs allow you to define security rules to permit or deny traffic based on source IP, destination IP, port, and protocol, effectively controlling which ports can be accessed from the Internet."
            )
    },
    {#82
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYour Azure environment contains multiple Azure virtual machines."
            "\nYou need to ensure that a virtual machine named VM1 is accessible from the Internet over HTTP."
            "\nSolution: You modify a network security group (NSG)."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": (
            "A Network Security Group (NSG) is used to control network traffic to and from Azure resources, such as virtual machines. To make VM1 accessible over HTTP, you can modify the NSG associated with the VM or its subnet by creating an inbound rule that allows traffic on port 80 (HTTP). This solution meets the goal."
            )
    },
    {#83
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYour Azure environment contains multiple Azure virtual machines."
            "\nYou need to ensure that a virtual machine named VM1 is accessible from the Internet over HTTP."
            "\nSolution: You modify a DDoS protection plan."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": (
            "A DDoS protection plan is designed to protect Azure resources from Distributed Denial of Service (DDoS) attacks, but it does not control access or manage inbound HTTP traffic."
            )
    },
    {#84
        "question": (
            "You need to collect and automatically analyze security events from Azure Active Directory (Azure AD)."
            "\nWhat should you use?"
            ),
        "options": [
            "A. Azure Sentinel",
            "B. Azure Synapse Analytics",
            "C. Azure AD Connect",
            "D. Azure Key Vault"
        ],
        "answer": "A",
        "explanation": (
            "Azure Sentinel is a cloud-native security information and event management (SIEM) solution. It collects, analyzes, and responds to security events from various sources, including Azure Active Directory (Azure AD). It offers built-in connectors for Azure AD to provide advanced analytics, threat detection, and automated incident response."
            )
    },
    {#85
        "question": (
            "You need to ensure that when Azure Active Directory (Azure AD) users connect to Azure AD from the Internet by using an anonymous IP address, the users are prompted automatically to change their password."
            "\nWhich Azure service should you use?"
            ),
        "options": [
            "A. Azure AD Connect Health",
            "B. Azure AD Privileged Identity Management",
            "C. Azure Advanced Threat Protection (ATP)",
            "D. Azure AD Identity Protection"
        ],
        "answer": "D",
        "explanation": (
            "Azure AD Identity Protection helps detect and respond to potential identity risks, such as sign-ins from anonymous IP addresses or other suspicious activity. It can automatically enforce policies like requiring users to change their passwords when such risks are detected."
            )
    },
    {#86
        "question": (
            "To what should an application connect to retrieve security tokens?"
            ),
        "options": [
            "A. an Azure Storage account",
            "B. Azure Active Directory (Azure AD)",
            "C. a certificate store",
            "D. an Azure key vault"
        ],
        "answer": "B",
        "explanation": (
            "Applications should connect to Azure Active Directory (Azure AD) to retrieve security tokens. Azure AD is an identity and access management service that provides authentication tokens for secure access to resources and APIs."
            )
    },
    {#87
        "question": (
            "Your network contains an Active Directory forest. The forest contains 5,000 user accounts."
            "\nYour company plans to migrate all network resources to Azure and to decommission the on-premises data center."
            "\nYou need to recommend a solution to minimize the impact on users after the planned migration."
            "\nWhat should you recommend?"
            ),
        "options": [
            "A. Implement Azure Multi-Factor Authentication (MFA)",
            "B. Sync all the Active Directory user accounts to Azure Active Directory (Azure AD)",
            "C. Instruct all users to change their password",
            "D. Create a guest user account in Azure Active Directory (Azure AD) for each user"
        ],
        "answer": "B",
        "explanation": (
            "Syncing the on-premises Active Directory user accounts to Azure Active Directory ensures a seamless transition for users."
            "\nThis approach allows users to continue using their existing credentials to access Azure resources, minimizing the impact of the migration and avoiding disruptions."
            )
    },
    {#88
        "question": (
            "You have a resource group named RG1."
            "\nYou need to prevent the creation of virtual machines only in RG1. The solution must ensure that other objects can be created in RG1."
            "\nWhat should you use?"
            ),
        "options": [
            "A. a lock",
            "B. an Azure role",
            "C. a tag",
            "D. an Azure policy"
        ],
        "answer": "D",
        "explanation": (
            "An Azure Policy can be used to define and enforce rules for resources within a specific scope, such as a resource group."
            "\nTo prevent the creation of virtual machines in RG1 while allowing other resources to be created, you can assign a policy with a rule that denies virtual machine deployments in that resource group."
            )
    },
    {#89
        "question": (
            "What can Azure Information Protection encrypt?"
            ),
        "options": [
            "A. network traffic",
            "B. documents and email messages",
            "C. an Azure Storage account",
            "D. an Azure SQL database"
        ],
        "answer": "B",
        "explanation": (
            "Azure Information Protection (AIP) is a cloud-based solution that helps organizations classify, label, and protect sensitive data. AIP can encrypt documents and email messages, ensuring that only authorized users can access the content."
            )
    },
    {#90
        "question": (
            "What should you use to evaluate whether your company’s Azure environment meets regulatory requirements?"
            ),
        "options": [
            "A. the Knowledge Center website",
            "B. the Advisor blade from the Azure portal",
            "C. Compliance Manager from the Service Trust Portal",
            "D. the Solutions blade from the Azure portal"
        ],
        "answer": "C",
        "explanation": (
            "Compliance Manager is a tool available through the Microsoft Service Trust Portal that helps organizations assess and manage compliance with regulatory requirements. It provides detailed assessments, recommendations, and tracking for meeting standards like GDPR, ISO, and others."
            )
    },
    {#91
        "question": (
            "Your company has an Azure subscription that contains resources in several regions."
            "\nA company policy states that administrators must only be allowed to create additional Azure resources in a region in the country where their office is located."
            "\nYou need to create the Azure resource that must be used to meet the policy requirement."
            "\nWhat should you create?"
            ),
        "options": [
            "A. a read-only lock",
            "B. an Azure policy",
            "C. a management group",
            "D. a reservation",
        ],
        "answer": "B",
        "explanation": (
            "An Azure Policy can be used to enforce organizational standards and compliance requirements, such as restricting the creation of resources to specific regions."
            "\nIn this case, you can create a policy definition that limits resource creation to regions in the administrator's country and assign it to the appropriate scope (e.g., subscription or resource group)."
            )
    },
    {#92
        "question": (
            "This question requires that you evaluate the underlined text to determine if it is correct."
            "\n\nFrom \"Azure Cloud Shell\", you can track your company’s regulatory standards and regulations, such as ISO 27001."
            "\n\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that makes the statement correct."
            ),
        "options": [
            "A. No change is needed."
            "B. the Microsoft Cloud Partner Portal"
            "C. Compliance Manager"
            "D. the Trust Center"
        ],
        "answer": "C",
        "explanation": (
            "Compliance Manager is the correct tool for tracking your company’s regulatory standards and compliance with regulations such as ISO 27001. It provides assessments, actionable insights, and tracking for regulatory requirements."
            )
    },
    {#93
        "question": (
            "Your company plans to migrate all on-premises data to Azure."
            "\nYou need to identify whether Azure complies with the company’s regional requirements."
            "\nWhat should you use?"
            ),
        "options": [
            "A. the Knowledge Center",
            "B. Azure Marketplace",
            "C. the Azure portal",
            "D. the Trust Center"
        ],
        "answer": "D",
        "explanation": (
            "The Microsoft Trust Center provides detailed information about Azure's compliance with regional and industry-specific standards, including certifications like ISO, GDPR, and others. It is the ideal resource for evaluating whether Azure aligns with your company’s regional compliance requirements."
            )
    },
    {#94
        "question": (
            "This question requires that you evaluate the underlined text to determine if it is correct."
            "\n\nAzure Germany can be used by \"legal residents of Germany only.\""
            "\n\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that makes the statement correct."
            ),
        "options": [
            "A. no change is needed",
            "B. only enterprises that are registered in Germany",
            "C. only enterprises that purchase their azure licenses from a partner based in Germany",
            "D. any user or enterprise that requires its data to reside in Germany"
        ],
        "answer": "D",
        "explanation": (
            "Azure Germany is designed for organizations that require their data to reside in Germany, adhering to strict German data protection laws and regulations. It is not restricted to legal residents or enterprises registered in Germany; it is open to any user or enterprise with data residency requirements in Germany."
            )
    },
    {#95
        "question": (
            "What should you use to evaluate whether your company’s Azure environment meets regulatory requirements?"
            ),
        "options": [
            "A. Azure Service Health",
            "B. Azure Knowledge Center",
            "C. Azure Security Center",
            "D. Azure Advisor"
        ],
        "answer": "C",
        "explanation": (
            "Azure Security Center provides tools and insights to evaluate and improve the security posture of your Azure environment. It includes regulatory compliance assessments to help determine whether your company’s Azure resources meet specific regulatory requirements."
            
            "\n\nIncorrect Answers:"
            "\nA. Azure Service Health: Monitors the health of Azure services but does not evaluate regulatory compliance."
            "\nB. Azure Knowledge Center: Provides general FAQs and guidance but does not include compliance evaluation tools."
            "\nD. Azure Advisor: Offers best practices and recommendations for cost, performance, and security but does not specifically address regulatory requirements."
            )
    },
    {#96
        "question": (
            "Your company has an Azure subscription that contains resources in several regions."
            "\nYou need to ensure that administrators can only create resources in those regions."
            "\nWhat should you use?"
            ),
        "options": [
            "A. a read-only lock",
            "B. an Azure policy",
            "C. a management group",
            "D. a reservation"
        ],
        "answer": "B",
        "explanation": (
            "An Azure Policy can be used to enforce rules and governance across your Azure environment. To ensure that administrators can only create resources in specific regions, you can define and assign a policy that restricts resource creation to the allowed regions."
            )
    },
    {#97
        "question": (
            "Which two types of customers are eligible to use Azure Government to develop a cloud solution? Each correct answer presents a complete solution."
            ),
        "options": [
            "A. a Canadian government contractor",
            "B. a European government contractor",
            "C. a United States government entity",
            "D. a United States government contractor",
            "E. a European government entity"
        ],
        "answer": ["C","D"],
        "explanation": (
            "Azure Government is a cloud offering specifically designed for U.S. government agencies and their contractors. It meets strict compliance requirements such as FedRAMP, CJIS, and DoD standards, ensuring security and regulatory compliance for U.S. government workloads."
            )
    },
    {#98
        "question": (
            "Which statement accurately describes the Modern Lifecycle Policy for Azure services?"
            ),
        "options": [
            "A. Microsoft provides mainstream support for a service for five years.",
            "B. Microsoft provides a minimum of 12 months’ notice before ending support for a service.",
            "C. After a service is made generally available, Microsoft provides support for the service for a minimum of four years.",
            "D. When a service is retired, you can purchase extended support for the service for up to five years."
        ],
        "answer": "B",
        "explanation": (
            "The Modern Lifecycle Policy applies to Azure services and ensures that customers are notified at least 12 months in advance before a service is retired, unless there are critical security issues. This policy allows customers time to plan and transition to alternative solutions."
            )
    },
    {#99
        "question": (
            "This question requires that you evaluate the underlined text to determine if it is correct."
            "\n\nYou can use \"Advisor recommendations\" in Azure to send email alerts when the cost of the current billing period for an Azure subscription exceeds a specified limit."
            "\n\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that makes the statement correct."
            ),
        "options": [
            "A. No change is needed.",
            "B. Access control (IAM)",
            "C. Budget alerts",
            "D. Compliance"
        ],
        "answer": "C",
        "explanation": (
            "Azure Budget alerts are used to notify users when the cost of the current billing period for an Azure subscription exceeds a specified limit. This allows organizations to monitor and control their spending effectively."
            )
    },
    {#100
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYour company has an Azure subscription that contains the following unused resources:"
            "\n- 20 user accounts in Azure Active Directory (Azure AD)"
            "\n- Five groups in Azure AD"
            "\n- 10 public IP addresses"
            "\n- 10 network interfaces"
            "\nYou need to reduce the Azure costs for the company."
            "\nSolution: You remove the unused network interfaces."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": (
            "Removing unused network interfaces does not directly reduce Azure costs, as they do not incur standalone charges."
            "\nCost reductions should focus on resources like public IP addresses, which do incur charges when reserved but unused. Therefore, removing only the network interfaces does not effectively meet the goal of reducing Azure costs."
            )
    },
    {#101
        "question": (
            "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals."
            "\nSome question sets might have more than one correct solution, while others might not have a correct solution."
            "\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen."
            
            "\n\n\nYour company has an Azure subscription that contains the following unused resources:"
            "\n- 20 user accounts in Azure Active Directory (Azure AD)"
            "\n- Five groups in Azure AD"
            "\n- 10 public IP addresses"
            "\n- 10 network interfaces"
            "\nYou need to reduce the Azure costs for the company."
            "\nSolution: You remove the unused public IP addresses."
            
            "\n\nDoes this meet the goal?"
            ),
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": (
            "Removing unused public IP addresses reduces Azure costs because public IP addresses are billable resources when reserved, even if they are not associated with active resources. Eliminating these unused public IPs directly contributes to cost savings for the company."
            )
    },
    {#102
        "question": (
            "This question requires that you evaluate the underlined text to determine if it is correct."
            "\n\nA support plan solution that gives you best practice information, health status and notifications, and 24/7 access to billing information at the lowest possible cost is a \"Standard\" support plan."
            "\n\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that makes the statement correct."
            ),
        "options": [
            "A. No change is needed",
            "B. Developer",
            "C. Basic",
            "D. Premier"
        ],
        "answer": "C",
        "explanation": (
            "The Basic support plan is free and provides best practice information, health status notifications, and 24/7 access to billing information. It is designed for users who do not require technical support or a higher level of service and is available at the lowest possible cost."
            
            "\n\nIncorrect Answers:"
            "\nA. No change is needed: The Standard support plan provides additional features, including technical support for issues, which is not the lowest cost plan."
            "\nB. Developer: This plan is for non-production environments and includes technical support but comes at a cost higher than Basic."
            "\nD. Premier: This is the most comprehensive and expensive plan, offering tailored support for large enterprises."
            )
    },
    {
        "question": "This question requires that you evaluate the underlined text to determine if it is correct.\nAn Availability Zone in Azure has physically separate locations across two continents.\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed.” If the statement is incorrect, select the answer choice that\nmakes the statement correct.",
        "options": [
            "A. No change is needed.",
            "B. within a single Azure region",
            "C. within multiple Azure regions",
            "D. within a single Azure datacenter"
        ],
        "answer": "A",
        "explanation": "Azure Site Recovery helps ensure business continuity by keeping business apps and workloads running during outages. Site Recovery replicates workloads running\non physical and virtual machines (VMs) from a primary site to a secondary location."
    },
    {
        "question": "This question requires that you evaluate the underlined text to determine if it is correct. \nAzure Key Vault is used to store secrets for Azure Active Directory (Azure AD) user accounts.\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that\nmakes the statement correct.",
        "options": [
            "A. the Knowledge Center",
            "B. Azure Marketplace",
            "C. the MyApps portal",
            "D. the Trust Center"
        ],
        "answer": "D",
        "explanation": "Azure has more than 90 compliance certifications, including over 50 specific to global regions and countries, such as the US, the European Union, Germany, Japan,\nthe United Kingdom, India and China.\nYou can view a list of compliance certifications in the Trust Center to determine whether Azure meets your regional requirements."
    },
    {
        "question": "This question requires that you evaluate the underlined text to determine if it is correct. \nResource groups provide organizations with the ability to manage the compliance of Azure resources across multiple subscriptions. \nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that\nmakes the statement correct.",
        "options": [
            "A. No change is needed",
            "B. Management groups",
            "C. Azure policies",
            "D. Azure App Service plans"
        ],
        "answer": "C",
        "explanation": "Azure AD authenticates users and provides access tokens. An access token is a security token that is issued by an authorization server. It contains information\nabout the user and the app for which the token is intended, which can be used to access Web APIs and other protected resources.\nInstead of creating apps that each maintain their own username and password information, which incurs a high administrative burden when you need to add or\nremove users across multiple apps, apps can delegate that responsibility to a centralized identity provider.\nAzure Active Directory (Azure AD) is a centralized identity provider in the cloud. Delegating authentication and authorization to it enables scenarios such as\nConditional Access policies that require a user to be in a specific location, the use of multi-factor authentication, as well as enabling a user to sign in once and then\nbe automatically signed in to all of the web apps that share the same centralized directory. This capability is referred to as Single Sign On (SSO)."
    },
    {
        "question": "This question requires that you evaluate the underlined text to determine if it is correct. \nFrom Azure Monitor, you can view which user turned off a specific virtual machine during the last 14 days.\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that\nmakes the statement correct.",
        "options": [
            "A. No change is needed",
            "B. Azure Event Hubs",
            "C. Azure Activity Log",
            "D. Azure Service Health"
        ],
        "answer": "C",
        "explanation": "Compliance Manager in the Service Trust Portal is a workflow-based risk assessment tool that helps you track, assign, and verify your organization's regulatory\ncompliance activities related to Microsoft Cloud services, such as Microsoft 365, Dynamics 365, and Azure.\nReference:\nhttps://docs.microsoft.com/en-us/microsoft-365/compliance/get-started-with-service-trust-portal?view=o365-worldwide\nQUESTION 80\nThis question requires that you evaluate the underlined text to determine if it is correct. \nFrom Azure Monitor, you can view which user turned off a specific virtual machine during the last 14 days.\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that\nmakes the statement correct. \nA. No change is needed\nB. Azure Event Hubs\nC. Azure Activity Log\nD. Azure Service Health\nCorrect Answer: C\nSection: Understand Security, Privacy, Compliance and Trust\nExplanation\nExplanation/Reference:\nExplanation:\nYou would use the Azure Activity Log, not Azure Monitor to view which user turned off a specific virtual machine during the last 14 days.\nActivity logs are kept for 90 days. You can query for any range of dates, as long as the starting date isn't more than 90 days in the past.\nIn this question, we would create a filter to display shutdown operations on the virtual machine in the last 14 days."
    },
    {
        "question": "This question requires that you evaluate the underlined text to determine if it is correct.\nThe Microsoft Online Services Privacy Statement explains what data Microsoft processes, how Microsoft processes the data, and the purpose of processing the\ndata.\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed.” If the statement is incorrect, select the answer choice that\nmakes the statement correct.",
        "options": [
            "A. No change is needed.",
            "B. the Microsoft Cloud Partner Portal",
            "C. Compliance Manager",
            "D. the Trust Center"
        ],
        "answer": "C",
        "explanation": "Microsoft Compliance Manager (Preview) is a free workflow-based risk assessment tool that lets you track, assign, and verify regulatory compliance activities\nrelated to Microsoft cloud services. Azure Cloud Shell, on the other hand, is an interactive, authenticated, browser-accessible shell for managing Azure resources."
    },
    {
        "question": "This question requires that you evaluate the underlined text to determine if it is correct.\nYou can create an Azure support request from support.microsoft.com.\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed.” If the statement is incorrect, select the answer choice that\nmakes the statement correct.",
        "options": [
            "A. No change is needed.",
            "B. the Azure portal",
            "C. the Knowledge Center",
            "D. the Security & Compliance admin center"
        ],
        "answer": "B",
        "explanation": "You can open support cases in the following plans: Premier, Professional Direct, Standard, and Developer only.\nYou cannot open support cases in the Basic support plan."
    },
    {
        "question": "This question requires that you evaluate the underlined text to determine if it is correct. \nThe Azure Standard support plan is the lowest cost option to receive 24x7 access to support engineers by phone.\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that\nmakes the statement correct.",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": "No explanation provided."
    },
    {
        "question": "This question requires that you evaluate the underlined text to determine if it is correct.\nAll Azure services that are in public preview are provided without any documentation.\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that\nmakes the statement correct.",
        "options": [
            "A. No change is needed",
            "B. only configurable from Azure CLI",
            "C. excluded from the Service Level Agreements",
            "D. only configurable from the Azure portal"
        ],
        "answer": "C",
        "explanation": "The Basic support plan is free so is therefore the cheapest.  The Developer support plan is the cheapest paid-for support plan.  The order of support plans in terms\nof cost ranging from the cheapest to most expensive is: Basic, Developer, Standard, Professional Direct, Premier.\nHowever, 24/7 access to technical support by email and phone is only available for Standard, Professional Direct, Premier plans."
    },
    {
        "question": "This question requires that you evaluate the underlined text to determine if it is correct. \nAn Azure service is available to all Azure customers when it is in public preview.\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that\nmakes the statement correct.",
        "options": [
            "A. uptime",
            "B. feature availability",
            "C. bandwidth",
            "D. performance"
        ],
        "answer": "A",
        "explanation": "The SLA for virtual machines guarantees ‘uptime’. The amount of uptime guaranteed depends on factors such as whether the VMs are in an availability set or\navailability zone if there is more than one VM, the distribution of the VMs if there is more than one or the disk type if it is a single VM.\nThe SLA for Virtual Machines states:\nFor all Virtual Machines that have two or more instances deployed across two or more Availability Zones in the same Azure region, we guarantee you will have\nVirtual Machine Connectivity to at least one instance at least 99.99% of the time.\nFor all Virtual Machines that have two or more instances deployed in the same Availability Set or in the same Dedicated Host Group, we guarantee you will have\nVirtual Machine Connectivity to at least one instance at least 99.95% of the time.\nFor any Single Instance Virtual Machine using Premium SSD or Ultra Disk for all Operating System Disks and Data Disks, we guarantee you will have Virtual\nMachine Connectivity of at least 99.9%."
    },
    {
        "question": "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution. \nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen. \nYour company plans to purchase an Azure subscription.\nThe company’s support policy states that the Azure environment must provide an option to access support engineers by phone or email.  \nYou need to recommend which support plan meets the support policy requirement. \nSolution: Recommend a Basic support plan. \nDoes this meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": "Public Preview means that the service is in public beta and can be tried out by anyone with an Azure subscription. Services in public preview are often offered at a\ndiscount price.  \nPublic previews are excluded from SLAs and in some cases, no support is offered.\nIncorrect Answers:\nB: Services in private preview are available only to selected people who has signed up to the private preview program.\nC: Services in development are not available to the public.\nD: Services provided under an Enterprise Agreement (EA) subscription are available only to the subscription owner."
    },
    {
        "question": "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution. \nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen. \nYour company plans to purchase an Azure subscription. \nThe company’s support policy states that the Azure environment must provide an option to access support engineers by phone or email.  \nYou need to recommend which support plan meets the support policy requirement. \nSolution: Recommend a Standard support plan. \nDoes this meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": "The Basic support plan does not have any technical support for engineers.\nAccess to Support Engineers via email or phone is available in the following support plans: Premier, Professional Direct and standard."
    },
    {
        "question": "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution. \nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen. \nYour company plans to purchase an Azure subscription.\nThe company’s support policy states that the Azure environment must provide an option to access support engineers by phone or email.  \nYou need to recommend which support plan meets the support policy requirement. \nSolution: Recommend a Premier support plan. \nDoes this meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": "The Standard, Professional Direct, and Premier support plans have technical support for engineers via email and phone."
    },
    {
        "question": "What is required to use Azure Cost Management?",
        "options": [
            "A. a Dev/Test subscription",
            "B. Software Assurance",
            "C. an Enterprise Agreement (EA)",
            "D. a pay-as-you-go subscription"
        ],
        "answer": "A",
        "explanation": "The Premier support plan provides customer specific architectural support such as design reviews, performance tuning, configuration and implementation\nassistance delivered by Microsoft Azure technical specialists."
    },
    {
        "question": "This question requires that you evaluate the underlined text to determine if it is correct. \nYour Azure trial account expired last week. You are now unable to create additional Azure Active Directory (Azure AD) user accounts. \nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that\nmakes the statement correct.",
        "options": [
            "A. No change is needed",
            "B. start an existing Azure virtual machine",
            "C. access your data stored in Azure",
            "D. access the Azure portal"
        ],
        "answer": "B",
        "explanation": "A stopped (deallocated) VM is offline and not mounted on an Azure host server.  Starting a VM mounts the VM on a host server before the VM starts.  As soon as\nthe VM is mounted, it becomes chargeable.  For this reason, you are unable to start a VM after a trial has expired.\nIncorrect Answers:\nA: You are not charged for Azure Active Directory user accounts so you can continue to create accounts.\nC: You can access data that is already stored in Azure.\nD: You can access the Azure Portal.  You can also reactivate and upgrade the expired subscription in the portal.\nQUESTION 106\nNote: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution. \nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen. \nYour company plans to purchase an Azure subscription. \nThe company’s support policy states that the Azure environment must provide an option to access support engineers by phone or email. \nYou need to recommend which support plan meets the support policy requirement. \nSolution: Recommend a Professional Direct support plan."
    },
    {
        "question": "Your company has 10 departments.\nThe company plans to implement an Azure environment.\nYou need to ensure that each department can use a different payment option for the Azure services it consumes.\nWhat should you create for each department?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": "The Basic support plan does not have any technical support for engineers.\nThe Developer support plan has only technical support for engineers via email.\nThe Standard, Professional Direct, and Premier support plans have technical support for engineers via email and phone."
    },
    {
        "question": "Which statement accurately describes the Modern Lifecycle Policy for Azure services?",
        "options": [
            "A. Microsoft provides mainstream support for a service for five years.",
            "B. Microsoft provides a minimum of 12 months’ notice before ending support for a service.",
            "C. After a service is made generally available, Microsoft provides support for the service for a minimum of four years.",
            "D. When a service is retired, you can purchase extended support for the service for up to five years."
        ],
        "answer": "B",
        "explanation": "For products governed by the Modern Lifecycle Policy, Microsoft will provide a minimum of 12 months' notification prior to ending support if no successor product or\nservice is offered—excluding free services or preview releases."
    },
    {#ex
        "question": (
            "This question requires that you evaluate the underlined text to determine if it is correct."
            
            "\n\nAn organization that hosts its infrastructure \"in a private cloud\" can close its data center."
            
            "\n\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that makes the statement correct."
            ),
        "options": [
            "A. No change is needed.",
            "B. in a hybrid cloud",
            "C. in the public cloud",
            "D. on a Hyper-V host"
        ],
        "answer": "C",
        "explanation": (
            "A private cloud is hosted in your datacenter. Therefore, you cannot close your datacenter if you are using a private cloud."
            "\nA public cloud is hosted externally, for example, in Microsoft Azure. An organization that hosts its infrastructure in a public cloud can close its data center."
            )
    },
]