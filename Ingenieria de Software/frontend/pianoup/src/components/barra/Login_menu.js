import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './login_menu.css';

const Login_menu = () => {
    const navigate = useNavigate();

    const [user, setUser] = useState(null);

    const createSession = () => {
        navigate('/register');
    }

    const openSession = () => {
        navigate('/');
    }

    const closeSession = () => {
        sessionStorage.removeItem("user");
        navigate('/');
    }

    useEffect(() => {
        const u_temp = sessionStorage.getItem("user");
        setUser(u_temp);
    })

    return (
        <>
            <ul className='dropdown-login-menu' >
                {
                    user
                    ?
                        <li className='dropdown-login-item'>
                            <Link to='/' className='dropdown-login-text' onClick={() => closeSession()}>
                                <h5>Cerrar sesion</h5>
                            </Link>
                        </li>
                    :
                        <>
                            <li className='dropdown-login-item'>
                                <Link to='/register' className='dropdown-login-text' onClick={() => createSession()}>
                                    <h5>Registrarse</h5>
                                </Link>
                            </li>
                            <li className='dropdown-login-item'>
                                <Link to='/login' className='dropdown-login-text' onClick={() => openSession()}>
                                    <h5>Ingresar usuario</h5>
                                </Link>
                            </li>      
                        </>                 
                }
            </ul>
        </>
    )
}

export default Login_menu;