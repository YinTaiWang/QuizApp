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
    {
        "question": "A team of developers at your company plans to deploy, and then remove, 50 customized virtual machines each week. Thirty of the virtual machines run Windows\nServer 2016 and 20 of the virtual machines run Ubuntu Linux. \nYou need to recommend which Azure service will minimize the administrative effort required to deploy and remove the virtual machines. \nWhat should you recommend?",
        "options": [
            "A. Azure Reserved Virtual Machines (VM) Instances",
            "B. Azure virtual machine scale sets",
            "C. Azure DevTest Labs",
            "D. Microsoft Managed Desktop"
        ],
        "answer": "C",
        "explanation": "DevTest Labs creates labs consisting of pre-configured bases or Azure Resource Manager templates.\nBy using DevTest Labs, you can test the latest versions of your applications by doing the following tasks:\nQuickly provision Windows and Linux environments by using reusable templates and artifacts.\nEasily integrate your deployment pipeline with DevTest Labs to provision on-demand environments.\nScale up your load testing by provisioning multiple test agents and create pre-provisioned environments for training and demos.\nReference:\nhttps://docs.microsoft.com/en-us/azure/lab-services/devtest-lab-overview\nQUESTION 24\nThis question requires that you evaluate the underlined text to determine if it is correct. \nOne of the benefits of Azure SQL Data Warehouse is that high availability is built into the platform. \nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that\nmakes the statement correct. \nA. No change is needed \nB. automatic scaling"
    },
    {
        "question": "A support engineer plans to perform several Azure management tasks by using the Azure CLI. \nYou install the CLI on a computer. \nYou need to tell the support engineer which tools to use to run the CLI. \nWhich two tools should you instruct the support engineer to use? Each correct answer presents a complete solution. \nNOTE: Each correct selection is worth one point.",
        "options": [
            "A. Command Prompt",
            "B. Azure Resource Explorer",
            "C. Windows PowerShell",
            "D. Windows Defender Firewall",
            "E. Network and Sharing Center"
        ],
        "answer": "A",
        "explanation": "Azure Data Warehouse (now known as Azure Synapse Analytics) is a PaaS offering from Microsoft.  As with all PaaS services from Microsoft, SQL Data\nWarehouse offers an availability SLA of 99.9%.  Microsoft can offer 99.9% availability because it has high availability features built into the platform."
    },
    {
        "question": "You plan to store 20 TB of data in Azure. The data will be accessed infrequently and visualized by using Microsoft Power BI. \nYou need to recommend a storage solution for the data. \nWhich two solutions should you recommend? Each correct answer presents a complete solution. \nNOTE: Each correct selection is worth one point.",
        "options": [
            "A. Azure Data Lake",
            "B. Azure Cosmos DB",
            "C. Azure SQL Data Warehouse",
            "D. Azure SQL Database",
            "E. Azure Database for PostgreSQL"
        ],
        "answer": "AC",
        "explanation": "You can use Power BI to analyze and visualize data stored in Azure Data Lake and Azure SQL Data Warehouse.\nAzure Data Lake includes all of the capabilities required to make it easy for developers, data scientists and analysts to store data of any size and shape and at any\nspeed, and do all types of processing and analytics across platforms and languages. It removes the complexities of ingesting and storing all your data while making\nit faster to get up and running with batch, streaming and interactive analytics. It also integrates seamlessly with operational stores and data warehouses so that you\ncan extend current data applications."
    },
    {
        "question": "You have a virtual machine named VM1 that runs Windows Server 2016. VM1 is in the East US Azure region. \nWhich Azure service should you use from the Azure portal to view service failure notifications that can affect the availability of VM1?",
        "options": [
            "A. a physical server failure",
            "B. an Azure region failure",
            "C. a storage failure",
            "D. an Azure data center failure"
        ],
        "answer": "D",
        "explanation": "Availability zones expand the level of control you have to maintain the availability of the applications and data on your VMs. An Availability Zone is a physically\nseparate zone, within an Azure region. There are three Availability Zones per supported Azure region.\nEach Availability Zone has a distinct power source, network, and cooling. By architecting your solutions to use replicated VMs in zones, you can protect your apps\nand data from the loss of a datacenter. If one zone is compromised, then replicated apps and data are instantly available in another zone.\nReference:\nhttps://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/availability\nQUESTION 28\nYou have a virtual machine named VM1 that runs Windows Server 2016. VM1 is in the East US Azure region. \nWhich Azure service should you use from the Azure portal to view service failure notifications that can affect the availability of VM1?\nA. Azure Service Fabric \nB. Azure Monitor \nC. Azure virtual machines \nD. Azure Advisor \nCorrect Answer: C\nSection: Understand Core Azure Services\nExplanation\nExplanation/Reference:\nExplanation:\nIn the Azure virtual machines page in the Azure portal, there is a named Maintenance Status.  This column will display service issues that could affect your virtual"
    },
    {
        "question": "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution. \nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen. \nAn Azure administrator plans to run a PowerShell script that creates Azure resources. \nYou need to recommend which computer configuration to use to run the script. \nSolution: Run the script from a computer that runs Linux and has the Azure CLI tools installed. \nDoes this meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": "A PowerShell script is a file that contains PowerShell cmdlets and code. A PowerShell script needs to be run in PowerShell.\nPowerShell can now be installed on Linux. However, the question states that the computer has Azure CLI tools, not PowerShell installed.  Therefore, this solution\ndoes not meet the goal."
    },
    {
        "question": "You have an Azure environment that contains 10 virtual networks and 100 virtual machines. \nYou need to limit the amount of inbound traffic to all the Azure virtual networks. \nWhat should you create?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": "A PowerShell script is a file that contains PowerShell cmdlets and code. A PowerShell script needs to be run in PowerShell.  \nIn this question, the computer has PowerShell Core 6.0 installed. Therefore, this solution does meet the goal.\nNote: To create Azure resources using PowerShell, you would need to import the Azure PowerShell module which includes the PowerShell cmdlets required to\ncreate the resources."
    },
    {
        "question": "You have an Azure environment that contains multiple Azure virtual machines.\nYou plan to implement a solution that enables the client computers on your on-premises network to communicate to the Azure virtual machines.\nYou need to recommend which Azure resources must be created for the planned solution.\nWhich two Azure resources should you include in the recommendation? Each correct answer presents part of the solution.\nNOTE: Each correct selection is worth one point.",
        "options": [
            "A. a virtual network gateway",
            "B. a load balancer",
            "C. an application gateway",
            "D. a virtual network",
            "E. a gateway subnet"
        ],
        "answer": "D",
        "explanation": "You can restrict traffic to multiple virtual networks with a single Azure firewall.\nAzure Firewall is a managed, cloud-based network security service that protects your Azure Virtual Network resources. It's a fully stateful firewall as a service with\nbuilt-in high availability and unrestricted cloud scalability.\nYou can centrally create, enforce, and log application and network connectivity policies across subscriptions and virtual networks. Azure Firewall uses a static public\nIP address for your virtual network resources allowing outside firewalls to identify traffic originating from your virtual network."
    },
    {
        "question": "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution. \nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen. \nYou have an Azure environment. You need to create a new Azure virtual machine from a tablet that runs the Android operating system. \nSolution: You use Bash in Azure Cloud Shell.\nDoes this meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": "With Azure Cloud Shell, you can create virtual machines using Bash or PowerShell.\nAzure Cloud Shell is an interactive, authenticated, browser-accessible shell for managing Azure resources. It provides the flexibility of choosing the shell experience\nthat best suits the way you work, either Bash or PowerShell.\nReference:\nhttps://docs.microsoft.com/en-us/azure/cloud-shell/quickstart\nhttps://docs.microsoft.com/en-us/azure/cloud-shell/overview"
    },
    {
        "question": "Your company plans to move several servers to Azure.\nThe company’s compliance policy states that a server named FinServer must be on a separate network segment.\nYou are evaluating which Azure services can be used to meet the compliance policy requirements.\nWhich Azure solution should you recommend?",
        "options": [
            "A. a resource group for FinServer and another resource group for all the other servers",
            "B. a virtual network for FinServer and another virtual network for all the other servers",
            "C. a VPN for FinServer and a virtual network gateway for each other server",
            "D. one resource group for all the servers and a resource lock for FinServer"
        ],
        "answer": "B",
        "explanation": "Networks in Azure are known as virtual networks.  A virtual network can have multiple IP address spaces and multiple subnets.  Azure automatically routes traffic\nbetween different subnets within a virtual network.\nThe question states that FinServer must be on a separate network segment.  The only way to separate FinServer from the other servers in networking terms is to\nplace the server in a different virtual network to the other servers."
    },
    {
        "question": "Your company plans to migrate all its network resources to Azure.\nYou need to start the planning process by exploring Azure.\nWhat should you create first?",
        "options": [
            "A. a subscription",
            "B. a resource group",
            "C. a virtual network",
            "D. a management group"
        ],
        "answer": "C",
        "explanation": "Azure Files is Microsoft's easy-to-use cloud file system. Azure file shares can be seamlessly used in Windows and Windows Server.\nTo use an Azure file share with Windows, you must either mount it, which means assigning it a drive letter or mount point path, or access it via its UNC path.\nUnlike other SMB shares you may have interacted with, such as those hosted on a Windows Server, Linux Samba server, or NAS device, Azure file shares do not\ncurrently support Kerberos authentication with your Active Directory (AD) or Azure Active Directory (AAD) identity, although this is a feature we are working on.\nInstead, you must access your Azure file share with the storage account key for the storage account containing your Azure file share. A storage account key is an\nadministrator key for a storage account, including administrator permissions to all files and folders within the file share you're accessing, and for all file shares and\nother storage resources (blobs, queues, tables, etc) contained within your storage account."
    },
    {
        "question": "You have an on-premises application that sends email notifications automatically based on a rule.\nYou plan to migrate the application to Azure.\nYou need to recommend a serverless computing solution for the application.\nWhat should you include in the recommendation?",
        "options": [
            "A. a web app",
            "B. a server image in Azure Marketplace",
            "C. a logic app",
            "D. an API app"
        ],
        "answer": "C",
        "explanation": "Azure Logic Apps is a cloud service that helps you schedule, automate, and orchestrate tasks, business processes, and workflows when you need to integrate\napps, data, systems, and services across enterprises or organizations. Logic Apps simplifies how you design and build scalable solutions for app integration, data\nintegration, system integration, enterprise application integration (EAI), and business-to-business (B2B) communication, whether in the cloud, on premises, or both.\nFor example, here are just a few workloads you can automate with logic apps:\nProcess and route orders across on-premises systems and cloud services.\nSend email notifications with Office 365 when events happen in various systems, apps, and services.\nMove uploaded files from an SFTP or FTP server to Azure Storage.\nMonitor tweets for a specific subject, analyze the sentiment, and create alerts or tasks for items that need review."
    },
    {
        "question": "You plan to deploy a website to Azure. The website will be accessed by users worldwide and will host large video files.\nYou need to recommend which Azure feature must be used to provide the best video playback experience.\nWhat should you recommend?",
        "options": [
            "A. an application gateway",
            "B. an Azure ExpressRoute circuit",
            "C. a content delivery network (CDN)",
            "D. an Azure Traffic Manager profile"
        ],
        "answer": "C",
        "explanation": "The question states that users are located worldwide and will be downloading large video files.  The video playback experience would be improved if they can\ndownload the video from servers in the same region as the users.  We can achieve this by using a content deliver network.\nA content delivery network (CDN) is a distributed network of servers that can efficiently deliver web content to users. CDNs store cached content on edge servers in\npoint-of-presence (POP) locations that are close to end users, to minimize latency.\nAzure Content Delivery Network (CDN) offers developers a global solution for rapidly delivering high-bandwidth content to users by caching their content at\nstrategically placed physical nodes across the world. Azure CDN can also accelerate dynamic content, which cannot be cached, by leveraging various network\noptimizations using CDN POPs. For example, route optimization to bypass Border Gateway Protocol (BGP).\nThe benefits of using Azure CDN to deliver web site assets include:\nBetter performance and improved user experience for end users, especially when using applications in which multiple round-trips are required to load content.\nLarge scaling to better handle instantaneous high loads, such as the start of a product launch event.\nDistribution of user requests and serving of content directly from edge servers so that less traffic is sent to the origin server."
    },
    {
        "question": "This question requires that you evaluate the underlined text to determine if it is correct.\nYou have an application that is comprised of an Azure web app that has a Service Level Agreement (SLA) of 99.95 percent and an Azure SQL database that has an\nSLA of 99.99 percent.\nThe composite SLA for the application is the product of both SLAs, which equals 99.94 percent.\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that\nmakes the statement correct.",
        "options": [
            "A. Azure CLI",
            "B. the Azure portal",
            "C. Azure Cloud Shell",
            "D. Windows PowerShell",
            "E. Azure Storage Explorer"
        ],
        "answer": "BC",
        "explanation": "The Azure portal is the web-based portal for managing Azure.  Being web-based, you can use the Azure portal on an iPhone.\nAzure Cloud Shell is a web-based command line for managing Azure. You access the Azure Cloud Shell from the Azure portal. Being web-based, you can use the\nAzure Cloud Shell on an iPhone.\nIncorrect Answers:\nA: Azure CLI can be installed on MacOS but it cannot be installed on an iPhone.\nD: Windows PowerShell can be installed on MacOS but it cannot be installed on an iPhone.\nE: Azure Storage Explorer is not used to manage Azure web apps."
    },
    {
        "question": "Your company plans to deploy an Artificial Intelligence (AI) solution in Azure. \nWhat should the company use to build, test, and deploy predictive analytics solutions?",
        "options": [
            "A. Azure Logic Apps",
            "B. Azure Machine Learning Studio",
            "C. Azure Batch",
            "D. Azure Cosmos DB"
        ],
        "answer": "A",
        "explanation": "Composite SLAs involve multiple services supporting an application, each with differing levels of availability. For example, consider an App Service web app that\nwrites to Azure SQL Database. At the time of this writing, these Azure services have the following SLAs:\nApp Service web apps = 99.95%\nSQL Database = 99.99%\nWhat is the maximum downtime you would expect for this application? If either service fails, the whole application fails. The probability of each service failing is\nindependent, so the composite SLA for this application is 99.95% × 99.99% = 99.94%. That's lower than the individual SLAs, which isn't surprising because an\napplication that relies on multiple services has more potential failure points."
    },
    {
        "question": "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution. \nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen. \nYou have an Azure subscription named Subscription1. You sign in to the Azure portal and create a resource group named RG1.\nFrom Azure documentation, you have the following command that creates a virtual machine named VM1.\naz vm create --resource-group RG1 --name VM1 --image UbuntuLTS --generate-ssh-keys\nYou need to create VM1 in Subscription1 by using the command.\nSolution: From the Azure portal, launch Azure Cloud Shell and select PowerShell. Run the command in Cloud Shell.\nDoes this meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": "The command can be run in the Azure Cloud Shell. Although this question says you select PowerShell rather than Bash, the Az commands will work in PowerShell.\n \nThe Azure Cloud Shell is a free interactive shell. It has common Azure tools preinstalled and configured to use with your account.\nTo open the Cloud Shell, just select Try it from the upper right corner of a code block. You can also launch Cloud Shell in a separate browser tab by going to https://\nshell.azure.com/bash.\nReference:"
    },
    {
        "question": "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution. \nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen. \nYou have an Azure subscription named Subscription1. You sign in to the Azure portal and create a resource group named RG1.\nFrom Azure documentation, you have the following command that creates a virtual machine named VM1.\naz vm create --resource-group RG1 --name VM1 --image UbuntuLTS \n--generate-ssh-keys\nYou need to create VM1 in Subscription1 by using the command.\nSolution: From a computer that runs Windows 10, install Azure CLI. From PowerShell, sign in to Azure and then run the command.\nDoes this meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": "The command can be run from PowerShell or the command prompt if you have the Azure CLI installed. However, it must be run on the Windows 10 computer, not\nin Azure."
    },
    {
        "question": "Which service provides serverless computing in Azure?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": "A PowerShell script is a file that contains PowerShell cmdlets and code. A PowerShell script needs to be run in PowerShell.\nIn this question, the computer has the Azure PowerShell module installed. Therefore, this solution does meet the goal."
    },
    {
        "question": "Which Azure service should you use to collect events from multiple resources into a centralized repository?",
        "options": [
            "A. Azure Resource Manager templates",
            "B. virtual machine scale sets",
            "C. the Azure API Management service",
            "D. management groups"
        ],
        "answer": "A",
        "explanation": "You can use Azure Resource Manager templates to automate the creation of the Azure resources.  Deploying resource through templates is known as\n‘Infrastructure as code’.\nTo implement infrastructure as code for your Azure solutions, use Azure Resource Manager templates. The template is a JavaScript Object Notation (JSON) file\nthat defines the infrastructure and configuration for your project. The template uses declarative syntax, which lets you state what you intend to deploy without having\nto write the sequence of programming commands to create it. In the template, you specify the resources to deploy and the properties for those resources."
    },
    {
        "question": "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution. \nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen. \nYou have an Azure environment. You need to create a new Azure virtual machine from a tablet that runs the Android operating system. \nSolution: You use PowerShell in Azure Cloud Shell. \nDoes this meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": "Azure Cloud Shell is a browser-based shell experience to manage and develop Azure resources.\nCloud Shell offers a browser-accessible, pre-configured shell experience for managing Azure resources without the overhead of installing, versioning, and\nmaintaining a machine yourself.\nBeing browser-based, Azure Cloud Shell can be run on a browser from a tablet that runs the Android operating system."
    },
    {
        "question": "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution. \nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen. \nYou have an Azure environment. You need to create a new Azure virtual machine from a tablet that runs the Android operating system. \nSolution: You use the Azure portal. \nDoes this meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": "PowerApps lets you quickly build business applications with little or no code.  It is not used to create Azure virtual machines. Therefore, this solution does not meet\nthe goal.\nPowerApps Portals allow organizations to create websites which can be shared with users external to their organization either anonymously or through the login\nprovider of their choice like LinkedIn, Microsoft Account, other commercial login providers."
    },
    {
        "question": "This question requires that you evaluate the underlined text to determine if it is correct.\nAzure Databricks is an Apache Spark-based analytics service.\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed.” If the statement is incorrect, select the answer choice that\nmakes the statement correct.",
        "options": [
            "A. No change is needed.",
            "B. Azure Data Factory",
            "C. Azure DevOps",
            "D. Azure HDInsight"
        ],
        "answer": "A",
        "explanation": "The Azure portal is a web-based, unified console that provides an alternative to command-line tools. With the Azure portal, you can manage your Azure subscription\nusing a graphical user interface. You can build, manage, and monitor everything from simple web apps to complex cloud deployments. Create custom dashboards\nfor an organized view of resources. Configure accessibility options for an optimal experience.\nBeing web-based, the Azure portal can be run on a browser from a tablet that runs the Android operating system."
    },
    {
        "question": "Which Azure service provides a set of version control tools to manage code?",
        "options": [
            "A. Azure Repos",
            "B. Azure DevTest Labs",
            "C. Azure Storage",
            "D. Azure Cosmos DB"
        ],
        "answer": "A",
        "explanation": "Azure Repos is a set of version control tools that you can use to manage your code.\nIncorrect Answers:\nB: Azure DevTest Labs creates labs consisting of pre-configured bases or Azure Resource Manager templates. These have all the necessary tools and software\nthat you can use to create environments.\nD: Azure Cosmos DB is Microsoft's globally distributed, multi-model database service."
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
        "question": "Your company plans to automate the deployment of servers to Azure. \nYour manager is concerned that you may expose administrative credentials during the deployment. \nYou need to recommend an Azure solution that encrypts the administrative credentials during the deployment. \nWhat should you include in the recommendation?",
        "options": [
            "A. Azure Key Vault",
            "B. Azure Information Protection",
            "C. Azure Security Center",
            "D. Azure Multi-Factor Authentication (MFA)"
        ],
        "answer": "A",
        "explanation": "Centralizing storage of application secrets in Azure Key Vault allows you to control their distribution. Key Vault greatly reduces the chances that secrets may be\naccidentally leaked. When using Key Vault, application developers no longer need to store security information in their application. Not having to store security\ninformation in applications eliminates the need to make this information part of the code. For example, an application may need to connect to a database. Instead of\nstoring the connection string in the app's code, you can store it securely in Key Vault."
    },
    {
        "question": "You plan to deploy several Azure virtual machines.\nYou need to control the ports that devices on the Internet can use to access the virtual machines.\nWhat should you use?",
        "options": [
            "A. a network security group (NSG)",
            "B. an Azure Active Directory (Azure AD) role",
            "C. an Azure Active Directory group",
            "D. an Azure key vault"
        ],
        "answer": "A",
        "explanation": "A network security group works like a firewall.  You can attach a network security group to a virtual network and/or individual subnets within the virtual network.  You\ncan also attach a network security group to a network interface assigned to a virtual machine.  You can use multiple network security groups within a virtual network\nto restrict traffic between resources such as virtual machines and subnets.\nYou can filter network traffic to and from Azure resources in an Azure virtual network with a network security group. A network security group contains security rules\nthat allow or deny inbound network traffic to, or outbound network traffic from, several types of Azure resources."
    },
    {
        "question": "This question requires that you evaluate the underlined text to determine if it is correct. \nAfter you create a virtual machine, you need to modify the network security group (NSG) to allow connections to TCP port 8080 on the virtual machine.\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that\nmakes the statement correct.",
        "options": [
            "A. no change is needed",
            "B. only enterprises that are registered in Germany",
            "C. only enterprises that purchase their azure licenses from a partner based in Germany",
            "D. any user or enterprise that requires its data to reside in Germany"
        ],
        "answer": "D",
        "explanation": "Azure Germany is available to eligible customers and partners globally who intend to do business in the EU/EFTA, including the United Kingdom.\nAzure Germany offers a separate instance of Microsoft Azure services from within German datacenters. The datacenters are in two locations, Frankfurt/Main and\nMagdeburg. This placement ensures that customer data remains in Germany and that the datacenters connect to each other through a private network. All\ncustomer data is exclusively stored in those datacenters. A designated German company--the German data trustee--controls access to customer data and the\nsystems and infrastructure that hold customer data."
    },
    {
        "question": "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution. \nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen. \nYour Azure environment contains multiple Azure virtual machines. \nYou need to ensure that a virtual machine named VM1 is accessible from the Internet over HTTP.\nSolution: You modify a network security group (NSG).\nDoes this meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": "When you create a virtual machine, the default setting is to create a Network Security Group attached to the network interface assigned to a virtual machine.\nA network security group works like a firewall.  You can attach a network security group to a virtual network and/or individual subnets within the virtual network.  You\ncan also attach a network security group to a network interface assigned to a virtual machine.  You can use multiple network security groups within a virtual network\nto restrict traffic between resources such as virtual machines and subnets.\nYou can filter network traffic to and from Azure resources in an Azure virtual network with a network security group. A network security group contains security rules\nthat allow or deny inbound network traffic to, or outbound network traffic from, several types of Azure resources.\nIn this question, we need to add a rule to the network security group to allow the connection to the virtual machine on port 8080."
    },
    {
        "question": "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution. \nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen. \nYour Azure environment contains multiple Azure virtual machines. \nYou need to ensure that a virtual machine named VM1 is accessible from the Internet over HTTP.\nSolution: You modify a DDoS protection plan. \nDoes this meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": "A network security group works like a firewall.  You can attach a network security group to a virtual network and/or individual subnets within the virtual network.  You\ncan also attach a network security group to a network interface assigned to a virtual machine.  You can use multiple network security groups within a virtual network\nto restrict traffic between resources such as virtual machines and subnets.\nYou can filter network traffic to and from Azure resources in an Azure virtual network with a network security group. A network security group contains security rules\nthat allow or deny inbound network traffic to, or outbound network traffic from, several types of Azure resources.\nIn this question, we need to add a rule to the network security group to allow the connection to the virtual machine on port 80 (HTTP)."
    },
    {
        "question": "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution. \nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen. \nYour Azure environment contains multiple Azure virtual machines. \nYou need to ensure that a virtual machine named VM1 is accessible from the Internet over HTTP.\nSolution: You modify an Azure firewall. \nDoes this meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": "Azure Firewall is a managed, cloud-based network security service that protects your Azure Virtual Network resources. It's a fully stateful firewall as a service with\nbuilt-in high availability and unrestricted cloud scalability.\nIn this question, we need to add a rule to Azure Firewall to allow the connection to the virtual machine on port 80 (HTTP)."
    },
    {
        "question": "Which two types of customers are eligible to use Azure Government to develop a cloud solution? Each correct answer presents a complete solution.\nNOTE: Each correct selection is worth one point.",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": "Azure Traffic Manager is a DNS-based load balancing solution.  It is not used to ensure that a virtual machine named VM1 is accessible from the Internet over\nHTTP.\nTo ensure that a virtual machine named VM1 is accessible from the Internet over HTTP, you need to modify a network security group or Azure Firewall.\nIn this question, we need to add a rule to a network security group or Azure Firewall to allow the connection to the virtual machine on port 80 (HTTP)."
    },
    {
        "question": "You need to ensure that when Azure Active Directory (Azure AD) users connect to Azure AD from the Internet by using an anonymous IP address, the users are\nprompted automatically to change their password. \nWhich Azure service should you use?",
        "options": [
            "A. Azure AD Connect Health",
            "B. Azure AD Privileged Identity Management",
            "C. Azure Advanced Threat Protection (ATP)",
            "D. Azure AD Identity Protection"
        ],
        "answer": "D",
        "explanation": "Azure Government is a cloud environment specifically built to meet compliance and security requirements for US government. This mission-critical cloud delivers\nbreakthrough innovation to U.S. government customers and their partners. Azure Government applies to government at any level — from state and local\ngovernments to federal agencies including Department of Defense agencies.\nThe key difference between Microsoft Azure and Microsoft Azure Government is that Azure Government is a sovereign cloud. It's a physically separated instance of\nAzure, dedicated to U.S. government workloads only. It's built exclusively for government agencies and their solution providers."
    },
    {
        "question": "Your company plans to deploy several web servers and several database servers to Azure. \nYou need to recommend an Azure solution to limit the types of connections from the web servers to the database servers. \nWhat should you include in the recommendation?",
        "options": [
            "A. network security groups (NSGs)",
            "B. Azure Service Bus",
            "C. a local network gateway",
            "D. a route filter"
        ],
        "answer": "A",
        "explanation": "A network security group works like a firewall.  You can attach a network security group to a virtual network and/or individual subnets within the virtual network.  You\ncan also attach a network security group to a network interface assigned to a virtual machine.  You can use multiple network security groups within a virtual network\nto restrict traffic between resources such as virtual machines and subnets.\nYou can filter network traffic to and from Azure resources in an Azure virtual network with a network security group. A network security group contains security rules\nthat allow or deny inbound network traffic to, or outbound network traffic from, several types of Azure resources."
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
        "question": "Your network contains an Active Directory forest. The forest contains 5,000 user accounts. \nYour company plans to migrate all network resources to Azure and to decommission the on-premises data center. \nYou need to recommend a solution to minimize the impact on users after the planned migration. \n  What should you recommend?",
        "options": [
            "A. Implement Azure Multi-Factor Authentication (MFA)",
            "B. Sync all the Active Directory user accounts to Azure Active Directory (Azure AD)",
            "C. Instruct all users to change their password",
            "D. Create a guest user account in Azure Active Directory (Azure AD) for each user"
        ],
        "answer": "B",
        "explanation": "To migrate to Azure and decommission the on-premises data center, you would need to create the 5,000 user accounts in Azure Active Directory.  The easy way to\ndo this is to sync all the Active Directory user accounts to Azure Active Directory (Azure AD).  You can even sync their passwords to further minimize the impact on\nusers.\nThe tool you would use to sync the accounts is Azure AD Connect. The Azure Active Directory Connect synchronization services (Azure AD Connect sync) is a\nmain component of Azure AD Connect. It takes care of all the operations that are related to synchronize identity data between your on-premises environment and\nAzure AD."
    },
    {
        "question": "Which service provides network traffic filtering across multiple Azure subscriptions and virtual networks?",
        "options": [
            "A. Azure Firewall",
            "B. an application security group",
            "C. Azure DDoS protection",
            "D. a network security group (NSG)"
        ],
        "answer": "A",
        "explanation": "You can restrict traffic to multiple virtual networks in multiple subscriptions with a single Azure firewall.\nAzure Firewall is a managed, cloud-based network security service that protects your Azure Virtual Network resources. It's a fully stateful firewall as a service with\nbuilt-in high availability and unrestricted cloud scalability.\nYou can centrally create, enforce, and log application and network connectivity policies across subscriptions and virtual networks. Azure Firewall uses a static public\nIP address for your virtual network resources allowing outside firewalls to identify traffic originating from your virtual network."
    },
    {
        "question": "You have a resource group named RG1.\nYou plan to create virtual networks and app services in RG1.\nYou need to prevent the creation of virtual machines only in RG1.\nWhat should you use?",
        "options": [
            "A. a lock",
            "B. an Azure role",
            "C. a tag",
            "D. an Azure policy"
        ],
        "answer": "D",
        "explanation": "Azure Key Vault is a secure store for storage various types of sensitive information including passwords and certificates.\nAzure Key Vault can be used to Securely store and tightly control access to tokens, passwords, certificates, API keys, and other secrets.\nSecrets and keys are safeguarded by Azure, using industry-standard algorithms, key lengths, and hardware security modules (HSMs). The HSMs used are Federal\nInformation Processing Standards (FIPS) 140-2 Level 2 validated.\nAccess to a key vault requires proper authentication and authorization before a caller (user or application) can get access. Authentication establishes the identity of\nthe caller, while authorization determines the operations that they are allowed to perform."
    },
    {
        "question": "What can Azure Information Protection encrypt?",
        "options": [
            "A. network traffic",
            "B. documents and email messages",
            "C. an Azure Storage account",
            "D. an Azure SQL database"
        ],
        "answer": "B",
        "explanation": "Azure Information Protection can encrypt documents and emails.\nAzure Information Protection is a cloud-based solution that helps an organization to classify and optionally, protect its documents and emails by applying labels.\nLabels can be applied automatically by administrators who define rules and conditions, manually by users, or a combination where users are given\nrecommendations.\nThe protection technology uses Azure Rights Management (often abbreviated to Azure RMS). This technology is integrated with other Microsoft cloud services and\napplications, such as Office 365 and Azure Active Directory. \nThis protection technology uses encryption, identity, and authorization policies. Similarly to the labels that are applied, protection that is applied by using Rights\nManagement stays with the documents and emails, independently of the location—inside or outside your organization, networks, file servers, and applications."
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
        "question": "Your company has an Azure subscription that contains resources in several regions. \nA company policy states that administrators must only be allowed to create additional Azure resources in a region in the country where their office is located. \nYou need to create the Azure resource that must be used to meet the policy requirement. \nWhat should you create?",
        "options": [
            "A. a read-only lock",
            "B. an Azure policy",
            "C. a management group",
            "D. a reservation"
        ],
        "answer": "B",
        "explanation": "Azure policies can be used to define requirements for resource properties during deployment and for already existing resources. Azure Policy controls properties\nsuch as the types or locations of resources.\nAzure Policy is a service in Azure that you use to create, assign, and manage policies. These policies enforce different rules and effects over your resources, so\nthose resources stay compliant with your corporate standards and service level agreements. Azure Policy meets this need by evaluating your resources for non-\ncompliance with assigned policies. All data stored by Azure Policy is encrypted at rest.\nAzure Policy offers several built-in policies that are available by default. In this question, we would use the ‘Allowed Locations’ policy to define the locations where\nresources can be deployed."
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
        "question": "You need to configure an Azure solution that meets the following requirements: \nSecures websites from attacks \nGenerates reports that contain details of attempted attacks \nWhat should you include in the solution?",
        "options": [
            "A. Azure Firewall",
            "B. a network security group (NSG)",
            "C. Azure Information Protection",
            "D. DDoS protection"
        ],
        "answer": "D",
        "explanation": "The Microsoft Privacy Statement explains what personal data Microsoft processes, how Microsoft processes the data, and the purpose of processing the data"
    },
    {
        "question": "Your company has 10 offices. You plan to generate several billing reports from the Azure portal. Each report will contain the Azure resource utilization of each\noffice. \nWhich Azure Resource Manager feature should you use before you generate the reports?",
        "options": [
            "A. Create a service health alert",
            "B. Upgrade your support plan",
            "C. Modify an Azure policy",
            "D. Create a new support request"
        ],
        "answer": "D",
        "explanation": "Many Azure resource have quote limits.  The purpose of the quota limits is to help you control your Azure costs.  However, it is common to require an increase to\nthe default quota.\nYou can request a quota limit increase by opening a support request.  In the support request, select ‘Service and subscription limits (quotas)’ for the Issue type,\nselect your subscription and the service you want to increase the quota for.  For this question, you would select ‘SQL Database Managed Instance’ as the quote\ntype."
    },
    {
        "question": "Your company plans to migrate to Azure. The company has several departments. All the Azure resources used by each department will be managed by a\ndepartment administrator. \nWhat are two possible techniques to segment Azure for the departments? Each correct answer presents a complete solution.\nNOTE: Each correct selection is worth one point.",
        "options": [
            "A. multiple subscriptions",
            "B. multiple Azure Active Directory (Azure AD) directories",
            "C. multiple regions",
            "D. multiple resource groups"
        ],
        "answer": "AD",
        "explanation": "You can use resource tags to ‘label’ Azure resources.  Tags are metadata elements attached to resources. Tags consist of pairs of key/value strings.  In this\nquestion, we would tag each resource with a tag to identify each office.  For example: Location = Office1.  When all Azure resources are tagged, you can generate\nreports to list all resources based on the value of the tag.  For example: All resources used by Office1."
    },
    {
        "question": "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.\nYour company has an Azure subscription that contains the following unused resources:\n20 user accounts in Azure Active Directory (Azure AD)\nFive groups in Azure AD\n10 public IP addresses\n10 network interfaces\nYou need to reduce the Azure costs for the company.\nSolution: You remove the unused public IP addresses.\nDoes this meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": "You are not charged for unused network interfaces. Therefore, deleting unused network interfaces will not reduce the Azure costs for the company."
    },
    {
        "question": "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.\nYour company has an Azure subscription that contains the following unused resources:\n20 user accounts in Azure Active Directory (Azure AD)\nFive groups in Azure AD\n10 public IP addresses\n10 network interfaces\nYou need to reduce the Azure costs for the company.\nSolution: You remove the unused user accounts.\nDoes this meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "B",
        "explanation": "You are charged for public IP addresses.  Therefore, deleting unused public IP addresses will reduce the Azure costs."
    },
    {
        "question": "This question requires that you evaluate the underlined text to determine if it is correct. \nA support plan solution that gives you best practice information, health status and notifications, and 24/7 access to billing information at the lowest possible cost is\na Standard support plan.\nInstructions: Review the underlined text. If it makes the statement correct, select “No change is needed”. If the statement is incorrect, select the answer choice that\nmakes the statement correct.",
        "options": [
            "A. No change is needed",
            "B. Developer",
            "C. Basic",
            "D. Premier"
        ],
        "answer": "C",
        "explanation": "A basic support plan provides:\n24x7 access to billing and subscription support, online self-help, documentation, whitepapers, and support forums\nBest practices: Access to full set of Azure Advisor recommendations\nHealth Status and Notifications: Access to personalized Service Health Dashboard & Health API"
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
    {
        "question": "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.\nYou plan to deploy several Azure virtual machines.\nYou need to ensure that the services running on the virtual machines are available if a single data center fails.\nSolution: You deploy the virtual machines to two or more availability zones.\nDoes this meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": "Availability zones expand the level of control you have to maintain the availability of the applications and data on your VMs. An Availability Zone is a physically\nseparate zone, within an Azure region. There are three Availability Zones per supported Azure region.\nEach Availability Zone has a distinct power source, network, and cooling. By architecting your solutions to use replicated VMs in zones, you can protect your apps\nand data from the loss of a datacenter. If one zone is compromised, then replicated apps and data are instantly available in another zone.\nReference:\nhttps://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/availability"
    },
    {
        "question": "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might\nmeet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.\nAfter you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.\nYou plan to deploy several Azure virtual machines.\nYou need to ensure that the services running on the virtual machines are available if a single data center fails.\nSolution: You deploy the virtual machines to two or more regions.\nDoes this meet the goal?",
        "options": [
            "A. Yes",
            "B. No"
        ],
        "answer": "A",
        "explanation": "By deploying the virtual machines to two or more regions, you are deploying the virtual machines to multiple datacenters.  This will ensure that the services running\non the virtual machines are available if a single data center fails.\nAzure operates in multiple datacenters around the world. These datacenters are grouped in to geographic regions, giving you flexibility in choosing where to build\nyour applications.\nYou create Azure resources in defined geographic regions like 'West US', 'North Europe', or 'Southeast Asia'. You can review the list of regions and their locations.\nWithin each region, multiple datacenters exist to provide for redundancy and availability.\nReference:\nhttps://docs.microsoft.com/en-us/azure/virtual-machines/windows/regions"
    },
    {
        "question": "A team of developers at your company plans to deploy, and then remove, 50 virtual machines each week. All the virtual machines are configured by using Azure\nResource Manager templates.\nYou need to recommend which Azure service will minimize the administrative effort required to deploy and remove the virtual machines. \nWhat should you recommend?",
        "options": [
            "A. Azure Reserved Virtual Machine (VM) Instances",
            "B. Azure DevTest Labs",
            "C. Azure virtual machine scale sets",
            "D. Microsoft Managed Desktop"
        ],
        "answer": "B",
        "explanation": "An Azure virtual machine is an example of Infrastructure as a Service (IaaS).\nAzure web app, Azure logic app and Azure SQL database are all examples of Platform as a Service (Paas)."
    },
]