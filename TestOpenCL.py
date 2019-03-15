#
# Display Device Information
#
# Script to print out some information about the OpenCL devices
# and platforms available on your system
#
# History: C++ version written by Tom Deakin, 2012
#          Ported to Python by Tom Deakin, July 2013
#

# Import the Python OpenCL API
import pyopencl as cl

# Create a list of all the platform IDs
platforms = cl.get_platforms()

print ("\nNumber of OpenCL platforms:" + str(len(platforms)))

print ("\n-------------------------")

# Investigate each platform
for p in platforms:
    # Print out some information about the platforms
    print ("Platform:"+ p.name)
    print ("Vendor:"+ p.vendor)
    print ("Version:"+ p.version)

    # Discover all devices
    devices = p.get_devices()
    print ("Number of devices:"+ str(len(devices)))

    # Investigate each device
    for d in devices:
        print ("\t-------------------------")
        # Print out some information about the devices
        print ("\t\tName:"+ d.name)
        print ("\t\tVersion:"+ d.opencl_c_version)
        print ("\t\tMax. Compute Units:"+ str(d.max_compute_units))
        print ("\t\tLocal Memory Size:"+ str(d.local_mem_size/1024)+ "KB")
        print ("\t\tGlobal Memory Size:"+ str(d.global_mem_size/(1024*1024))+ "MB")
        print ("\t\tMax Alloc Size:"+ str(d.max_mem_alloc_size/(1024*1024))+ "MB")
        print ("\t\tMax Work-group Total Size:"+ str(d.max_work_group_size))

        # Find the maximum dimensions of the work-groups
        dim = d.max_work_item_sizes
        print ("\t\tMax Work-group Dims:("+ str(dim[0])+ " ".join(map(str, dim[1:]))+ ")")

        print ("\t-------------------------")

    print ("\n-------------------------")