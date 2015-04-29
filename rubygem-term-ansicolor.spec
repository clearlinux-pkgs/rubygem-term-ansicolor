#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-term-ansicolor
Version  : 1.3.2
Release  : 5
URL      : https://rubygems.org/downloads/term-ansicolor-1.3.2.gem
Source0  : https://rubygems.org/downloads/term-ansicolor-1.3.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: rubygem-term-ansicolor-bin
BuildRequires : ruby
BuildRequires : rubygem-gem_hadar
BuildRequires : rubygem-minitest
BuildRequires : rubygem-minitest_tu_shim
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-simplecov
BuildRequires : rubygem-test-unit

%description
= Term::ANSIColor - ANSI escape sequences in Ruby
== Description
This library can be used to color/decolor strings using ANSI escape sequences.

%package bin
Summary: bin components for the rubygem-term-ansicolor package.
Group: Binaries

%description bin
bin components for the rubygem-term-ansicolor package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n term-ansicolor-1.3.2
gem spec %{SOURCE0} -l --ruby > rubygem-term-ansicolor.gemspec

%build
gem build rubygem-term-ansicolor.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
term-ansicolor-1.3.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/term-ansicolor-1.3.2
ruby -I"lib:tests" test*/test_*.rb
ruby -I"lib:tests" test*/*_test.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/term-ansicolor-1.3.2.gem
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/%5b%5d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/apply-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/attributes-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/background%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/cdesc-Attribute.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/code-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/distance_to-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/get-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/gradient_to-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/gray%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/named_attributes-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/nearest_rgb_color-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/nearest_rgb_on_color-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/rgb-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/rgb_color%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/rgb_colors-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/set-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/Attribute/to_rgb_triple-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/PPMReader/cdesc-PPMReader.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/PPMReader/each_row-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/PPMReader/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/PPMReader/next_line-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/PPMReader/parse_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/PPMReader/parse_next_pixel-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/PPMReader/parse_row-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/PPMReader/reset_io-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/PPMReader/to_a-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/PPMReader/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/CIELab/CIELabTriple/cdesc-CIELabTriple.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/CIELab/CIELabTriple/from_rgb_triple-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/CIELab/cdesc-CIELab.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/CIELab/distance-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/CIEXYZ/CIEXYZTriple/cdesc-CIEXYZTriple.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/CIEXYZ/CIEXYZTriple/from_rgb_triple-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/CIEXYZ/cdesc-CIEXYZ.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/CIEXYZ/distance-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/CompuPhase/cdesc-CompuPhase.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/CompuPhase/distance-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/Euclidean/cdesc-Euclidean.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/Euclidean/distance-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/NTSC/cdesc-NTSC.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/NTSC/distance-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/YUV/YUVTriple/cdesc-YUVTriple.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/YUV/YUVTriple/from_rgb_triple-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/YUV/cdesc-YUV.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/YUV/distance-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/cdesc-RGBColorMetrics.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/metric%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/metric-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetrics/metrics-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetricsHelpers/NormalizeRGBTriple/cdesc-NormalizeRGBTriple.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetricsHelpers/NormalizeRGBTriple/normalize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetricsHelpers/NormalizeRGBTriple/normalize_rgb_triple-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetricsHelpers/WeightedEuclideanDistance/cdesc-WeightedEuclideanDistance.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetricsHelpers/WeightedEuclideanDistance/weighted_euclidean_distance_to-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBColorMetricsHelpers/cdesc-RGBColorMetricsHelpers.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/%5b%5d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/blue-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/cdesc-RGBTriple.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/convert_value-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/distance_to-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/from_array-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/from_hash-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/from_html-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/gradient_to-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/gray%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/green-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/html-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/initialize_copy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/red-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/to_a-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/to_rgb_triple-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/RGBTriple/values-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/attributes-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/attributes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/cdesc-ANSIColor.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/color-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/coloring%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/coloring%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/create_color_method-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/on_color-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/support%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/term_ansicolor_attributes-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/term_ansicolor_attributes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/uncolor-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/ANSIColor/uncolored-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/Term/cdesc-Term.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/term-ansicolor-1.3.2/ri/page-README_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/.travis.yml
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/CHANGES
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/COPYING
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/README.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/VERSION
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/bin/cdiff
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/bin/colortab
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/bin/decolor
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/bin/term_display
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/bin/term_mandel
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/examples/ColorTest.gif
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/examples/Mona_Lisa.jpg
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/examples/Stilleben.jpg
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/examples/example.rb
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/examples/lambda-red-plain.ppm
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/examples/lambda-red.png
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/examples/lambda-red.ppm
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/examples/pacman.jpg
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/examples/smiley.png
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/examples/wool.jpg
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/lib/term/ansicolor.rb
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/lib/term/ansicolor/.keep
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/lib/term/ansicolor/attribute.rb
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/lib/term/ansicolor/ppm_reader.rb
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/lib/term/ansicolor/rgb_color_metrics.rb
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/lib/term/ansicolor/rgb_triple.rb
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/lib/term/ansicolor/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/term-ansicolor.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/tests/ansicolor_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/tests/attribute_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/tests/ppm_reader_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/tests/rgb_color_metrics_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/tests/rgb_triple_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/term-ansicolor-1.3.2/tests/test_helper.rb
/usr/lib64/ruby/gems/2.2.0/specifications/term-ansicolor-1.3.2.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/cdiff
/usr/bin/colortab
/usr/bin/decolor
/usr/bin/term_display
/usr/bin/term_mandel
