<template>
    <div>
        <AppHeader />
            <v-container grid-list-md text-xs-center>
                <v-layout row wrap>
                    <v-flex xs12>
                        <v-card color="white">
                            <v-card-text>Kasutusjuhendid siin</v-card-text>
                        </v-card>
                    </v-flex>
                </v-layout>
            </v-container>
        <AppFooter />
    </div>
</template>

<script>
import AppHeader from '../components/layout/AppHeader'
import AppFooter from '../components/layout/AppFooter'

export default {
    components: {
        AppHeader,
        AppFooter
    }
}
</script>

<style>
</style>
