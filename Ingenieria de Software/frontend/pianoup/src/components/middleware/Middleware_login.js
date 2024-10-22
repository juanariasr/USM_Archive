import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const Middleware_login = () => {
    const navigate = useNavigate();

    useEffect(() => {
        if (sessionStorage.getItem('user')) {
            navigate('/home');
        } else {
            navigate('/', { state: 'failed' });
        }
    })
}

export default Middleware_login;