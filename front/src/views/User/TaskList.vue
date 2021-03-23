<template>
  <div class="task-list">
    <div class="task" v-for="task in taskList" :key="task.id_task">
      {{ task.name_task }}
      {{ task.description_task }}
    </div>
  </div>
</template>

<script>
import api from "@/services/api";

export default {
  name: "TaskList",
  data() {
    return {
      taskList: [],
    };
  },
  methods: {
    async getAllTasks() {
      this.taskList = await api.getAllTasks();
      console.log(this.taskList);
    },
  },
  async created() {
    await this.getAllTasks();
  },
};
</script>

<style></style>
