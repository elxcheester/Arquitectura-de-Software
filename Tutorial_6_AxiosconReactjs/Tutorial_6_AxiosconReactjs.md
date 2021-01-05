# Tutorial #6 : Axios con React


## 1. Introducción

Los proyectos que se encuentran en la web la mayoría de veces interactuan con una API REST en algún momento en su desarrollo. Axios es un cliente HTTP ligero basado en el servicio http en Angular .so v1.x y es similar a la API Fetch nativa de JavaScript.

Axios se basa en promesas, lo que le permite aprovechar async y await de JavaScript para obtener un código asíncrono más legible.

También puede interceptar y cancelar solicitudes, y hay una protección integrada del lado del cliente contra la falsificación de solicitudes entre sitios.

En este tutorial, verá ejemplos de cómo usar Axios para acceder a la popular API JSON Placeholder en una aplicación React.

## Requisitos previos

Para seguir este artículo, necesitará lo siguiente:

 - Node.js versión 10.16.0 instalado en su computadora. Para instalarlo en macOS o Ubuntu 18.04, siga los pasos del tutorial anterior.
 - Un nuevo proyecto React configurado con Create React App siguiendo el tutorial anterior.
 - También será útil tener conocimientos básicos de JavaScript.
 
Nota bene: Se utilizará una API en línea JSON PlaceHolder para hacer ejemplos más complejos y para simular un llamado hacia una API.
 
## 2. Añadir Axios al proyecto

En esta sección, añadirá Axios al proyecto anterior de Reactjs que creó siguiendo el tutorial pasado.

Para añadir Axios al proyecto, abra su terminal y cambie los directorios a su proyecto:

    $ cd nombre_del_proyecto

A continuación, ejecute este comando para instalar Axios:

    $ yarn add axios 

Luego, tendrá que importar Axios al archivo en el que desea usarlo.

## 3. Realizar una solicitud GET

En este ejemplo, creará un nuevo componente e importará Axios a él para enviar una solicitud GET.

Dentro de la carpeta src de su proyecto React, cree un nuevo componente llamado PersonList.jsx.

Añada el siguiente código al componente:

    import React from 'react';
    import axios from 'axios';

    export default class PersonList extends React.Component {
        state = {
        persons: []
        }

        componentDidMount() {
            axios.get(`https://jsonplaceholder.typicode.com/users`)
                .then(res => {
                    const persons = res.data;
                    this.setState({ persons });
                     })
                 }

        render() {
            return (
                <ul>
                 { this.state.persons.map(person => <li>{person.name}</li>)}
                </ul>
             )
        }
    }
Primero, debe importar React y Axios para que ambos puedan usarse en el componente. A continuación, enlazará en el enlace de ciclo de vida componentDidMount y realizará una solicitud GET.

Utiliza axios.get(url) con una URL desde un endpoint API para obtener una promesa que devuelve un objeto de respuesta. Dentro del objeto de respuesta, hay datos que se asignan al valor de person.

También puede obtener otra información sobre la solicitud, como el código de estado bajo res.status o más información dentro de res.request.

## 3. Realizar una solicitud POST

En este paso, usará Axios con otro método de solicitud HTTP llamado POST.

Elimine el código anterior en PersonList y añada el siguiente para crear un formulario que permita la entrada del usuario y, posteriormente, haga POST del contenido a una API:

    import React from 'react';
    import axios from 'axios';

    export default class PersonList extends React.Component {
        state = {
            name: '',
        }

        handleChange = event => {
            this.setState({ name: event.target.value });
        }

        handleSubmit = event => {
            event.preventDefault();
            const user = {
            name: this.state.name
        };

        axios.post(`https://jsonplaceholder.typicode.com/users`, { user })
            .then(res => {
             console.log(res);
             console.log(res.data);
            })
        }

        render() {
            return (
                 <div>
                 <form onSubmit={this.handleSubmit}>
                    <label>
                        Person Name:
                        <input type="text" name="name" onChange={this.handleChange} />
                     </label>
                    <button type="submit">Add</button>
                </form>
                </div>
            )
        }
    }

Dentro de la función handleSubmit, evita la acción predeterminada del formulario. A continuación actualice el estado para la entrada user.

Usar POST le proporciona el mismo objeto de respuesta con información que puede usar dentro de una invocación then.

Para completar la solicitud POST, primero debe capturar la entrada user.
A continuación añade la entrada junto con la solicitud POST, lo que le proporciona una respuesta. Luego puede hacer console.log a la respuesta, que debería mostrar la entrada user en el formulario.

## 4. Realizar una solicitud DELETE

En este tutorial, verá cómo eliminar elementos de una API usando axios.delete y pasando una URL como parámetro.

Cambie el código para el formulario desde el ejemplo POST para eliminar a un usuario en vez de añadir uno nuevo:

    import React from 'react';
    import axios from 'axios';

    export default class PersonList extends React.Component {
        state = {
            id: '',
        }

        handleChange = event => {
            this.setState({ id: event.target.value });
        }

        handleSubmit = event => {
            event.preventDefault();

            axios.delete(`https://jsonplaceholder.typicode.com/users/${this.state.id}`)
            .then(res => {
                console.log(res);
                console.log(res.data);
            })
        }

        render() {
            return (
                <div>
                    <form onSubmit={this.handleSubmit}>
                        <label>
                            Person ID:
                            <input type="text" name="id" onChange={this.handleChange} />
                        </label>
                        <button type="submit">Delete</button>
                    </form>
                </div>
            )
         }
    }
    
De nuevo, el objeto res le proporciona información sobre la solicitud. Luego, puede aplicar console.log a esta información de nuevo tras enviar el formulario.

## 6. Conclusión

En este tutorial, exploró varios ejemplos sobre cómo usar Axios dentro de una aplicación React para crear solicitudes HTTP y gestionar las respuestas.



