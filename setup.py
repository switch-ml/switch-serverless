"""
Copyright 2022 Switchml.
Licensed under the Apache License, Version 2.0.
"""
import os
import pathlib

from setuptools import find_packages, setup

# Load version in cloudstate package.
from setuptools.command.build_py import build_py

exec(open("switchml/version.py").read())


version = __version__  # noqa
name = "switchml"

print(f"package name: {name}, version: {version}", flush=True)
proto_lib_roots = ["protobuf"]
proto_roots = ["."]


class FetchBuildProtosCommand(build_py):
    """fetch libs and install the protocol buffer generated sources."""

    def run(self):
        for proto_root in proto_roots + proto_lib_roots:
            for root, subdirs, files in os.walk(proto_root):
                for file in [f for f in files if f.endswith(".proto")]:
                    file_path = pathlib.Path(root) / file
                    destination = name
                    print(f"compiling {file_path} to {destination}")
                    command = f"protoc -I=. --python_out={destination} {file_path}"
                    print(command, "command")
                    os.system(command)

        return super().run()


packages = find_packages(exclude=[])

print(f"packages: {packages}")
setup(
    name=name,
    version=version,
    url="https://github.com/switch-ml/switch-serverless",
    license="Apache 2.0",
    description="Switchml SDK",
    packages=packages,
    long_description=open("Description.md", "r").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    install_requires=[
        "spawn @ file:///home/venkatesh/repos/devfi/dev/spawn-python-sdk",
        "numpy",
        "grpcio",
        "grpcio-tools",
    ],
    cmdclass={
        "build_py": FetchBuildProtosCommand,
    },
)
