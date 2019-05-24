<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div id="navbarTogglerDemo01" class="collapse navbar-collapse">
            <router-link to="/" class="navbar-brand">Kaugjuhtimislabor</router-link>
            <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
                <li class="nav-item">
                    <router-link to="/labs" class="nav-link">Laborid</router-link>
                </li>
                <li class="nav-item">
                    <router-link to="/measurements" class="nav-link">Mõõtmistulemused</router-link>
                </li>
            </ul>
            </div>
        </nav>
    </div>
</template>

<script>
export default {
}
</script>

<style>
</style>
