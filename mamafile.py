
import mama

##
# Explore Mama docs at https://github.com/RedFox20/Mama
#
class libgtest(mama.BuildTarget):

    workspace = 'build'

    def dependencies(self):
        self.nothing_to_build()

    def configure(self):
        pass

    def package(self):
        self.export_libs('lib', ['.a'], src_dir=True)
        self.export_include('include')
