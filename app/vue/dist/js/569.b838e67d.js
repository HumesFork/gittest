"use strict";(self["webpackChunkmall_management"]=self["webpackChunkmall_management"]||[]).push([[569],{36569:function(t,e,a){a.r(e),a.d(e,{default:function(){return c}});var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("div",[a("el-link",{staticStyle:{"font-size":"16px",cursor:"pointer",float:"right","margin-bottom":"10px"},attrs:{underline:!1,type:"primary"},on:{click:t.add}},[a("i",{staticClass:"iconfont iconxinjian",staticStyle:{"padding-right":"5px"}}),t._v("新增")])],1),a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:t.loading,expression:"loading"}],ref:"multipleTable",staticStyle:{width:"100%","text-align":"center","line-height":"18px"},attrs:{data:t.tableData,size:"small",border:"",height:t.height-60}},[a("el-table-column",{attrs:{label:"角色",align:"center",prop:"name","show-overflow-tooltip":""}}),a("el-table-column",{attrs:{label:"标识",align:"center",prop:"sign"}}),a("el-table-column",{attrs:{label:"权限",align:"center",width:"300"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("el-checkbox-group",{model:{value:e.row.authority,callback:function(a){t.$set(e.row,"authority",a)},expression:"scope.row.authority"}},[a("el-checkbox",{attrs:{label:"add",disabled:""}},[t._v("新增")]),a("el-checkbox",{attrs:{label:"edit",disabled:""}},[t._v("编辑")]),a("el-checkbox",{attrs:{label:"delete",disabled:""}},[t._v("删除")])],1)]}}])}),a("el-table-column",{attrs:{label:"账号",align:"center",prop:"account","show-overflow-tooltip":""}}),a("el-table-column",{attrs:{label:"密码",width:"200",align:"center",prop:"password","show-overflow-tooltip":""}}),a("el-table-column",{attrs:{label:"操作",align:"center",width:"140"},scopedSlots:t._u([{key:"default",fn:function(e){var i=e.row;return[a("i",{staticClass:"el-icon-edit",staticStyle:{"margin-right":"20px"},on:{click:function(e){return t.handleEdit(i)}}}),a("i",{staticClass:"el-icon-delete",staticStyle:{"margin-right":"0"},on:{click:function(e){return t.handleDelete(i)}}})]}}])}),a("template",{slot:"empty"},[a("div",[a("i",{staticClass:"iconfont iconzanwuziyuan",staticStyle:{"font-size":"40px",color:"#8c8c8c"}},[a("p",{staticStyle:{"font-size":"14px","margin-top":"-30px"}},[t._v("暂无资源")])])])])],2),a("el-dialog",{attrs:{title:t.dialogTitle,visible:t.dialogFormVisible,width:"650px","close-on-click-modal":!1,"append-to-body":!0},on:{"update:visible":function(e){t.dialogFormVisible=e},closed:t.resetForm}},[a("el-form",{ref:"ruleForm",attrs:{model:t.form,rules:t.rules,size:"mini"}},[a("el-form-item",{attrs:{label:"角色名字:",prop:"name"}},[a("el-input",{attrs:{autocomplete:"off"},model:{value:t.form.name,callback:function(e){t.$set(t.form,"name",e)},expression:"form.name"}})],1),a("el-form-item",{attrs:{label:"标识:",prop:"sign"}},[a("el-input",{attrs:{autocomplete:"off"},model:{value:t.form.sign,callback:function(e){t.$set(t.form,"sign",e)},expression:"form.sign"}})],1),a("el-form-item",{attrs:{label:"账号:",prop:"account"}},[a("el-input",{attrs:{autocomplete:"off"},model:{value:t.form.account,callback:function(e){t.$set(t.form,"account",e)},expression:"form.account"}})],1),a("el-form-item",{attrs:{label:"密码:",prop:"password"}},[a("el-input",{attrs:{autocomplete:"off"},model:{value:t.form.password,callback:function(e){t.$set(t.form,"password",e)},expression:"form.password"}})],1),a("el-form-item",{attrs:{label:"权限:",prop:"authority"}},[a("el-checkbox-group",{model:{value:t.form.authority,callback:function(e){t.$set(t.form,"authority",e)},expression:"form.authority"}},[a("el-checkbox",{attrs:{label:"add"}},[t._v("新增")]),a("el-checkbox",{attrs:{label:"edit"}},[t._v("编辑")]),a("el-checkbox",{attrs:{label:"delete"}},[t._v("删除")])],1)],1)],1),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{attrs:{size:"mini"},on:{click:t.cancelForm}},[t._v("取 消")]),a("el-button",{attrs:{type:"primary",size:"mini"},on:{click:function(e){return t.submitForm("ruleForm")}}},[t._v("提 交")])],1)],1)],1)},o=[],l={name:"authority_cop",components:{},props:{height:{type:Number}},data(){return{loading:!1,tableData:[],dialogFormVisible:!1,dialogTitle:"管理",id:null,form:{name:"",sign:"",account:"",password:"",authority:[]},rules:{name:[{required:!0,message:"请输入名称",trigger:"blur"},{min:1,max:32,message:"长度在 1 到 32 个字符",trigger:"blur"}],sign:[{required:!0,message:"请输入",trigger:"blur"},{min:1,max:32,message:"长度在 1 到 32 个字符",trigger:"blur"}],account:[{required:!0,message:"请输入",trigger:"blur"},{min:1,max:32,message:"长度在 1 到 32 个字符",trigger:"blur"}],password:[{required:!0,message:"请输入",trigger:"blur"},{min:1,max:32,message:"长度在 1 到 32 个字符",trigger:"blur"}]}}},created(){},mounted(){this.getData()},methods:{getData(){this.$reqGet("/authority/allData").then((t=>{200==t.code?(t.data.forEach((t=>{t.authority=[],t.add&&t.authority.push("add"),t.edit&&t.authority.push("edit"),t.delete&&t.authority.push("delete")})),this.tableData=t.data):this.$message.error(t.msg)}))},submitForm(t){this.$refs[t].validate((t=>{if(!t)return console.log("error submit!!"),!1;{this.form.add=!1,this.form.edit=!1,this.form.delete=!1,this.form.authority.forEach((t=>{this.form[t]=!0}));let t=this.id?"authority/edit":"/authority/add";this.$reqPost(t,{...this.form,id:this.id}).then((t=>{200==t.code?(t.data&&(this.dialogFormVisible=!1),this.getData()):this.$message.error(t.msg)}))}}))},cancelForm(){this.dialogFormVisible=!1},resetForm(){this.$refs["ruleForm"].resetFields(),this.form={name:"",sign:"",account:"",password:"",authority:[]},this.id=null,this.getData()},add(){this.dialogFormVisible=!0},handleEdit(t){let e=JSON.parse(JSON.stringify(t));this.form=e,this.dialogFormVisible=!0,this.id=e.id},handleDelete(t){this.$confirm("确定删除?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning",closeOnClickModal:!1}).then((()=>{let e=t.id;this.$reqPost("/authority/del",{id:e}).then((t=>{200==t.code?this.getData():this.$message.error(t.msg)}))}))}}},r=l,s=a(43736),n=(0,s.Z)(r,i,o,!1,null,"04b1a4cc",null),c=n.exports}}]);
//# sourceMappingURL=569.b838e67d.js.map