import React from "react";
import { Redirect } from "react-router-dom";

// Layout Types
import { BlankLayout, DefaultLayout } from './layouts'

// Route Views
import Dashboard from './views/Dashboard'
import Controller from './views/Controller'
import LogControllers from './views/LogControllers'
import ControllerDoor from './views/ControllerDoor'
import LogDoor from './views/LogDoor'
import Page404 from './views/Page404'

export default [
  {
    path: "/",
    exact: true,
    layout: DefaultLayout,
    component: () => <Redirect to="/home" />
  },
  {
    path: "/home",
    layout: DefaultLayout,
    component: Dashboard
  },
  {
    path: "/controller/door",
    layout: DefaultLayout,
    component: ControllerDoor
  },
  {
    path: "/controller/:id",
    layout: DefaultLayout,
    component: Controller
  },
  {
    path: "/log/controllers",
    layout: DefaultLayout,
    component: LogControllers
  },
  {
    path: "/log/door",
    layout: DefaultLayout,
    component: LogDoor
  },
  {
    path: "/",
    exact: false,
    layout: BlankLayout,
    component: Page404
  },
];
