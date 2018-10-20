import React, { Component } from 'react';
import { connect } from 'react-redux';
import ScheduleItem from './ScheduleItem';

class Schedule extends Component {
    constructor(props) {
        super(props);

        this.state = data;
    }

    renderSchedule() {
        return this.state.data.map((item) => {
            return <ScheduleItem fields={item} />;
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