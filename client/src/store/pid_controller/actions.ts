import actionCreatorFactory from 'typescript-fsa';

import { GetPidControllersRequest, GetPidControllersSuccess } from './types';
import { Action, Dispatch } from 'redux';

export const GET_PID_CONTROLLERS = 'GET_PID_CONTROLLERS';

const actionCreator = actionCreatorFactory();

export const getPidControllersAction = actionCreator.async<
  GetPidControllersRequest,
  GetPidControllersSuccess,
  Error
>(GET_PID_CONTROLLERS);

export const getPidControllers = (dispatch: Dispatch) => {
  console.log("called...")
  return (payload: GetPidControllersRequest): Action =>
    dispatch(getPidControllersAction.started(payload));
};
