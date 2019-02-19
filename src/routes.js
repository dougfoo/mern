import React from "react";
import { Route } from "react-router-dom";

import LoanList from "./containers/LoanListView";
import LoanDetail from "./containers/LoanDetailView";
import Login from "./containers/Login";
import Signup from "./containers/Signup";

const BaseRouter = () => (
  <div>
    <Route exact path="/" component={LoanList} />{" "}
    <Route exact path="/loanss/:loanID/" component={LoanDetail} />{" "}
    <Route exact path="/login/" component={Login} />{" "}
    <Route exact path="/signup/" component={Signup} />{" "}
  </div>
);

export default BaseRouter;
