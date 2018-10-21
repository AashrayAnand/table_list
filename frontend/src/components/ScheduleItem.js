import React from 'react';
import PropTypes from "prop-types";
import key from "weak-key";

const ScheduleItem = ({data}) => (
    <div className="card my-2" key={data.pk}>
        <div className="card-body">
            <h3 className="card-title">{data.location}</h3>
            <ul>
                <li>{dateTime(new Date(data.date))}</li>
            </ul>
        </div>
    </div> 
);

const dateTime = (d) => {
    var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    var month = months[d.getUTCMonth()];
    var day = d.getUTCDate();
    var year = d.getUTCFullYear();
    var time = "" + d.getUTCHours() + ":" + (d.getUTCMinutes()==0?"00":"30") + (d.getUTCHours()>=12?"PM":"AM");
    return (month + " " + day + " " + year + " - " + time);
}

export default ScheduleItem;