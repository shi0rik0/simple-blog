<script setup lang="ts">
import {computed, onMounted, onUnmounted, reactive, Ref, ref} from 'vue'

interface Props {
    title: string,
    date: Date,
    link: string
}

const props = defineProps<Props>()

</script>

<template>
  <div class="space-x-10">
   <router-link :to="props.link">{{ props.title }}</router-link>
   <span>{{ props.date.toLocaleDateString() }}</span>
  </div>
</template>

<style scoped>
a {
    color: red
}
</style>
