function X = ScatteringGaussian(E, hsize, sigma)
%SCATTERINGGAUSSIAN Summary of this function goes here
f = fspecial('gaussian',hsize, sigma);
X = conv2(E, f, 'same');
end

