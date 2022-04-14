const router = require("express").Router();
const db = require("../lib/sqliteConnection");

/**
 * Lookup on a date API
 * req.body.date in YYYY-MM-DD format
 */
router.post("/ondate", (req, res) => {
  var date = req.body.date;

  try {
    var stmt = db.prepare(
      "SELECT * FROM vulnerability WHERE date(published) = ?"
    );
    const rows = stmt.all(date);
    if (rows.length === 0)
      return res.json([
        { message: `No vulnerabilities found on date ${date}` },
      ]);
    else return res.json(rows);
  } catch (err) {
    return res.sendStatus(500);
  }
});

/**
 * Lookup between two dates API
 * req.body.startDate in YYYY-MM-DD format
 * req.body.endDate in YYYY-MM-DD format
 */
router.post("/betweendate", (req, res) => {
  // console.log(req.body);
  var startDate = req.body.startDate.replace(/(..).(..).(....)/, "$3-$1-$2");
  var endDate = req.body.endDate.replace(/(..).(..).(....)/, "$3-$1-$2");

  console.log(startDate, endDate);

  try {
    var stmt = db.prepare(
      "SELECT * FROM vulnerability WHERE date(published) BETWEEN date(?) AND date(?)"
    );

    const rows = stmt.all(startDate, endDate);
    if (rows.length === 0)
      return res.json([
        {
          message: `No vulnerabilities found between ${startDate} and ${endDate}`,
        },
      ]);
    else return res.json(rows);
  } catch (err) {
    return res.sendStatus(500);
  }
});

/**
 * Lookup based on CVE ID/Number
 */
router.post("/cve", (req, res) => {
  var cveId = req.body.cveId;

  try {
    var stmt = db.prepare("SELECT * FROM vulnerability WHERE cve = ?");

    const rows = stmt.all(cveId);
    if (rows.length === 0)
      return res.json([
        {
          message: `No vulnerability found with CVE ID ${cveId}`,
        },
      ]);
    else return res.json(rows);
  } catch (err) {
    return res.sendStatus(500);
  }
});

module.exports = router;
