import os

BASE_DIR = "domains"

# Domain structure
domains = {
    "core": [
        "ecommerce",
        "media",
        "social_media",
        "finance",
        "healthcare"
    ],
    "healthcare_subdomains": [
        "genetics",
        "bioinformatics",
        "genomics",
        "clinical_trials",
        "medical_records",
        "drug_discovery",
        "epidemiology"
    ],
    "business_product": [
        "marketing",
        "advertising",
        "customer_analytics",
        "crm",
        "saas",
        "product_analytics",
        "retail",
        "sales_analytics"
    ],
    "operations": [
        "supply_chain",
        "logistics",
        "manufacturing",
        "telecom",
        "energy",
        "utilities",
        "transportation",
        "mobility"
    ],
    "advanced": [
        "fraud_detection",
        "recommendation_systems",
        "search_ranking",
        "cybersecurity",
        "adtech",
        "clickstream_analytics"
    ],
    "optional": [
        "edtech",
        "real_estate",
        "gaming",
        "insurance",
        "government"
    ]
}

# Dummy file templates
def create_files(path, domain_name):
    files_content = {
        "README.md": f"# {domain_name.capitalize()} Domain\n\nOverview of the domain.\n",
        "business.md": "# Business Understanding\n\n- KPIs:\n- Workflows:\n- Decisions:\n",
        "data.md": "# Data Understanding\n\n- Data Sources:\n- Events:\n- Schema:\n",
        "system.md": "# Technical Implementation\n\n- Ingestion:\n- Processing:\n- Storage:\n"
    }

    for filename, content in files_content.items():
        file_path = os.path.join(path, filename)
        with open(file_path, "w") as f:
            f.write(content)


def create_structure():
    os.makedirs(BASE_DIR, exist_ok=True)

    # Core domains
    for domain in domains["core"]:
        domain_path = os.path.join(BASE_DIR, domain)
        os.makedirs(domain_path, exist_ok=True)
        create_files(domain_path, domain)

        # Healthcare subdomains
        if domain == "healthcare":
            for sub in domains["healthcare_subdomains"]:
                sub_path = os.path.join(domain_path, sub)
                os.makedirs(sub_path, exist_ok=True)
                create_files(sub_path, sub)

    # Other categories
    for category in ["business_product", "operations", "advanced", "optional"]:
        for domain in domains[category]:
            domain_path = os.path.join(BASE_DIR, domain)
            os.makedirs(domain_path, exist_ok=True)
            create_files(domain_path, domain)


if __name__ == "__main__":
    create_structure()
    print("✅ Domain structure created successfully!")