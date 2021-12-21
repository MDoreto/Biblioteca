<template>
  <v-dialog @click:outside="close" :value="dialog" max-width="800px">
    <v-card>
      <v-card-title>
        <span class="text-h5">Empréstimo</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12" sm="6" md="4">
              <v-text-field
                label="Título"
                v-model="book.title"
                disabled
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field
                label="Autor"
                v-model="book.author_1"
                disabled
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field
                label="Exemplar"
                v-model="book.id"
                disabled
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" sm="6" md="4">
              <v-autocomplete
                v-model="search"
                :items="users"
                item-text="cpf"
                label="CPF"
                placeholder="Busque usuário pelo CPF"
              ></v-autocomplete
            ></v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field
                label="Nome"
                v-model="user.name"
                disabled
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field
                label="Telefone"
                v-model="user.phone"
                disabled
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field
                label="Email"
                v-model="user.email"
                disabled
              ></v-text-field> </v-col
            ><v-col cols="12" sm="6" md="4"
              ><v-menu
                v-model="dateDialog"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="date"
                    label="Data de Devolução"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="date"
                  @input="dateDialog = false"
                ></v-date-picker> </v-menu
            ></v-col>
          </v-row>
        </v-container>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="close"> Cancel </v-btn>
        <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import axios from "axios";
export default {
  data: () => ({
    users: [],
    search: "",
    date: "",
    dateDialog: false,
    book: {},
  }),
  props: {
    item: { type: Object, required: true },
    dialog: { type: Boolean, required: true },
  },
  computed: {
    user() {
      if (this.search) return this.users.find((o) => o.cpf == this.search);
      return {};
    },
  },
  methods: {
    close() {
      this.$emit("update:dialog", false);
    },
    async save() {
     await axios.post(process.env.VUE_APP_ROOT_API + "loans", {
        user_cpf: this.user.cpf,
        copy_id: this.item.id,
        date_return: this.date,
      });
      this.$emit("save");
      this.close();
    },
  },
  created() {
    axios
      .get(process.env.VUE_APP_ROOT_API + "users")
      .then((response) => (this.users = response.data));
    axios
      .get(process.env.VUE_APP_ROOT_API + "copys/" + this.item.id)
      .then((response) => (this.book = response.data.book));
  },
};
</script>