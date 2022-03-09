<template>
  <div id="app" class="container">
    <b-row class="mb-3">
      <b-col md="3">
        <b-form-input v-model="filter" type="search" id="filterInput" placeholder="Type to Search"></b-form-input>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-table
          striped
          hover
          outlined
          :per-page="perPage"
          :items="posts"
          :current-page="currentPage"
          :filter="filter"
        >
        </b-table>
        <b-pagination
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="my-table"
        ></b-pagination>
      </b-col>
    </b-row>
  </div>

</template>

<script>
export default {
  metaInfo() {
    return {
      title: this.$store.getters.appTitle,
      titleTemplate: `${this.$t('about.TITLE')} - %s`
    }
  },
  name: "App",
  data() {
    return {
      filter: "",
      perPage: 1,
      currentPage: 1,
      posts:[],
      /* posts: [
        {
          userId: 1,
          id: 1,
          title:
            "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        },
        {
          userId: 1,
          id: 2,
          title: "qui est esse",
        },
        {
          userId: 1,
          id: 3,
          title: "ea molestias quasi exercitationem repellat qui ipsa sit aut",
        },
      ],*/
    }
  },
  mounted() {
    this.axios.get('http://localhost:3000/resulting').then(res => {
      console.log(res)
        this.posts = res.data
    })

  },
  computed: {
    rows() {
      return this.posts.length
    },
  }
}

</script>

<style>
#app {
  width: 95%;
  margin-top: 50px; 
}


.VuePagination {
  text-align: center;
}
