	PROGRAM ADD_BURSTS

	! Adds sed''s corresponding to 2 different bursts of star formation.
	! The sed for each burst must be computed previously.

	! Array declaration
	include 'SSP_4.dec'
	include 'SSP_13.dec'
	parameter (imw=30000) 		!	lower than in SSP_0.dec
	parameter (its=5000,maxbu=2)
	character*128 temp,argu*1024,atlas,shell*32
	logical stelib
	real tb1(its),tb2(its),tb3(maxbu*its),fi(40),fc(40),tx(3)
	real w(imw),h(imw),fl1(imw,its),fl2(imw,its),rsn(0:4)
	real  bflx1(its),  bflx2(its),  bflx3(maxbu*its)
	real  strm1(its),  strm2(its),  strm3(maxbu*its)
	real   sfr1(its),   sfr2(its),   sfr3(maxbu*its)
	real  evfl1(its),  evfl2(its),  evfl3(maxbu*its)
	real  snbr1(its),  snbr2(its),  snbr3(maxbu*its)
	real  pnbr1(its),  pnbr2(its),  pnbr3(maxbu*its)
	real  bhtn1(its),  bhtn2(its),  bhtn3(maxbu*its)
	real  sntn1(its),  sntn2(its),  sntn3(maxbu*its)
	real  wdtn1(its),  wdtn2(its),  wdtn3(maxbu*its)
	real  rmtm1(its),  rmtm2(its),  rmtm3(maxbu*its)
	real  toff1(its),  toff2(its),  toff3(maxbu*its)
	real bolms1(its), bolms2(its), bolms3(maxbu*its)
	real gasms1(its), gasms2(its), gasms3(maxbu*its)
	real galms1(its), galms2(its), galms3(maxbu*its)
	real   rml1(its),   rml2(its),   rml3(maxbu*its)
	real   rdp1(its),   rdp2(its),   rdp3(maxbu*its)
	real   sn11(its),   sn12(its),   sn13(maxbu*its)
	real   sn21(its),   sn22(its),   sn23(maxbu*its)
	real   sn31(its),   sn32(its),   sn33(maxbu*its)
	real   sn41(its),   sn42(its),   sn43(maxbu*its)

	real*8 td0(2),t2,tl,t(its),z(its)

	data ihrd/0/,atlas/' '/

	! Check filter file assignment
	j=ifilter()
	if (j == 0) then
		write (6,'(2a)') char(7),'Please assign correct filter file'
		write (6,'(2a)') char(7),'Use command: stdfilt'
		stop
	endif

	! Information message
	write (6,*)
	write (6,*) ' This program computes the combined sed for 2 bursts of star formation.'
	write (6,*) ' The sed corresponding to each burst must be computed first.'
	write (6,*) ' Each burst is characterized by the beginning time (in Gyr) and'
	write (6,*) ' the burst strength (absolute, NOT relative).'
	write (6,*) ' Each individual burst can follow an arbitrary star formation law.'
	write (6,*)
	
	! Ask for independent sed files
	write (6,'(x,a,$)') 'First BC_GALAXEV sed in file  = '
	read (5,'(a)',end=10) name1
	call chaext(name1,'ised',mm)
	write (6,'(x,a,$)') 'Second BC_GALAXEV sed in file = '
	read (5,'(a)',end=10) name2
	call chaext(name2,'ised',mm)

	! Ask for burst information
	st=0.
	do i=1,2
2	write (6,100) i
100	format(' Burst',i2,': Beginning time (Gyr), Burst amplitude = ',$)
	! Found a problem with gfortran in reading more arguments that have been actually entered.
	! Use function nargu(argu) to count how many arguments have been entered
	! read (5,'(3e20.0)',err=2,end=10) td0(i),s(i),tshift
	read (5,'(a)',end=10) argu
	ngu = nargu(argu)
	read (argu,*,err=2) (tx(j),j=1,ngu)
	if (ngu == 2) then
		td0(i)=tx(1)
		  s(i)=tx(2)
		tshift=0.
	elseif (ngu == 3) then
		td0(i)=tx(1)
		  s(i)=tx(2)
		tshift=tx(3)
	else
		goto 2
	endif
	td0(i)=td0(i)*1.E9
	tshift=tshift*1.E9
	enddo
	shift=td0(1)
	if (td0(2) < shift) shift=td0(2)
	if (tshift == 0.) tshift=shift
	td0(1)=td0(1)-shift
	td0(2)=td0(2)-shift
	t0(1)=td0(1)
	t0(2)=td0(2)

	! Read first burst file
	write (6,*)
	write (6,'(2a)') ' Reading file ',name1
	imx=irec_check(1,name1)
	open (1,file=name1,form='unformatted',status='old')
	read (1) nsteps,(tb1(i),i=1,nsteps),ml,mu,iseg,(xx(i),lm(i),um(i),baux(i),cn(i),cc(i),i=1,iseg),totm,totn,avs,jo,tauo,id,ttt,ttt,ttt,ttt,id,id,igw,stelib
	write (6,*) nsteps,' steps'
	read (1,err=15) inl,(w(i),i=1,inl),nbrite,kdef,sissa20
	! write (6,*) 'nbrite, kdef, sissa20 =',nbrite, kdef, sissa20
	goto 16
	! Old format model (nbrite = 0)
15	nbrite   = 0
	kdef    = 0
	sissa20 = .false.
16	write (6,*) inl,' lambda points'
	do n=1,nsteps
	if (imx > 0) then
		read (1) inl,(fl1(i,n),i=1,inl),inx,(fl1(i,n),i=inl+1,inl+inx)
	else
		read (1) inl,(fl1(i,n),i=1,inl)
		inx=0
	endif
	enddo
	mw=inl+imx
	write (6,*) inl,' wavelength points per record'
	write (6,*) inx,' spectral index points per record'
	write (6,*)  mw,' total points per record'
	read (1,end=21) nsteps,( bflx1(i), i=1,nsteps)
	read (1,end=21) nsteps,( strm1(i), i=1,nsteps)
	read (1,end=21) nsteps,(  sfr1(i), i=1,nsteps)
	read (1,end=21) nsteps,( evfl1(i), i=1,nsteps)
	read (1,end=21) nsteps,( snbr1(i), i=1,nsteps)
	read (1,end=21) nsteps,( pnbr1(i), i=1,nsteps)
	read (1,end=21) nsteps,( bhtn1(i), i=1,nsteps)
	read (1,end=21) nsteps,( sntn1(i), i=1,nsteps)
	read (1,end=21) nsteps,( wdtn1(i), i=1,nsteps)
	read (1,end=21) nsteps,( rmtm1(i), i=1,nsteps)
	read (1,end=21) nsteps,( toff1(i), i=1,nsteps)
	read (1,end=21) nsteps,(bolms1(i), i=1,nsteps)
	read (1,end=21) nsteps,(gasms1(i), i=1,nsteps)
	read (1,end=21) nsteps,(galms1(i), i=1,nsteps)
	read (1,end=21) nsteps,(  rml1(i), i=1,nsteps)
	read (1,end=21) nsteps,(  rdp1(i), i=1,nsteps)
	read (1,end=21) nsteps,(  sn11(i), i=1,nsteps)
	read (1,end=21) nsteps,(  sn21(i), i=1,nsteps)
	read (1,end=21) nsteps,(  sn31(i), i=1,nsteps)
	read (1,end=21) nsteps,(  sn41(i), i=1,nsteps)
21	close (1)

	! Read second burst file
	if (name1 == name2) then
		write (6,*)
		write (6,'(2a)') ' Copying file ',name2
		do n=1,nsteps
		tb2(n)    = tb1(n)
		bflx2(n)  = bflx1(n)
		strm2(n)  = strm1(n)
		 sfr2(n)  = sfr1(n)
		evfl2(n)  = evfl1(n)
		snbr2(n)  = snbr1(n)
		pnbr2(n)  = pnbr1(n)
		bhtn2(n)  = bhtn1(n)
		sntn2(n)  = sntn1(n)
		wdtn2(n)  = wdtn1(n)
		rmtm2(n)  = rmtm1(n)
		toff2(n)  = toff1(n)
		bolms2(n) = bolms1(n)
		gasms2(n) = gasms1(n)
		galms2(n) = galms1(n)
		rml2(n)   = rml1(n)
		rdp2(n)   = rdp1(n)
		sn12(n)   = sn11(n)
		sn22(n)   = sn21(n)
		sn32(n)   = sn31(n)
		sn42(n)   = sn41(n)
		do i=1,mw
		fl2(i,n) = fl1(i,n)
		enddo
		enddo
		ksteps=nsteps
	else
		write (6,*)
		write (6,'(2a)') ' Reading file ',name2
		im2=irec_check(2,name2)
		open (2,file=name2,form='unformatted',status='old')
		read (2) ksteps,(tb2(i),i=1,ksteps),ml,mu,iseg,(xx(i),lm(i),um(i),baux(i),cn(i),cc(i),i=1,iseg),totm,totn,avs,jo,tauo,id,ttt,ttt,ttt,ttt,id,id,igw,stelib
		read (2) iml,(w(i),i=1,iml)
		if (iml.ne.inl.or.im2.ne.imx) then
			write (6,*) 'Wavelength scales differ.',inl,iml,imx,iml
			stop
		endif
		write (6,*) ksteps,' steps'
		do n=1,ksteps
		if (imx > 0) then
			read (2) inl,(fl2(i,n),i=1,inl),inx,(fl2(i,n),i=inl+1,inl+inx)
		else
			read (2) inl,(fl2(i,n),i=1,inl)
			inx=0
		endif
		enddo
		write (6,*) inl,' wavelength points per record'
		write (6,*) inx,' spectral index points per record'
		write (6,*)  mw,' total points per record'
		read (2,end=22) ksteps,( bflx2(i), i=1,ksteps)
		read (2,end=22) ksteps,( strm2(i), i=1,ksteps)
		read (2,end=22) ksteps,(  sfr2(i), i=1,ksteps)
		read (2,end=22) ksteps,( evfl2(i), i=1,ksteps)
		read (2,end=22) ksteps,( snbr2(i), i=1,ksteps)
		read (2,end=22) ksteps,( pnbr2(i), i=1,ksteps)
		read (2,end=22) ksteps,( bhtn2(i), i=1,ksteps)
		read (2,end=22) ksteps,( sntn2(i), i=1,ksteps)
		read (2,end=22) ksteps,( wdtn2(i), i=1,ksteps)
		read (2,end=22) ksteps,( rmtm2(i), i=1,ksteps)
		read (2,end=22) ksteps,( toff2(i), i=1,ksteps)
		read (2,end=22) ksteps,(bolms2(i), i=1,ksteps)
		read (2,end=22) ksteps,(gasms2(i), i=1,ksteps)
		read (2,end=22) ksteps,(galms2(i), i=1,ksteps)
		read (2,end=22) ksteps,(  rml2(i), i=1,ksteps)
		read (2,end=22) ksteps,(  rdp2(i), i=1,ksteps)
		read (2,end=22) ksteps,(  sn12(i), i=1,ksteps)
		read (2,end=22) ksteps,(  sn22(i), i=1,ksteps)
		read (2,end=22) ksteps,(  sn32(i), i=1,ksteps)
		read (2,end=22) ksteps,(  sn42(i), i=1,ksteps)
22		close (2)
	endif

	! Build combined time scale for 2 bursts
	mix=0
	if (ksteps /= nsteps) then
		mix=1
	else
		do i=1,nsteps
		if (td0(1)+dble(tb1(i)).ne.td0(2)+dble(tb2(i))) mix=1
		enddo
	endif
	if (mix > 0) then
		k=0
		do i=1,nsteps
		k=k+1
		t(k)=td0(1)+dble(tb1(i))
		z(k)=1.
		enddo
		k1=k
		do i=1,ksteps
		k=k+1
		t(k)=td0(2)+dble(tb2(i))
		z(k)=2.
		enddo
		t2=t(k1+1)

		! Sort time scale
		call dsort2(k,t,z)

		! Suppress duplicate entries
		n=1
		tb3(n)=t(n)
		do i=2,k
		tl=0.
		if (t(i-1) <= 0.) then
			if (t(i) > 0.) then
				tl=1.
			else
				tl=0.
			endif
		else
			tl=dlog10(t(i))-dlog10(t(i-1))
		endif
		if (tl > 1.E-6) then
			n=n+1
			t(n)=t(i)
			z(n)=z(i)
			tb3(n)=t(n)
		else
			! write (6,*) 'Suppress t =',t(i)
		endif
		if (t(n) > tb1(nsteps)) then
			n=n-1
			goto 3
		endif
		enddo
3		msteps=n
		write (6,*)
		write (6,*) msteps,' different time steps in combined sed'
	
		! Find time steps for which first burst exists by itself
		do i=1,msteps
		if (t(i) > t2) then
			i1=i-1
			goto 4
		endif
		enddo
4		write (6,'(i12,a,1pe10.3,a)') i1,'  steps for first burst alone, up to age',t(i1),' yr'
		interp=1
	else
		msteps=nsteps
		interp=0
		do i=1,msteps
		tb3(i)=tb1(i)
		enddo
	endif

	! Ask for output file name
	io=5
	jdef=jjdef(name1)
	lun=-1
	ioption=99
	ldef=0
	call name_sed(lun,jun,0,ihrd,ioption,jdef,ldef,ml,mu,temp,atlas)

	! Open temporay file to store output file name and kdef (needed to build fits file)
	open (2020,file='csp_fits.tmp')
	if (index(shell(),'csh') > 0) then
		! csh in use
		write (2020,'(a)')    'setenv name0 ' // trim(temp) // '.ised'
		write (2020,'(a,i5)') 'setenv ioptn ',kdef
	else
		! zsh or bash in use
		write (2020,'(a)')      'export name0="' // trim(temp) //'.ised"'
		write (2020,'(a,i5,a)') 'export ioptn="',kdef,'"'
	endif
	close (2020)
	! Write in file fort.2001 current time scale (needed to build fits file)
	write (2001,'(a)') '# age-yr'
	do i=1,msteps
	write (2001,'(1pe12.5)') tb3(i)+tshift
	enddo
	close (2001)

	! Write time scale, IMF, and wavelength scale in output file
	write (lun) msteps,(tb3(i)+tshift,i=1,msteps),ml,mu,iseg,(xx(i),lm(i),um(i),baux(i),cn(i),cc(i),i=1,iseg),totm,totn,avs,io,tau,id,t0,s,name1,name2,igw,stelib
	write (lun) inl,(w(i),i=1,inl),nbrite,kdef,sissa20
	if (nbrite > 0 .and. sissa20) then
		! SISSA20 tracks with zero flux in first time steps
		! Here nbrite = ndark + 1 = first luminous record. Write ndark + 1 zero flux records, extra one for t = 0.
		do lb=1,nbrite
		call dark_galaxy(lun,tb3(lb)+tshift)
		enddo
	endif
	do n=1,msteps
	if (interp == 0) then
		! Add bursts without interpolation in time
		do i=1,mw
		h(i)=s(1)*fl1(i,n)+s(2)*fl2(i,n)
		enddo
		tb3(n)    = tb1(n)
		bflx3(n)  = s(1)*bflx1(n)  + s(2)*bflx2(n)
		strm3(n)  = s(1)*strm1(n)  + s(2)*strm2(n)
		sfr3(n)   = s(1)* sfr1(n)  + s(2)* sfr2(n)
		evfl3(n)  = s(1)*evfl1(n)  + s(2)*evfl2(n)
		snbr3(n)  = s(1)*snbr1(n)  + s(2)*snbr2(n)
		pnbr3(n)  = s(1)*pnbr1(n)  + s(2)*pnbr2(n)
		bhtn3(n)  = s(1)*bhtn1(n)  + s(2)*bhtn2(n)
		sntn3(n)  = s(1)*sntn1(n)  + s(2)*sntn2(n)
		wdtn3(n)  = s(1)*wdtn1(n)  + s(2)*wdtn2(n)
		rmtm3(n)  = s(1)*rmtm1(n)  + s(2)*rmtm2(n)
		toff3(n)  = s(1)*toff1(n)  + s(2)*toff2(n)
		bolms3(n) = s(1)*bolms1(n) + s(2)*bolms2(n)
		gasms3(n) = s(1)*gasms1(n) + s(2)*gasms2(n)
		galms3(n) = s(1)*galms1(n) + s(2)*galms2(n)
		rml3(n)   = s(1)*rml1(n)   + s(2)*rml2(n)
		rdp3(n)   = s(1)*rdp1(n)   + s(2)*rdp2(n)
		sn13(n)   = s(1)*sn11(n)   + s(2)*sn12(n)
		sn23(n)   = s(1)*sn21(n)   + s(2)*sn22(n)
		sn33(n)   = s(1)*sn31(n)   + s(2)*sn32(n)
		sn43(n)   = s(1)*sn41(n)   + s(2)*sn42(n)
	else
		if (n <= i1) then
			! First burst alone
			do i=1,mw
			h(i)=s(1)*fl1(i,n)
			enddo
			bflx3(n)  = s(1)*bflx1(n)
			strm3(n)  = s(1)*strm1(n)
			sfr3 (n)  = s(1)*sfr1 (n)
			evfl3(n)  = s(1)*evfl1(n)
			snbr3(n)  = s(1)*snbr1(n)
			pnbr3(n)  = s(1)*pnbr1(n)
			bhtn3(n)  = s(1)*bhtn1(n)
			sntn3(n)  = s(1)*sntn1(n)
			wdtn3(n)  = s(1)*wdtn1(n)
			rmtm3(n)  = s(1)*rmtm1(n)
			toff3(n)  = s(1)*toff1(n)
			bolms3(n) = s(1)*bolms1(n)
			gasms3(n) = s(1)*gasms1(n)
			galms3(n) = s(1)*galms1(n)
			rml3(n)   = s(1)*rml1(n)
			rdp3(n)   = s(1)*rdp1(n)
			sn13(n)   = s(1)*sn11(n)
			sn23(n)   = s(1)*sn21(n)
			sn33(n)   = s(1)*sn31(n)
			sn43(n)   = s(1)*sn41(n)
		else
			! Combine both seds by linear interpolation in log t
			if (z(n) == 2.) then
				! Interpolate first sed
				! Locate sed at this age in first model and compute interpolatation coefficient
				to=t(n)-td0(1)
				call locate(tb1,nsteps,to,i)
				if (tb1(i) > 0.) then
					a=alog10(to/tb1(i))/alog10(tb1(i+1)/tb1(i))
				else
					a=to/tb1(i+1)
				endif
				! Locate sed at this age in second model
				to=t(n)-td0(2)
				call locate(tb2,ksteps,to,j)
				! Compute combined sed
				b=s(1)*(1.-a)
				a=s(1)*a
				c=s(2)
				do l=1,mw
				h(l)=b*fl1(l,i)+a*fl1(l,i+1)+c*fl2(l,j+1)
				enddo
				bflx3(n)  = b*bflx1(i)  + a*bflx1(i+1)  + c*bflx2(j+1)
				strm3(n)  = b*strm1(i)  + a*strm1(i+1)  + c*strm2(j+1)
				sfr3(n)   = b*sfr1(i)   + a*sfr1(i+1)   + c*sfr2(j+1)
				evfl3(n)  = b*evfl1(i)  + a*evfl1(i+1)  + c*evfl2(j+1)
				snbr3(n)  = b*snbr1(i)  + a*snbr1(i+1)  + c*snbr2(j+1)
				pnbr3(n)  = b*pnbr1(i)  + a*pnbr1(i+1)  + c*pnbr2(j+1)
				bhtn3(n)  = b*bhtn1(i)  + a*bhtn1(i+1)  + c*bhtn2(j+1)
				sntn3(n)  = b*sntn1(i)  + a*sntn1(i+1)  + c*sntn2(j+1)
				wdtn3(n)  = b*wdtn1(i)  + a*wdtn1(i+1)  + c*wdtn2(j+1)
				rmtm3(n)  = b*rmtm1(i)  + a*rmtm1(i+1)  + c*rmtm2(j+1)
				toff3(n)  = b*toff1(i)  + a*toff1(i+1)  + c*toff2(j+1)
				bolms3(n) = b*bolms1(i) + a*bolms1(i+1) + c*bolms2(j+1)
				gasms3(n) = b*gasms1(i) + a*gasms1(i+1) + c*gasms2(j+1)
				galms3(n) = b*galms1(i) + a*galms1(i+1) + c*galms2(j+1)
				rml3(n)   = b*rml1(i)   + a*rml1(i+1)   + c*rml2(j+1)
				rdp3(n)   = b*rdp1(i)   + a*rdp1(i+1)   + c*rdp2(j+1)
				sn13(n)   = b*sn11(i)   + a*sn11(i+1)   + c*sn12(j+1)
				sn23(n)   = b*sn21(i)   + a*sn21(i+1)   + c*sn22(j+1)
				sn33(n)   = b*sn31(i)   + a*sn31(i+1)   + c*sn32(j+1)
				sn43(n)   = b*sn41(i)   + a*sn41(i+1)   + c*sn42(j+1)
			elseif (z(n) == 1.) then
				! Interpolate second sed
				! Locate sed at this age in second model and compute interpolatation coefficient
				to=t(n)-td0(2)
				call locate(tb2,ksteps,to,i)
				if (tb2(i) > 0.) then
					a=alog10(to/tb2(i))/alog10(tb2(i+1)/tb2(i))
				else
					a=to/tb2(i+1)
				endif
				! Locate sed at this age in first model
				to=t(n)-td0(1)
				call locate(tb1,nsteps,to,j)
				! Compute combined sed
				b=s(2)*(1.-a)
				a=s(2)*a
				c=s(1)
				do l=1,mw
				h(l)=b*fl2(l,i)+a*fl2(l,i+1)+c*fl1(l,j+1)
				enddo
				bflx3(n)  = b*bflx2(i)  + a*bflx2(i+1)  + c*bflx1(j+1)
				strm3(n)  = b*strm2(i)  + a*strm2(i+1)  + c*strm1(j+1)
				sfr3(n)   = b*sfr2 (i)  + a*sfr2 (i+1)  + c*sfr1 (j+1)
				evfl3(n)  = b*evfl2(i)  + a*evfl2(i+1)  + c*evfl1(j+1)
				snbr3(n)  = b*snbr2(i)  + a*snbr2(i+1)  + c*snbr1(j+1)
				pnbr3(n)  = b*pnbr2(i)  + a*pnbr2(i+1)  + c*pnbr1(j+1)
				bhtn3(n)  = b*bhtn2(i)  + a*bhtn2(i+1)  + c*bhtn1(j+1)
				sntn3(n)  = b*sntn2(i)  + a*sntn2(i+1)  + c*sntn1(j+1)
				wdtn3(n)  = b*wdtn2(i)  + a*wdtn2(i+1)  + c*wdtn1(j+1)
				rmtm3(n)  = b*rmtm2(i)  + a*rmtm2(i+1)  + c*rmtm1(j+1)
				toff3(n)  = b*toff2(i)  + a*toff2(i+1)  + c*toff1(j+1)
				bolms3(n) = b*bolms2(i) + a*bolms2(i+1) + c*bolms1(j+1)
				gasms3(n) = b*gasms2(i) + a*gasms2(i+1) + c*gasms1(j+1)
				galms3(n) = b*galms2(i) + a*galms2(i+1) + c*galms1(j+1)
				rml3(n)   = b*rml2(i)   + a*rml2(i+1)   + c*rml1(j+1)
				rdp3(n)   = b*rdp2(i)   + a*rdp2(i+1)   + c*rdp1(j+1)
				sn13(n)   = b*sn12(i)   + a*sn12(i+1)   + c*sn11(j+1)
				sn23(n)   = b*sn22(i)   + a*sn22(i+1)   + c*sn21(j+1)
				sn33(n)   = b*sn32(i)   + a*sn32(i+1)   + c*sn31(j+1)
				sn43(n)   = b*sn42(i)   + a*sn42(i+1)   + c*sn41(j+1)
			endif
		endif
	endif

	! Write results
	! Standard model colors
	rsn(0) = snbr3(n)
	rsn(1) = sn13(n)
	rsn(2) = sn23(n)
	rsn(3) = sn33(n)
	rsn(4) = sn43(n)
	write (lun) inl,(h(i),i=1,inl),inx,(h(i),i=inl+1,inl+inx)
	call rf_color(10,tb3(n)+tshift,w,h,inl,lun,bflx3(n),strm3(n),sfr3(n),evfl3(n),rsn,pnbr3(n),bhtn3(n),sntn3(n),wdtn3(n),rmtm3(n),toff3(n),bolms3(n),gasms3(n),galms3(n),rml3(n),rdp3(n),sissa20)
	if (n > 1) call percent(6,n,msteps,'ADD_BURSTS ' // temp(1:nargo(temp)))
	! Guy Worthey Spectral indices
	inx2=inx/2
	do i=1,inx2
	fi(i)=h(inl+i)
	fc(i)=h(inl+inx2+i)
	enddo
	igw=0
	call gw_indices(tb3(n),fi,fc,lun,igw)
	enddo
	write (lun) msteps,(bflx3(i),i=1,msteps)
	write (lun) msteps,(strm3(i),i=1,msteps)
	write (lun) msteps,(sfr3(i),i=1,msteps)
	write (lun) msteps,(evfl3(i),i=1,msteps)
	write (lun) msteps,(snbr3(i),i=1,msteps)
	write (lun) msteps,(pnbr3(i),i=1,msteps)
	write (lun) msteps,(bhtn3(i),i=1,msteps)
	write (lun) msteps,(sntn3(i),i=1,msteps)
	write (lun) msteps,(wdtn3(i),i=1,msteps)
	write (lun) msteps,(rmtm3(i),i=1,msteps)
	write (lun) msteps,(toff3(i),i=1,msteps)
	write (lun) msteps,(bolms3(i),i=1,msteps)
	write (lun) msteps,(gasms3(i),i=1,msteps)
	write (lun) msteps,(galms3(i),i=1,msteps)
	write (lun) msteps,(rml3(i),i=1,msteps)
	write (lun) msteps,(rdp3(i),i=1,msteps)
	write (lun) msteps,(sn13(i),i=1,msteps)
	write (lun) msteps,(sn23(i),i=1,msteps)
	write (lun) msteps,(sn33(i),i=1,msteps)
	write (lun) msteps,(sn43(i),i=1,msteps)

	! Write command file to delete unwnated files
	call delete_files(temp,inl,1)
	close (3)
	close (4)
	close (lun)
	close (lun+1)
	close (lun+2)
	close (lun+3)
	close (lun+4)
	close (lun+5)
	close (lun+8)
	close (lun+9)
	close (lun+10)
	close (lun+11)
	close (lun+12)
	close (lun+13)
	close (lun+14)
	close (lun+55)

10	end
