const FixityStorage = artifacts.require("FixityStorage");

module.exports = function(deployer){
    deployer.deploy(FixityStorage);
};