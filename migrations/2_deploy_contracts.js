var Manuscript = artifacts.require("./Manuscript.sol");
var Mortal = artifacts.require("./Mortal.sol");

module.exports = function(deployer) {
  deployer.deploy(Manuscript);
  deployer.deploy(Mortal);
};
