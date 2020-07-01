export interface GetPidControllersRequest {}

export interface GetPidControllersSuccess {
  controllers: {}[];
}

export interface PidControllerState {
  controllers: {}[];
  isLoading: boolean;
  error?: any;
}

export interface RootPidControllerState {
  pidController: PidControllerState;
}
