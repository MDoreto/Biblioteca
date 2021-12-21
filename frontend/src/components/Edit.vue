<template>
  <v-dialog @click:outside="close" :value="dialog" max-width="800px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="secondary" dark class="mb-2" v-bind="attrs" v-on="on">
        Novo {{ title }}
      </v-btn>
    </template>
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
        <v-btn color="blue darken-1" text @click="close"> Cancel </v-btn>
        <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import axios from "axios";
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
  computed: {
    formTitle() {
      return (this.idx < 0 ? "Novo " : "Editar ") + this.title;
    },
  },
  methods: {
    close() {
      this.$emit("update:dialog", false);
      this.$emit("update:idx", -1);
    },
    async save() {
      if (this.idx > -1) {
        delete this.item.copys;
        delete this.item.book_id;
        delete this.item.status;
        await axios.put(process.env.VUE_APP_ROOT_API + this.endpoint, this.item);
      } else {
        await axios.post(process.env.VUE_APP_ROOT_API + this.endpoint, this.item);
      }
      
      this.close();
    },
  },
};
</script>