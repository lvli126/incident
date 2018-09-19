prefix_in = 'SPF'; suffix = '.mat';
prefix_out = 'SPF_s';
tic;
n_total_file = 1024;
sz0 = 128;
sz1 = 64;
for id = 1 : n_total_file
    filename_in = [prefix_in, num2str(id), suffix];    
    load(filename_in);
    X = resize_multiple(X, sz0, sz0, sz1, sz1);
    filename_out = [prefix_out, num2str(id), suffix];
    save(filename_out,'X');
    time_cost = toc;
    time_remain = time_cost * (n_total_file/id - 1);
    disp(['ID = ', num2str(id), ' Time remain = ' , num2str(time_remain)]);
end