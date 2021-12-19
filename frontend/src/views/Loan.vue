<template>
  <v-card class="ma-6 pa-4">
    <v-data-table :headers="headers" :items="items" :search="search" class="">
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Empréstimos</v-toolbar-title>
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
        </v-toolbar>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon  v-if="!item.date_effective" color="green dark-2" class="mr-2" @click="returnItem(item)">
          mdi-check
        </v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize"> Reset </v-btn>
      </template>
    </v-data-table>
    <v-dialog v-model="dialogReturn" max-width="500px">
      <v-card>
        <p class="text-h5 text-center pt-4 font-weight-bold">
          Confirmar devolução deste livro?
        </p>
        <v-card-text>
          <v-textarea
            class="px-12"
            label="Observações"
            v-model="editedItem.obs"
            height="100"
          ></v-textarea
        ></v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="returnItemConfirm"
            >OK</v-btn
          >
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
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
    dialogReturn: false,
    editedItem: {},
    obs: "",
    headers: [
      {
        text: "ID",
        align: "center",
        value: "id",
      },
      { text: "Título", value: "copy.book.title" },
      { text: "Exemplar", value: "copy.book.id" },
      { text: "Usuário", value: "user.name" },
      { text: "CPF", value: "user.cpf" },
      { text: "Retirada", value: "date_loan" },
      { text: "Prazo", value: "date_return" },
      { text: "Devolução", value: "date_effective" },
      { text: "Obs", value: "obs" },
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
  }),
  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  created() {
    this.initialize();
  },

  methods: {
    initialize() {
      axios
        .get(process.env.VUE_APP_ROOT_API + "loans")
        .then((response) => (this.items = response.data));
    },

    returnItem(item) {
      this.editedItem = JSON.parse(JSON.stringify(item));
      this.dialogReturn = true;
    },

    returnItemConfirm() {
      axios.patch(process.env.VUE_APP_ROOT_API + "loans", this.editedItem);
      this.close();
    },

    close() {
      this.dialogReturn = false;
    },
  },
};
</script>
