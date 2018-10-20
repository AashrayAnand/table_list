import { combineReducers } from 'redux';
import ScheduleReducer from './reducer_schedule';

const rootReducer = combineReducers({
  schedule: ScheduleReducer
});

export default rootReducer;
