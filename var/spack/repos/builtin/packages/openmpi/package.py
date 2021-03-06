##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################

import os

from spack import *


def _verbs_dir():
    """Try to find the directory where the OpenFabrics verbs package is
    installed. Return None if not found.
    """
    try:
        # Try to locate Verbs by looking for a utility in the path
        ibv_devices = which("ibv_devices")
        # Run it (silently) to ensure it works
        ibv_devices(output=str, error=str)
        # Get path to executable
        path = ibv_devices.exe[0]
        # Remove executable name and "bin" directory
        path = os.path.dirname(path)
        path = os.path.dirname(path)
        # There's usually no "/include" on Unix; use "/usr/include" instead
        if path == "/":
            path = "/usr"
        return path
    except TypeError:
        return None
    except ProcessError:
        return None


def _mxm_dir():
    """Look for default directory where the Mellanox package is
    installed. Return None if not found.
    """
    # Only using default directory; make this more flexible in the future
    path = "/opt/mellanox/mxm"
    if os.path.isdir(path):
        return path
    else:
        return None


class Openmpi(AutotoolsPackage):
    """The Open MPI Project is an open source Message Passing Interface
       implementation that is developed and maintained by a consortium
       of academic, research, and industry partners. Open MPI is
       therefore able to combine the expertise, technologies, and
       resources from all across the High Performance Computing
       community in order to build the best MPI library available.
       Open MPI offers advantages for system and software vendors,
       application developers and computer science researchers.
    """

    homepage = "http://www.open-mpi.org"
    url = "https://www.open-mpi.org/software/ompi/v3.0/downloads/openmpi-3.0.0.tar.bz2"
    list_url = "http://www.open-mpi.org/software/ompi/"

    # Current
    version('3.0.0', '757d51719efec08f9f1a7f32d58b3305')  # libmpi.so.40.00.0

    # Still supported
    version('2.1.2', 'ff2e55cc529802e7b0738cf87acd3ee4')  # libmpi.so.20.10.2
    version('2.1.1', 'ae542f5cf013943ffbbeb93df883731b')  # libmpi.so.20.10.1
    version('2.1.0', '4838a5973115c44e14442c01d3f21d52')  # libmpi.so.20.10.0
    version('2.0.3', '6c09e56ac2230c4f9abd8ba029f03edd')  # libmpi.so.20.0.3
    version('2.0.2', 'ecd99aa436a1ca69ce936a96d6a3fa48')  # libmpi.so.20.0.2
    version('2.0.1', '6f78155bd7203039d2448390f3b51c96')  # libmpi.so.20.0.1
    version('2.0.0', 'cdacc800cb4ce690c1f1273cb6366674')  # libmpi.so.20.0.0

    version('1.10.7', 'c87c613f9acb1a4eee21fa1ac8042579')  # libmpi.so.12.0.7
    version('1.10.6', '2e65008c1867b1f47c32f9f814d41706')  # libmpi.so.12.0.6
    version('1.10.5', 'd32ba9530a869d9c1eae930882ea1834')  # libmpi.so.12.0.5
    version('1.10.4', '9d2375835c5bc5c184ecdeb76c7c78ac')  # libmpi.so.12.0.4
    version('1.10.3', 'e2fe4513200e2aaa1500b762342c674b')  # libmpi.so.12.0.3
    version('1.10.2', 'b2f43d9635d2d52826e5ef9feb97fd4c')  # libmpi.so.12.0.2
    version('1.10.1', 'f0fcd77ed345b7eafb431968124ba16e')  # libmpi.so.12.0.1
    version('1.10.0', '280cf952de68369cebaca886c5ce0304')  # libmpi.so.12.0.0

    # Retired
    version('1.8.8', '0dab8e602372da1425e9242ae37faf8c')  # libmpi.so.1.6.3
    version('1.8.7', '2485ed6fa0fab9bb5b4e7a9f63718630')  # libmpi.so.1.6.2
    version('1.8.6', 'eb569e7dc97eeaa5b1876cccf114f377')  # libmpi.so.1.6.1
    version('1.8.5', '93e958914ff0e4d9634d668d2d48c793')  # libmpi.so.1.6.0
    version('1.8.4', '93b7ea2c4ebae76947f942579608ae4a')  # libmpi.so.1.6.0
    version('1.8.3', '2067d00853e0c33d498153fc7d268d2b')  # libmpi.so.1.6.0
    version('1.8.2', '339a9fc199563bacbb359875ce8c9e20')  # libmpi.so.1.5.2
    version('1.8.1', '0e12c24a28a605f681ff9a19a1aca2f1')  # libmpi.so.1.5.0
    version('1.8',   '5999cfb177a50c480b5d0bced379aff1')  # libmpi.so.1.5.0

    version('1.7.5', '321ab81147ac69a5bbca72652fb3b468')  # libmpi.so.1.4.0
    version('1.7.4', '4aea4fb00f8956dd56ccf50e5784e03f')  # libmpi.so.1.3.0
    version('1.7.3', '7d0779f73c43eb1d098ad037d60649bc')  # libmpi.so.1.2.0
    version('1.7.2', 'b897b92100bd13b367e651df483421d5')  # libmpi.so.1.1.2
    version('1.7.1', 'f25b446a9dcbbd6a105a99d926d34441')  # libmpi.so.1.1.1
    version('1.7',   'c0e3c4b3bfcd8b8bbd027f6f4c164acb')  # libmpi.so.1.1.0

    version('1.6.5', '03aed2a4aa4d0b27196962a2a65fc475')  # libmpi.so.1.0.8
    version('1.6.4', '62119579ab92b2592cd96b6a9d2a8cc3')  # libmpi.so.1.0.7
    version('1.6.3', 'eedb73155a7a40b0b07718494298fb25')  # libmpi.so.1.0.6
    version('1.6.2', '219754715a8e40beb468bbc8f0b3251a')  # libmpi.so.1.0.3
    version('1.6.1', '33d2782c20ff6be79130a703b85da8f0')  # libmpi.so.1.0.3
    version('1.6',   'dd6f5bd4b3cb14d93bbf530e50e46e60')  # libmpi.so.1.0.3

    # Ancient
    version('1.5.5', 'f882fd61ff89db856bfd8f0dfa42e1bd')  # libmpi.so.1.0.3
    version('1.5.4', '51153d794c49ce6d275dba2793ab0c68')  # libmpi.so.1.0.2
    version('1.5.3', '0eb8ec2aa05c74a4bc7602b01847131e')  # libmpi.so.1.0.1
    version('1.5.2', 'faaee6a2777bf607d7fa1297c0b3a9ed')  # libmpi.so.1.0.1
    version('1.5.1', '3f9409f5d3b617c04dea48ba8fbd703a')  # libmpi.so.1.0.0
    version('1.5',   '86bf5f9ef7337231abbca3350b31f112')  # libmpi.so.1.0.0

    version('1.4.5', '84ddd2772f46d35da79e1db8a274c99d')  # libmpi.so.0.0.4
    version('1.4.4', 'e58a1ea7b8af62453aaa0ddaee5f26a0')  # libmpi.so.0.0.3
    version('1.4.3', 'd2ead141c43b915343f5c5a18f3b5016')  # libmpi.so.0.0.2
    version('1.4.2', '53b26fa2586aedaf73cf40effbfcc2f3')  # libmpi.so.0.0.2
    version('1.4.1', '28a820c85e02973809df881fdeddd15e')  # libmpi.so.0.0.1
    version('1.4',   '9786ec0698afed9498ce43dc3978a435')  # libmpi.so.0.0.1

    version('1.3.4', '978c29f3b671856daa0fc67459b73e01')  # libmpi.so.0.0.1
    version('1.3.3', 'f6cdc9c195daa8571b2e509e952d6755')  # libmpi.so.0.0.0
    version('1.3.2', '75781dc31255cd841701c065e239d994')  # libmpi.so.0.0.0
    version('1.3.1', 'd759523b0752139872c534714d641d64')  # libmpi.so.0.0.0
    version('1.3',   'efbba7d652d1e430d456f65d7a2e339b')  # libmpi.so.0.0.0

    version('1.2.9', '78c2aebbb746610ed12bdedcc2b6ec0e')  # libmpi.so.0.0.0
    version('1.2.8', '7f2d5af02101c5f01173f4f6de296549')  # libmpi.so.0.0.0
    version('1.2.7', 'b5ae3059fba71eba4a89a2923da8223f')  # libmpi.so.0.0.0
    version('1.2.6', 'f126793b68e71f5ec4a192c40675af2d')  # libmpi.so.0.0.0
    version('1.2.5', 'c6e82aab6cdcd425bf29217e8317d7dc')  # libmpi.so.0.0.0
    version('1.2.4', '311b38c597f54d8d6b277225ef458666')  # libmpi.so.0.0.0
    version('1.2.3', 'ae980bb00f9686934a1143701cc041e4')  # libmpi.so.0.0.0
    version('1.2.2', '7f553317e388c4efe479e908b66f910d')  # libmpi.so.0.0.0
    version('1.2.1', 'ceaa42891edba2324a94fdd0b87e46ca')  # libmpi.so.0.0.0
    version('1.2',   '37e8d4edad54a8d8c3127fbef87ebda1')  # libmpi.so.0.0.0

    version('1.1.5', '6aada92896a1830ece6d3ba1e66a17fa')  # libmpi.so.0.0.0
    version('1.1.4', '28940b182156478fa442397b0c9660e1')  # libmpi.so.0.0.0
    version('1.1.3', 'bbaa7fe9d556212d877d872544a31569')  # libmpi.so.0.0.0
    version('1.1.2', '53877ec8bca5f6e505496b6b94b1d850')  # libmpi.so.0.0.0
    version('1.1.1', '498b9322ae0ad512026a008a30c7e0b5')  # libmpi.so.0.0.0
    version('1.1',   '821af8bbb7a8e85ec707cb4c3b6bcbf6')  # libmpi.so.0.0.0

    version('1.0.2', 'fd32861d643f9fe539a01d0d5b836f41')  # libmpi.so.0.0.0
    version('1.0.1', '8abccca5cdddc81a6d9d9e22b3bb6db9')  # libmpi.so.0.0.0
    version('1.0',   'f5dcb5d3a98f2e5a9c2a0caaef54d806')  # libmpi.so.0.0.0

    patch('ad_lustre_rwcontig_open_source.patch', when="@1.6.5")
    patch('llnl-platforms.patch', when="@1.6.5")
    patch('configure.patch', when="@1.10.1")
    patch('fix_multidef_pmi_class.patch', when="@2.0.0:2.0.1")

    variant(
        'fabrics',
        default=None if _verbs_dir() is None else 'verbs',
        description='List of fabrics that are enabled',
        values=('psm', 'psm2', 'pmi', 'verbs', 'mxm'),
        multi=True
    )

    variant(
        'schedulers',
        description='List of schedulers for which support is enabled',
        values=('alps', 'lsf', 'tm', 'slurm', 'sge', 'loadleveler'),
        multi=True
    )

    # Additional support options
    variant('java', default=False, description='Build Java support')
    variant('sqlite3', default=False, description='Build SQLite3 support')
    variant('vt', default=True, description='Build VampirTrace support')
    variant('thread_multiple', default=False,
            description='Enable MPI_THREAD_MULTIPLE support')
    variant('cuda', default=False, description='Enable CUDA support')

    provides('mpi')
    provides('mpi@:2.2', when='@1.6.5')
    provides('mpi@:3.0', when='@1.7.5:')
    provides('mpi@:3.1', when='@2.0.0:')

    depends_on('hwloc')
    depends_on('hwloc +cuda', when='+cuda')
    depends_on('java', when='+java')
    depends_on('sqlite', when='+sqlite3@:1.11')

    conflicts('+cuda', when='@:1.6')  # CUDA support was added in 1.7
    conflicts('fabrics=psm2', when='@:1.8')  # PSM2 support was added in 1.10.0
    conflicts('fabrics=pmi', when='@:1.5.4')  # PMI support was added in 1.5.5
    conflicts('fabrics=mxm', when='@:1.5.3')  # MXM support was added in 1.5.4

    def url_for_version(self, version):
        url = "http://www.open-mpi.org/software/ompi/v{0}/downloads/openmpi-{1}.tar.bz2"
        return url.format(version.up_to(2), version)

    @property
    def libs(self):
        query_parameters = self.spec.last_query.extra_parameters
        libraries = ['libmpi']

        if 'cxx' in query_parameters:
            libraries = ['libmpi_cxx'] + libraries

        return find_libraries(
            libraries, root=self.prefix, shared=True, recurse=True
        )

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        spack_env.set('MPICC',  join_path(self.prefix.bin, 'mpicc'))
        spack_env.set('MPICXX', join_path(self.prefix.bin, 'mpic++'))
        spack_env.set('MPIF77', join_path(self.prefix.bin, 'mpif77'))
        spack_env.set('MPIF90', join_path(self.prefix.bin, 'mpif90'))

        spack_env.set('OMPI_CC', spack_cc)
        spack_env.set('OMPI_CXX', spack_cxx)
        spack_env.set('OMPI_FC', spack_fc)
        spack_env.set('OMPI_F77', spack_f77)

    def setup_dependent_package(self, module, dependent_spec):
        self.spec.mpicc = join_path(self.prefix.bin, 'mpicc')
        self.spec.mpicxx = join_path(self.prefix.bin, 'mpic++')
        self.spec.mpifc = join_path(self.prefix.bin, 'mpif90')
        self.spec.mpif77 = join_path(self.prefix.bin, 'mpif77')
        self.spec.mpicxx_shared_libs = [
            join_path(self.prefix.lib, 'libmpi_cxx.{0}'.format(dso_suffix)),
            join_path(self.prefix.lib, 'libmpi.{0}'.format(dso_suffix))
        ]

    def with_or_without_verbs(self, activated):
        # Up through version 1.6, this option was previously named
        # --with-openib
        opt = 'openib'
        # In version 1.7, it was renamed to be --with-verbs
        if self.spec.satisfies('@1.7:'):
            opt = 'verbs'
        # If the option has not been activated return
        # --without-openib or --without-verbs
        if not activated:
            return '--without-{0}'.format(opt)
        line = '--with-{0}'.format(opt)
        path = _verbs_dir()
        if (path is not None) and (path not in ('/usr', '/usr/local')):
            line += '={0}'.format(path)
        return line

    def with_or_without_mxm(self, activated):
        opt = 'mxm'
        # If the option has not been activated return --without-mxm
        if not activated:
            return '--without-{0}'.format(opt)
        line = '--with-{0}'.format(opt)
        path = _mxm_dir()
        if (path is not None):
            line += '={0}'.format(path)
        return line

    @run_before('autoreconf')
    def die_without_fortran(self):
        # Until we can pass variants such as +fortran through virtual
        # dependencies depends_on('mpi'), require Fortran compiler to
        # avoid delayed build errors in dependents.
        if (self.compiler.f77 is None) or (self.compiler.fc is None):
            raise InstallError(
                'OpenMPI requires both C and Fortran compilers!'
            )

    def configure_args(self):
        spec = self.spec
        config_args = [
            '--enable-shared',
            '--enable-static'
        ]
        if self.spec.satisfies('@2.0:'):
            # for Open-MPI 2.0:, C++ bindings are disabled by default.
            config_args.extend(['--enable-mpi-cxx'])

        # Fabrics and schedulers
        config_args.extend(self.with_or_without('fabrics'))
        config_args.extend(self.with_or_without('schedulers'))

        # Hwloc support
        if spec.satisfies('@1.5.2:'):
            config_args.append('--with-hwloc={0}'.format(spec['hwloc'].prefix))

        # Java support
        if spec.satisfies('@1.7.4:'):
            if '+java' in spec:
                config_args.extend([
                    '--enable-java',
                    '--enable-mpi-java',
                    '--with-jdk-dir={0}'.format(spec['java'].prefix)
                ])
            else:
                config_args.extend([
                    '--disable-java',
                    '--disable-mpi-java'
                ])

        # SQLite3 support
        if spec.satisfies('@1.7.3:1.999'):
            if '+sqlite3' in spec:
                config_args.append('--with-sqlite3')
            else:
                config_args.append('--without-sqlite3')

        # VampirTrace support
        if spec.satisfies('@1.3:1.999'):
            if '+vt' not in spec:
                config_args.append('--enable-contrib-no-build=vt')

        # Multithreading support
        if spec.satisfies('@1.5.4:'):
            if '+thread_multiple' in spec:
                config_args.append('--enable-mpi-thread-multiple')
            else:
                config_args.append('--disable-mpi-thread-multiple')

        # CUDA support
        # See https://www.open-mpi.org/faq/?category=buildcuda
        if spec.satisfies('@1.7:'):
            if '+cuda' in spec:
                # OpenMPI dynamically loads libcuda.so, requires dlopen
                config_args.append('--enable-dlopen')
                # Searches for header files in DIR/include
                config_args.append('--with-cuda={0}'.format(
                    spec['cuda'].prefix))
                if spec.satisfies('@1.7:1.7.2'):
                    # This option was removed from later versions
                    config_args.append('--with-cuda-libdir={0}'.format(
                        spec['cuda'].libs.directories[0]))
                if spec.satisfies('@1.7.2'):
                    # There was a bug in 1.7.2 when --enable-static is used
                    config_args.append('--enable-mca-no-build=pml-bfo')
                if spec.satisfies('%pgi^cuda@7.0:7.999'):
                    # OpenMPI has problems with CUDA 7 and PGI
                    config_args.append(
                        '--with-wrapper-cflags=-D__LP64__ -ta:tesla')
                    if spec.satisfies('%pgi@:15.8'):
                        # With PGI 15.9 and later compilers, the
                        # CFLAGS=-D__LP64__ is no longer needed.
                        config_args.append('CFLAGS=-D__LP64__')
            else:
                config_args.append('--without-cuda')

        return config_args

    @run_after('install')
    def filter_compilers(self):
        """Run after install to make the MPI compilers use the
        compilers that Spack built the package with.

        If this isn't done, they'll have CC, CXX and FC set
        to Spack's generic cc, c++ and f90.  We want them to
        be bound to whatever compiler they were built with.
        """
        kwargs = {'ignore_absent': True, 'backup': False, 'string': False}
        wrapper_basepath = join_path(self.prefix, 'share', 'openmpi')

        wrappers = [
            ('mpicc-vt-wrapper-data.txt', self.compiler.cc),
            ('mpicc-wrapper-data.txt', self.compiler.cc),
            ('ortecc-wrapper-data.txt', self.compiler.cc),
            ('shmemcc-wrapper-data.txt', self.compiler.cc),
            ('mpic++-vt-wrapper-data.txt', self.compiler.cxx),
            ('mpic++-wrapper-data.txt', self.compiler.cxx),
            ('ortec++-wrapper-data.txt', self.compiler.cxx),
            ('mpifort-vt-wrapper-data.txt', self.compiler.fc),
            ('mpifort-wrapper-data.txt', self.compiler.fc),
            ('shmemfort-wrapper-data.txt', self.compiler.fc),
            ('mpif90-vt-wrapper-data.txt', self.compiler.fc),
            ('mpif90-wrapper-data.txt', self.compiler.fc),
            ('mpif77-vt-wrapper-data.txt',  self.compiler.f77),
            ('mpif77-wrapper-data.txt',  self.compiler.f77)
        ]

        for wrapper_name, compiler in wrappers:
            wrapper = join_path(wrapper_basepath, wrapper_name)
            if not os.path.islink(wrapper):
                # Substitute Spack compile wrappers for the real
                # underlying compiler
                match = 'compiler=.*'
                substitute = 'compiler={compiler}'.format(compiler=compiler)
                filter_file(match, substitute, wrapper, **kwargs)
                # Remove this linking flag if present
                # (it turns RPATH into RUNPATH)
                filter_file('-Wl,--enable-new-dtags', '', wrapper, **kwargs)
