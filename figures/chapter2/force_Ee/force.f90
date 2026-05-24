program Force

  DOUBLE PRECISION :: pi, eps_0, m_e, e, coul_log, n_e, D
  DOUBLE PRECISION :: tau_s, v_e_min, v_e_max
  REAL :: v_e, out
  INTEGER :: n

  n = 1000

  v_e_min = 0*1e1
  v_e_max = 3000

  pi = 3.1415926
  eps_0 = 8.85418782e-12
  m_e = 9.109383713e-37
  e = 1.602176634e-19
  n_e = 1e20

  D = 2/e

  coul_log = 17

  open(10, file="force.dat", form="formatted", status="replace")
  open(20, file="Ee.dat", form="formatted", status="replace")

  DO i=0,n

    v_e = v_e_min + i * (v_e_max - v_e_min) / n

    tau_s = 4 * pi * eps_0*eps_0 * m_e*m_e * v_e*v_e*v_e / (3 * n_e * e*e*e*e * coul_log)

    if (v_e < 1000 .AND. m_e*100 * v_e / 2.2e-33 < 8) then
      out = m_e*100 * v_e / 2.2e-33
      write(10, *) v_e, out
    else
      if (m_e*2000 * v_e / tau_s < 8) then
        out = m_e*2000 * v_e / tau_s
        write(10, *) v_e, out
      end if
    end if
    out = D * e
    write(20, *) v_e, out
  end DO

 end program Force
