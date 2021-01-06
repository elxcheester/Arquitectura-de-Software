import { BrowserRouter, Route, Switch } from "react-router-dom";
import React, { Component } from 'react';

import PersonList from './PersonList';
import Home from './Home';

class App extends Component {
    render() {    
        return (
            <BrowserRouter>
                <Switch>
                    <Route exact path="/listapersonas" component={PersonList} />
                    <Route exact path="/" component={Home} />
                </Switch>
            </BrowserRouter>
        );
    }
}
export default App;