<template>
  <div>
    <v-btn
      color="secondary"
      dark
      class="mb-2"
      @click="$emit('update:dialog', true)"
    >
      Novo {{ title }}
    </v-btn>
    <v-dialog @click:outside="close" :value="dialog" max-width="800px">
      <v-card>
        <v-card-title>
          <span class="text-h5">{{ formTitle }}</span>
        </v-card-title>

        <v-card-text>
          <v-container>
            <v-row>
              <v-col
                cols="12"
                sm="6"
                md="4"
                v-for="h in idx >= 0
                  ? headers.filter((o) => !o.static && !o.primary)
                  : headers.filter((o) => !o.static && !o.default)"
                :key="h.value"
              >
                <v-select
                  v-if="h.type"
                  :items="h.type"
                  :label="h.text"
                  v-model="item[h.value]"
                ></v-select>

                <v-text-field
                  v-else-if="h.value == 'phone'"
                  :label="h.text"
                  v-model="item[h.value]"
                  v-mask="'+## (##) #####-####'"
                ></v-text-field>
                <v-text-field
                  v-else-if="h.value == 'cpf'"
                  :label="h.text"
                  v-model="item[h.value]"
                  v-mask="'###.###.###-##'"
                ></v-text-field
                ><v-text-field
                  v-else-if="h.value == 'email'"
                  v-model="item[h.value]"
                  :rules="emailRules"
                  :label="h.text"
                  required
                ></v-text-field>
                <v-combobox
                  v-else-if="h.value == 'category'"
                  v-model="item[h.value]"
                  :items="categorys"
                  :label="h.text"
                ></v-combobox>
                <v-text-field
                  v-else
                  :label="h.text"
                  v-model="item[h.value]"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="close"> Cancelar </v-btn>
          <v-btn color="blue darken-1" text @click="save"> Salvar </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
import { apiService } from "@/api";
export default {
  props: {
    item: { type: Object, required: true },
    headers: { type: Array, required: true },
    idx: { required: true },
    dialog: { type: Boolean, required: true },
    title: {
      type: String,
      required: true,
    },
    endpoint: {
      type: String,
      required: true,
    },
  },
  data: () => ({
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
    categorys: [],
  }),
  computed: {
    formTitle() {
      return (this.idx < 0 ? "Novo " : "Editar ") + this.title;
    },
  },
  methods: {
    getCategorys() {
      apiService()
        .get("categorys")
        .then((response) => {
          console.log(response);
          this.categorys = response.data;
        });
    },
    close() {
      this.$emit("update:dialog", false);
    },
    async save() {
      if (this.idx > -1) {
        delete this.item.copys;
        delete this.item.book_id;
        delete this.item.status;
        await apiService().put(this.endpoint, this.item);
      } else {
        await apiService().post(this.endpoint, this.item);
      }
      this.close();
      this.$emit("save");
    },
  },
  created() {
    this.getCategorys();
  },
};
</script>