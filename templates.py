import os

BASE_DIR = "domains"

# Ordered domain structure with priority
domain_structure = [
    ("01_core", [
        "ecommerce",
        "media",
        "social_media",
        "finance",
        "healthcare"
    ]),
    ("02_business_product", [
        "marketing",
        "advertising",
        "customer_analytics",
        "crm",
        "saas",
        "product_analytics",
        "retail",
        "sales_analytics"
    ]),
    ("03_operations", [
        "supply_chain",
        "logistics",
        "manufacturing",
        "telecom",
        "energy",
        "utilities",
        "transportation",
        "mobility"
    ]),
    ("04_advanced", [
        "fraud_detection",
        "recommendation_systems",
        "search_ranking",
        "cybersecurity",
        "adtech",
        "clickstream_analytics"
    ]),
    ("05_optional", [
        "edtech",
        "real_estate",
        "gaming",
        "insurance",
        "government"
    ])
]

# Healthcare subdomains (priority inside healthcare)
healthcare_subdomains = [
    "01_genetics",
    "02_bioinformatics",
    "03_genomics",
    "04_clinical_trials",
    "05_medical_records",
    "06_drug_discovery",
    "07_epidemiology"
]

# Dummy file templates
def create_files(path, domain_name):
    files_content = {
        "README.md": f"# {domain_name.replace('_', ' ').title()} Domain\n\nOverview of the domain.\n",
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

    for group_name, domains in domain_structure:
        group_path = os.path.join(BASE_DIR, group_name)
        os.makedirs(group_path, exist_ok=True)

        for i, domain in enumerate(domains, start=1):
            domain_folder = f"{str(i).zfill(2)}_{domain}"
            domain_path = os.path.join(group_path, domain_folder)

            os.makedirs(domain_path, exist_ok=True)
            create_files(domain_path, domain)

            # Special handling for healthcare subdomains
            if domain == "healthcare":
                for sub in healthcare_subdomains:
                    sub_path = os.path.join(domain_path, sub)
                    os.makedirs(sub_path, exist_ok=True)
                    create_files(sub_path, sub)


if __name__ == "__main__":
    create_structure()
    print("✅ Priority-based domain structure created successfully!")