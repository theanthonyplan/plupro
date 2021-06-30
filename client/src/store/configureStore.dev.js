import { createStore, applyMiddleware } from 'redux';
import rootReducer from '../reducers';
import createDebounce from 'redux-debounced';
import { enableBatching } from 'redux-batched-actions';

// import thunkMiddleware from 'redux-thunk';
import thunk from 'redux-thunk';
import { createLogger } from 'redux-logger';

let doLogging = false; // change to true to enable logging to add a feature flag for 'redux_logging'

const configureStore = (preloadedState) => {
    const logger = createLogger({
        level: {
            prevState: 'log',
            action: 'log',
            nextState: (nextState) => {
                // if (!doLogging && nextState.global.featureFlags.redux_logging) {
                //     doLogging = true;
                // }
                return 'log';
            },
            error: 'error',
        },
        logger: {
            log: function() {
                if (doLogging) {
                    console.log.apply(console, arguments);
                }
            },
            warn: function() {
                if (doLogging) {
                    console.warn.apply(console, arguments);
                }
            },
            error: function() {
                if (doLogging) {
                    console.error.apply(console, arguments);
                }
            },
            trace: function() {
                if (doLogging) {
                    console.trace.apply(console, arguments);
                }
            },
            group: function() {
                if (doLogging) {
                    console.group.apply(console, arguments);
                }
            },
            groupEnd: function() {
                if (doLogging) {
                    console.groupEnd.apply(console, arguments);
                }
            },
            groupCollapsed: function() {
                if (doLogging) {
                    console.groupCollapsed.apply(console, arguments);
                }
            },
        },
    });
    let middleware = applyMiddleware(createDebounce(), thunk, logger);
    const store = createStore(enableBatching(rootReducer), preloadedState, middleware);
    return store;
};

export default configureStore;
