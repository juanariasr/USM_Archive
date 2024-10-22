import React, { useState, useEffect } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { Form, Button } from 'react-bootstrap';
import './Login.css';

const baseUrl = "http://localhost:8000";

export default function Login() {
    const axios = require('axios')

    const { state } = useLocation();
    const navigate = useNavigate();

    const [response, setResponse] = useState('');
    const [check, setCheck] = useState('');
    const [formData, setFormData] = useState({
        username: '',
        password: '',
    });

    useEffect(() => {
        setResponse(state);
    }, [state])

    const handleLogin = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post(baseUrl +'/users/login/', {
                username: formData.username,
                password: formData.password, 
            });

            if (response.data) 
            {
                const message = response.data.message;
                if (message === "Success") {
                    console.log(message);
                    sessionStorage.setItem('user', formData.username);
                }
            }
        }

        catch (error) {
            if (error.response && error.response.status === 401) {
                console.log('Unauthorized');
                setCheck(401);
            } 
            else {
                console.error(error);
            }
        }

        navigate('/m-login');
    };

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData((prevFormData) => ({
          ...prevFormData,
          [name]: value,
        }));
    };
    
    return (
        <div className="screen">
            <div className="left-row">
                <video className="login-video" src="bg_video.mov" autoPlay loop muted/>
            </div>
            <div className="right-row">
                <div className="login-wrapper">
                    <h2>Login</h2>
                    <Form onSubmit={handleLogin}>
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
                            <Form.Label>Password</Form.Label>
                            <Form.Control 
                                type="password" 
                                name="password"
                                placeholder="Enter password"
                                value={formData.password}
                                onChange={handleChange}/>
                                {check === 401 && <Form.Text 
                                    style={{ color: 'red' }}>
                                    Wrong password.
                            </Form.Text>}
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
                                    <p className="warning-txt">Nombre de usuario o contraseña incorrectos</p>
                                    <p className="warning-txt">Intente nuevamente</p>
                                </div>
                            )
                    }
                </div>
                <div className='register-div'>
                    <h5>¿No tiene cuenta?</h5>
                    <Link to='/register' className="register-txt">
                        <h5>Registrese</h5>
                    </Link>
                </div>
            </div>
        </div>
    )
}   
