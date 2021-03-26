# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# type: ignore
# isort: skip_file
from setuptools import find_namespace_packages, setup

import sys
from os.path import abspath, dirname, join

helpers = join(dirname(dirname(dirname(abspath(__file__)))))
sys.path.append(helpers)
from build_helpers.build_helpers import find_version  # noqa E402

with open("README.md", "r") as fh:
    LONG_DESC = fh.read()
    setup(
        name="hydra-ax-sweeper",
        version=find_version(
            dirname(__file__), "hydra_plugins/hydra_ax_sweeper/__init__.py"
        ),
        author="Omry Yadan, Shagun Sodhani",
        author_email="omry@fb.com, sshagunsodhani@gmail.com",
        description="Hydra Ax Sweeper plugin",
        long_description=LONG_DESC,
        long_description_content_type="text/markdown",
        url="https://github.com/facebookresearch/hydra/",
        packages=find_namespace_packages(include=["hydra_plugins.*"]),
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Operating System :: POSIX :: Linux",
            "Operating System :: MacOS",
            "Development Status :: 4 - Beta",
        ],
        install_requires=[
            "hydra-core>=1.0.0",
            "ax-platform>=0.1.20",
            "torch<1.8.0",  # remove once torch 1.8.0 issue is addressed in Ax.
        ],
        include_package_data=True,
    )
