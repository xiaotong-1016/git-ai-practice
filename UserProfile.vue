<!-- 【v2.0 优化版】前端组件：新增 bio 签名与输入字数限制 -->
<template>
  <div class="user-card">
    <h2>个人中心 (v2.0 优化版)</h2>
    <div v-if="loading">加载中...</div>
    <div v-else>
      <p>用户ID: {{ user.id }}</p>
      <p>邮箱: {{ user.email }}</p>
      
      <!-- 优化1：增加昵称限制 -->
      <label>昵称：</label>
      <input v-model="editName" :disabled="!isEditing" maxlength="10" placeholder="2-10字" />
      
      <!-- 优化2：新增签名 bio -->
      <label>签名：</label>
      <textarea v-model="editBio" :disabled="!isEditing" maxlength="50" placeholder="个人签名" />

      <button v-if="!isEditing" @click="isEditing = true">编辑</button>
      <button v-else @click="saveProfile">保存</button>
    </div>
  </div>
</template>
