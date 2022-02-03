<template>
  <v-data-table
    class="ma-7 elevation-3 pa-2"
    :headers="header.filter((o) => !o.hide)"
    :items="book.copys"
    disable-pagination
    hide-default-footer
    ><template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Exemplares</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider
        ><v-spacer></v-spacer>
        <Edit
          :dialog.sync="dialog"
          :item="getCopy(editedItem)"
          :idx.sync="editedIndex"
          :headers="header.filter((o) => !o.static)"
          title="Exemplar"
          endpoint="copys"
          @save="initialize"
        />
        <Loan v-if="loanDialog" :dialog.sync="loanDialog" :item="editedItem" @save="initialize" />
      </v-toolbar> </template
    ><template v-slot:[`item.actions`]="{ item }">
      <v-icon small class="mr-2" @click="edit(item)"> mdi-pencil </v-icon>
      <v-icon v-if="item.status == 'Disponível'" small @click="loan(item)">
        mdi-share
      </v-icon> </template
    ><template v-slot:[`item.status`]="{ item }">
      <v-chip :color="$colorStatus[item.status]" dark>
        {{ item.status }}
      </v-chip>
    </template>
  </v-data-table>
</template>
<script>
export default {
  components: {
    Loan: () => import("@/components/Loan.vue"),
    Edit: () => import("@/components/Edit.vue"),
  },
  props: {
    book: { type: Object, required: true },
  },
  watch: {
    dialog(value) {
      if (value == false) this.editedItem = {};
    },
  },
  data: () => ({
    editedIndex: -1,
    loanDialog: false,
    editedItem: {},
    dialog: false,
    header: [
      { text: "Número", value: "id", static: true },
      {
        text: "Estoque",
        value: "stock",
        type: ["Disponível", "Removido"],
        default: true,
        hide: true,
      },
      { text: "Status", value: "status", static: true },
      { text: "Actions", value: "actions", static: true },
    ],
  }),
  methods: {
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
    loan(item) {
      this.editedItem = item;
      this.loanDialog = true;
    },
    getCopy(i) {
      i.book_id = this.book.id;
      return i;
    },
    initialize() {
      this.$emit("save");
    },
  },
};
</script>