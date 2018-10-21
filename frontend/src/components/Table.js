import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";
import ScheduleItem from "./ScheduleItem";

const Table = ({ data }) =>
  !data.length ? (
    <p>Nothing to show</p>
  ) : (
    <div className="container w-75 col col-9 bg-light" id="sched">
        <h2 className="text-center p-2">Scheduled Room Bookings</h2>
        <h3 className="text-center p-1 text-muted"><strong>{data.length}</strong> bookings</h3>
        <div className="container" id="times">
            {data.map(el => (
                <ScheduleItem data={el} key={key(el)}/>
            ))}
        </div>
    </div>
  );
Table.propTypes = {
  data: PropTypes.array.isRequired
};
export default Table;