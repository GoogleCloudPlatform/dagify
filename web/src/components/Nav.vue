<template>
    <div class="fixed flex items-center top-0 left-0 w-full bg-gray-800 text-white justify-between h-16">
        <span class="pl-4">Logo</span>
        <nav class="flex space-x-4">
            <router-link to="/">
                Home
            </router-link>
            <router-link to="/about">
                About
            </router-link>
            <router-link to="/faq">
                FAQ
            </router-link>
            <router-link to="/contact">
                Contact
            </router-link>
        </nav>
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-md focus:outline-none mr-4">Start Converting</button>
    </div>
</template>