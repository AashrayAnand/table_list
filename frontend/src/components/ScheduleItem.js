import React from 'react';

const ScheduleItem = ({data}) => (
    <div className="card my-4 mx-auto px-4">
        <div className="card-body text-center">
            <h3 className="card-title">{data.location}</h3>
            <ul className="card-text">
                <li className="lead">{convDate(new Date(data.start_date))}</li>
                <li>{convTime(new Date(data.start_date))} - {convTime(new Date(data.end_date))}</li>
            </ul>
            <div className="card-footer text-muted d-none d-sm-block">
                <small>Available In: {timeUntil(new Date(data.start_date))}</small>
            </div>
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
    var pm = hours >= 12;
    hours = (pm && hours != 12 ? hours - 12 : hours);
    var time = hours + ":" + (d.getUTCMinutes() == 0 ? "00" : "30") + (pm ? "PM" : "AM");
    return (time);
}

const timeUntil = (d) => {
    var millis = d - Date.now() + d.getTimezoneOffset() * 60000;
    var minutes = Math.floor(millis / 60000);
    var hours = Math.floor(minutes / 60);
    var days = Math.floor(hours / 24);
    minutes = Math.floor(minutes % 60);
    hours = Math.floor(hours % 24);
    return (days + (days == 1 ? " day " : " days ") + 
            hours + (hours == 1 ? " hour " : " hours ") + 
            minutes + (minutes == 1 ? " minute" : " minutes"));
}

export default ScheduleItem;