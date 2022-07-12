#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "pybuilder_try"
default_task = "publish"


@init
def set_properties(project):
    pass
# # key-value based configuration
# @init
# def set_properties(project):
#     project.set_property('coverage_break_build', True)
#     project.set_property('flake8_break_build', True)
#     project.set_property('coverage_threshold_warn', 75)
#     project.build_depends_on("mock")
#     for dependency in ["docopt", "ultrajson", "treq"]:
#         project.depends_on(dependency)
#     project.depends_on("twisted", ">=13.2.0")
#     project.set_property("install_dependencies_index_url",
#                          "http://devpi-server.invalid/root/pypi")
