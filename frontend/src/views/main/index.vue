<template>
  <v-app>
    <v-navigation-drawer
      permanent
      expand-on-hover
      :mini-variant.sync="mini"
      app
      dark
      color="orange accent-2"
    >
      <v-list>
        <v-list-item link>
          <v-list-item-content>
            <v-list-item-title class="title">
              <v-img src="@/assets/logo.png" height="80" contain />
            </v-list-item-title>
            <v-list-item-subtitle class="text-center"
              >Sistema Bibliotecário</v-list-item-subtitle
            >
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
          </v-list-item> </router-link
        ><router-link style="text-decoration: none" :to="{ name: 'User' }">
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Usuários</v-list-item-title>
          </v-list-item> </router-link
        ><router-link style="text-decoration: none" :to="{ name: 'Loan' }">
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-clipboard-text-clock-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Emprestimos</v-list-item-title>
          </v-list-item>
        </router-link></v-list
      >
      <template v-slot:append>
        <div class="pa-1">
          <v-btn block width="50%"
            ><v-icon> mdi-logout </v-icon> <span v-if="!mini">Logout</span>
          </v-btn>
        </div>
      </template></v-navigation-drawer
    ><v-app-bar app hide-on-scroll short>
      <span class="titlebar">BIBLIOTECA</span> </v-app-bar
    ><v-main class="teste blue-grey lighten-1">
      <transition name="fade"> <router-view></router-view></transition> </v-main
  ></v-app>
</template>
<style scoped>
.titlebar {
  font-family: Helvetica, Arial;
  font-size: 32px;
}
.teste {
  background-image: url("../../assets/logo.png");
  background-position: center;
  background-position-y: 2;
  background-size: 25%;
}
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
