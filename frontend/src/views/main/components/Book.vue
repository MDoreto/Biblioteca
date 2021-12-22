<template>
  <v-card class="ma-6 pa-4">
    <v-data-table
      :headers="headers.filter((o) => !o.secondary)"
      :items="items"
      :search="search"
      class=""
      :single-expand="true"
      :expanded.sync="expanded"
      @click:row="(item, slot) => slot.expand(!slot.isExpanded)"
      item-key="id"
      multi-sort
      ><template v-slot:expanded-item="{ item }">
        <td :colspan="headers.length">
          <v-row class="nowrap"
            ><v-col cols="6">
              <v-row justify="center"
                ><Copy :book="item" @save="initialize" /></v-row
            ></v-col>
            <v-col cols="6">
              <v-row justify="center" class="ma-5">
                <v-col
                  cols="5"
                  v-for="h in headers.filter((o) => o.secondary)"
                  :key="h.value"
                >
                  <v-text-field
                    :label="h.text"
                    v-model="item[h.value]"
                    readonly
                  ></v-text-field></v-col></v-row></v-col
          ></v-row></td
      ></template>
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Livros</v-toolbar-title>
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
            :headers="headers.filter((o) => !o.static)"
            title="Livro"
            endpoint="books"
            @save="initialize"
          />
        </v-toolbar>
      </template>
      <template v-slot:[`item.status`]="{ item }">
        <v-chip :color="$colorStatus[item.status]" dark>
          {{ item.status }}
        </v-chip>
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
<style>
</style>
<script>
import { apiService } from "@/api";
export default {
  components: {
    Edit: () => import("@/components/Edit.vue"),

    Copy: () => import("@/components/Copy.vue"),
  },
  data: () => ({
    dialog: false,
    expanded: [],
    headers: [
      {
        text: "Título",
        align: "center",
        value: "title",
      },
      { text: "Substituto", value: "substitute" },
      { text: "Autor 1", value: "author_1" },
      { text: "Autor 2", value: "author_2" },
      { text: "Autor 3", value: "author_3" },
      { text: "Editora", value: "publisher" },
      { text: "Edição", value: "edition" },
      { text: "Volume", value: "volume" },

      {
        text: "ID",
        value: "id",
        primary: true,
        secondary: true,
      },
      {
        text: "Área de concentração",
        value: "concentration_area",
        secondary: true,
      },
      { text: "Área específica", value: "specific_area", secondary: true },
      { text: "Localização", value: "location", secondary: true },
      { text: "Status", value: "status", static: true },
      { text: "Actions", value: "actions", sortable: false, static: true },
    ],
    items: [],
    search: "",
    editedIndex: -1,
    editedItem: {},
  }),

  created() {
    this.initialize();
  },
  watch: {
    dialog(value) {
      if (value == false) this.editedItem = {};
    },
  },
  methods: {
    initialize() {
      apiService().get("books").then((response) => {
        this.items = response.data;
        this.items.forEach((item) => (item.status = this.getStatus(item)));
      });
    },
    getStatus(item) {
      if (item.copys.some((o) => o.status == "Disponível")) return "Disponível";
      if (item.copys.some((o) => o.status == "Emprestado")) return "Emprestado";
      return "Removido";
    },
    edit(item) {
      this.editedIndex = 1;
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = {};
        this.editedIndex = -1;
      });
    },
  },
};
</script>