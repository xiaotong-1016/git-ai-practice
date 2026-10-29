<!-- 【v1.0 初始版本】前端组件 -->
<template>
  <div class="user-card">
    <h2>个人中心 (v1.0)</h2>
    <div v-if="loading">加载中...</div>
    <div v-else>
      <p>用户ID: {{ user.id }}</p>
      <p>邮箱: {{ user.email }}</p>
      <input v-model="editName" :disabled="!isEditing" />
      <button v-if="!isEditing" @click="isEditing = true">编辑</button>
      <button v-else @click="saveProfile">保存</button>
    </div>
  </div>
</template>
