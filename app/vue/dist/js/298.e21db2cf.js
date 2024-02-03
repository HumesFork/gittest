"use strict";(self["webpackChunkmall_management"]=self["webpackChunkmall_management"]||[]).push([[298],{298:function(e,t,a){a.r(t),a.d(t,{default:function(){return p}});var l=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("div",{staticStyle:{"font-size":"16px",position:"absolute",top:"12px",right:"40px"}},[a("el-link",{staticStyle:{"font-size":"16px",cursor:"pointer","margin-top":"10px"},attrs:{underline:!1,type:"primary"},on:{click:e.exportExcel}},[a("i",{staticClass:"iconfont iconxinjian",staticStyle:{"padding-right":"5px"}}),e._v("导出")])],1),a("div",{attrs:{id:"top"}},[a("div",[a("span",[e._v("微信号")]),a("el-input",{staticClass:"search",attrs:{placeholder:"请输入",size:"mini"},model:{value:e.params.openid,callback:function(t){e.$set(e.params,"openid",t)},expression:"params.openid"}}),a("span",[e._v("ID")]),a("el-input",{staticClass:"search",attrs:{placeholder:"请输入",size:"mini"},model:{value:e.params.id,callback:function(t){e.$set(e.params,"id",t)},expression:"params.id"}}),a("span",[e._v("手机号码")]),a("el-input",{staticClass:"search",attrs:{placeholder:"请输入",size:"mini"},model:{value:e.params.phoneNumber,callback:function(t){e.$set(e.params,"phoneNumber",t)},expression:"params.phoneNumber"}}),a("span",{staticStyle:{"margin-left":"20px"}},[e._v("状态")]),a("el-select",{staticClass:"search",attrs:{placeholder:"请选择",size:"mini"},model:{value:e.params.status,callback:function(t){e.$set(e.params,"status",t)},expression:"params.status"}},[a("el-option",{attrs:{label:"禁言",value:"disabled"}}),a("el-option",{attrs:{label:"正常",value:"normal"}})],1),a("el-button-group",{staticStyle:{"margin-left":"20px"}},[a("el-button",{attrs:{type:"primary",size:"mini"},on:{click:e.search}},[e._v("搜索")]),a("el-button",{attrs:{size:"mini"},on:{click:e.resetTable}},[e._v("重置")])],1)],1)]),a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.loading,expression:"loading"}],ref:"multipleTable",staticStyle:{width:"100%","text-align":"center","line-height":"18px"},attrs:{data:e.tableData,size:"small",border:"",height:e.height-130}},[a("el-table-column",{attrs:{label:"微信号",align:"center",prop:"openid",width:"250","show-overflow-tooltip":""}}),a("el-table-column",{attrs:{label:"手机号码",align:"center",prop:"phoneNumber"}}),a("el-table-column",{attrs:{label:"微信名",align:"center",width:"100",prop:"username"}}),a("el-table-column",{attrs:{label:"状态",align:"center",prop:"status"},scopedSlots:e._u([{key:"default",fn:function(t){var a=t.row;return[e._v(" "+e._s("disabled"==a.status?"禁言中":"正常")+" ")]}}])}),a("el-table-column",{attrs:{label:"id",align:"center",prop:"id","show-overflow-tooltip":""}}),a("el-table-column",{attrs:{label:"vip",align:"center","show-overflow-tooltip":""},scopedSlots:e._u([{key:"default",fn:function(t){var a=t.row;return[e._v(" "+e._s(a.vip?"是":"否")+" ")]}}])}),a("el-table-column",{attrs:{label:"积分",width:"100",align:"center",prop:"points","show-overflow-tooltip":""}}),a("el-table-column",{attrs:{label:"打卡记录",width:"100",align:"center",prop:"remarks","show-overflow-tooltip":""}}),a("el-table-column",{attrs:{label:"操作",align:"center",width:"140"},scopedSlots:e._u([{key:"default",fn:function(t){var l=t.row;return[a("el-link",{staticStyle:{"margin-right":"10px"},attrs:{type:"success"},on:{click:function(t){return e.edit(l)}}},[e._v("编辑")]),a("el-link",{staticStyle:{"margin-right":"10px"},attrs:{type:"warning"},on:{click:function(t){return e.handleDisabled(l,"disabled")}}},[e._v("禁言")]),a("el-link",{attrs:{type:"success"},on:{click:function(t){return e.handleDisabled(l,"normal")}}},[e._v("解封")])]}}])}),a("template",{slot:"empty"},[a("div",[a("i",{staticClass:"iconfont iconzanwuziyuan",staticStyle:{"font-size":"40px",color:"#8c8c8c"}},[a("p",{staticStyle:{"font-size":"14px","margin-top":"-30px"}},[e._v("暂无资源")])])])])],2),a("el-pagination",{staticStyle:{float:"right","margin-top":"20px"},attrs:{"current-page":e.currentPage,"page-sizes":[20,100,150,200],"page-size":e.pageSize,layout:"total, sizes, prev, pager, next, jumper",total:e.total},on:{"size-change":e.handleSizeChange,"current-change":e.handleCurrentChange}}),a("el-dialog",{attrs:{title:"编辑",visible:e.dialogFormVisible},on:{"update:visible":function(t){e.dialogFormVisible=t},close:e.reset}},[a("el-form",{attrs:{model:e.form,size:"small"}},[a("el-form-item",{attrs:{label:"VIP日期范围"}},[a("el-date-picker",{attrs:{type:"daterange",align:"right","unlink-panels":"","range-separator":"至","start-placeholder":"开始日期","end-placeholder":"结束日期"},model:{value:e.form.date,callback:function(t){e.$set(e.form,"date",t)},expression:"form.date"}})],1)],1),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{attrs:{size:"small"},on:{click:function(t){e.dialogFormVisible=!1}}},[e._v("取 消")]),a("el-button",{attrs:{type:"primary",size:"small"},on:{click:e.submit}},[e._v("确 定")])],1)],1)],1)},s=[],i={name:"User_management",components:{},props:{height:{type:Number}},data(){return{loading:!1,currentPage:1,pageSize:20,total:0,params:{openid:"",id:"",phoneNumber:"",status:""},tableData:[],dialogFormVisible:!1,form:{date:[]},row:{}}},created(){},mounted(){this.getData()},methods:{getData(){this.$reqPost("/user/allData",{...this.params}).then((e=>{200==e.code?this.tableData=e.data:this.$message.error(e.msg)}))},handleDisabled(e,t){let a=e.openid;this.$reqPost("/user/disabled",{openid:a,status:t}).then((e=>{200==e.code?this.getData():this.$message.error(e.msg)}))},handleSizeChange(e){this.pageSize=e},handleCurrentChange(e){this.currentPage=e},handleSelectionChange(e){console.log(e)},search(){console.log(this.params),this.getData()},resetTable(){this.params={openid:"",id:"",phoneNumber:"",status:""},this.getData()},reset(){this.row={}},edit(e){if(this.row=e,e.vip){let t=e.vip.split(",");t[0]=new Date(Number(t[0])).toLocaleDateString(),t[1]=new Date(Number(t[1])).toLocaleDateString(),console.log(t),this.form={date:t}}this.dialogFormVisible=!0},submit(){let e=this.form.date,t=new Date(e[0]).getTime(),a=new Date(e[1]).getTime();this.$reqPost("/user/setVip",{date:[t.toString(),a.toString()],openid:this.row.openid}).then((e=>{200==e.code?(this.$message.success("提交成功"),this.dialogFormVisible=!1,this.getData()):this.$message.error(e.msg)}))},exportExcel(){this.$reqGet("/user/exportExcel").then((e=>{200==e.code?console.log(e):this.$message.error(e.msg)}))}}},r=i,o=a(43736),n=(0,o.Z)(r,l,s,!1,null,"2a98c7b2",null),p=n.exports}}]);
//# sourceMappingURL=298.e21db2cf.js.map