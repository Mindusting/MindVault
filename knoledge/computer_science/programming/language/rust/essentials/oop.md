---
aliases: [OOP en Rust]
author: Mindusting
corrected: false
creationDate: 2026-10-04 02:44:57
headerFile: false
modificationDate: 2026-10-04 02:48:07
rating: 
tags: [Programming, Rust, OOP]
---

# OOP EN RUST

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

```rust
struct Vec2d {
    x: f32,
    y: f32
}

impl Vec2d {
    pub fn new(x: f32, y: f32) -> Vec2d {
        Vec2d {x: x, y: y}
    }

    pub fn mag(&self) -> f32 {
        ((self.x * self.x) + (self.y * self.y)).sqrt()
    }

    pub fn cos(&self) -> f32 {
        self.x / self.mag()
    }

    pub fn sin(&self) -> f32 {
        self.y / self.mag()
    }

    pub fn tan(&self) -> f32 {
        self.y / self.x
    }

    pub fn norm(&mut self) -> &mut Vec2d {
        let mag = self.mag();
        self.x /= mag;
        self.y /= mag;
        self
    }

    pub fn is_null(&self) -> bool {
        self.x == 0.0 && self.y == 0.0
    }

    pub fn is_unit(&self) -> bool {
        ((self.x * self.x) + (self.y * self.y)) == 1.0
    }

    pub fn to_string(& self) -> String {
        format!("Vec2d(x: {}, y: {})", self.x, self.y)
    }

    pub fn add(&self, other: &Vec2d) -> Vec2d {
        Vec2d::new(
            self.x + other.x,
            self.y + other.y
        )
    }

    pub fn sub(&self, other: &Vec2d) -> Vec2d {
        Vec2d::new(
            self.x - other.x,
            self.y - other.y
        )
    }

    pub fn mul(&self, other: &Vec2d) -> Vec2d {
        Vec2d::new(
            self.x * other.x,
            self.y * other.y
        )
    }

    pub fn div(&self, other: &Vec2d) -> Vec2d {
        Vec2d::new(
            self.x / other.x,
            self.y / other.y
        )
    }
}
```