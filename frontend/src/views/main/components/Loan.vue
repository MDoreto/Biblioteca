<template>
  <v-card class="ma-6 pa-4">
    <v-data-table
      :headers="headers"
      :items="filteredItems"
      :search="search"
      :item-class="itemClass"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Empréstimos</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider
          ><v-spacer></v-spacer>
          <v-row align="center">
            <v-col cols="3">
              <v-select
                :items="['Vigente', 'Concluído', '']"
                label="Prazo"
                class="pt-5 mx-6"
                v-model="deadline"
              ></v-select
            ></v-col>
            <v-col cols="3"
              ><v-select
                :items="['Atrasado', 'OK', '']"
                label="Entrega"
                class="pt-5 mx-6"
                v-model="delivery"
              ></v-select
            ></v-col>
            <v-col
              ><v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Busca"
                single-line
                hide-details
                class="mx-6"
              ></v-text-field></v-col
          ></v-row>
        </v-toolbar>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon
          v-if="!item.date_effective"
          color="green dark-2"
          class="mr-2"
          @click="returnItem(item)"
        >
          mdi-check
        </v-icon>
        <v-icon>mdi-at</v-icon
        ><v-icon @click="openWhats(item.user.phone)">mdi-whatsapp</v-icon>
      </template>
      <template v-slot:[`item.date_effective`]="{ item }">
        {{ new Date(item.date_effective).toLocaleDateString("pt-BR") }}
      </template>
      <template v-slot:[`item.date_return`]="{ item }">
        {{ new Date(item.date_return).toLocaleDateString("pt-BR") }}
      </template>
      <template v-slot:[`item.date_loan`]="{ item }">
        {{ new Date(item.date_loan).toLocaleDateString("pt-BR") }}
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
import { apiService } from "@/api";
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
    deadline: "",
    delivery: "",
    editedItem: {},
    obs: "",
    headers: [
      { text: "Título", value: "copy.book.title", align: "center" },
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
  computed: {
    filteredItems() {
      var temp = this.items;
      if (this.deadline == "Vigente")
        temp = temp.filter((o) => !o.date_effective);
      if (this.deadline == "Concluído")
        temp = temp.filter((o) => o.date_effective);
      if (this.delivery == "Atrasado")
        temp = temp.filter((o) => {
          let date = o.date_effective ? o.date_effective : new Date();
          return (
            new Date(o.date_return).toLocaleDateString("pt-BR") <
            new Date(date).toLocaleDateString("pt-BR")
          );
        });
      if (this.delivery == "OK")
        temp = temp.filter((o) => {
          let date = o.date_effective ? o.date_effective : new Date();
          return (
            new Date(o.date_return).toLocaleDateString("pt-BR") >=
            new Date(date).toLocaleDateString("pt-BR")
          );
        });
      return temp;
    },
  },

  created() {
    this.initialize();
  },

  methods: {
    initialize() {
      apiService()
        .get(process.env.VUE_APP_ROOT_API + "loans")
        .then((response) => (this.items = response.data));
    },

    returnItem(item) {
      this.editedItem = JSON.parse(JSON.stringify(item));
      this.dialogReturn = true;
    },

    async returnItemConfirm() {
      await apiService().patch(
        process.env.VUE_APP_ROOT_API + "loans",
        this.editedItem
      );
      this.close();
    },

    close() {
      this.dialogReturn = false;
      this.initialize();
    },
    openWhats(phone) {
      window.open(`https://api.whatsapp.com/send?phone=${phone}`, "_blank");
    },
    itemClass(item) {
      if (!item.date_effective) {
        if (
          new Date().toLocaleDateString("pt-BR") ==
          new Date(item.date_return).toLocaleDateString("pt-BR")
        )
          return "orange lighten-4";
        if (new Date() > new Date(item.date_return)) return "red lighten-4";
      } else {
        if (
          new Date(item.date_return).toLocaleDateString("pt-BR") >=
          new Date(item.date_effective).toLocaleDateString("pt-BR")
        )
          return "green lighten-4";
        else return "red lighten-4";
      }
    },
  },
};
</script>
