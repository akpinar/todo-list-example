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

        <TaskModal
          :visible="modalVisible"
          @update:visible="changeModalStatus"
          @update:tasks="getTasks()"
        />
      </div>
    </div>

    <div class="row">
      <TaskContainer
        :tasks="openTasks"
        title="OPEN"
        card-name="testing"
        @fetch-task="getTasks()"
      />
      <TaskContainer
        :tasks="testingTasks"
        title="TESTING"
        card-name="done"
        @fetch-task="getTasks()"
      />
      <TaskContainer 
        :tasks="doneTasks" 
        title="DONE" 
        @fetch-task="getTasks()" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import TaskContainer from './TaskContainer.vue';
import TaskModal from './TaskModal.vue';

export default {
  components:{
    TaskModal,
    TaskContainer
  },
  created() {
      this.getTasks();
  },
  data() {
    return {
        openTasks: {},
        testingTasks: {},
        doneTasks: {},
        modalVisible: false,
    };
  },
  methods: {
    changeModalStatus() {
      this.modalVisible = !this.modalVisible;
    },
    async getTasks(){
      this.getOpenTasks();
      this.getTestingTasks();
      this.getDoneTasks();

    },
    async getOpenTasks() {
      axios
      .get(`http://127.0.0.1:5000/task/search/1`)
      .then((response) => {
        this.openTasks = response.data.data
      })
      .catch((error) => {
        return error;
      });
    },
    async getTestingTasks() {
      axios
      .get(`http://127.0.0.1:5000/task/search/2`)
      .then((response) => {
        this.testingTasks = response.data.data

      })
      .catch((error) => {
        return error;
      });
    },
    async getDoneTasks() {
      axios
      .get(`http://127.0.0.1:5000/task/search/3`)
      .then((response) => {
        this.doneTasks = response.data.data
      })
      .catch((error) => {
        return error;
      });
    },
  },
};
</script>

<style></style>
