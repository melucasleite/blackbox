import React, { useEffect } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";

import routes from "./routes";
import "bootstrap/dist/css/bootstrap.min.css";
import "./assets/main.scss";
import withTracker from "./withTracker";
import "./utils/chart";
import { fetchControllers } from "./api/api";
import store from "./store";
import { Provider } from "react-redux";

export default () => {
  useEffect(() => {
    const fetchData = async () => {
      let controllers = await fetchControllers();
      console.log(controllers);
    };
    fetchData();
  }, [fetchControllers]);
  return (
    <Provider store={store}>
      <Router basename={process.env.REACT_APP_BASENAME || ""}>
        <div>
          {routes.map((route, index) => {
            return (
              <Route
                key={index}
                path={route.path}
                exact={route.exact}
                component={withTracker((props) => {
                  return (
                    <route.layout {...props}>
                      <route.component {...props} />
                    </route.layout>
                  );
                })}
              />
            );
          })}
        </div>
      </Router>
    </Provider>
  );
};
