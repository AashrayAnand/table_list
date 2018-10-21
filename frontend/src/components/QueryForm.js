import React from 'react';

const QueryForm = () => {
    return (
        <div className="container col col-3" id="qform">
            <div className="sticky-top">
                <h2 className="text-center p-2">Search Criteria</h2>
                <form>
                    <div className="form-group">
                        <label className="text-muted" htmlFor="whenSelect">When:</label>
                        <select className="form-control" id="whenSelect">
                            <option>Today</option>
                            <option>Next 7 Days</option>
                            <option>Next 14 Days</option>
                        </select>
                    </div>
                </form>
            </div>
        </div>
    );
}

$("#whenSelect").change(() => {
    alert("Changed to: " + $("#whenSelect").value());
});

export default QueryForm;