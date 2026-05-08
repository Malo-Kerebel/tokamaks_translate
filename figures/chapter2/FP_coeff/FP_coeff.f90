program FP_coeff

  REAL :: pi, deux_sqrtpi
  REAL :: x, x2, x_max, dx, phi, phi_prime, psi
  INTEGER :: n, n2

  n = 1000
  n2 = 100000
  x_max = 4

  pi = 3.1415926
  deux_sqrtpi = 2 / sqrt(pi)

  open(10, file="phi.dat", form="formatted", status="replace")
  open(20, file="psi.dat", form="formatted", status="replace")
  open(30, file="phi-psi.dat", form="formatted", status="replace")

  DO i=0,n

    x = i * x_max / n

    dx = x/n2
    x2 = 1*x/n2 * 1*x/n2
    phi = exp(-x2)*dx
    DO j=2,n2
      x2 = (j)*x/n2 * (j)*x/n2
      phi = phi + exp(-x2)*dx
    end DO
    phi = phi * deux_sqrtpi

    phi_prime = deux_sqrtpi * exp(-x*x)

    psi = (phi - x*phi_prime) / (2 * x*x)

    write(10, *) x, phi
    write(20, *) x, psi
    write(30, *) x, phi-psi
  end DO

 end program FP_coeff
