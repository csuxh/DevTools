<template>
  <div>
    <div class="container">
      <div class="handle-box">
        <el-button type="primary">
          add
        </el-button>

        <el-table :data="rabbit_servers"
                  border
                  stripe
                  style="width: 100%">
          <el-table-column prop="env"
                           label="env"
                           width="100%"
                           align="center">
          </el-table-column>
          <el-table-column prop="hostname"
                           label="hostname"
                           width="100%"
                           align="center">
          </el-table-column>
          <el-table-column prop="ip"
                           label="ip"
                           width="100%"
                           align="center">
          </el-table-column>
        </el-table>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'rabbitmqctl',
  data () {
    return {
      rabbit_servers: [],
    };
  },
  created () {
    this.getData();
  },
  methods: {
    getData () {
      this.rabbit_servers = [{ "env": "prod", "hostname": "wqsrc1079.cn.prod", "ip": "10.27.30.39" }, { "env": "uat", "hostname": "wqsrc1078.cn.prod", "ip": "10.27.31.39" }];
    },
  }

}
</script>