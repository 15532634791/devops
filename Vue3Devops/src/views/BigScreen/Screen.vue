<template>

    <div style="width: 99%; margin: 10px;">
        <h4 style="text-align: center;">趋势分析</h4>
        <el-row :gutter="24">
            <el-col :span="24">
                <el-row :gutter="23">
                    <el-col :span="7">
                        <InstallAndMaintainPersonnelSatisfaction/>
                    </el-col>
                    <el-col :span="10">
                        <TopSatisfactionResponseInArea/>
                    </el-col>
                    <el-col :span="7">
                        <ProportionOfDecorationServices />
                    </el-col>
                </el-row>

                <el-row :gutter="24">
                    <el-col :span="12">
                        <AccumulatedDataOfCounty />
                    </el-col>
                    <el-col :span="12">
                        <OverviewOfGridOutboundCalls />
                    </el-col>
                </el-row>
                <el-row :gutter="24">
                    <el-col :span="6">
                        <!--                    <TestView/>-->
                    </el-col>
                    <el-col :span="12">

                    </el-col>
                    <el-col :span="6">

                    </el-col>
                </el-row>
            </el-col>
            <el-col :span="6">
                <el-row :gutter="24">
                    <el-col :span="24">

                    </el-col>
                </el-row>
                <el-row :gutter="24">
                    <el-col :span="24">

                    </el-col>
                </el-row>
            </el-col>
        </el-row>
    </div>

</template>

<script>
// import TestView from "./TestView.vue";
import {defineComponent} from 'vue';
import TopSatisfactionResponseInArea from "@/views/BigScreen/TopSatisfactionResponseInArea.vue";
import InstallAndMaintainPersonnelSatisfaction from "./InstallAndMaintainPersonnelSatisfaction.vue";
import ProportionOfDecorationServices from "@/views/BigScreen/ProportionOfDecorationServices.vue";
// import Acc from "@/views/BigScreen/ProportionOfInternetQuality.vue";
import OverviewOfGridOutboundCalls from "@/views/BigScreen/OverviewOfGridOutboundCalls.vue";
import AccumulatedDataOfCounty from "@/views/BigScreen/AccumulatedDataOfCounty.vue";
export default defineComponent({
    name: "BigScreen",
    components: {
        // 添加组件选项
        TopSatisfactionResponseInArea,
        InstallAndMaintainPersonnelSatisfaction,
        ProportionOfDecorationServices,
        AccumulatedDataOfCounty,
        OverviewOfGridOutboundCalls

    },

});
</script>

<style scoped>
.title {
    height: 48px;
    line-height: 48px;
    font-size: 24px;
    text-align: center;
}

.el-row {
    margin-bottom: 20px;
}

.el-row:last-child {
    margin-bottom: 0;
}

.el-col {
    border-radius: 4px;
}

.grid-content {
    border-radius: 4px;
    height: 275px;
    min-height: 36px;
    background-color: #e6e6ee;
}
</style>