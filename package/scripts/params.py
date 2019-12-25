#!/usr/bin/env python
from resource_management import *
from resource_management.libraries.script.script import Script
from resource_management.libraries.functions.default import default


# server configuration
config = Script.get_config()
base_dir = "/opt/flink/"

flink_archive_file = 'flink-1.9.1-bin-scala_2.11.tgz'

stack_name = default("/hostLevelParams/stack_name", None)
stack_version = config['hostLevelParams']['stack_version']

# flink archive on agent nodes
flink_package_dir = "/var/lib/ambari-agent/cache/stacks/HDP/2.6/services/FLINK/package/"

# params from flink-ambari-config
flink_install_dir = config['configurations']['flink-ambari-config']['flink_install_dir']
hadoop_conf_dir = config['configurations']['flink-ambari-config']['hadoop_conf_dir']

# params from flink-conf.yaml
flink_yaml_content = config['configurations']['flink-env']['content']
flink_dependency_jar = config['configurations']['flink-env']['flink_dependency_jar']

