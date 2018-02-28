<p align="center">
  <img src="https://github.com/david-hopper/arXain/blob/master/src/images/logo_name.png" alt="arXain" /></center>
</p>

Welcome to the arXain, an open source academic journal wich combines a distributed index and a distributed file network to completely decentralize the process. This allows us to replicate many of the features that traditional academic journals and pre-print servers provide, but in an open-source, decentralized fashion. Instead of centralized journals storing and hosting all academic manuscripts, the users of arXain will store, backup, and host their own manuscripts. This strategy has the benefits of reduced bandwidth, reduced hosting fees, and decreased submit to "public" time. The use of blockchain allows us to autonomously implement the peer review process. No longer are reviews shuttled between a third party and the authors and reviewers, as the blockchain mantains a public history of these exchanges. We hope that arXain will allow scientists to focus on what they do best, science.

## Getting started

### Requirements

Below are the requirements for running the development version of arXain. You may choose to use other tools where applicable, but we do not support them. Feel free to test and submit a pull request if any changes need to be made to accommodate these alternative tools.

* OSX/Linux (Windows not officially supported yet)
* [go-ipfs v0.4.13](https://dist.ipfs.io/#go-ipfs)
* [node.js](https://nodejs.org/en/)
* [npm](https://www.npmjs.com/)
* [MetaMask](https://metamask.io/)
* [Python3](https://www.python.org/), a few of us use [Anaconda](https://www.anaconda.com/download/) to manage packages

### Development Setup

There are a few components that need to be running in order for an arXain development session to function properly. They are briefly outlined below.

#### IPFS Node

- After installing go-ipfs, initialize and run the daemon in a terminal session.
```
> ipfs init
> ipfs daemon
```
- Valid IPFS hashes on the IPFS network can be view by directing a browser to `http://localhost:8080/ipfs/<hash>`

#### arXain local client

- Follow the installation and run instructions in [arXain/node_client/SETUP.md](https://github.com/david-hopper/arXain/blob/master/node_client/SETUP.md)

#### Website

- `$ npm install`
    - Installs all the packages you need to run, including webpack. See a list of what will be installed in `package.json`.
- `$ npm run build`
    - Builds the webpack bundle of all the javascript. Configuration for building in `webpack.config.js`. All you need to do is include `dist/build.js` in any html file.
- Establish the default connection to a blockchain by editing `truffle.js` to point to where your testRPC is running.
- `$ npm install -g truffle`
    - You may need to use sudo to install it.
- `$ npm install -g ganache-cli` and then simply `$ ganache-cli` to run it.
    - This is to run a blockchain locally for testing.
    - The default port it runs on is 8545.
- `$ truffle compile && truffle migrate`
    - This will compile the contracts written in solidity into a form such that they interact with javascript. `truffle migrate` then migrates your contract to the blockchain.
- `$ npm run dev`
    - Launches the dev server on port 4000.
- View the website at http://127.0.0.1:4000

## Running Tests

All submitted code should be tesed. Testing frameworks are still under construction.

## Contributing

See our [CONTRIBUTING.md](CONTRIBUTING.md) for a more detailed example of how to contribute to arXain.

## Authors

arXain was founded and is maintained by four Physics PhD students from the University of Pennsylvania.

- Bijan Haney
- David Hopper
- Saul Kohn
- Khilesh Mistry

## License

arXain is distributed under a "insert license" and can be found in the LICENSE.md file

## Acknowledgements

This project would not be possible without the huge amount of work done on Ethereum and IPFS.

## News

- Won "Best Blockchain Hack" and "Most Promising Hack" at [PennApps 2018](https://devpost.com/software/arxain)
