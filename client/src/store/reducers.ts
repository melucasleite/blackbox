import { combineReducers, Reducer } from "redux";
import { pidControllerReducer } from "./pid_controller/reducer";
import { RootPidControllerState } from "./pid_controller/types";

const rootReducer = (): Reducer =>
  combineReducers({
    pidController: pidControllerReducer,
  });

export interface RootState extends RootPidControllerState {}
export default rootReducer;
