# How to contribute

We're really glad that you are reading this and are considering helping us create an open science platform.

Please direct any inquires to arxain@protonmail.com

Our inspiration comes from the [arXiv](http://arxiv.org). This is a pre-print server for Astronomy, Physics, Mathematics, and Engineering maintained by Cornell University. A quick look at the [functionality and architecture](https://arxiv.org/help/general) provides a great introduction to what we are trying to build, but in a decentralized manner.


Here are some important resources for what arXain runs on:

  * [InterPlanetaryFileSystem](https://ipfs.io) our file sharing protocol
  * [Ethereum](https://www.ethereum.org/) our block chain for public tracking
  * [Vue.js](https://vuejs.org/) our chosen web framework for the browser UI
  * [MetaMask](https://metamask.io/) the bridge between the browser and Ethereum
  * [Python3](https://www.python.org/) our middleware for managing manuscripts and comments published on IPFS.

## Testing

Please submit tests for any new features added. No tests means no merge. We use TravisCI to run a set of tests designed to maintain the core functionality of arXain.

## Proposing major changes

Currently, we submit major changes as issues that a developer can work on. Please submit any proposed change, along with a SMART summary at [GitHub New Issue](https://github.com/david-hopper/arXain/issues/new).

Overview of SMART
* __Specific__ - The task isn’t just “build an upload page” but something like “write a page that has a button to create an empty contract on the block chain, then a field to drag and drop a pdf into, which will upload the pdf to IPFS, and then once the file is uploaded, automatically initialize the contract with the IPFS hash”.
* __Measurable__ - There is a real threshold where the task moves from “in Progress” to “Complete”. E.g. Once the page successfully executes the three steps: creates the contract, uploads the pdf to IPFS, and initializes the contract with the IPFS hash, the task is done and will be closed”
* __Actionable__ - Is the task possible to complete? Do you have all the resources you need to finish the task? Or does something else need to built first? E.g. Maybe loading things to IPFS from the webpage is a big task in itself, and should be made into its own task with its own “SMART” list.
* __Relevant__ - Is the task relevant to the over-all goals? E.g. Yes, to build a journal you will need a way to submit articles to it.
* __Time-Bound__ - Give a real time in which you expect the task to be complete. 3 days. 1 week. 1 month. If you miss the deadline, reevaluate the task and possibly break it up into smaller tasks. E.g. The IPFS file upload may very well be a week or two of work in itself. Based on this break down, it may make sense to make the IPFS upload task a separate task with its own issue, and just work on creating the smart contract and initializing it, which may only take a few days.

## Submitting changes

 If you have resolved an issue, implemented a feature addition, or updated any documentation, please submit your branch for an [arXain Pull Request](http://github.com/david-hopper/arXain/pull/new/master) with a clear list of what you've done (read more about [pull requests](http://help.github.com/pull-requests/)). Please follow our coding conventions (below) and make sure all of your commits are atomic (one feature per commit).

Code organization:

- UI edits goes in Vue components in `src/components`, while UX edits go in `app_*.js` files in `src/js`.

- all pyXain functionality should be contained in `node_client/pyXain/pyXain/pyXain.py` and subsequently incorporated into the flask node `node_client/node/node/node.py`

Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:

    $ git commit -m "A brief summary of the commit
    >
    > A paragraph describing what changed and its impact."

## Coding conventions

Start reading our code and you'll get the hang of it. We optimize for readability:

  * This is open source software. Consider the people who will read your code, and make it look nice for them. It's sort of like driving a car: Perhaps you love doing donuts when you're alone, but with passengers the goal is to make the ride as smooth as possible.
  * Document and comment all functions and chunks of code to improve readability, and ease the review of the merge request.

Thanks,

The arXain dev team
