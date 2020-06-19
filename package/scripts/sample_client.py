#!/usr/bin/env python

import sys
from resource_management import *
class SampleClient(Script):
  def install(self, env):
    import params
    print 'Install the Sample Srv Client';
    # Install packages listed in metainfo.xml
    env.set_params(params)

    cmd = '/bin/rm -rf  /usr/hdp/current/flink'
    Execute(cmd)

    # delete  the base_dir dir
    cmd = '/bin/rm -rf ' + params.flink_install_dir
    Execute(cmd)

    Execute('wget -O flink.tgz {0}'.format(params.flink_download_url))
    Execute('tar -zxvf flink.tgz -C {0} && rm -f flink.tgz'.format(params.hdp_base_dir))
    Execute('mv {0}/flink-* {1}'.format(params.hdp_base_dir,params.flink_install_dir))

    cmd = '/bin/ln' + ' -s  {0} /usr/hdp/current/flink'.format(params.flink_install_dir)
    Execute(cmd)
    Execute("hadoop fs -put {0}/lib/* {1}/*".format(params.flink_install_dir,params.flink_dependency_jar))
    self.configure(env)


  def configure(self, env):
      import params
      env.set_params(params)
      Execute('rm -rf {0}/lib/*'.format(params.flink_install_dir))
      Execute( '/usr/bin/hadoop fs -get {0}/* {1}/lib/'.format(params.flink_dependency_jar,params.flink_install_dir))
      Execute( 'chmod 777 -R {0}/lib'.format(params.flink_install_dir))
      Execute( 'chmod 777 -R {0}/log'.format(params.flink_install_dir))

      # copy hadoop conf to flink
      Execute('cp {0}/hdfs-site.xml {1}/conf'.format(params.hadoop_conf_dir,params.flink_install_dir))
      Execute('cp {0}/yarn-site.xml {1}/conf'.format(params.hadoop_conf_dir,params.flink_install_dir))
      Execute('cp {0}/core-site.xml {1}/conf'.format(params.hadoop_conf_dir,params.flink_install_dir))

      # write out flink-conf.yaml
      properties_conf = InlineTemplate(params.flink_yaml_content)
      File(format(params.flink_install_dir+"/conf/flink-conf.yaml"), content=properties_conf)

      #log4j property
      properties_log4j = InlineTemplate(params.flink_log4j)
      File(format(params.flink_install_dir+"/conf/log4j.properties"), content=properties_log4j)

if __name__ == "__main__":
  SampleClient().execute()
