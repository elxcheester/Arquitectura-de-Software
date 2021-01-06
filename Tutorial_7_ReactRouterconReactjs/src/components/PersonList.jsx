import React, { Component } from 'react';
import { Link } from 'react-router-dom';

export default class PersonList extends Component {
    render() {
        return (
            <div>
                <Link to="/" className="link">Go to Home</Link>
            </div>
        )
    }
}