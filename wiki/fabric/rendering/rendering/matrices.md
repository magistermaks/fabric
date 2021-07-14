## Matrices
[Back](rendering.md)

The `MatrixStack` class allows for classical matrix transformations such as scale, translate and rotate, the state of this matrix can saved and restored with `push()` and `pop()` calls. 

Example:
```java
// store current state
matrices.push();

// translate matrix
matrices.translate(0.5f, 0.5f, 0.5f);

// scale matrix
matrices.scale(2.0f, 2.0f, 2.0f);

// rotate matrix
matrices.multiply( /* quaternion */ )

// restore state prior to translating and scaling  
matrices.pop();
```

Quaternions are used to represent rotation in 3D space, learn about them here: [Quaternions](quaternions.md).

A reference to a particular state of the matrix stack can be obtained by calling `peek()`:

```java
MatrixStack.Entry matrix = matrices.peek();

// get Normal matrix and Model matrix
Matrix4f model = matrix.getModel();
Matrix3f normal = matrix.getNormal();
```

Model matrix represents the all transformations of model geometry and is used to translate points from _Model Space_ to _World Space_. And the Normal matrix is used for light and shading calculations. 

The basic concept behind this is explained on the great [Learn OpenGL](https://learnopengl.com/Getting-started/Transformations) website.

