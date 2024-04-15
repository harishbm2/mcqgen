from setuptools import find_packages, setup

setup(
    name = 'mcqgenerator',
    version = '0.0.1',
    author = 'Harish Magganmane',
    author_email = 'harishbm2@yahoo.com',
    install_requires = ["openai", "langchain", "streamlit", "python-dotenv", "PyPDF1"],
    packages = find_packages()
)