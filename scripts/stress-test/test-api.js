import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  stages: [
    { duration: '1m', target: 30 },  // Ramp up to 20 virtual users over 1 minute
    { duration: '1m', target: 20 },  // Stay at 20 virtual users for 1 minutes
    { duration: '1m', target: 0 },   // Ramp down to 0 virtual users over 1 minute
  ],
};

export default function () {
  http.get('http://localhost:8000/api/v1/users/');
  sleep(0.3);  // Sleep for 0.3 second between requests
}