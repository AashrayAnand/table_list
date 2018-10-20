import React, { Component } from 'react';
import { connect } from 'react-redux';

class Schedule extends Component {
    renderSchedule() {
        return this.props.schedule.map((apt) => {
            return (
                <div className="card my-2" key={apt.id}>
                    <div className="card-body">
                        <h3 className="card-title">{apt.room}</h3>
                        <ul>
                            <li className="card-text text-muted">{apt.day}</li>
                            <li className="card-text text-muted">From: {apt.sTime} to {apt.eTime}</li>
                        </ul>
                    </div>
                </div> 
            );
        });
    }

    render() {
        return(
            <div className="container w-75 col col-9 bg-light" id="sched">
                <h2 className="text-center p-2">Scheduled Room Bookings</h2>
                <div className="container" id="times">
                    {this.renderSchedule()}
                </div>
            </div>
        );
    }
}

function mapStateToProps(state) {
    return {
        schedule: state.schedule
    };
}

export default connect(mapStateToProps)(Schedule);