<template>
  <v-app>
    <v-navigation-drawer
      permanent
      expand-on-hover
      :mini-variant.sync="mini"
      app
      dark
      color="yellow darken-4"
    >
      <v-list>
        <v-list-item link>
          <v-list-item-content>
            <v-list-item-title class="title"> Administrator </v-list-item-title>
            <v-list-item-subtitle>teste</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list nav dense>
        <router-link style="text-decoration: none" :to="{ name: 'Book' }">
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-book</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Livros</v-list-item-title>
          </v-list-item>
        </router-link><router-link style="text-decoration: none" :to="{ name: 'User' }">
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Usuários</v-list-item-title>
          </v-list-item>
        </router-link><router-link style="text-decoration: none" :to="{ name: 'Loan' }">
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-clipboard-text-clock-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Emprestimos</v-list-item-title>
          </v-list-item>
        </router-link></v-list
      ></v-navigation-drawer
    ><v-app-bar app hide-on-scroll short>
      <span class="display-1" style="white-space: pre"
        >BIBLIOTECA</span
      > </v-app-bar
    ><v-main class="blue-grey lighten-4">
      <transition name="fade"> <router-view></router-view></transition> </v-main
  ></v-app>
</template>
<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition-property: opacity;
  transition-duration: 0.45s;
}
.fade-enter-active {
  transition-delay: 0.25s;
}
.fade-enter,
.fade-leave-active {
  opacity: 0;
}
</style>
<script>
export default {
  name: "App",

  data: () => ({
    mini: true,
  }),
};
</script>
