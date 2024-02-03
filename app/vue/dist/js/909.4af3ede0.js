"use strict";(self["webpackChunkmall_management"]=self["webpackChunkmall_management"]||[]).push([[909],{77001:function(e,t,r){r.d(t,{Z:function(){return y}});var a=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("el-upload",{staticClass:"avatar-uploader",attrs:{"show-file-list":!1,limit:1,action:"",headers:{"content-type":"application/json"},data:{url:e.imageUrl},name:"file","on-success":e.handleAvatarSuccess,"before-upload":e.beforeAvatarUpload,"before-remove":e.handleRemove}},[e.imageUrl?r("img",{staticClass:"avatar",attrs:{src:e.imageUrl}}):r("i",{staticClass:"el-icon-plus avatar-uploader-icon"})])},o=[],l=r(15677);const i="undefined"!==typeof crypto&&crypto.randomUUID&&crypto.randomUUID.bind(crypto);var s={randomUUID:i};r(48675),r(37380),r(1118),r(21703);let n;const c=new Uint8Array(16);function u(){if(!n&&(n="undefined"!==typeof crypto&&crypto.getRandomValues&&crypto.getRandomValues.bind(crypto),!n))throw new Error("crypto.getRandomValues() not supported. See https://github.com/uuidjs/uuid#getrandomvalues-not-supported");return n(c)}const m=[];for(let w=0;w<256;++w)m.push((w+256).toString(16).slice(1));function d(e,t=0){return(m[e[t+0]]+m[e[t+1]]+m[e[t+2]]+m[e[t+3]]+"-"+m[e[t+4]]+m[e[t+5]]+"-"+m[e[t+6]]+m[e[t+7]]+"-"+m[e[t+8]]+m[e[t+9]]+"-"+m[e[t+10]]+m[e[t+11]]+m[e[t+12]]+m[e[t+13]]+m[e[t+14]]+m[e[t+15]]).toLowerCase()}function p(e,t,r){if(s.randomUUID&&!t&&!e)return s.randomUUID();e=e||{};const a=e.random||(e.rng||u)();if(a[6]=15&a[6]|64,a[8]=63&a[8]|128,t){r=r||0;for(let e=0;e<16;++e)t[r+e]=a[e];return t}return d(a)}var f=p,g={name:"upload-com",props:{height:{type:Number},url:{type:String}},watch:{url(e){""!=e&&null!=e&&(this.imageUrl=e)}},data(){return{imageUrl:""}},created(){this.imageUrl=this.url},methods:{handleAvatarSuccess(e,t){this.imageUrl=URL.createObjectURL(t.raw)},beforeAvatarUpload(e){const t="image/jpeg"===e.type,r="image/png"===e.type,a=e.size/1024/1024<5;if(t||r)if(a){let t=f(),r=(new Date).getTime().toString().split("").reverse().join(""),a=e.type.split("/")[1],o=`${t}-${r}.${a}`;console.log(o),l.Z.putFile(o,e).then((e=>{this.$emit("success",e.data)})).catch((function(e){this.$emit("fail",e)}))}else this.$message.error("上传图片大小不能超过 5MB!");else this.$message.error("上传图片只能是 JPG或者PNG 格式!");return(t||r)&&a},setImage(e){this.imageUrl=e},handleRemove(){this.imageUrl=""}}},h=g,b=r(43736),v=(0,b.Z)(h,a,o,!1,null,"bc914e22",null),y=v.exports},50909:function(e,t,r){r.r(t),r.d(t,{default:function(){return u}});var a=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("div",[r("el-link",{staticStyle:{"font-size":"16px",cursor:"pointer",float:"right","margin-bottom":"10px",color:""},attrs:{underline:!1,type:"primary"},on:{click:e.add}},[r("i",{staticClass:"iconfont iconxinjian",staticStyle:{"padding-right":"5px"}}),e._v("新增")])],1),r("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.loading,expression:"loading"}],ref:"multipleTable",staticStyle:{width:"100%","text-align":"center","line-height":"18px","overflow-y":"auto"},attrs:{data:e.tableData,size:"small",border:"",height:e.height-60}},[r("el-table-column",{attrs:{label:"社群名",align:"center",prop:"name","show-overflow-tooltip":""}}),r("el-table-column",{attrs:{label:"当前人数",align:"center",width:"100",prop:"persons"}}),r("el-table-column",{attrs:{label:"是否启用",align:"center",prop:"status"},scopedSlots:e._u([{key:"default",fn:function(t){var r=t.row;return[e._v(" "+e._s(r.status?"是":"否")+" ")]}}])}),r("el-table-column",{attrs:{label:"群二维码",align:"center",prop:"qrcode"},scopedSlots:e._u([{key:"default",fn:function(e){var t=e.row;return[r("el-image",{staticStyle:{width:"100px",height:"100px"},attrs:{src:t.qrcode,fit:"cover"}})]}}])}),r("el-table-column",{attrs:{label:"操作",align:"center",width:"140"},scopedSlots:e._u([{key:"default",fn:function(t){var a=t.row;return[r("i",{staticClass:"el-icon-edit",staticStyle:{"margin-right":"20px"},on:{click:function(t){return e.handleEdit(a)}}}),r("i",{staticClass:"el-icon-delete",staticStyle:{"margin-right":"0"},on:{click:function(t){return e.handleDelete(a)}}})]}}])}),r("template",{slot:"empty"},[r("div",[r("i",{staticClass:"iconfont iconzanwuziyuan",staticStyle:{"font-size":"40px",color:"#8c8c8c"}},[r("p",{staticStyle:{"font-size":"14px","margin-top":"-30px"}},[e._v("暂无资源")])])])])],2),r("el-dialog",{attrs:{title:e.dialogTitle,visible:e.dialogFormVisible,width:"650px","close-on-click-modal":!1,"append-to-body":!0},on:{"update:visible":function(t){e.dialogFormVisible=t},closed:e.resetForm}},[r("el-form",{ref:"ruleForm",attrs:{model:e.form,rules:e.rules,size:"mini"}},[r("el-form-item",{attrs:{label:"社群名:",prop:"name"}},[r("el-input",{attrs:{autocomplete:"off"},model:{value:e.form.name,callback:function(t){e.$set(e.form,"name",t)},expression:"form.name"}})],1),r("el-form-item",{attrs:{label:"二维码:",prop:"qrcode"}},[r("upload",{ref:"myupload",attrs:{url:e.url},on:{success:e.handleSuccess}})],1),r("el-form-item",{attrs:{label:"是否启用:"}},[r("el-switch",{attrs:{"active-color":"#13ce66","inactive-color":"#ccc"},model:{value:e.form.status,callback:function(t){e.$set(e.form,"status",t)},expression:"form.status"}})],1)],1),r("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[r("el-button",{attrs:{size:"mini"},on:{click:e.cancelForm}},[e._v("取 消")]),r("el-button",{attrs:{type:"primary",size:"mini"},on:{click:function(t){return e.submitForm("ruleForm")}}},[e._v("提 交")])],1)],1)],1)},o=[],l=r(77001),i={name:"community_cop",components:{upload:l.Z},props:{height:{type:Number}},data(){return{loading:!1,tableData:[],dialogFormVisible:!1,dialogTitle:"管理",form:{name:"",qrcode:"",status:!1},rules:{name:[{required:!0,message:"请输入名称",trigger:"blur"},{min:1,max:24,message:"长度在 1 到 24 个字符",trigger:"blur"}]},url:null}},created(){},mounted(){this.getData()},methods:{getData(){this.$reqGet("/group/data").then((e=>{200==e.code?this.tableData=e.data:this.$message.error(e.msg)}))},submitForm(e){this.$refs[e].validate((e=>{if(!e)return console.log("error submit!!"),!1;{let e=this.form.id?"/group/edit":"/group/add";this.$reqPost(e,{...this.form}).then((e=>{200==e.code?(this.dialogFormVisible=!1,this.getData()):this.$message.error(e.msg)}))}}))},cancelForm(){this.dialogFormVisible=!1},resetForm(){this.$refs["ruleForm"].resetFields(),this.form.name="",this.form.qrcode=null,this.form.status=!1,this.url=null,this.$refs.myupload.handleRemove()},add(){this.dialogFormVisible=!0},handleEdit(e){this.form={...e},this.url=e.qrcode,this.dialogFormVisible=!0},handleDelete(e){this.$confirm("确定删除?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning",closeOnClickModal:!1}).then((()=>{console.log(e)}))},handleSuccess(e){console.log(e),this.form.qrcode=e.url}}},s=i,n=r(43736),c=(0,n.Z)(s,a,o,!1,null,"b96a661c",null),u=c.exports}}]);
//# sourceMappingURL=909.4af3ede0.js.map