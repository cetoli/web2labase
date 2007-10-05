bridge = visual.ellipsoid()
bridge.length=10
bridge.width=10
sh= visual.cylinder()
sh.radius=1
sh.rotate(angle=pi/4, axis=(0,0,1))
sh.length=4
sh.radius=0.6
sh.pos=(-4,-3,0)
hlk=frame()
hk=cylinder(frame=hlk,length=5,pos=(-6,-6,0), radius=0.8)
fore=sphere(frame=hlk,length=5,pos=(-2,-6,0), radius=0.8)
fore.pos = (-1,-6,0)
aft=sphere(frame=hlk,length=5,pos=(-7,-6,0), radius=0.8)
aft.pos = (-6,-6,0)
bridge.height=1.5
