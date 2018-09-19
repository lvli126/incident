N_FILE = 4096;
N_IMGS = 1024;
N_SIZE = 256;
N_THETA_LARGE = 256;
N_THETA_SMALL = 64;

prefix = 'SFP_SINO_';
suffix = ',mat';
tic
for i = 1 : N_FILE
    filename = [prefix, num2str(i), suffix];
    [phantom, sinogram] = GenerateSheppLoganAndSinogramPair(N_IMGS, N_SIZE, N_THETA_LARGE, 0.1);
    sino_tmp = sinogram(:,:,1);
    n_s = size(sino_tmp, 1);
    sinogram2 = zeros(n_s, N_THETA_LARGE, N_IMGS);
    for j = 1 : N_IMGS
        sino_tmp = sinogram(:,:,j);
        sino_m = imresize(sino_tmp, [n_s, N_THETA_SMALL]);
        sino_s = imresize(sino_m, [n_s, N_THETA_LARGE]);
        sinogram2(:, :, j) = sino_s;
    end
    save(filename, 'phantom','sinogram','sinogram2');
    time_cost = toc;
    time_remain = time_cost*(N_FILE/i-1);
    disp(['FID = ', num2str(i), ' Time remain = ', num2str(time_remain), 'seconds.']);
end