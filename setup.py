from setuptools import setup, find_packages

setup(
    name="jaime_project",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pyjwt==2.8.0",
        "fastapi==0.110.3"
        "python-dotenv==1.0.0",
        "python-multipart==0.0.9",
        "passlib===1.7.4",
        "bcrypt==3.2.2"
    ],
)
