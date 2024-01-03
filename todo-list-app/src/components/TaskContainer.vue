<template>
  <div class="col-md-4">
    <div class="card mb-4">
      <div class="card-body">
        <h5 class="card-title">{{ title }}</h5>
        <div v-for="(task,key) in tasks" :key="key">
          <TaskCard
            :task="task"
            :card-name="cardName"
            :id="key"
            @fetch-task="fetchTask(key)"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TaskCard from './TaskCard.vue';

export default {
  components:{
    TaskCard
},
props:{
  title:String,
  tasks: Object,
  cardName: String,
},
methods:{
  fetchTask(index) {
    this.$emit('fetch-task', index);
  }
}
};
</script>

<style></style>
