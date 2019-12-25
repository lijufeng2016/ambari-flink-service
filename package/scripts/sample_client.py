#!/usr/bin/env python

import sys
from resource_management import *
class SampleClient(Script):
  def install(self, env):
    import params
    print 'Install the Sample Srv Client';

    # Install packages listed in metainfo.xml
    self.install_packages(env)
    env.set_params(params)

    # delete  the base_dir dir
    cmd = '/bin/rm -rf ' + params.base_dir
    Execute('echo "Running ' + cmd + '"')
    Execute(cmd)

    # Create the base_dir dir
    cmd = '/bin/mkdir' + ' -p ' + params.base_dir
    Execute('echo "Running ' + cmd + '"')
    Execute(cmd)

    cmd = '/bin/tar' + ' -zxf ' + params.flink_package_dir + 'files/' + params.flink_archive_file + ' --strip 1 -C ' + params.base_dir
    Execute('echo "Running ' + cmd + '"')
    Execute(cmd)

    cmd = '/bin/chown ' + 'root:root ' +params.base_dir
    Execute('echo "Running ' + cmd + '"')
    Execute(cmd)

    cmd = '/bin/chmod ' + '777 ' +params.base_dir + 'log'
    Execute('echo "Running ' + cmd + '"')
    Execute(cmd)


    cmd = '/bin/ln' + ' -s ' + params.base_dir  + ' /usr/hdp/current/flink'
    Execute('echo "Running ' + cmd + '"')

    try:
        Execute(cmd)
    except:
        pass

    self.configure(env)

  def configure(self, env):
      import params

      cmd = '/usr/bin/hadoop fs -get ' + params.flink_dependency_jar +'/* '+ params.base_dir + 'lib/'
      Execute('echo "Running ' + cmd + '"')
      Execute(cmd)

      # write out flink-conf.yaml
      properties_content = InlineTemplate(params.flink_yaml_content)
      File(format(params.base_dir+"conf/flink-conf.yaml"), content=properties_content)
if __name__ == "__main__":
  SampleClient().execute()