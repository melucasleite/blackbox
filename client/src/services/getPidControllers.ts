import superagent from "superagent";
import { FETCH_CONTROLLERS_ROUTE } from "../constants";

export const formatBody = (response) => {
  return response.body.controllers.map((controller) => {
    if (controller.unit == "percent") {
      controller.unit = "%";
    }
    return controller;
  });
};

export default (): Promise<any> => {
  return superagent.get(FETCH_CONTROLLERS_ROUTE).then(formatBody);
};
