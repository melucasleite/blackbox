import superagent from 'superagent';
import {FETCH_CONTROLLERS_ROUTE} from "../constants";

export const formatBody = (response) => {
  return response.body.controllers;
};

export default (): Promise<any> => {
  return superagent.get(FETCH_CONTROLLERS_ROUTE).then(formatBody);
};
