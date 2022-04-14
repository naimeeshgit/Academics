//import { useState, useEffect } from "react";
// import React, { Component } from "react";
import { useNavigate } from "react-router-dom";
// import { Link } from "react-router-dom";
import Grid from "@mui/material/Grid";
// import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, Container, Image, Nav } from 'react-bootstrap';




// class Home extends Component {
//   render() {
const Home = () => {
    let navigate = useNavigate();
    // var retrievedObject = localStorage.getItem('local');
    // var userInfo = JSON.parse(retrievedObject.name);
    return (

        <>
            <Navbar bg="dark" variant="dark">
                <Container>

                    <Navbar.Brand href="#home">
                        <Button variant="outlined" color="success" size="large" onClick={() => navigate("/")}>
                            :)
                        </Button>
                    </Navbar.Brand>
                    
                </Container>
                <Container>
                    <Navbar.Toggle />
                    <Navbar.Collapse className="justify-content-end">
                        <Navbar.Text>
                            Signed in as: <a href="#login">.....</a>
                        </Navbar.Text>
                    </Navbar.Collapse>
                    <Nav.Link href="#home">LOGOUT</Nav.Link>
                </Container>
            </Navbar>
        </>



    );
    // }
};
export default Home;

