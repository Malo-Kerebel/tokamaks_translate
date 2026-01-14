program potential

  REAL :: pi, epsilon_0, e, lambda_D, r, r_max
  REAL :: x, phi, phi_shield
  INTEGER :: n

  n = 100

  lambda_D = 5e-5
  r_max = 2.05 * lambda_D
  pi = 3.1415926
  epsilon_0 = 8.85418782e-12
  e = 1.602176620e-19

  open(10, file="potential.dat", form="formatted", status="replace")
  open(20, file="potential_shield.dat", form="formatted", status="replace")

  DO i=1,n
    IF (modulo(n, 10) .eq. 0) THEN
        print *, i, "/", n
    END IF
    r = i * r_max / n
    x = r/lambda_D
    phi = e / (4*pi*epsilon_0*x*lambda_D)
    phi_shield = e / (4*pi*epsilon_0*r * exp(sqrt(2.0) * x))

    write(10, *) x, phi
    write(20, *) x, phi_shield
  end DO

 end program potential
