# π Approximator using Collisions

This Python project visualizes and simulates an amusing fact of linear elastic collisions: the number of elastic collisions between two blocks (one significantly more massive than the other) and a wall can approximate the digits of π.

This project was inspired by 3b1b and his video on the subject: https://www.youtube.com/watch?v=6dTyOl1fmDo&t=7s&ab_channel=3Blue1Brown
I set out to verify for myself the suprising facts presented in it and with this project, I did.

## 📌 Principle

If one block is `100^n` times heavier than another, and both undergo linear elastic collisions with a wall, the total number of collisions equals the first `n` digits of π.

## 🧪 How It Works

- There are two blocks: one with mass `m`, another with mass `100^n * m`
- Initially The heavier block moves toward the lighter block and a wall with unit velocity and made to collide
- Each elastic collision (with wall or other block) is counted
- Total collisions = Digits of π 

## 📊 Visualizations

- `plot_VelocityVsVelocity`: Phase diagram of block root mass * velocities versuse each other to form an circle
(conservation of energy)
- `plot_VelocityVsCollision`: Smaller block velocity vs. collision count with various fits 
(fun)

## 🛠 Requirements

- Python 3.8+
- matplotlib
- numpy
- scipy