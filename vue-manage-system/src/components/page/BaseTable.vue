<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-lx-cascades"></i> Servers
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="container">
      <div class="handle-box">
        <el-button type="primary"
                   icon="el-icon-circle-plus"
                   class="handle-add mr10"
                   @click="">add</el-button>
        <el-select v-model="query.server_type"
                   placeholder="Service Level"
                   class="handle-select mr10">
          <el-option key="1"
                     label="prod"
                     value="Production"></el-option>
          <el-option key="2"
                     label="non-prod"
                     value="Non-Prod"></el-option>
        </el-select>
        <el-input v-model="query.name"
                  placeholder="hostname or ip"
                  class="handle-input mr10"></el-input>
        <el-button type="primary"
                   icon="el-icon-search"
                   @click="handleSearch">search</el-button>
        <el-button type="danger"
                   icon="el-icon-remove"
                   class="handle-del mr10"
                   @click="delAllSelection">delete</el-button>
      </div>
      <el-table :data="tableData"
                border
                class="table"
                ref="multipleTable"
                header-cell-class-name="table-header"
                @selection-change="handleSelectionChange">
        <el-table-column type="selection"
                         width="55"
                         align="center"></el-table-column>
        <el-table-column prop="id"
                         label="id"
                         width="55"
                         align="center">
          <template slot-scope="scope">{{scope.row.server_id}}</template>
        </el-table-column>
        <!--<el-table-column prop="name" label="name"></el-table-column>-->
        <el-table-column label="name">
          <template slot-scope="scope">{{scope.row.name}}</template>
        </el-table-column>
        <!--
                <el-table-column label="头像(查看大图)" align="center">
                    <template slot-scope="scope">
                        <el-image
                            class="table-td-thumb"
                            :src="scope.row.thumb"
                            :preview-src-list="[scope.row.thumb]"
                        ></el-image>
                    </template>
                </el-table-column>
                -->
        <el-table-column prop="address"
                         label="ip">
          <template slot-scope="scope">{{scope.row.ip1}}</template>
        </el-table-column>
        <el-table-column prop="site"
                         label="site">
          <template slot-scope="scope">{{scope.row.site}}</template>
        </el-table-column>
        <el-table-column prop="app_support"
                         label="app_support">
          <template slot-scope="scope">{{scope.row.app_support}}</template>
        </el-table-column>
        <el-table-column prop="platform_support"
                         label="platform_support">
          <template slot-scope="scope">{{scope.row.platform_support}}</template>
        </el-table-column>
        <el-table-column prop="modify_time"
                         label="modify_time">
          <template slot-scope="scope">{{scope.row.modify_time}}</template>
        </el-table-column>

        <el-table-column label="stats"
                         align="center">
          <template slot-scope="scope">
            <el-tag :type="scope.row.in_service==='Yes'?'success':(scope.row.state==='No'?'danger':'')">{{scope.row.in_service}}</el-tag>
          </template>
        </el-table-column>

        <el-table-column label="operation"
                         width="180"
                         align="center">
          <template slot-scope="scope">
            <el-button type="text"
                       icon="el-icon-edit"
                       @click="handleEdit(scope.$index, scope.row)">edit</el-button>
            <el-button type="text"
                       icon="el-icon-delete"
                       class="red"
                       @click="handleDelete(scope.$index, scope.row)">delete</el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="pagination">
        <el-pagination background
                       layout="total, sizes, prev, pager, next, jumper"
                       :current-page="query.page"
                       :page-size="query.pageSize"
                       :total="pageTotal"
                       @current-change="handlePageChange"
                       @size-change="handleSizeChange"></el-pagination>
      </div>
    </div>

    <!-- 编辑弹出框 -->
    <el-dialog title="Modify Server"
               :visible.sync="editVisible"
               width="30%">
      <el-form ref="form"
               :model="form"
               label-width="120px">
        <el-form-item label="hostname">
          <el-input v-model="form.hostname"></el-input>
        </el-form-item>
        <el-form-item label="ip">
          <el-input v-model="form.ip"></el-input>
        </el-form-item>
        <el-form-item label="app support">
          <el-input v-model="form.app_support"></el-input>
        </el-form-item>
        <el-form-item label="platform support">
          <el-input v-model="form.platform_support"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="editVisible = false">cancel</el-button>
        <el-button type="primary"
                   @click="saveEdit">confirm</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { fetchCMDB, queryCMDB } from '../../api/index';
// import {{ queryCMDB }} from '../../api/index';

export default {
  name: 'basetable',
  data () {
    return {
      query: {
        server_type: '',
        name: '',
        page: 1
      },
      tableData: [],
      multipleSelection: [],
      delList: [],
      editVisible: false,
      pageTotal: 0,
      form: {},
      idx: -1,
      id: -1
    };
  },
  created () {
    this.getData();
  },
  methods: {
    // 获取 easy-mock 的模拟数据
    getData () {
      fetchCMDB(this.query).then(data => {
        this.tableData = data.results;
        this.pageTotal = data.count;
      });
    },
    // 触发搜索按钮
    handleSearch () {
      delete this.query.page;
      console.log(this.query);
      queryCMDB(this.query).then(res => {
        this.tableData = res.results;
        this.pageTotal = res.count;
      });
    },
    // 删除操作
    handleDelete (index, row) {
      // 二次确认删除
      this.$confirm('确定要删除吗？', '提示', {
        type: 'warning'
      })
        .then(() => {
          this.$message.success('删除成功');
          this.tableData.splice(index, 1);
        })
        .catch(() => { });
    },
    // 多选操作
    handleSelectionChange (val) {
      this.multipleSelection = val;
    },
    delAllSelection () {
      const length = this.multipleSelection.length;
      let str = '';
      this.delList = this.delList.concat(this.multipleSelection);
      for (let i = 0; i < length; i++) {
        str += this.multipleSelection[i].name + ' ';
      }
      this.$message.error(`删除了${str}`);
      this.multipleSelection = [];
    },
    // 编辑操作
    handleEdit (index, row) {
      this.idx = index;
      this.form = row;
      this.editVisible = true;
    },
    // 保存编辑
    saveEdit () {
      this.editVisible = false;
      this.$message.success(`修改第 ${this.idx + 1} 行成功`);
      this.$set(this.tableData, this.idx, this.form);
    },
    // 分页导航
    handlePageChange (val) {
      this.$set(this.query, 'page', val);
      this.getData();
    },
    handleSizeChange (val) {
      this.pageSize = val;
      // console.log(`每页 ${val} 条`);
    }
  }
};
</script>

<style scoped>
.handle-box {
    margin-bottom: 20px;
}

.handle-select {
    width: 120px;
}

.handle-input {
    width: 300px;
    display: inline-block;
}
.table {
    width: 100%;
    font-size: 14px;
}
.red {
    color: #ff0000;
}
.mr10 {
    margin-right: 10px;
}
.table-td-thumb {
    display: block;
    margin: auto;
    width: 40px;
    height: 40px;
}
</style>
