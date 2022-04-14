import { useState } from "react";
import axios from "axios";
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import * as React from 'react';
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";

import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, Container, Image, Nav } from 'react-bootstrap';

const Login = (props) => {
  const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
  
    const onChangeEmail = (event) => {
      setEmail(event.target.value);
    };
  
    const onChangePassword = (event) => {
      setPassword(event.target.value);
    };
  

    const resetInputs = () => {
      setEmail("");
      setPassword("");
    };
  
  
    const onSubmit = (event) => {
      event.preventDefault();
  
      const newUser = {
        email: email,
        password: password,
      };

      console.log(newUser)

       
      axios
        .post("http://localhost:4000/user/login", newUser)
        .then((response) => {
          if(response.data.found !== "true"){
          alert("Please check the credentials\t");
          }
          else
          {
            alert("Login Successful");
            // console.log(response.data);
            localStorage.setItem('local', JSON.stringify(response.data)); // local has the stringified data , we need to parse it at the time of use
         // if user is buyer then redirect to profile buyer
              navigate("/profileBuyer");
              // console.log("buyer")
              
          }
          //console.log(response.data.found);
        });
  
      resetInputs();
    };
  
    return (
      <>
      
      <Navbar bg="dark" variant="dark">
        <Container>
          
          <Navbar.Brand href="#home">
          <Button variant="outlined" color="success" size="large"  onClick={() => navigate("/")}>
              :)
            </Button>
          </Navbar.Brand>
        </Container>
        <Container>
        </Container>
      </Navbar>
      <Grid container align={"center"} spacing={2}>
        <div style={{margin: "auto"}}>
          <br/>
        <h1 style={{ margin: "20px auto", color: "blue" }}  > User <b>Login</b>{'\n'}</h1>
        <br/>
        
  
        <h4 style={{color: "red"}}>Don't have an account ?</h4>
        <Link to="/register" style={{color:"green"}}>Register</Link>
        {/* <Link to="/login" style={{color: "blue"}}>Login</Link> */}
          </div>
       
        <Grid item xs={12}>
          <TextField
            label="Email"
            variant="outlined"
            value={email}
            onChange={onChangeEmail}
          />
        </Grid>
       
        <Grid item xs={12}>
          <TextField
            label="Password"
            variant="outlined"
            value={password}
            onChange={onChangePassword}
          />
        </Grid>
        <Grid item xs={12}>
          <Button variant="contained" onClick={onSubmit}>
            Login
          </Button>
        </Grid>
      </Grid>
      </>
    );
  };
  
  export default Login;
  