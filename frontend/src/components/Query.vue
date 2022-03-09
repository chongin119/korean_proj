<template>
  <v-container fluid>
    <v-layout row wrap>
      <Heading :title="$t('about.TITLE')" />
      <Description :description="$t('about.DESCRIPTION')" />
    </v-layout>

    <div>
      <code>query: {{ query }}</code>
      <datatable v-bind="$data" />
    </div>
  </v-container>
</template>

<script>
export default {
  metaInfo() {
    return {
      title: this.$store.getters.appTitle,
      titleTemplate: `${this.$t('about.TITLE')} - %s`
    }
  },
  data: () => ({
    columns: [
      { title: 'User ID', field: 'uid', sortable: true },
      { title: 'Username', field: 'name' },
      { title: 'Age', field: 'age', sortable: true },
      { title: 'Email', field: 'email' },
      { title: 'Country', field: 'country' }
    ],
    data: [],
    total: 0,
    query: {}
  }),
  watch: {
    /* query: {
      handler (query) {
        mockData(query).then(({ rows, total }) => {
          this.data = rows
          this.total = total
        })
      },
      deep: true
    } */
  }
}
</script>
