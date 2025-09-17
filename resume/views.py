from django.shortcuts import render
from django.http import HttpResponse

def cv_view(request):
    """Resume/CCV View"""
    resume_data = {
        'personal_info': {
            'name': 'Krapa Karthik',
            'phone': '+1 (646) 529-6839',
            'email': 'karthik.krapa18@gmail.com',
            'univemail': 'kk5754@nyu.edu',
            'linkedin': 'linkedin.com/in/karthik-krapa-kk18/',
            'location': 'Brooklyn, NY - 11220',
            'summary': "MS CS Graduate Student @ NYU with a keen interest in Cloud DevOps, Machine Learning, and Big Data. Experienced software engineer passionate about Cloud Computing, Machine Learning, and Generative AI.",
            'languages': ['English', 'Hindi', 'Telugu']
        },
        'education': [
            {
                'institution': 'New York University',
                'degree': 'Master of Science in Computer Science',
                'graduation_date': 'May 2026',
                'courses': 'Machine Learning, Computer Networking, Big Data, Data structures and Algorithms, Deep Learning, Opensource Software and Professional Software Development'
            },
            {
                'institution': 'SRM University',
                'degree': 'Bachelor of Technology in Computer Science and Engineering',
                'gpa': '3.8/4',
                'graduation_date': 'May 2022',
                'courses': 'Artificial Intelligence, Machine Learning, Computer Networking, Cloud Computing with IBM, Data Science, Software Engineering, and Deep Learning'
            }
        ],
        'technical_skills': {
            'programming_languages': 'Python, Java, C, JavaScript, HTML, CSS, JSON, YAML, SQL',
            'cloud_platforms': 'AWS (Solutions Architect Professional), GCP (Associate Cloud Engineer), Microsoft Azure',
            'ai_ml_frameworks': 'TensorFlow, PyTorch, Scikit-learn, LangChain, LangGraph, Machine Learning, Deep Learning, Generative AI',
            'devops_tools': 'Docker, Kubernetes, Terraform, Jenkins, Ansible, Git, CI/CD, OpenShift, Istio',
            'data_technologies': 'Apache Kafka, Apache Spark, Apache Airflow, ETL, Big Data Processing',
            'databases': 'MongoDB, PostgreSQL, Redis, Memcached, Microsoft SQL Server, Elasticsearch',
            'monitoring_observability': 'Prometheus, Grafana, Kibana, Datadog, AWS CloudWatch, Elasticsearch, Fluentd',
            'security_tools': 'Wazuh SIEM, Prowler, Vulnerability Analysis, AWS PrivateLink'
        },
        'work_experience': [
            {
                'company': 'QualtricsXM',
                'position': 'Machine Learning Engineer Intern',
                'duration': 'June 2025 - Aug 2025',
                'location': 'Seattle, WA',
                'responsibilities': [
                    'Migrated two production AI agents from legacy agent-stack to modern LangGraph platform, improving system reliability and enabling faster feature development while maintaining 100% compatibility.',
                    'Built modular tooling infrastructure and MCP (Model Context Protocol) setup for standardized agent communication, enabling reusable components across teams and reducing integration complexity by 40%.',
                    'Implemented structured response frameworks and comprehensive error handling strategies, improving system resilience and reducing debugging time while ensuring consistent API outputs for downstream services.',
                    'Onboarded production-ready agent graphs to internal Socrates LangGraph Platform, establishing scalable deployment pipelines and enabling enterprise-grade monitoring and observability for AI workflows.'
                ]
            },
            {
                'company': 'Acidaes Solutions Pvt. Ltd.',
                'position': 'Junior Software Engineer', 
                'duration': 'July 2023 - August 2024',
                'location': 'India',
                'responsibilities': [
                    'Architected AWS cloud solutions for top-tier financial institutions, ensuring 99% uptime and reducing operational disruptions by 30% through proactive issue resolution.',
                    'Developed anomaly detection with machine learning time series model using Prometheus and Grafana, cutting incident resolution time by 25% and meeting 100% of SLAs.',
                    'Deployed secure hybrid access to Amazon S3 via AWS PrivateLink, reducing data exposure by 50% and data transfer costs by 15% while improving access efficiency by 20%.',
                    'Collaborated and led cross-functional teams to ensure project alignment and client satisfaction, while mentoring new joiners to improve team onboarding and productivity.'
                ]
            },
            {
                'company': 'Acidaes Solutions Pvt. Ltd.',
                'position': 'Graduate Software Engineer',
                'duration': 'July 2022 - June 2023',
                'location': 'India',
                'responsibilities': [
                    'Developed and maintained cloud infrastructure automation scripts using Python and Terraform.',
                    'Implemented monitoring solutions using Elasticsearch, Kibana, and Grafana for real-time system health tracking.',
                    'Collaborated on microservices architecture design and deployment using Docker and Kubernetes.',
                    'Participated in code reviews and agile development processes to ensure high-quality software delivery.'
                ]
            },
        ],
        'projects': [
            {
                'title': 'Regkey Regulatory Intelligence Platform',
                'technologies': 'Machine Learning with Python, LLMs, Generative AI',
                'description': 'Implemented a regulatory intelligence platform using AWS Lambda, API Gateway, Bedrock, vector databases, and Generative AI with LLMs, enabling metadata-driven search to streamline pharmaceutical workflows and reduce task completion time by 40%.'
            },
            {
                'title': 'Metrics Anomaly Detection and Control Surface',
                'technologies': 'Machine Learning Timeseries Forecasting, Prometheus and Grafana',
                'description': 'Designed a machine learning model for anomaly detection in metrics, integrated with Grafana dashboards and alerting mechanisms, resulting in 30% faster incident response times, enhanced application performance insights, and 99.9% service uptime.'
            }
        ],
        'certifications': [
            {'name': 'Google Cloud Platform Associate Cloud Engineer(ACE)', 'year': '2022'},
            {'name': 'AWS Solutions Architect Professional(SAP)', 'year': '2024'},
            {'name': 'Elastic GenAI Associate', 'year': '2024'},
            {'name': 'Certified Kubernetes Application Developer', 'year': '2025'}
        ],
        'activities': [
            {'description': 'Research project Assistant with NYU Stern', 'year': '2024'},
            {'description': 'Show & Tell Innovative Presenter across CRMNEXT organization for Cloud innovations', 'year': '2023'},
            {'description': 'Club Core Member and Programming Language Trainer in Initiators Coding Club at SRM University', 'year': '2022'}
        ],
        'interests': [
            {'category': 'Photography', 'description': 'Passionate about capturing moments and visual storytelling'},
            {'category': 'Basketball', 'description': 'Regular player and sports enthusiast'},
            {'category': 'Technology Blogging', 'description': 'Writing about cloud technologies and AI/ML trends'},
            {'category': 'Open Source', 'description': 'Contributing to open-source projects and community learning'}
        ],
    }
    
    return render(request, 'resume/cv.html', resume_data)

def about_view(request):
    """About page view - demonstrates Django URL routing"""
    return render(request, 'resume/about.html', {
        'page_title': 'About Karthik Krapa',
        'description': 'Machine Learning Engineer | MS CS Graduate Student @ NYU with a keen interest in Cloud DevOps, Machine Learning, and Big Data'
    })
