<template>
    <div style="width: 100%">
        <el-row :gutter="20">
            <el-col :span="12">
                <div class="grid-content ep-bg-purple">
                    <el-form :model="ipForm" ref="ipFormRef" @submit.prevent>
                        <div class="form-item">
                            <h5 style="text-align: center">网络测试工具</h5>
                            <span class="form-label">源 IP 地址</span>
                            <el-form-item label="" prop="sourceIp">
                                <el-input v-model="ipForm.sourceIp" placeholder="请输入源 IP 地址"
                                          @blur="validateIP('sourceIp')"></el-input>
                                <div v-if="sourceIpValidationMessage" class="feedback">{{
                                    sourceIpValidationMessage
                                    }}
                                </div>
                            </el-form-item>
                        </div>
                        <div class="form-item">
                            <span class="form-label">目的 IP 地址</span>
                            <el-form-item label="" prop="destinationIp">
                                <el-input v-model="ipForm.destinationIp" placeholder="请输入目的 IP 地址"
                                          @blur="validateIP('destinationIp')" ></el-input>
                                <div v-if="destinationIpValidationMessage" class="feedback">
                                    {{ destinationIpValidationMessage }}
                                </div>
                            </el-form-item>
                        </div>
                        <div class="form-item">
                            <span class="form-label">端口号</span>
                            <el-form-item label="" prop="port">
                                <el-input v-model="ipForm.port" placeholder="请输入端口号"
                                          @blur="validatePort"></el-input>
                                <div v-if="portValidationMessage" class="feedback">{{ portValidationMessage }}</div>
                            </el-form-item>
                        </div>
                        <el-form-item>
                            <el-button type="primary" @click="submitForm">提交</el-button>
                        </el-form-item>
                    </el-form>
                </div>
            </el-col>

            <el-col :span="12">
                <div class="grid-content-tools ep-bg-purple">
                    <p>网络测试工具输出： </p>
<!--                    {{ networkToolsOutput }}-->
                    <br>
                    <p>ping 源IP</p>
                    <pre>
                        {{ sourceIpOutput }}
                    </pre>
                    <pre>
                        {{ destinationIpOutput }}
                    </pre>
                    <pre>
                        {{ portOutput }}
                    </pre>
<!--                    <p style="background-color: #f4f4f4;border: 1px solid #ddd;padding: 10px;border-radius: 4px;overflow-x: auto;"> {{ sourceIpOutput }} </p>-->
<!--                    <p style="background-color: #f4f4f4;border: 1px solid #ddd;padding: 10px;border-radius: 4px;overflow-x: auto;"> {{ destinationIpOutput }} </p>-->
<!--                    <p style="background-color: #f4f4f4;border: 1px solid #ddd;padding: 10px;border-radius: 4px;overflow-x: auto;"> {{ portOutput }} </p>-->


                </div>
            </el-col>

            <el-col :span="12">
                <div class="grid-content ep-bg-purple">
                    <div class="form-item">
                        <h5 style="text-align: center">自定义shell工具</h5>
                        <span class="form-label">Shell <span
                                style="font-size: 12px; color: red">多个命令以换行拼接</span> </span>
                        <el-form-item label="">
                            <el-input v-model="shellCommandForm.shellCommand" type="textarea"
                                      style="width: 100%; height: 100%;font-size: 17px;" :rows="8"/>

                            <el-button type="primary" @click="onSubmit">提交</el-button>
                        </el-form-item>
                    </div>
                </div>
            </el-col>


            <el-col :span="12">
                <div class="grid-content-tools ep-bg-purple">

                    <p>自定义shell输出：</p>
                    <div v-for="command in shellCommandOutput" :key="command.command">
                        <b style="margin: 2px;padding: 2px">{{ command.command }}</b>
                        <pre>{{ command.output }}</pre>
                    </div>


                </div>
            </el-col>


        </el-row>

    </div>
</template>

<script lang="ts" setup>
import {ref, computed} from 'vue';
import axios from "axios";

const ipFormRef = ref(null);
const ipForm = ref({
    sourceIp: '',
    destinationIp: '',
    port: ''
});
const shellCommandForm = ref(
    {
        shellCommand: ''
    }
)

const shellCommandOutput = ref('');
const networkToolsOutput = ref('')
const sourceIpOutput = ref('')
const destinationIpOutput = ref('')
const portOutput = ref('')
const sourceIpValidationMessage = ref('');
const destinationIpValidationMessage = ref('');
const portValidationMessage = ref('');
const ipPattern = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
const portPattern = /^(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[0-9]{1,4})$/;

const validateIP = (ipType: string) => {
    let ipValue = ipForm.value[ipType];
    let validationMessageRef = ipType === 'sourceIp' ? sourceIpValidationMessage : destinationIpValidationMessage;

    if (ipValue === '') {
        validationMessageRef.value = '';
    } else if (ipPattern.test(ipValue)) {
        validationMessageRef.value = `${ipType === 'sourceIp' ? '源' : '目的'} IP 地址格式正确`;
    } else {
        validationMessageRef.value = `${ipType === 'sourceIp' ? '源' : '目的'} IP 地址格式不正确`;
    }
};

const validatePort = () => {
    let portValue = ipForm.value.port;

    if (portValue === '') {
        portValidationMessage.value = '';
    } else if (portPattern.test(portValue)) {
        portValidationMessage.value = '端口号格式正确';
    } else {
        portValidationMessage.value = '端口号格式不正确';
    }
};

const submitForm = () => {
    ipFormRef.value.validate((valid: boolean) => {
        if (valid) {
            console.log('提交表单', ipForm.value.sourceIp, ipForm.value.destinationIp, ipForm.value.port);
            console.log('提交表单', ipForm.value);

            axios.post('/api/config/script/network/', ipForm.value).then(response => {
                console.log(response.data);
                networkToolsOutput.value = response.data
                sourceIpOutput.value = response.data.source_ping
                destinationIpOutput.value = response.data.destination_ping
                portOutput.value = response.data.telnet
            }).catch(error => {
                console.log(error);
            })


        } else {
            console.log('表单验证失败');
            return false;
        }
    });
};

const onSubmit = () => {
    console.log(shellCommandForm.value);
    axios.post('/api/config/script/shell/', shellCommandForm.value).then(response => {
        console.log(response.data);
        shellCommandOutput.value = response.data

    }).catch(error => {
        console.log(error);
    })
};
</script>

<style scoped>

.grid-content-tools {
    padding: 20px;
    border-radius: 2px;
    box-shadow: 0 0 10px rgba(255, 255, 255, 0.66);
    margin: 10px;

}

.grid-content {
    padding: 20px;
    border-radius: 1px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.32);
    margin: 10px
}

.feedback {
    margin-top: 2px;
    color: #8bb9fe;
}

.form-item {
    margin-bottom: 12px;
}

.form-label {
    display: block;
    text-align: left;
    font-size: 13px;
    margin-bottom: 2px;
}

pre {
    background-color: #f4f4f4;
    border: 1px solid #ddd;
    padding: 10px;
    border-radius: 4px;
    overflow-x: auto;
}

.custom-textarea .el-textarea__inner {
    font-size: 26px; /* 设置字体大小 */
}
</style>