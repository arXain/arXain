var Paper = artifacts.require("./Paper.sol");
var Comments = artifacts.require("./Comments.sol");

module.exports = function(deployer) {
  deployer.deploy(Paper);
  deployer.deploy(Comments, 0x0);
};
