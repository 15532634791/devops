<template>

    <ul>
        <li>
            {{ this.age }}
        </li>
        <li>  {{ this.level }} </li>
        <li> {{this.user_account}} </li>
        <li> {{this.user_nickname}} </li>
        <li> {{this.user_age}} </li>
        <li> {{this.user_level}} </li>


        <button @click="this.user_age += 1">点击增加</button>


    </ul>




</template>

<script>
import {Message} from "@element-plus/icons-vue";
import axios from 'axios';
import {mapState, mapWritableState} from "pinia";
import {useUserStore} from "@/store/useUserStore";
export default {
    name: 'MyComponent',
    components: {Message},
    data() {
        return {
            showOverlay: false,

        }
    },
    created() {},
    computed: {
        ...mapState(useUserStore, ["age", "level"]),
        ...mapState(useUserStore, {
            user_account: 'account',
            user_nickname: 'nickname'
        }),
        ...mapWritableState(useUserStore, {
            user_age: 'age',
            user_level: 'level'
        })
    },
    methods: {}

}
</script>

