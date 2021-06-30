import React from 'react'
import { render } from 'react-dom'
import { Provider } from 'react-redux'
import { ConnectedRouter } from 'connected-react-router'
// import store, { history } from './store'
import App from './containers/app'

import 'sanitize.css/sanitize.css'
import 'semantic-ui-css/semantic.min.css'
import './index.css'

// const target = document.querySelector('#root')

// render(
//   <Provider store={store}>
//     <ConnectedRouter history={history}>
//       <div>
//         <App />
//       </div>
//     </ConnectedRouter>
//   </Provider>,
//   target
// )


import Root from './containers/root.container';
import configureStore from './store/configureStore';

const store = configureStore();

// $FlowFixMe
let rootElement: Element = document.getElementById('js-plupro-app');


window.plupro = {
    init: function() {
        render(
            <Provider store={store}>
                <Root />
            </Provider>,
            // rootElement
        );
    },
};
