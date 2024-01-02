<template>
  <div class="container-fluid px-5">
    <div class="d-flex justify-content-between align-tasks-center py-3">
      <div>
        <h3>Task Management Platform</h3>
      </div>
      <div>
        <button class="btn btn-outline-primary" @click="changeModalStatus">
          Create New Task
        </button>

        <TaskModal :visible="modalVisible" @update:visible="changeModalStatus"/>
      </div>
    </div>

    <div class="row">
      <TaskContainer :tasks="tasks" title="OPEN"/>
      <TaskContainer :tasks="tasks" title="TESTING"/>
      <TaskContainer :tasks="tasks" title="DONE"/>

    </div>
  </div>
</template>

<script>
import TaskContainer from './TaskContainer.vue';
import TaskModal from './TaskModal.vue';

export default {
  components:{
    TaskModal,
    TaskContainer
},
    data() {
        return {
            tasks: [
                { id: "1", title: 'Card 1', description: 'Description 1' },
                { id: "2", title: 'Card 2', description: 'Description 2' },
                { id: "3", title: 'Card 3', description: 'Description 3' },
            ],
            modalVisible: false,
            newTask: { title: "", description: "", status: "open" }
        };
    },
    methods: {
        changeModalStatus() {
            this.modalVisible = !this.modalVisible;
        }
    },
};
</script>

<style></style>
