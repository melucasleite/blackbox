import { applyMiddleware, createStore, Store } from "redux";
import { createLogicMiddleware } from "redux-logic";
import { composeWithDevTools } from "redux-devtools-extension";

import rootReducer, { RootState } from "./reducers";

import { pidControllerInitialState } from "./pid_controller/reducer";

import logics from "./logic";

export const initialState: RootState = {
  pidController: pidControllerInitialState,
};

export const creatBlackBoxStore = (
  initialStoreState: RootState = initialState
): Store => {
  const logicMiddleware = createLogicMiddleware(logics);

  return createStore(
    rootReducer(),
    initialStoreState,
    composeWithDevTools({ trace: true, traceLimit: 25 })(
      applyMiddleware(logicMiddleware)
    )
  );
};

const store = creatBlackBoxStore();

export default store;
