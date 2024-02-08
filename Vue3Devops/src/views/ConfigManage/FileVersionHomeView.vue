<template>
  <div style="width: 100%; height: 100%">
    <iframe :src="iframeUrl" width="100%" height="100%"></iframe>
  </div>
</template>

<script>
export default {
  data() {
    return {
      iframeUrl: 'https://aibox.cool/' // 设置要嵌套的网页 URL
    }
  }
}
</script>