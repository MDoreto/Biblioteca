<template>
  <v-row justify="center" align="center">
    <v-col cols="3"
      ><v-card class=""
        ><v-row><v-img src="@/assets/logo.png" contain height="100" /></v-row
        ><v-row justify="center" class="display-1 orange--text pt-4"
          >LOGIN</v-row
        ><v-row class="px-12">
          <v-text-field
            v-model="user"
            label="Usuário"
            prepend-icon="mdi-account"
            disabled
            class="input-group--focused"
            @click:append="show = !show"
            width="50%"
          ></v-text-field></v-row
        ><v-row class="px-12">
          <v-text-field
            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show ? 'text' : 'password'"
            prepend-icon="mdi-lock"
            v-model="password"
            label="Senha"
            hint="At least 8 characters"
            class="input-group--focused"
            @click:append="show = !show"
            width="50%"
          ></v-text-field
        ></v-row>
        <v-row class="px-12 pb-6"
          ><v-btn color="orange accent-2" block @click="login"
            >LOGIN</v-btn
          ></v-row
        ></v-card
      ></v-col
    ></v-row
  >
</template>
<script>
import { apiService } from "@/api";
export default {
  data: () => ({
    show: false,
    user: "master",
    password: "12345678",
    rules: {
      required: (value) => !!value || "Required.",
      min: (v) => v.length >= 8 || "Min 8 characters",
    },
  }),
  methods: {
    login() {
      apiService()
        .post("login", {
          user: this.user,
          password: this.password,
        })
        .then(() => {
          this.$store.dispatch("login");
          this.$router.push({ name: "Index" });
        });
    },
  },
};
</script>