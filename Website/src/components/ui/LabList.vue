<template>
    <div>
        <v-flex xs12 sm6 offset-sm3>
            <v-card>
                <v-toolbar>
                    <v-toolbar-title>Laborid</v-toolbar-title>
                </v-toolbar>
                <v-progress-linear v-if='labs.length == 0' :indeterminate="true" height="2"></v-progress-linear>
                <v-list two-line>
                    <template v-for="(item) in labs">
                        <v-list-tile :key="item.id">
                            <v-list-tile-content>
                                <v-list-tile-title v-text="item.name"></v-list-tile-title>
                                <v-list-tile-sub-title v-text="item.description"></v-list-tile-sub-title>
                            </v-list-tile-content>
                            <v-btn v-if="item.taken === true" :class="{'disable-events': item.taken === true}" color="error">Hõivatud</v-btn>
                            <v-btn v-else color="success">Alusta</v-btn>
                        </v-list-tile>
                    </template>
                </v-list>
            </v-card>
        </v-flex>
    </div>
</template>

<script>
export default {
    computed: {
        labs() {
            return this.$store.getters.getLabs
        }
    },
    created() {
        this.$store.dispatch('fetchLabs')
    }
}
</script>

<style>
.disable-events {
  pointer-events: none
}
</style>
