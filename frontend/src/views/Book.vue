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
          <v-row
            ><v-col cols="6">
              <v-row justify="center"
                ><v-data-table
                  class="ma-7 elevation-3 pa-2"
                  :headers="exemplarHeader"
                  :items="item.copys"
                  disable-pagination
                  hide-default-footer
                  ><template v-slot:top>
                    <v-toolbar flat>
                      <v-toolbar-title>Exemplares</v-toolbar-title>
                      <v-divider class="mx-4" inset vertical></v-divider
                      ><v-spacer></v-spacer>
                      <Edit
                        :dialog.sync="copyDialog"
                        :item="getCopy(editedItem, item)"
                        :idx.sync="editedIndex"
                        :headers="exemplarHeader"
                        title="Exemplar"
                        endpoint="copys"
                      />
                    </v-toolbar> </template
                  ><template v-slot:[`item.actions`]="{ item }">
                    <v-icon
                      small
                      class="mr-2"
                      @click="editCopy(item)"
                    >
                      mdi-pencil
                    </v-icon>
                    <v-icon v-if="item.status=='Disponível'" small @click="loan(item)">
                      mdi-share
                    </v-icon> </template
                  ><template v-slot:[`item.status`]="{ item }">
                    <v-chip
                      :color="item.status === 'Disponível' ? 'green' : 'red'"
                      dark
                    >
                      {{ item.status }}
                    </v-chip>
                  </template></v-data-table
                ></v-row
              ></v-col
            >
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
            :dialog.sync="editDialog"
            :item="editedItem"
            :idx.sync="editedIndex"
            :headers="headers"
            title="Livro"
            endpoint="books"
          />
          <Loan v-if="loanDialog" :dialog.sync="loanDialog" :item="editedItem" />
        </v-toolbar>
      </template>
      <template v-slot:[`item.status`]="{ item }">
        <v-chip :color="item.status === 'Disponível' ? 'green' : 'red'" dark>
          {{ item.status }}
        </v-chip>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small class="mr-2" @click="editBook(item)">
          mdi-pencil
        </v-icon>
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
import axios from "axios";
export default {
  components: {
    Edit: () => import("@/components/Edit.vue"),
    Loan: () => import("@/components/Loan.vue"),
  },
  watch: {
    editedIndex(value) {
      console.log(value);
    },
  },
  data: () => ({
    copyDialog: false,
    editDialog: false,
    loanDialog: false,
    dialogDelete: false,
    expanded: [],
    exemplarHeader: [
      { text: "Número", value: "id", primary: true },
      {
        text: "Status",
        value: "status",
        type: ["Disponível", "Removido"],
        default: true,
      },
      { text: "Actions", value: "actions", static: true },
    ],
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
        text: "Número do exemplar",
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

      { text: "Actions", value: "actions", sortable: false, static: true },
    ],
    items: [],
    search: "",
    editedIndex: -1,
    editedItem: {},
    defaultItem: {},
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
        .get(process.env.VUE_APP_ROOT_API + "books")
        .then((response) => (this.items = response.data));
    },

    editBook(item) {
      this.editedIndex = 1;
      this.editedItem = Object.assign({}, item);
      this.editDialog = true;
    },
    editCopy(item) {
      this.editedIndex = 1;
      this.editedItem = Object.assign({}, item);
      this.copyDialog = true;
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },
    loan(item) {
      this.editedItem = item;
      this.loanDialog = true;
    },
    getCopy(i, item) {
      i.book_id = item.id;
      return i;
    },
  },
};
</script>
