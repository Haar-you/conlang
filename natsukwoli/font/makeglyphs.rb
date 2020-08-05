#!/usr/bin/ruby

require "rexml/document"
require "builder"

svg = REXML::Document.new(open("glyphs.svg"))

svg.elements.each("svg/g/path") do |elem|
  id = elem.attributes["id"]
  d = elem.attributes["d"]

  m = d.scan(/[\-\d\.]+/)
  dx = m[0].to_i
  dy = 1052.3622 - m[1].to_i

  File.open("glyphs/#{id}.svg", "w") do |file|
    xml = Builder::XmlMarkup.new(:indent=>2, :target=>file)
    xml.instruct!(:xml, :version=>"1.0", :encoding=>"UTF-8")
    xml.svg(
      :'xmlns:svg'=>"http://www.w3.org/2000/svg",
      :xmlns=>"http://www.w3.org/2000/svg",
      :viewBox=>"0 0 1000 1000"){

      xml.path(
        :transform=>"translate(#{-(dx/1000).to_i*1000},#{-52.3622+((dy/1000).to_i*1000)})",
        :style=>"fill:#000000;fill-opacity:1;stroke:none",
        :d=>d
      )

    }
  end
end

