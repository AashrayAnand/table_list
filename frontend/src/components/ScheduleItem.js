import React from 'react';

const ScheduleItem = ({data}) => (
    <div className="card my-2">
        <div className="card-body">
            <h3 className="card-title">{data.location}</h3>
            <ul className="m-0">
                <li>{convDate(new Date(data.date))}</li>
                <li>{convTime(new Date(data.start_date))} - {convTime(new Date(data.end_date))}</li>
            </ul>
        </div>
    </div> 
);

const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

const convDate = (d) => {
    var month = months[d.getUTCMonth()];
    var day = d.getUTCDate();
    var year = d.getUTCFullYear();
    return (month + " " + day + " " + year);
}

const convTime = (d) => {
    var hours = d.getUTCHours();
    var pm = hours > 12;
    hours = (pm ? hours - 12 : hours);
    var time = hours + ":" + (d.getUTCMinutes() == 0 ? "00" : "30") + (pm ? "PM" : "AM");
    return (time);
}

export default ScheduleItem;