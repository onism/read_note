function [ particles ] = fpf( F,Q,H,R,particles, z )
  x_pred = zeros(size(particles));
  for i = 1 : size(particles,2)
      x_pred(:,i) = F * particles(:,i) + Q * randn(2,1);
  end
  for l = 1 : 100
      P_ = cov(x_pred');
      K = (P_ * H');
      mean_x = mean(x_pred,2);
      for i = 1 : size(x_pred,2)
          x_pred(:,i) = x_pred(:,i) + Q * randn(2,1) + K*(z - 0.5 * H *(x_pred(:,i) + mean_x) );
      end
  end
  particles = x_pred;
end

