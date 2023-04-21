<script setup lang="ts">
import Article from "./Article.vue";
import {onMounted, reactive} from "vue";

interface Article {
    title: string,
    date: Date,
    link: string,
}

const articles = reactive<Article[]>([])

onMounted(() => {
    fetch('./articles/__metadata.json')
        .then(function(response) {
            return response.json();
        })
        .then(function(jsonResponse) {
            for (let i of jsonResponse) {
                articles.push({title: i.title, date: new Date(i.date), link: i.link})
            }
        })
        .catch(function(error) {
            // 处理请求错误
        });
})

</script>

<template>
    <div class="flex flex-col my-10 mx-20 justify-center space-y-10 bg-gray-200">
        <h1>标题</h1>
        <ol reversed>
            <li v-for="i in articles">
                <Article :title="i.title" :date="i.date" :link="i.link"></Article>
            </li>
        </ol>
    </div>
</template>

<style scoped>
ol {
				list-style-type: decimal;
}
</style>
