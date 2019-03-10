<template>
    <div>
        <AppHeader />
        <v-container grid-list-md text-xs-center>
            <v-layout row>
                <v-flex xs12>
                    <ResultsList />
                </v-flex>
            </v-layout>
        </v-container>
        <AppFooter />
    </div>
</template>

<script>
import AppHeader from '../components/layout/AppHeader'
import AppFooter from '../components/layout/AppFooter'
import ResultsList from '../components/ui/ResultsList'

export default {
    components: {
        AppHeader,
        AppFooter,
        ResultsList
    }
}
</script>

<style>
</style>
