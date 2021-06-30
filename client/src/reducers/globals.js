// @flow
import u from 'updeep';
import _ from 'lodash';

import Lockr from 'lockr';

import * as types from '../constants/actionTypes';

import { LOGGED_IN } from '../constants/constants';

let initialState = {
    loggedIn: false,
    currentUser: {},
    users: [],
    ENV: {},
    CONSTANTS: {},
    me: {},
    modalData: null,
};

function globalsReducer(state: any = initialState, action: any) {
    console.log('globalsReducer');
    console.log('globalsReducer.action', action);
    switch (action.type) {
        case types.RECEIVE_ME:
            return Object.assign({}, state, {
                me: action.data,
            });
        
        case types.SET_CURRENT_USER:
            return Object.assign({}, state, {
                loggedIn: !!action.data.id,
                currentUser: action.data,
                me: action.data,
            });
        
        case types.SET_USERS:
            return Object.assign({}, state, {
                users: action.data,
            });

        case types.LOGGED_OUT:
            return Object.assign({}, state, {
                loggedIn: false,
            });

        case types.SET_MODAL_DATA:
            return Object.assign({}, state, {
                modalData: action.modalData,
            });

        default:
            return state;
    }
}

export default globalsReducer;
