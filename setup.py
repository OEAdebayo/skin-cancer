import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "DL_Benign_vs_Malignant_skin_tumour_with_keloid"
AUTHOR_USER_NAME = "OEAdebayo"
SRC_REPO = "cnnClassifier_benign_vs_malignant"
AUTHOR_EMAIL = "olusegun.adebayo@univ-fcomte.fr"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=" A python package for CNN classification of skin lesion app",
    long_description=long_description,
    long_description_content = "text/marldown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages = setuptools.find_packages(where = "src")
)
