import React from "react";
import axios from "axios";
import Loans from "../components/Loan";
import CustomForm from "../components/Form";


class LoanList extends React.Component {
  state = {
    loans: []
  };

  fetchLoans = () => {
    axios.get("http://127.0.0.1:8000/api/").then(res => {
      this.setState({
        loans: res.data
      });
    });
  }

  componentDidMount() {
    this.fetchLoans();
  }

  componentWillReceiveProps(newProps) {
    if (newProps.token) {
      this.fetchLoans();      
    }
  }

  render() {
    return (
      <div>
        <Loans data={this.state.loans} /> <br />
        <h2> Create an loan </h2>
        <CustomForm requestType="post" loanID={null} btnText="Create" />
      </div>
    );
  }
}

export default LoanList;
