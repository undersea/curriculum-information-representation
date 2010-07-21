import tidy #to normalise the html to a valid xml document format
import urllib2
from page_finder import urls
import libxml2, libxslt


xslt = libxslt.parseStylesheetDoc(libxml2.parseDoc("""
<xsl:stylesheet version='1.0'
  xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>

<xsl:template match="div">
  begin
  <xsl:value-of select="name()"/>
  <xsl:if test="@class='progSectionText'">
    <p><xsl:value-of select="@class"/></p>
  </xsl:if>
  <xsl:if test="name()='div'">
    
    
  </xsl:if>
  end
</xsl:template>



</xsl:stylesheet>
"""))


class Parser(object):
    def __init__(self, programme):
        url = urls[programme]
        options = dict(output_xhtml=1, add_xml_decl=1, indent=1, tidy_mark=0)
        self.data = libxml2.parseDoc(str(tidy.parseString(urllib.urlopen(url).read(), **options)))
        
