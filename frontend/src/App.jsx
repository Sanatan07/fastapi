import React, { useState, useEffect } from 'react';

const App = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/')
      .then((response) => response.json())
      .then((json) => setData(json))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>API DATA</h1>
      {data ? (
        <p>Message: {data.message}</p>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default App;