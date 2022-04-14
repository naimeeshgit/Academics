import { useState } from "react";
import axios from "axios";
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import * as React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Stack from '@mui/material/Stack';
import { Link } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, Container, Image, Nav } from 'react-bootstrap';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputAdornment from '@mui/material/InputAdornment';
import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';
import IconButton from '@mui/material/IconButton';
import Alert from '@mui/material/Alert';
// import Dropdown from 'react-dropdown';
// import 'react-dropdown/style.css';
import { useNavigate } from "react-router-dom";

const Register = (props) => {
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [date, setDate] = useState(null);
  const [contact, setContact] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [values1, setValues1] = React.useState({
    showPassword: false,
  });
  const [values2, setValues2] = React.useState({
    showPassword: false,
  });
  
  const handleClickShowPassword = () => {
    setValues1({
      ...values1,
      showPassword: !values1.showPassword,
    });
  };
  const handleClickShowConfirmPassword = () => {
    setValues2({
      ...values2,
      showPassword: !values2.showPassword,
    });
  };
  const onChangepassword = (event) => {
    setPassword(event.target.value);
  };
  const onChangeconfirmpassword = (event) => {
    setConfirmPassword(event.target.value);
  };

  const onChangeUsername = (event) => {
    setName(event.target.value);
  };

  const onChangeEmail = (event) => {
    setEmail(event.target.value);
  };

  const onChangeContact = (event) => {
    setContact(event.target.value);
  };



  const resetInputs = () => {
    setName("");
    setEmail("");
    setDate(null);
    setContact("");
    setPassword(null);
    setConfirmPassword(null);
  };


  const onSubmit = (event) => {
    event.preventDefault();

    if (password !== confirmPassword) {
      alert("Invalid entries");
      return;
    }

    const newUser = {
      name: name,
      email: email,
      contact: contact,
      password: password,
    };
    console.log(newUser)
    axios
      .post("http://localhost:4000/user/register", newUser)
      .then((response) => {
        alert("Created\t" + response.data.name);
        console.log(response.data);
        navigate("/login");
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
        <div style={{ margin: "auto" }}>
          <br />
          <h1 style={{ margin: "20px auto", color: "blue" }}  > New User Registration</h1>
          <br />


          <h4 style={{ color: "green" }}>Already have an account ?</h4>
          <Link to="/login" style={{ color: "blue" }}>Login</Link>
          <br />
          {/* <Link to="/login" style={{color: "blue"}}>Login</Link> */}
        </div>

        <Grid item xs={12}>
          <TextField
            label="Name"
            variant="outlined"
            value={name}
            onChange={onChangeUsername}
          />
        </Grid>
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
            label="Contact"
            variant="outlined"
            value={contact}
            onChange={onChangeContact}
          />
        </Grid>

        <Grid item xs={12}>
          <FormControl sx={{ m: 1, width: '25ch' }} variant="outlined">
            <InputLabel htmlFor="outlined-adornment-password">Password</InputLabel>
            <OutlinedInput
              id="outlined-adornment-password"
              type={values1.showPassword ? 'text' : 'password'}
              value={values1.password}
              onChange={onChangepassword}
              endAdornment={
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    onClick={handleClickShowPassword}
                    edge="end"
                  >
                    {values1.showPassword ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              }
              label="Password"
            />
          </FormControl>
        </Grid>
        <Grid item xs={12}>
          <FormControl sx={{ m: 1, width: '25ch' }} variant="outlined">
            <InputLabel htmlFor="outlined-adornment-password">Confirm Password</InputLabel>
            <OutlinedInput
              id="outlined-adornment-password"
              type={values2.showPassword ? 'text' : 'password'}
              value={values2.password}
              onChange={onChangeconfirmpassword}
              endAdornment={
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    onClick={handleClickShowConfirmPassword}
                    edge="end"
                  >
                    {values2.showPassword ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              }
              label="Confirm Password"
            />
          </FormControl>
        </Grid>

        {password !== confirmPassword ? <Grid item xs={12}><FormControl sx={{ m: 1, width: '50ch' }} variant="outlined">
          <Alert severity="error">Password and Confirm Password does not match</Alert></FormControl></Grid> : null}
        <Grid item xs={12}>
          <Button variant="contained" onClick={onSubmit}>
            Register
          </Button>
        </Grid>
      </Grid>
    </>
  );

};

export default Register;
