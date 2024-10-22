import * as React from "react";
import {useEffect, useState} from 'react';

import Menu from './components/menu/Menu';
import Login from './components/user/Login';
import Navbar from './components/barra/NavBar';
import Navbar2 from './components/ResponsiveAppBar';


export default function Home() {

    const [user, setUser] = useState(null);
    const [logged, setLogged] = useState(false);

    useEffect(() => {
        if (sessionStorage.getItem('user')){
            setUser(sessionStorage.getItem('user'));
            setLogged(true);
        }
    }, [user, logged]);

    return (
        <>
            <Menu user={user}/>
        </>
    );
}
