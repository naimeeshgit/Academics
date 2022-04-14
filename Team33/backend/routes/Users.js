var express = require("express");
var router = express.Router();
var bcrypt = require("bcryptjs");
var jwt = require('jsonwebtoken');

// Load User model
const User = require("../models/Users");

// GET request 
// Getting all the users
router.get("/", function (req, res) {
    User.find(function (err, users) {
        if (err) {
            console.log(err);
        } else {
            res.json(users);
        }
    })
});

router.post("/register", (req, res) => {
    const email = req.body.email;
    // Find user by email
    User.findOne({ email }).then(user => {
        // Check if user email exists
        if (user) {
            return res.status(404).json({
                error: "Email already exists",
            });
        }
        else {
            const newUser = new User({
                name: req.body.name,
                email: req.body.email,
                contact: req.body.contact,
                password: req.body.password,
            });
            // Hash password before saving in database
            //Hash is created only when password is not an empty string else throw an error

            if (newUser.password) {

                bcrypt.genSalt(10, (err, salt) => {
                    bcrypt.hash(newUser.password, salt, (err, hash) => {
                        if (err) throw err;
                        newUser.password = hash;
                        newUser.save()
                        .then(user => {
                            console.log(user);
                            res.status(200).json(user);
                        })
                        .catch(err => {
                            res.status(400).send(err);
                        });
        
                    });
                });
            }
            else
            {
                newUser.save()
                .then(user => {
                    res.status(200).json(user);
                })
                .catch(err => {
                    res.status(400).send(err);
                });

            }

            // Save user in database
           
        }
    });
});

// POST request 
// Login
router.post("/login", (req, res) => {
    const email = req.body.email;
    const password = req.body.password;
    //const found = false;
    //print password
    // console.log(password);
    // Find user by email
    User.findOne({ email }).then(user => {
        // Check if user email exists
        if (!user) {
            return res.status(200).json({
                found: "Email not found",
            });
        }
        
//console.log(user.password);
            bcrypt.compare(password, user.password).then(isMatch => {
                ////console.log(isMatch);
                if (isMatch) {
                    // res.send("Email Found");
                    // User matched
                    // Create JWT Payload
                    const payload = {
                        id: user.id,
                        name: user.name,
                        email: user.email,
                        found: "true",
                        password: user.password

                    };

                    // Sign token
                    const token = jwt.sign(
                        payload,
                        'secret',
                        {
                            expiresIn: 31556926 // 1 year in seconds
                        }
                        
                    );
                    return res.status(200).json(payload);
                    
                }
                else {
                    // res.send("Email Found");
                    return res.status(200).json({ found : "Password incorrect" });
                }
            });
            // res.send("Email Found");
            // return user;
        
    });
});



module.exports = router;

