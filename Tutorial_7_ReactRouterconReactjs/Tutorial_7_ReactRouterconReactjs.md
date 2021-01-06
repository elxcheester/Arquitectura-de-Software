# Tutorial #7: Rutas en Reactjs con React Router

## 1. Introducción

React Router es una libería para gestionar rutas en aplicaciones que utilicen ReactJS. Está inspirada en el sistema de enrutado de Ember.js y su forma de manejar las rutas es un poco diferente de lo que podemos ver en otros sistemas, como ASP. NET MVC, AngularJS, Express o Compojure, por poner unos cuantos ejemplos.

Para añadir React Router al proyecto, abra su terminal y cambie los directorios a su proyecto del tutorial anterior:

    $ cd nombre_del_proyecto
    
A continuación, ejecute este comando para instalar la librería:

    yarn add react-router-dom --s

Además también añadiremos la librería history ejecutando este comando:

    yarn add history --s
    
    
## 2. Primer ejemplo

Para este tutorial se continuará utilizando el proyecto del tutorial anterior, por lo tanto, ya con la instalación echa deberemos configurarlo.

Primero que todo debemos configurar nuestro archivo index.js, el cual quedará de este modo:

  
    import React from 'react';
    import ReactDOM from 'react-dom';
    import { Router } from 'react-router-dom'
    import { createBrowserHistory } from "history";
    import './assets/index.css';
    import App from './components/App';

    const history = createBrowserHistory() 

    ReactDOM.render(
        <Router history={history}>
            <App />
        </Router>,
        document.getElementById('root')
    );

En  el componente app, indicaremos que componente se cargará al escribir cada ruta y además crearemos un componente llamado Home, el cual tendrá el siguiente código:

    import React, { Component } from 'react';

    class Home extends Component {
        render () {
            return (
                <H1>
                    Esto es un mensaje desde el componente Home
                </H1>
            );
        }
    }

    export default Home;
    
### Componentes
React Router utiliza componentes, miremos algunos de ellos y que podemos hacer a través de algunos ejemplos:
 - BrowserRouter
    Es una envoltura para nuestra aplicación. Esta envoltura nos da acceso al API de historia de HTML5 para mantener nuestra interfaz gráfica en sincronía con la locación actual o URL. Debemos tener en cuenta que esta envoltura solo puede tener un hijo. Por lo general es Switch.

 - Switch
    Este componente, causa que solo se renderice el primer hijo Route o Redirect que coincida con la locación o URL actual.
    En el caso que no usemos Switch todas las rutas que cumplan con la condición se renderizarán.
 - Route
    Para definir las diferentes rutas de nuestra aplicación, podemos usar el componente Route. La función de este componente es elegir que renderizar según la locación actual. Este es el caso que vimos anteriormente, todos los componentes Route siempre renderizan, pero algunas veces renderizan un componente y otras veces retornan null.

Por lo tanto, debajo de la primera línea dentro del componente App, importamos BrowserRouter, Route y Switch de la librería «react-router-dom» y además importaremos los siguientes componentes.

    import { BrowserRouter, Route, Switch } from "react-router-dom";
    import React, { Component } from 'react';
    
    import PersonList from '../components/PersonList';
    import Home from '../components/Home';

    class App extends Component {
        render() {    
            return (
                <div>
                    <PersonList />
                    <Home />
                </div>
            );
        }
    }
    export default App;
    
Después, dentro del return, escribiremos lo siguiente:

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

Debes añadir tantas etiquetas Route como componentes tengas, indicando en el path la ruta y en el component el componente que quieres mostrar.

BrowserRouter se encargará de recuperar la ruta y mostrar el contenido que hayamos indicado.

En caso que la locación actual sea localhost:3000/listapersonas se mostrara la segunda ruta la cual mostrará el componente PersonList.

Este componente recibe las siguientes propiedades:
 - path: la ruta en la que se renderizará el componente en forma de cadena de texto
 
 - exact: un booleano para definir si queremos que la ruta tiene o no que ser exacta    para renderizar un componente. Eg: /index !== /index/all.
 
 - strict: un booleano para definir si queremos que el último slash sea tomado en     cuenta para renderizar un componente. Eg: /index !== /index/.
 
 - sensitive: un booleano para definir si queremos distinguir entre minúsculas y       mayúsculas, y tomar esto en cuenta para renderizar un componente. Eg: /index !==    /Index
 
 - component: recibe un componente a renderizar. Crea un nuevo elemento de React       cada vez. Esto causa que el componente se monte y desmonte cada vez (no            actualiza).
 
 - render: recibe un método que retorna un componente. A diferencia de component no    remonta el componente.
 
 - children: funciona muy similar a render, pero con algunas adiciones. Hoy no voy a    ahondar mucho en está propiedad. 

Este ejemplo renderizará los componentes de la siguiente manera:

si la ruta es exactamente / renderizará el componente Home.

si la ruta es exactamente /listapersona renderiza el componente PersonList.

## Link

Ya hemos configurado nuestras rutas, pero aún no tenemos forma de navegar por nuestra aplicación. Si queremos cambiar de un componente a otro nos tocaría navegar cambiando la URL de manera manual.
Link crea un hipervínculo que nos permite navegar por nuestra aplicación. Al contrario de Redirect, este agrega una nueva locación a la historia.

Recibe las siguientes propiedades:
 - to: una locación en forma de cadena de text. Esta será la locación a la que        navegaremos cuando le damos click a un hipervínculos.
 - replace: un booleano que nos permite modificar el comportamiento de Link. Cuando    este es verdadero en lugar de agregar una nueva locación a la historia, este       reemplaza la locación actual.

Para incorporar links a nuestro código, modificaremos nuestros componentes Home y PersonList, quedando de la siguiente manera:

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
    
posteriormente:

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
    
En Resumen

React Router nos provee todos los componentes necesarios para hacer que nuestra SPA (single page application) se mantenga en sincronía con nuestra locación actual.
BrowserRouter, Route, Switch, Redirect, y Link, son los componentes más básicos y obligatorios, y son solo algunos de los componentes que tenemos a nuestra disposición a la hora de trabajar con rutas en React.




