<script setup lang="ts">

import {onMounted, ref} from "vue";
import {useRoute} from "vue-router";
import {marked} from "marked"

const route = useRoute()
const title = route.params.title
const html = ref("")

onMounted(() => {
    fetch('./articles/' + title + '.md')
     .then(function(response) {
         return response.text()
     })
     .then(function(response) {
         html.value = marked(response)
     })
     .catch(function(error) {
         // 处理请求错误
     });
})
</script>

<template>
    <div v-html="html"></div>
</template>

<style scoped>

</style>
