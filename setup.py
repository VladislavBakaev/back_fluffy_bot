from setuptools import setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

reqs = parse_requirements('requirements.txt')

setup(
    name="back_fluffy_bot",
    version="1.0.0",
    description="Web server fluffy bot",
    py_modules=["start_http_app"],
    packages=["fluffy_http_app"],
    install_requires=reqs,
    scripts=['start_http_app.py']
)