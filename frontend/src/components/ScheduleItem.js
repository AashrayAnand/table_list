import React from 'react';
import PropTypes from "prop-types";
import key from "weak-key";

const ScheduleItem = ({data}) => (
    <div className="card my-2" key={data.pk}>
        <div className="card-body">
            <h3 className="card-title">{data.location}</h3>
            <ul>
                <li className="card-text text-muted">{data.day_of_week}</li>
                <li className="card-text text-muted">{data.date}</li>
            </ul>
        </div>
    </div> 
);

export default ScheduleItem;