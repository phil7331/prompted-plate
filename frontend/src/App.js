import React from 'react';
import Card from './components/Card';
import ImageUpload from './components/ImageUpload';

function App() {
  const exampleDish = {
    name: "Grilled Chicken Salad",
    imageUrl: "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=800&q=80",
    calories: 350,
    protein: 30,
    fat: 12,
    carbs: 20,
  };

  return (
    <div style={{ padding: '2rem' }}>
      <ImageUpload />
      
      <div style={{ marginTop: '3rem', display: 'flex', justifyContent: 'center' }}>
        <Card
          name={exampleDish.name}
          imageUrl={exampleDish.imageUrl}
          calories={exampleDish.calories}
          protein={exampleDish.protein}
          fat={exampleDish.fat}
          carbs={exampleDish.carbs}
        />
      </div>
    </div>
  );
}

export default App;
