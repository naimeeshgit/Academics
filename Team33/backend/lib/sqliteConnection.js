const Database = require("better-sqlite3");
const DB_NAME = "vuln";

module.exports = new Database(`../db/${DB_NAME}.db`, {
  readonly: true,
  verbose: console.log,
});
