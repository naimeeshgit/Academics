import { useNavigate } from "react-router-dom";
import Grid from "@mui/material/Grid";
import Button from "@mui/material/Button";
import "bootstrap/dist/css/bootstrap.min.css";
import { Navbar, Container, Image, Nav } from "react-bootstrap";
import React, { useState } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
// import * as React from 'react';
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import axios from "axios";

// class Home extends Component {
//   render() {
const Home = () => {
  let navigate = useNavigate();
  var retrievedObject = localStorage.getItem("local");
  var userInfo = JSON.parse(retrievedObject);
  const [startDate, setStartDate] = useState("");
  const [endDate, setendDate] = useState("");
  const [cve, setcve] = useState("");

  const onChangecve = (e) => {
    setcve(e.target.value);
  };

  const onSubmit = (e) => {
    e.preventDefault();
    let input = {
      cveId: cve,
      startDate: new Date(startDate).toLocaleDateString([], {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
      }),
      endDate: new Date(endDate).toLocaleDateString([], {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
      }),
    };

    console.log(input);

    // let date1 = new Date(input.startDate);
    // let date2 = new Date(input.endDate);

    // console.log(b1.toUTCString(), b2.toUTCString());

    if (input.cveId === "" && input.startDate === "" && input.endDate === "") {
      alert("Please enter a value either dates or cve");
    }
    else{
      if(input.cveId === ""){
        axios.post("http://localhost:4000/search/betweendate", input)
        .then(res => {
          console.log(res.data);

          if(res.data.length === 0){
            alert("No CVEs found");
          }
          else{
            localStorage.setItem('results', JSON.stringify(res.data));
            navigate("/results", res);
          }
          
        })
      }
      else{
        axios.post("http://localhost:4000/search/cve", input)
        .then(res => {
          console.log(res.data);

          if(res.data.length === 0){
            alert("No CVEs found");
          }
          else{
            localStorage.setItem('results', JSON.stringify(res.data));
            navigate("/results", res);
          }
        })
      }
      
    }

    

  }


  return (
    <>
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="#home">
            <Button
              variant="outlined"
              color="success"
              size="large"
              onClick={() => navigate("/")}
            >
              :)
            </Button>
          </Navbar.Brand>
        </Container>
        <Container></Container>
        <Container></Container>
        <Container></Container>
        <Container></Container>
        <Container></Container>
        <Container></Container>
        <Container></Container>
        <Container>
          <Nav className="me-auto">
            <Button color="success" onClick={() => navigate("/login")}>
              login
            </Button>
          </Nav>
          <Nav className="me-auto">
            <Button color="success" onClick={() => navigate("/register")}>
              Registrer
            </Button>
          </Nav>
        </Container>
      </Navbar>
      <br />
      <Grid
        container
        spacing={0}
        direction="column"
        alignItems="center"
        justifyContent="center"
        style={{ minHeight: "20vh" }}
      >
        <Grid item xs={6}>
          <label>From</label>
          <DatePicker
            selected={startDate}
            onChange={(date) => setStartDate(date)}
          />
          <br />
          <br />
          <label>To</label>
          <DatePicker
            selected={endDate}
            onChange={(date) => setendDate(date)}
          />
          <br />
          <br />

          <TextField
            required
            id="outlined-required"
            style={{ width: 255 }}
            label="CVE Number"
            value={cve}
            onChange={onChangecve}
            defaultValue="Please enter valid cve number"
          />
          <br />
          <br />
          <div>
            <Grid container justify="center" alignItems="center">
              <Button
                variant="contained"
                color="primary"
                size="large"
                onClick={onSubmit}
              >
                Search
              </Button>
            </Grid>
          </div>
        </Grid>
      </Grid>
    </>
  );
  // }
};
export default Home;
