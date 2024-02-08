<template>

    <div class="container" style=" max-width:100%; margin-top:20px; margin-left: 10px;margin-right: 40px">
        <el-button type="primary" @click="editText" style="margin-bottom: 10px">编辑</el-button>
        <el-form>
          <el-input v-model="textContent" type="textarea"  :disabled="editAble" rows="21" style="font-size: 16px;"/>
          <el-button type="primary" @click="onSubmit" style="margin-top: 10px">保 存</el-button>
          <el-button @click="cancelSave" style="margin-top: 10px">取 消</el-button>

      </el-form>
    </div>

</template>

<script lang="ts" setup>
import { reactive, ref, onBeforeMount } from 'vue'
import axios from "axios";

const editAble = ref(true)
const textContent = ref('wqeqweqwe')

const onSubmit = () => {
  // console.log('submit!')
    editAble.value = true
}

const editText = () => {
  // console.log('submit!')
    editAble.value = false
}

const getJsonContent = () => {
  console.log('getJsonContent!')
    editAble.value = true
    axios.get('/api/project/manage/namespace/modify/').then(response => {
        // console.log(response.data);
        textContent.value = JSON.stringify(response.data)
        textContent.value = JSON.stringify(JSON.parse(textContent.value), null, '\t')
    }).catch(error => {
        console.log(error);
    })
}


const cancelSave = () => {
    getJsonContent()
}


onBeforeMount(() => {
    getJsonContent()
});
</script>
