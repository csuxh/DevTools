<template>
  <div class="sidebar">
    <el-menu class="sidebar-el-menu"
             :default-active="onRoutes"
             :collapse="collapse"
             background-color="#324157"
             text-color="#bfcbd9"
             active-text-color="#20a0ff"
             unique-opened
             router>
      <template v-for="item in items">
        <template v-if="item.subs">
          <el-submenu :index="item.url"
                      :key="item.url">
            <template slot="title">
              <i :class="item.icon"></i>
              <span slot="title">{{ item.name }}</span>
            </template>
            <template v-for="subItem in item.subs">
              <el-submenu v-if="subItem.subs"
                          :index="subItem.url"
                          :key="subItem.url">
                <template slot="title">{{ subItem.name }}</template>
                <el-menu-item v-for="(threeItem,i) in subItem.subs"
                              :key="i"
                              :index="threeItem.url">{{ threeItem.name }}</el-menu-item>
              </el-submenu>
              <el-menu-item v-else
                            :index="subItem.url"
                            :key="subItem.url">{{ subItem.name }}</el-menu-item>
            </template>
          </el-submenu>
        </template>
        <template v-else>
          <el-menu-item :index="item.url"
                        :key="item.url">
            <i :class="item.icon"></i>
            <span slot="title">{{ item.name }}</span>
          </el-menu-item>
        </template>
      </template>
    </el-menu>
  </div>
</template>

<script>
import bus from '../common/bus';
import { menueList } from '../../api/index';
import axios from 'axios';
// import { FlatToNested } from '../../utils/db2menue'

export default {
  data () {
    return {
      collapse: false,
      items: [{
        icon: 'el-icon-lx-cascades',
        index: 'table',
        title: 'CMDB'
      }]
    };
  },
  methods: {
    FlatToNested (data, option) {
      option = option || {};
      let idProperty = option.idProperty || 'id';
      let parentProperty = option.parentProperty || 'parent';
      let childrenProperty = option.childrenProperty || 'children';
      let res = [],
        tmpMap = [];
      for (let i = 0; i < data.length; i++) {
        tmpMap[data[i][idProperty]] = data[i];
        if (tmpMap[data[i][parentProperty]] && data[i][idProperty] != data[i][parentProperty]) {
          if (!tmpMap[data[i][parentProperty]][childrenProperty])
            tmpMap[data[i][parentProperty]][childrenProperty] = [];
          tmpMap[data[i][parentProperty]][childrenProperty].push(data[i]);
        } else {
          res.push(data[i]);
        }
      }
      console.log(res);
      return res;
    },
    getData () {
      menueList(this.query).then(res => {
        // console.log(this.FlatToNested(res.results), {
        //   idProperty: 'id',            //唯一的节点标识符。
        //   nameProperty: 'name',         //节点的名称。
        //   parentProperty: 'parent'        });
        this.items = this.FlatToNested(res.results, {
          idProperty: 'id',            //唯一的节点标识符。
          nameProperty: 'name',         //节点的名称。
          parentProperty: 'parent',
          childrenProperty: 'subs'        })
      });
    }
  },
  computed: {
    onRoutes () {
      return this.$route.path.replace('/', '');
    }
  },
  created () {
    // 通过 Event Bus 进行组件间通信，来折叠侧边栏
    bus.$on('collapse', msg => {
      this.collapse = msg;
      this.getData();
      bus.$emit('collapse-content', msg);
    });
  }
};
</script>

<style scoped>
.sidebar {
    display: block;
    position: absolute;
    left: 0;
    top: 70px;
    bottom: 0;
    overflow-y: scroll;
}
.sidebar::-webkit-scrollbar {
    width: 0;
}
.sidebar-el-menu:not(.el-menu--collapse) {
    width: 250px;
}
.sidebar > ul {
    height: 100%;
}
</style>
