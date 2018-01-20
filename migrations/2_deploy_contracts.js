var Manuscript = artifacts.require("./Manuscript.sol");

module.exports = function(deployer) {
  deployer.deploy(Manuscript);
};
