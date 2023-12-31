
// A random walker class!

class Walker {
  PVector location;
  PVector velocity;
  PVector acceleration;

  ArrayList<PVector> history;

  PVector noff;


  Walker() {
    location = new PVector(width/2, height/2);
    history = new ArrayList<PVector>();
    noff = new PVector(random(1000), random(1000));
    velocity = new PVector();
    acceleration = new PVector();
  }

  void display() {
    stroke(0);
    fill(175);
    rectMode(CENTER);
    rect(location.x, location.y, 16, 16);

    beginShape();
    stroke(0);
    noFill();
    for (PVector v: history) {
      vertex(v.x, v.y);
    }
    endShape();
  }

  // Randomly move up, down, left, right, or stay in one place
  void walk() {
    
    noff.add(0.01, 0.01, 0);
    acceleration.x = map(noise(noff.x), 0, 1, -1, 1);
    acceleration.y = map(noise(noff.y), 0, 1, -1, 1);
    acceleration.mult(0.1);

    //noff.add(0.6, 0.6, 0);

    velocity.add(acceleration);
    velocity.limit(1);
    location.add(velocity);
    

    history.add(location.get());
    if (history.size() > 1000) {
      history.remove(0);
    }

    // Stay on the screen
    location.x = constrain(location.x, 0, width-1);
    location.y = constrain(location.y, 0, height-1);
  }
}
