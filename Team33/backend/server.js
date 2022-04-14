const express = require("express");
const app = express();
const cors = require("cors");
const mongoose = require("mongoose");
const PORT = 4000;
const DB_NAME = "vuln"; // "tutorial" TODO:

// routes
var testAPIRouter = require("./routes/testAPI");
var UserRouter = require("./routes/Users");
var lookupAPI = require("./routes/lookupAPI");

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Connection to MongoDB
mongoose.connect("mongodb://127.0.0.1:27017/" + DB_NAME, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const connection = mongoose.connection;
connection.once("open", function () {
  console.log("MongoDB database connection established successfully !");
});

// setup API endpoints
app.use("/search", lookupAPI);
app.use("/testAPI", testAPIRouter);
app.use("/user", UserRouter);

app.listen(PORT, function () {
  console.log("Server is running on Port: " + PORT);
});
