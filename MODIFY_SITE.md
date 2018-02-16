## How to modify the website

- `main.html` is where all the magic happens. It load Web3Box, which is the central controller for find, loading, and manipulating ethereum contracts. 
- Web3box finds the MetaMask instance (or any other web3 instance the user is running) and hands it to the contracts to use. It also holds the navbar, the page header, and loads contracts from TruffleContract.
    - LoadContracts vue takes the JSON of your contracts from `build/contracts` and puts them into an easy to use TruffleContract. It also passes the web3 instance from Web3Box to each of the specific contract components.
    - submitContract.vue, statusContract.vue, amendContract.vue, and commentsContract.vue are components that interface between the specific contract code and the user.

- Each Contract component has a `<script>` tag that loads the javascript which does all the heavy lifting. It also has a `<template>` tag that describes how the page looks like in html. All the components are located in `src/components`. 

Here is a picture of the site outline so far:

![flow look](simple_flow.jpg)
