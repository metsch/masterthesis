const FixityStorage = artifacts.require("FixityStorage");

/*
 * uncomment accounts to access the test accounts made available by the
 * Ethereum client
 * See docs: https://www.trufflesuite.com/docs/truffle/testing/writing-tests-in-javascript
 */
contract("FixityStorage", function (/* accounts */) {
  it("should assert true", async function () {
    await FixityStorage.deployed();
    return assert.isTrue(true);
  });
});
