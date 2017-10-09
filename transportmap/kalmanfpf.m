% Example: (1D point mass)
%  >> est = filter_kalman([1 1;0 1], [1 0], .1*eye(2), .1);
%  >> x = [0 0]';
%  >> P = .1*eye(2);
%  >> [x P] = est(x,P,  4); % x=[3.1 1.0]
%  >> [x P] = est(x,P,  7); % x=[6.4 2.2]
%  >> [x P] = est(x,P, 10); % x=[9.7 2.8]
clear;
close all
dbstop if error
F = [1 1; 0 1];
H = [1 0];
Q = 0.1 * eye(2);
R = 1;
T = 50;
x(:,1) = [3.1 1.0];
z(:,1) = H * x(:,1) + R * randn;
for t = 2 : T
    x(:,t) = F * x(:,t-1) + Q * randn(2,1);
    z(:,t) = H * x(:,t) + R * randn;
end
x_est = [0 0]';
P_est = .1*eye(2);
for t = 1 : T
    [x_est P_est] = kf(F,Q,H,R,x_est, P_est, z(:,t));
    kf_x(:,t) = x_est;
end
figure
hold on
plot(kf_x(1,:),'b*-')
plot(x(1,:),'ro-')

N_sample = 10;
x_est = [0 0]';
P_est = .1*eye(2);
particles =  gen_gms(1,x_est,P_est,N_sample);
for t = 1 : T
    [ particles ] = fpf( F,Q,H,R,particles, z(:,t) );
    fpf_x(:,t) = mean(particles);
end

plot(fpf_x(1,:),'kd-')

  
