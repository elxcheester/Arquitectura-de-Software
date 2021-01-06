import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Home extends Component {
    render () {
        return (
             <div>
                 <Link to="/listapersonas" className="link">Go to PersonList</Link>
             </div>
        );
    }
}

export default Home