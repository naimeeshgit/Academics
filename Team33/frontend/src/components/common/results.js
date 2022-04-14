import { useState, useEffect } from "react";
import axios from "axios";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";
import TableCell from "@mui/material/TableCell";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import Button from "@mui/material/Button";
import * as React from 'react';
import { useNavigate } from "react-router-dom";

const ItemList = (event) => {


    const [users, setUsers] = useState([]);


    // list of items
    useEffect(() => {


        let results = localStorage.getItem('results');
        setUsers(JSON.parse(results));


    });

    


    return (

        <div>
            <Grid container>
                <Grid item xs={12} md={9} lg={9}>
                    <Paper>
                        <Table size="small">
                            <TableHead>
                                <TableRow>
                                    <TableCell>Sr No.</TableCell>
                                    <TableCell>CVE ID</TableCell>
                                    <TableCell>Description</TableCell>
                                    <TableCell>Reference</TableCell>
                                    <TableCell>Published Date</TableCell>
                                    <TableCell>Modified Date</TableCell>
                                    {/* <TableCell>addons</TableCell> */}
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {users.map((user, ind) => (
                                    <TableRow key={ind}>
                                        <TableCell>{ind}</TableCell>
                                        <TableCell>{user.cve}</TableCell>
                                        <TableCell>{user.description}</TableCell>
                                        <TableCell>{user.reference}</TableCell>
                                        <TableCell>{user.published}</TableCell>
                                        <TableCell>{user.modified}</TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </Paper>
                </Grid>
            </Grid>

        </div>

    );
};

export default ItemList;
