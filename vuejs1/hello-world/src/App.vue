<template>
  <div id="app">
    <div class="col-md-6 mx-auto text-center">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/login">Login</router-link>
      <button v-if="isLoggedIn" class="btn btn-danger" @click="logout">Logout</button>
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      isLoggedIn: false
    };
  },
  created() {
    if (localStorage.getItem('token')) {
      this.isLoggedIn = true;
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('token');
      this.isLoggedIn = false;
      // Use router push to navigate to the login page
      this.$router.push('/login');
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #2c3e50;
  margin-top: 60px;
}

nav {
  padding: 20px;
  background-color: #f8f9fa;
  border-bottom: 1px solid #ccc;
}

router-link {
  margin-right: 10px;
  text-decoration: none;
  color: #2c3e50;
  font-weight: bold;
}
</style>
