<div class="breadcrumbs">
<a href="projects.html" class="breadcrumb">Projects</a> > 
<a href="programming_projects.html" class="current-breadcrumb">Programming Projects</a>
</div>

# Dynamically Textured Sun

https://github.com/larsendt/dynamic-tex

<img src="img/mini_dynamic_tex.png" class="thumb">This was a project I built
for an Advanced Graphics class. It uses the shaders from the warping project
below to texture a sphere and create a sun-like effect. In addition to the
warping shader, the texture undergoes an equirectangular projection
(similar to a Mercator projection) and a horizontal blending stage to make
it apply cleanly without seams or distortion on the sphere. After the
texture is wrapped around the sphere, the resulting image is copied to a
framebuffer and a god-ray (or Crepuscular ray) shader is applied to give
the sphere the glowing effect.

On Youtube: http://youtu.be/4KthEQq7fdA


# Procedural Warping Texture in GLSL

https://github.com/larsendt/glsl-warping

<img src="img/warping.png" class="thumb">I wrote this project for fun over the
2011/2012 winter break. The inspiration came from <a
href="http://www.iquilezles.org/www/articles/warp/warp.htm">here</a>. The
project is written mostly in Python, which sets up a viewport and a framebuffer
and deals with all the input, but most of the magic is in the shaders. The
(GLSL) shaders generate a perlin noise texture and then distort it and color it
with several more Perlin noise textures. Nearly everything is done in the
shader, including the Perlin noise.

<a href="warping/warping.html">Here's a live demo in WebGL.</a> (Note: requires
a moderately powerful graphics card and a browser than can do WebGL.)

On Youtube: http://youtu.be/oUq5B4XukBo

(As a sidenote, <a href="http://www.iquilezles.org/">Inigo's site</a> is the
craziest and most amazing collection of realtime graphics work I've ever seen.
He's partially responsible for one of the <a
href="https://www.youtube.com/watch?v=jB0vBmiTr6o">greatest 4K intros
ever</a>).


# OpenCL N-Body Simulator

https://github.com/larsendt/opencl-nbody

<img src="img/nbody.png" class="thumb">This is probably the prettiest thing
I've ever built (maybe only contested by the dynamically textured sun or the
glsl warping demo). I built it, like the Marching Cubes terrain above, for the
Advanced Graphics class. This is the first (and only significant) OpenCL
application I've written. The n-body calculations are done entirely in OpenCL.
The main C++ application stores and draws the state of the particles, and then
passes position and velocity and mass of each particle to the OpenCL kernel
which calculates the next state. My laptop's 560M can do 1024 particles at ~40
FPS.

On Youtube: http://youtu.be/lMWt3LCbsYQ

The framerate is terrible in this video, but I swear it runs great normally.


# Hashtable

https://github.com/larsendt/hashtable

<img src="img/hashtable.png" class="thumb">I started this project in June 2012
to refresh my C skills. It's a very simple hashtable implementation in pure C.
It's reasonably stable and pretty fast. It can do 1 million inserts in about a
quarter of a second with static-size keys and a pre-allocated table (Core
i5-2430M @ 2.4GHz). It uses MurmurHash as the internal hashing algorithm. It's
BSD licensed (so feel free to use it!).
