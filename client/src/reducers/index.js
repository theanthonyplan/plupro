// @flow
import { combineReducers } from 'redux';

import globalsReducer from './globals';
import userReducer from './user';
// import questionnaireReducer from './questionnaire';
// import questionReducer from './question';
// import organizationReducer from './organization';

const rootReducer = combineReducers({
    global: globalsReducer,
    user: userReducer,
    // questionnaire: questionnaireReducer,
    // organization: organizationReducer,
    // question: questionReducer,
});

export default rootReducer;
