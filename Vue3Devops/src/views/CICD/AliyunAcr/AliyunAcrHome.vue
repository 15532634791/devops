<template>
  <div>
    <button @click="toggleOverlay" class="btn" style="background-color:#5CADAD; witdh: 200px;font-size: 20px">点击展开</button>
    <div class="overlay" :class="{ show: showOverlay }">
      <div class="overlay-content">



        <form @submit.prevent="submitForm">
            <div style="margin: 10px; border: #0b2e13">
                        <form className="row g-4">
                            <h5> 构建信息 </h5>
                            <div className="col-5">

                                <label for=""> <b><span style="color: red">*</span> 构建名称 </b></label>
                                <input type="text" className="form-control" id="inputAddress"
                                       placeholder="请输入构建名称">
                            </div>

                            <div className="col-5">

                                <label for=""> <b><span style="color: red">*</span>文件URL</b></label>
                                <input type="text" className="form-control" id="inputAddress"
                                       placeholder="请输入文件URL">

                            </div>

                            <div className="col-5">

                                <label for=""> <b>credentialID</b></label>
                                <input type="text" className="form-control" id="inputAddress"
                                       placeholder="credentialID为jenkins凭据ID，非必填">
                            </div>

                            <div className="col-5">

                                <label for=""> <b>分支</b></label>
                                <input type="text" className="form-control" id="inputAddress"
                                       placeholder="./*master">

                            </div>


                            <h5> 镜像信息 </h5>
                            <div className="col-5">

                                <label for=""> <b> <span style="color: red">*</span>镜像名称</b></label>
                                <input type="text" className="form-control" id="inputAddress"
                                       placeholder="请输入镜像名称">
                            </div>

                            <div className="col-5">

                                <label for=""> <b> <span style="color: red">*</span>镜像版本</b></label>
                                <input type="text" className="form-control" id="inputAddress"
                                       placeholder="请输入镜像版本号">

                            </div>

                            <div className="col-5">

                                <label for=""> <b> <span style="color: red">*</span>Dockerfile位置</b></label>
                                <input type="text" className="form-control" id="inputAddress"
                                       placeholder="http://">
                            </div>

                            <div className="col-5">

                                <label for=""> <b> <span style="color: red">*</span>构建参数</b></label>
                                <input type="text" className="form-control" id="inputAddress"
                                       placeholder="">

                            </div>

                            <div className="col-10">

                                <label for=""> <b> 构建脚本</b></label>
                                <textarea className="form-control" style="height: 100px" name="description" placeholder="echo 'Hello World!'"></textarea>

                            </div>



                        </form>
                    </div>

          <div class="overlay-buttons" style="text-align: center">
            <button @click="closeOverlay" class="btn btn-info" style="witdh: 300px;font-size: 20px"> 确 定 </button> &nbsp;
            <button type="submit" class="btn btn-light" style="witdh: 200px;font-size: 20px"> 取 消 </button>
          </div>


        </form>
      </div>
    </div>
  </div>

  <div>

       申请状态
      已完成 未完成
  </div>
</template>

<script>
export default {
  data() {
    return {
      showOverlay: false,
      formData: {
        name: "",
        email: ""
      }
    };
  },
  methods: {
    toggleOverlay() {
      this.showOverlay = !this.showOverlay;
    },
    closeOverlay() {
      this.showOverlay = false;
    },
    submitForm() {
      console.log(this.formData); // 提交表单数据
      this.closeOverlay();
    }
  }
};
</script>

<style scoped>
.overlay {
  position: fixed;
  right: 0;
  top: 0;
  width: 70%;
  height: 100vh;
  background-color: rgb(255, 255, 255);
  z-index: 9999;
  overflow-x: hidden;
  transition: 0.1s;
  transform: translateX(100%);
}

.overlay.show {
  transform: translateX(0);
}

.overlay-content {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.overlay-buttons {
  margin-top: 20px;
}
</style>
