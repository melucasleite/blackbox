import dispatcher from "./dispatcher";
import constants from "./constants";

const Actions = {
  selectController(name) {
    dispatcher.dispatch({
      type: constants.SELECT_CONTROLLER,
      name,
    });
  },
};

export default Actions;
