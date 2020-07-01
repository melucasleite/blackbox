import { reducerWithInitialState } from 'typescript-fsa-reducers';

import { PidControllerState } from './types';
import { getPidControllersAction } from './actions';

export const pidControllerInitialState: PidControllerState = {
  controllers: [],
  isLoading: false,
  error: null,
};

export const pidControllerReducer = reducerWithInitialState<PidControllerState>(pidControllerInitialState)
  .case(getPidControllersAction.started, (state) => {
    return {
      ...state,
      error: null,
      isLoading: true,
    };
  })
  .case(getPidControllersAction.done, (state, { result: { controllers } }) => {
    return {
      ...state,
      controllers,
      error: null,
      isLoading: false,
    };
  })
  .case(getPidControllersAction.failed, (state, { error }) => {
    return { ...state, error, isLoading: false };
  });
