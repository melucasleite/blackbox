import { createLogic } from 'redux-logic';

import getPidControllers from '../../services/getPidControllers';

import { getPidControllersAction } from './actions';
import { GetPidControllersRequest, RootPidControllerState } from './types';

export const getPidControllerLogic = createLogic<
    RootPidControllerState,
    GetPidControllersRequest,
  any
>({
  type: getPidControllersAction.started.type,
  process: async ({ action }, dispatch: any, done) => {
    try {
      const controllers = await getPidControllers();
      dispatch(
          getPidControllersAction.done({
          params: action.payload,
          result: {
              controllers,
          },
        })
      );
    } catch (error) {
      dispatch(
          getPidControllersAction.failed({
          params: action.payload,
          error,
        })
      );
    }
    done();
  },
});
