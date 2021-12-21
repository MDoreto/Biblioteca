<template>
  <v-card class="ma-6 pa-4">
    <v-data-table :headers="headers" :items="items" :search="search" class="">
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Usuários</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider
          ><v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Busca"
            single-line
            hide-details
            class="mx-12"
          ></v-text-field>
          <Edit
            :dialog.sync="dialog"
            :item="editedItem"
            :idx.sync="editedIndex"
            :headers="headers"
            title="Usuário"
            endpoint="users"
            @save="initialize"
          />
        </v-toolbar>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small class="mr-2" @click="edit(item)"> mdi-pencil </v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize"> Reset </v-btn>
      </template>
    </v-data-table>
  </v-card>
</template>
<script>
import axios from "axios";
export default {
  components: {
    Edit: () => import("@/components/Edit.vue"),
  },
  watch: {
    editedIndex(value) {
      console.log(value);
    },
  },
  data: () => ({
    dialog: false,
    headers: [
      {
        text: "Nome",
        align: "center",
        value: "name",
      },
      { text: "Telefone", value: "phone" },
      { text: "Email", value: "email" },
      { text: "CPF", value: "cpf", primary: true },
      {
        text: "Actions",
        value: "actions",
        sortable: false,
        static: true,
        align: "center",
      },
    ],
    items: [],
    search: "",
    editedIndex: -1,
    editedItem: {},
  }),
  watch: {
    dialog(value) {
      if (value == false) this.editedItem = {};
    },
  },

  created() {
    this.initialize();
  },

  methods: {
    initialize() {
      axios
        .get(process.env.VUE_APP_ROOT_API + "users")
        .then((response) => (this.items = response.data));
    },

    edit(item) {
      this.editedIndex = this.items.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },
  },
};
</script>
