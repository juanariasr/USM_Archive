import React, { useState, useEffect } from "react";
import { useNavigate, useLocation} from 'react-router-dom';
import { TextField, Card, Grid } from "@mui/material";
import {Form, Button} from 'react-bootstrap';
import './Register.css';

const baseUrl = "http://localhost:8000";

function Register() {
    const axios = require('axios')

    const [isChecked, setIsChecked] = useState(false)
    const [isCheckedprev, setIsCheckedprev] = useState(false)
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        is_tutor: '', 
      });

    const checkHandler = () => {
        setIsChecked(!isChecked);
    };

    const [response, setResponse] = useState("");
    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData((prevState) => ({ ...prevState, [name]: value }));
    };


    const navigate = useNavigate();
    const { state } = useLocation();

    useEffect(() => {
        setResponse(state);
    }, [state])

    const checkExists = async () => {
        try {
            const response = await axios.get(baseUrl + '/users/check/', {
              params: {
                username: formData.username
              }
            });

            if (response.data) 
            {
                const message = response.data.message;
                if (message === "Success") {
                    console.log(message);
                    return true;
                }
                else if (message === "Not Exist") {
                    console.log(message);
                    return false;
                }
            }
        }

        catch (error) {
            if (error.response) {
                console.error(error);
            }
        }
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const userExists = await checkExists();
        formData.is_tutor = isChecked.toString();
        console.log(formData);
        if (!userExists) {
            alert("User registered succesfully")
            console.log(formData.is_tutor);
            axios.post(baseUrl + '/users/create/', formData)
              .then(function (response) {
                console.log(response);
              })
              .catch(function (error) {
                console.log(error);
              });
            sessionStorage.setItem('user', formData.username);
            navigate('/');
        }

        else {
            navigate('/register', { state: 'failed'});
            setFormData({
                username: '',
                email: '',
                password: '',
                is_tutor: '', 
            });
        }
    };

  return (
    <div className="screen">
        <div className='inner-row'>
            <div className="login-wrapper">
                <h2>Register</h2>
                <Form onSubmit={handleSubmit}> 
                    <Form.Group className="mb-3">
                        <Form.Label>Username</Form.Label>
                        <Form.Control 
                            type="text" 
                            name="username"
                            placeholder="Enter username"
                            value={formData.username}
                            onChange={handleChange}/>
                    </Form.Group>
                    <Form.Group className="mb-3">
                        <Form.Label>Email</Form.Label>
                        <Form.Control 
                            type="text" 
                            name="email"
                            placeholder="Enter email"
                            value={formData.email}
                            onChange={handleChange}/>
                    </Form.Group>
                    <Form.Group className="mb-3">
                        <Form.Label>Password</Form.Label>
                        <Form.Control 
                            type="password" 
                            name="password"
                            placeholder="Enter password"
                            value={formData.password}
                            onChange={handleChange}/>
                    </Form.Group>
                    <Form.Group className="mb-3">
                        <Form.Check
                            type='checkbox'
                            label='Es tutor?'
                            onChange={checkHandler}/>
                    </Form.Group>
                    <Button variant="primary" type="submit">Enviar</Button>{''}
                </Form>
            </div>
            <div className="warning-div">
                {
                    response === 'failed'
                    &&
                        (
                            <div>
                                <p className="warning-txt">Nombre de usuario ocupado</p>
                                <p className="warning-txt">Intente uno diferente</p>
                            </div>
                        )
                }
            </div>
        </div>
    </div>
  )
}

export default Register;
