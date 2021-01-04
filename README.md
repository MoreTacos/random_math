# One Textbook A Day
From scratch fluid simulation built entirely with Rust!

<img src="./fluid.jpg" alt="Fluid simulation" width="360" height="270">

## About The Project
I was trying to learn about fluid simulations - specifically SPH fluid simulations from the 2014 Eurograph guide on state of the art fluid simulations - and decided to make my own implementation in Rust.

## Built With
The project is built entirely in Rust! The shaders are built with GLSL and compiled into SPIR-V. The project uses wGPU, which is a Rust library that uses basically the same implementation as Vulkan, but can also interface into Metal and other graphics API's. The crates are seperated into a main binary crate that runs the example, and three helper library crates: scene, sph and utils. The scene crate is for all utility related to displaying the instances. The sph crate is for all physics related calculations. And the utils crate if for structs that are common to both the scene and sph crate.

## Usage
You will need to download rustc and cargo. Once you do, run the command "cargo run" in the base directory. If you have any trouble please send me an email.

## Contact
Davide Radaelli - @daviderady - daviderady AT gmail DOT com
Project Link: https://github.com/MoreTacos/sph
