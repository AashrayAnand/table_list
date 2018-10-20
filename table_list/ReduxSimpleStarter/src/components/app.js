import React, { Component } from 'react';
import QueryForm from './query_form';
import Schedule from './schedule';

export default class App extends Component {
  render() {
    return (
      <div>
        <h1 className="text-center py-3">LibCal Schedule</h1>
        <div className="row">
          <QueryForm />
          <Schedule />
        </div>
      </div>
    );
  }
}
