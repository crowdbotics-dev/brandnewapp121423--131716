from setuptools import setup
from setuptools.command.build import build


class BuildCommand(build):
    def initialize_options(self):
        build.initialize_options(self)
        self.build_base = "/tmp"


setup(
    name="cb_django_paypal_integration",
    version="0.1",
    packages=["paypal_integration"],
    install_requires=["paypalrestsdk"],
    cmdclass={"build": BuildCommand},
)
