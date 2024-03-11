select salary,dense_rank() over (order by sal desc) dens_rank from employee where dens_rank=2;
