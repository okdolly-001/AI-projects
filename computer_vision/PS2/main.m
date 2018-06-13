clc; clear all; close all; profile on;

im = imread('jupiter.jpg'); 
centers = detect_radii(im,  0);

