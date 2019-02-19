import React from "react";
import axios from "axios";
import { connect } from "react-redux";
import { Button, Card } from "antd";
import CustomForm from "../components/Form";


class LoanDetail extends React.Component {
  state = {
    loan: {}
  };

  componentDidMount() {
    const loanID = this.props.match.params.loanID;
    axios.get(`http://127.0.0.1:8000/api/${loanID}`).then(res => {
      this.setState({
        loan: res.data
      });
    });
  }

  handleDelete = event => {
    event.preventDefault();
    const loanID = this.props.match.params.loanID;
    axios.defaults.headers = {
      "Content-Type": "application/json",
      Authorization: `Token ${this.props.token}`
    };
    axios.delete(`http://127.0.0.1:8000/api/${loanID}/delete/`)
    .then(res => {
      if (res.status === 204) {
        this.props.history.push(`/`);
      }
    })
  };

  render() {
    return (
      <div>
        <Card title={this.state.loan.title}>
          <p> {this.state.loan.content} </p>
        </Card>
        <CustomForm
          {...this.props}
          token={this.props.token}
          requestType="put"
          loanID={this.props.match.params.loanID}
          btnText="Update"
        />
        <form onSubmit={this.handleDelete}>
          <Button type="danger" htmlType="submit">
            Delete
          </Button>
        </form>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    token: state.token
  };
};

export default connect(mapStateToProps)(LoanDetail);
