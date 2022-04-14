const mongoose = require("mongoose");
const Schema = mongoose.Schema;
const validator = require("validator");

//import { isEmail } from 'validator';

// Create Schema
const UserSchema = new Schema({
	name: {
		type: String,
		required: false,
	},
	email: {
		type: String,
		unique : true,
		required: false,
	},
	contact: {
		type: String,
		required: false,
	},
	password: {
		type: String,
		required: false,
	  },
});

module.exports = User = mongoose.model("Users", UserSchema);
