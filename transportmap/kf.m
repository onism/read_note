  function [x P] = kf(F,Q,H,R,x, P, z)
    x_ = F*x;
    P_ = F*P*F' + Q;
    K = (P_ * H') / (H*P_*H' + R);
    x = x_ + K*(z - H*x_);
    P = P_ - K*H*P_;
  end