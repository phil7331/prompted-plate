import React from 'react';

const Card = ({ imageUrl, name, calories, protein, fat, carbs }) => {
  return (
    <div style={styles.card}>
      <img src={imageUrl} alt={name} style={styles.image} />
      <div style={styles.content}>
        <h2 style={styles.name}>{name}</h2>
        <ul style={styles.macros}>
          <li><strong>Calories:</strong> {calories} kcal</li>
          <li><strong>Protein:</strong> {protein} g</li>
          <li><strong>Fat:</strong> {fat} g</li>
          <li><strong>Carbs:</strong> {carbs} g</li>
        </ul>
      </div>
    </div>
  );
};

const styles = {
  card: {
    maxWidth: 320,
    border: '1px solid #ddd',
    borderRadius: 8,
    overflow: 'hidden',
    boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
    fontFamily: 'Arial, sans-serif',
    margin: '1rem auto',
  },
  image: {
    width: '100%',
    height: 180,
    objectFit: 'cover',
  },
  content: {
    padding: '1rem',
  },
  name: {
    margin: '0 0 0.5rem 0',
    fontSize: '1.25rem',
    color: '#333',
  },
  macros: {
    listStyleType: 'none',
    padding: 0,
    margin: 0,
    color: '#555',
  },
};

export default Card;
