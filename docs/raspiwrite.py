


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>RasPiWrite/raspiwrite.py at master · exaviorn/RasPiWrite · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="https://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta property="og:image" content="https://a248.e.akamai.net/assets.github.com/images/modules/logos_page/Octocat.png">
    <meta name="hostname" content="fe3.rs.github.com">
    <link rel="assets" href="https://a248.e.akamai.net/assets.github.com/">
    <link rel="xhr-socket" href="/_sockets" />
    
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" />

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="5dhFHRvpv9SIDSzAt4pYVycr1snPBARiHQdvg1PL0ns=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-51f046bb24b211de3abde37dc8e6e0e3069e1ee6.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-b046d81a359bd0dd393698ea6a790d082330c2d8.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-5356b8919752ed538d797b3aa4996eed793b46a1.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-c8d11dc916e5476e1fc9f8ef2f896f487badc71f.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="0b472c00b16d62432d95c4ee6eb8616f">

        <link data-pjax-transient rel='permalink' href='/exaviorn/RasPiWrite/blob/413db87d444866048bc02a9d0f2d77780a7dff69/raspiwrite.py'>
  <meta property="og:title" content="RasPiWrite"/>
  <meta property="og:type" content="githubog:gitrepository"/>
  <meta property="og:url" content="https://github.com/exaviorn/RasPiWrite"/>
  <meta property="og:image" content="https://a248.e.akamai.net/assets.github.com/images/gravatars/gravatar-user-420.png"/>
  <meta property="og:site_name" content="GitHub"/>
  <meta property="og:description" content="RasPiWrite - A Python Script that prepairs and installs a Raspberry Pi compatiable distro to an SD Card"/>

  <meta name="description" content="RasPiWrite - A Python Script that prepairs and installs a Raspberry Pi compatiable distro to an SD Card" />

  <meta content="1570715" name="octolytics-dimension-user_id" /><meta content="exaviorn" name="octolytics-dimension-user_login" /><meta content="3817748" name="octolytics-dimension-repository_id" /><meta content="exaviorn/RasPiWrite" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="3817748" name="octolytics-dimension-repository_network_root_id" /><meta content="exaviorn/RasPiWrite" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/exaviorn/RasPiWrite/commits/master.atom" rel="alternate" title="Recent Commits to RasPiWrite:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob macintosh vis-public env-production ">

    <div class="wrapper">
      
      
      

      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
      <a class="button primary" href="/signup">Sign up</a>
      <a class="button" href="/login?return_to=%2Fexaviorn%2FRasPiWrite%2Fblob%2Fmaster%2Fraspiwrite.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">


      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
        <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey=" s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
      data-repo="exaviorn/RasPiWrite"
      data-branch="master"
      data-sha="88974c8522f7742247a0df4ea876fa4f9dbb3644"
  >

    <input type="hidden" name="nwo" value="exaviorn/RasPiWrite" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>


      


          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">


    <li>
      <a href="/login?return_to=%2Fexaviorn%2FRasPiWrite"
        class="minibutton with-count js-toggler-target star-button entice tooltipped upwards"
        title="You must be signed in to use this feature" rel="nofollow">
        <span class="octicon octicon-star"></span>Star
      </a>
      <a class="social-count js-social-count" href="/exaviorn/RasPiWrite/stargazers">
        189
      </a>
    </li>
    <li>
      <a href="/login?return_to=%2Fexaviorn%2FRasPiWrite"
        class="minibutton with-count js-toggler-target fork-button entice tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-git-branch"></span>Fork
      </a>
      <a href="/exaviorn/RasPiWrite/network" class="social-count">
        154
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author">
            <a href="/exaviorn" class="url fn" itemprop="url" rel="author"><span itemprop="title">exaviorn</span></a></span
          ><span class="repohead-name-divider">/</span><strong
          ><a href="/exaviorn/RasPiWrite" class="js-current-repository js-repo-home-link">RasPiWrite</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">

      <div class="repository-with-sidebar repo-container
            ">

          <div class="repository-sidebar">

              

<div class="repo-nav repo-nav-full js-repository-container-pjax js-octicon-loaders">
  <div class="repo-nav-contents">
    <ul class="repo-menu">
      <li class="tooltipped leftwards" title="Code">
        <a href="/exaviorn/RasPiWrite" class="js-selected-navigation-item selected" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /exaviorn/RasPiWrite">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped leftwards" title="Issues">
          <a href="/exaviorn/RasPiWrite/issues" class="js-selected-navigation-item js-disable-pjax" data-gotokey="i" data-selected-links="repo_issues /exaviorn/RasPiWrite/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>62</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped leftwards" title="Pull Requests"><a href="/exaviorn/RasPiWrite/pulls" class="js-selected-navigation-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /exaviorn/RasPiWrite/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>45</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>




    </ul>
    <div class="repo-menu-separator"></div>
    <ul class="repo-menu">

      <li class="tooltipped leftwards" title="Pulse">
        <a href="/exaviorn/RasPiWrite/pulse" class="js-selected-navigation-item " data-pjax="true" data-selected-links="pulse /exaviorn/RasPiWrite/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Graphs">
        <a href="/exaviorn/RasPiWrite/graphs" class="js-selected-navigation-item " data-pjax="true" data-selected-links="repo_graphs repo_contributors /exaviorn/RasPiWrite/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Network">
        <a href="/exaviorn/RasPiWrite/network" class="js-selected-navigation-item js-disable-pjax" data-selected-links="repo_network /exaviorn/RasPiWrite/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

    </ul>

  </div>
</div>


              <div class="only-with-full-nav">

                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>

  <input type="text" class="clone js-url-field"
         value="https://github.com/exaviorn/RasPiWrite.git" readonly="readonly">

  <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/exaviorn/RasPiWrite.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>

  <input type="text" class="clone js-url-field"
         value="https://github.com/exaviorn/RasPiWrite" readonly="readonly">

  <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/exaviorn/RasPiWrite" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
</div>



<p class="clone-options">You can clone with
    <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
    <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>,
  and <a href="https://help.github.com/articles/which-remote-url-should-i-use">other methods.</a>
</p>

  <a href="http://mac.github.com" class="minibutton sidebar-button">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>



                  <a href="/exaviorn/RasPiWrite/archive/master.zip"
                     class="minibutton sidebar-button"
                     title="Download this repository as a zip file"
                     rel="nofollow">
                    <span class="octicon octicon-cloud-download"></span>
                    Download ZIP
                  </a>

              </div>
          </div>

          <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
            


<!-- blob contrib key: blob_contributors:v21:9477922454ae0e8af1af2b5f57fb70fe -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:9477922454ae0e8af1af2b5f57fb70fe -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/exaviorn/RasPiWrite/find/master" data-pjax data-hotkey="t" style="display:none">Show File Finder</a>

<div class="file-navigation">
  


<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/exaviorn/RasPiWrite/blob/master/raspiwrite.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/exaviorn/RasPiWrite" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">RasPiWrite</span></a></span></span><span class="separator"> / </span><strong class="final-path">raspiwrite.py</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="raspiwrite.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


  
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/d5f36fbefbf4a5f37d328ef5177794f7?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
    <span class="author"><a href="/tech2077" rel="author">tech2077</a></span>
    <time class="js-relative-date" datetime="2012-07-14T12:29:29-07:00" title="2012-07-14 12:29:29">July 14, 2012</time>
    <div class="commit-title">
        <a href="/exaviorn/RasPiWrite/commit/f406d657d8998791b444c5542c2f001f4c5e4f3d" class="message">Fix wrong dd block size notation for OS X with OS check and add prope…</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>4</strong> contributors</a></p>
          <a class="avatar tooltipped downwards" title="exaviorn" href="/exaviorn/RasPiWrite/commits/master/raspiwrite.py?author=exaviorn"><img height="20" src="https://secure.gravatar.com/avatar/197bc69efbedc62375c469083743c20d?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="tech2077" href="/exaviorn/RasPiWrite/commits/master/raspiwrite.py?author=tech2077"><img height="20" src="https://secure.gravatar.com/avatar/d5f36fbefbf4a5f37d328ef5177794f7?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="alecthegeek" href="/exaviorn/RasPiWrite/commits/master/raspiwrite.py?author=alecthegeek"><img height="20" src="https://secure.gravatar.com/avatar/650806949023f752870363ad7de45188?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="andypiper" href="/exaviorn/RasPiWrite/commits/master/raspiwrite.py?author=andypiper"><img height="20" src="https://secure.gravatar.com/avatar/1526dcb784188b422544c6344ef223c2?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li class="facebox-user-list-item">
          <img height="24" src="https://secure.gravatar.com/avatar/197bc69efbedc62375c469083743c20d?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/exaviorn">exaviorn</a>
        </li>
        <li class="facebox-user-list-item">
          <img height="24" src="https://secure.gravatar.com/avatar/d5f36fbefbf4a5f37d328ef5177794f7?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/tech2077">tech2077</a>
        </li>
        <li class="facebox-user-list-item">
          <img height="24" src="https://secure.gravatar.com/avatar/650806949023f752870363ad7de45188?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/alecthegeek">alecthegeek</a>
        </li>
        <li class="facebox-user-list-item">
          <img height="24" src="https://secure.gravatar.com/avatar/1526dcb784188b422544c6344ef223c2?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/andypiper">andypiper</a>
        </li>
      </ul>
    </div>
  </div>


<div id="files" class="bubble">
  <div class="file">
    <div class="meta">
      <div class="info">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">executable file</span>
          <span>468 lines (422 sloc)</span>
        <span>19.0 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton js-entice" href=""
                 data-entice="You must be signed in and on a branch to make or propose changes">Edit</a>
          <a href="/exaviorn/RasPiWrite/raw/master/raspiwrite.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/exaviorn/RasPiWrite/blame/master/raspiwrite.py" class="button minibutton ">Blame</a>
          <a href="/exaviorn/RasPiWrite/commits/master/raspiwrite.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
            <a class="minibutton danger empty-icon js-entice" href=""
               data-entice="You must be signed in and on a branch to make or propose changes">
            Delete
          </a>
      </div><!-- /.actions -->

    </div>
        <div class="blob-wrapper data type-python js-blob-data">
      <table class="file-code file-diff">
        <tr class="file-code-line">
          <td class="blob-line-nums">
            <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>
<span id="L420" rel="#L420">420</span>
<span id="L421" rel="#L421">421</span>
<span id="L422" rel="#L422">422</span>
<span id="L423" rel="#L423">423</span>
<span id="L424" rel="#L424">424</span>
<span id="L425" rel="#L425">425</span>
<span id="L426" rel="#L426">426</span>
<span id="L427" rel="#L427">427</span>
<span id="L428" rel="#L428">428</span>
<span id="L429" rel="#L429">429</span>
<span id="L430" rel="#L430">430</span>
<span id="L431" rel="#L431">431</span>
<span id="L432" rel="#L432">432</span>
<span id="L433" rel="#L433">433</span>
<span id="L434" rel="#L434">434</span>
<span id="L435" rel="#L435">435</span>
<span id="L436" rel="#L436">436</span>
<span id="L437" rel="#L437">437</span>
<span id="L438" rel="#L438">438</span>
<span id="L439" rel="#L439">439</span>
<span id="L440" rel="#L440">440</span>
<span id="L441" rel="#L441">441</span>
<span id="L442" rel="#L442">442</span>
<span id="L443" rel="#L443">443</span>
<span id="L444" rel="#L444">444</span>
<span id="L445" rel="#L445">445</span>
<span id="L446" rel="#L446">446</span>
<span id="L447" rel="#L447">447</span>
<span id="L448" rel="#L448">448</span>
<span id="L449" rel="#L449">449</span>
<span id="L450" rel="#L450">450</span>
<span id="L451" rel="#L451">451</span>
<span id="L452" rel="#L452">452</span>
<span id="L453" rel="#L453">453</span>
<span id="L454" rel="#L454">454</span>
<span id="L455" rel="#L455">455</span>
<span id="L456" rel="#L456">456</span>
<span id="L457" rel="#L457">457</span>
<span id="L458" rel="#L458">458</span>
<span id="L459" rel="#L459">459</span>
<span id="L460" rel="#L460">460</span>
<span id="L461" rel="#L461">461</span>
<span id="L462" rel="#L462">462</span>
<span id="L463" rel="#L463">463</span>
<span id="L464" rel="#L464">464</span>
<span id="L465" rel="#L465">465</span>
<span id="L466" rel="#L466">466</span>
<span id="L467" rel="#L467">467</span>

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env python</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="c">#   ;d0KOd.  .oOK0x:  </span></div><div class='line' id='LC4'><span class="c">#  0xlllcoxolkolllloX </span></div><div class='line' id='LC5'><span class="c">#  ;OccloddKNdxdocckc </span></div><div class='line' id='LC6'><span class="c">#   .dkddkWNNMOdoxd,  </span></div><div class='line' id='LC7'><span class="c">#   .o:,x0....xd,ck&#39;  </span></div><div class='line' id='LC8'><span class="c">#   K:xOoloOOccloocW  </span></div><div class='line' id='LC9'><span class="c"># .x;N:....xO....&#39;K;k,</span></div><div class='line' id='LC10'><span class="c"># O..Nc...:XNl...:X.,X</span></div><div class='line' id='LC11'><span class="c"># .kkx0NXk&#39;...dNNxldK&#39;</span></div><div class='line' id='LC12'><span class="c">#  &#39;k...0o....,O...d: </span></div><div class='line' id='LC13'><span class="c">#   ;o;&#39;oM0olkWc.;oc  </span></div><div class='line' id='LC14'><span class="c">#     .cOx....dOl.    </span></div><div class='line' id='LC15'><span class="c">#        .x00k.    </span></div><div class='line' id='LC16'><br/></div><div class='line' id='LC17'><span class="c">#//////////////////////////// </span></div><div class='line' id='LC18'><span class="c">#	* Raspberry Pi SD Writer </span></div><div class='line' id='LC19'><span class="c">#	* Matt Jump</span></div><div class='line' id='LC20'><span class="c">#	* exaviorn.com</span></div><div class='line' id='LC21'><span class="c">#///////////////////////////</span></div><div class='line' id='LC22'><span class="c"># Copyright Matthew Jump 2012</span></div><div class='line' id='LC23'><span class="c"># The following code is licenced under the Gnu Public Licence, please see gpl.txt for reference</span></div><div class='line' id='LC24'><span class="c">#  This program is free software: you can redistribute it and/or modify</span></div><div class='line' id='LC25'><span class="c">#    it under the terms of the GNU General Public License as published by</span></div><div class='line' id='LC26'><span class="c">#   the Free Software Foundation, either version 3 of the License, or</span></div><div class='line' id='LC27'><span class="c">#    (at your option) any later version.</span></div><div class='line' id='LC28'><span class="c">#</span></div><div class='line' id='LC29'><span class="c">#    This program is distributed in the hope that it will be useful,</span></div><div class='line' id='LC30'><span class="c">#    but WITHOUT ANY WARRANTY; without even the implied warranty of</span></div><div class='line' id='LC31'><span class="c">#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the</span></div><div class='line' id='LC32'><span class="c">#    GNU General Public License for more details.</span></div><div class='line' id='LC33'><span class="c">#</span></div><div class='line' id='LC34'><span class="c">#    You should have received a copy of the GNU General Public License</span></div><div class='line' id='LC35'><span class="c">#    along with this program.  If not, see &lt;http://www.gnu.org/licenses/&gt;.</span></div><div class='line' id='LC36'><br/></div><div class='line' id='LC37'><span class="c"># VERSION 1.15 -MACOSX- (June 2012) BETA</span></div><div class='line' id='LC38'><span class="c">#	* Fix to unzipping system - credit to alecthegeek</span></div><div class='line' id='LC39'><span class="c">#	* More user friendly device selection, no chance of the root or time machine backup drive being selected</span></div><div class='line' id='LC40'><span class="c">#	* Some spelling and grammar corrections</span></div><div class='line' id='LC41'><span class="c">#	* FINALLY drag/drop file support, with full path support, e.g. /Users/me/Downloads - Thanks to Lewis Boon</span></div><div class='line' id='LC42'><br/></div><div class='line' id='LC43'><span class="kn">import</span> <span class="nn">re</span><span class="o">,</span> <span class="nn">os</span><span class="o">,</span> <span class="nn">urllib2</span><span class="o">,</span> <span class="nn">time</span><span class="o">,</span> <span class="nn">sys</span><span class="o">,</span> <span class="nn">threading</span></div><div class='line' id='LC44'><span class="kn">from</span> <span class="nn">commands</span> <span class="kn">import</span> <span class="o">*</span></div><div class='line' id='LC45'><span class="kn">from</span> <span class="nn">sys</span> <span class="kn">import</span> <span class="nb">exit</span></div><div class='line' id='LC46'><span class="kn">from</span> <span class="nn">random</span> <span class="kn">import</span> <span class="n">choice</span></div><div class='line' id='LC47'><span class="kn">from</span> <span class="nn">xml.dom.minidom</span> <span class="kn">import</span> <span class="n">parseString</span></div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'><span class="n">version</span> <span class="o">=</span> <span class="mf">1.15</span></div><div class='line' id='LC50'><br/></div><div class='line' id='LC51'><span class="c">#Display Augs</span></div><div class='line' id='LC52'><span class="n">boldStart</span> <span class="o">=</span> <span class="s">&quot;</span><span class="se">\033</span><span class="s">[1m&quot;</span></div><div class='line' id='LC53'><span class="n">end</span> <span class="o">=</span> <span class="s">&quot;</span><span class="se">\033</span><span class="s">[0;0m&quot;</span></div><div class='line' id='LC54'><span class="n">WARNING</span> <span class="o">=</span> <span class="s">&#39;</span><span class="se">\033</span><span class="s">[0;31m&#39;</span></div><div class='line' id='LC55'><br/></div><div class='line' id='LC56'><span class="n">OS</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">uname</span><span class="p">()</span> <span class="c">#gets OS vars</span></div><div class='line' id='LC57'><br/></div><div class='line' id='LC58'><span class="k">def</span> <span class="nf">checkforUpdate</span><span class="p">():</span></div><div class='line' id='LC59'>	<span class="k">print</span> <span class="s">&#39;Checking for updates...&#39;</span></div><div class='line' id='LC60'>	<span class="k">global</span> <span class="n">version</span></div><div class='line' id='LC61'><br/></div><div class='line' id='LC62'>	<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC63'>		<span class="nb">file</span> <span class="o">=</span> <span class="n">urllib2</span><span class="o">.</span><span class="n">urlopen</span><span class="p">(</span><span class="s">&#39;http://www.exaviorn.com/raspiwrite.xml&#39;</span><span class="p">,</span> <span class="n">timeout</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC64'><br/></div><div class='line' id='LC65'>		<span class="n">data</span> <span class="o">=</span> <span class="nb">file</span><span class="o">.</span><span class="n">read</span><span class="p">()</span></div><div class='line' id='LC66'>		<span class="nb">file</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC67'><br/></div><div class='line' id='LC68'>		<span class="n">dom</span> <span class="o">=</span> <span class="n">parseString</span><span class="p">(</span><span class="n">data</span><span class="p">)</span></div><div class='line' id='LC69'><br/></div><div class='line' id='LC70'>		<span class="n">versionToDate</span> <span class="o">=</span> <span class="nb">float</span><span class="p">(</span><span class="n">dom</span><span class="o">.</span><span class="n">getElementsByTagName</span><span class="p">(</span><span class="s">&#39;Version&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">toxml</span><span class="p">()</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;&lt;Version&gt;&#39;</span><span class="p">,</span><span class="s">&#39;&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;&lt;/Version&gt;&#39;</span><span class="p">,</span><span class="s">&#39;&#39;</span><span class="p">))</span></div><div class='line' id='LC71'>		<span class="n">summary</span> <span class="o">=</span> <span class="n">dom</span><span class="o">.</span><span class="n">getElementsByTagName</span><span class="p">(</span><span class="s">&#39;Summary&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">toxml</span><span class="p">()</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;&lt;Summary&gt;&#39;</span><span class="p">,</span><span class="s">&#39;&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;&lt;/Summary&gt;&#39;</span><span class="p">,</span><span class="s">&#39;&#39;</span><span class="p">)</span></div><div class='line' id='LC72'>		<span class="n">dlURL</span> <span class="o">=</span> <span class="n">dom</span><span class="o">.</span><span class="n">getElementsByTagName</span><span class="p">(</span><span class="s">&#39;URL&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">toxml</span><span class="p">()</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;&lt;URL&gt;&#39;</span><span class="p">,</span><span class="s">&#39;&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;&lt;/URL&gt;&#39;</span><span class="p">,</span><span class="s">&#39;&#39;</span><span class="p">)</span></div><div class='line' id='LC73'><br/></div><div class='line' id='LC74'>		<span class="k">if</span> <span class="n">version</span> <span class="o">&lt;</span> <span class="n">versionToDate</span><span class="p">:</span></div><div class='line' id='LC75'>			<span class="k">print</span> <span class="n">WARNING</span> <span class="o">+</span> <span class="s">&#39;#####################################################################################################################&#39;</span></div><div class='line' id='LC76'>			<span class="k">print</span> <span class="s">&#39;Your current version (</span><span class="si">%s</span><span class="s">) of RasPiWrite is not the latest, please go to the link below to update to version </span><span class="si">%s</span><span class="s">,&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">version</span><span class="p">,</span> <span class="n">versionToDate</span><span class="p">)</span></div><div class='line' id='LC77'>			<span class="k">print</span> <span class="s">&#39;The Changes include: </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">summary</span></div><div class='line' id='LC78'>			<span class="k">print</span> <span class="s">&#39;&#39;&#39;</span></div><div class='line' id='LC79'><span class="s">Please download the latest version of RasPiWrite from </span><span class="si">%s</span><span class="s">&#39;&#39;&#39;</span> <span class="o">%</span> <span class="n">dlURL</span></div><div class='line' id='LC80'>			<span class="k">print</span> <span class="s">&#39;&#39;&#39;#####################################################################################################################</span></div><div class='line' id='LC81'><span class="s">			&#39;&#39;&#39;</span> <span class="o">+</span> <span class="n">end</span></div><div class='line' id='LC82'>		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC83'>			<span class="k">print</span> <span class="s">&#39;&#39;&#39;Your version of RasPiWrite is up-to-date</span></div><div class='line' id='LC84'><span class="s">			&#39;&#39;&#39;</span></div><div class='line' id='LC85'><br/></div><div class='line' id='LC86'>	<span class="k">except</span> <span class="n">urllib2</span><span class="o">.</span><span class="n">URLError</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;		<span class="k">print</span> <span class="s">&quot;&quot;&quot;There was an error in checking for an update: </span><span class="si">%r</span><span class="s"></span></div><div class='line' id='LC88'><span class="s">    		&quot;&quot;&quot;</span> <span class="o">%</span> <span class="n">e</span></div><div class='line' id='LC89'><br/></div><div class='line' id='LC90'><br/></div><div class='line' id='LC91'><span class="k">def</span> <span class="nf">grabRoot</span><span class="p">(</span><span class="n">distro</span><span class="p">):</span> <span class="c">#Parses the raspberry pi downloads page for the links for the currently RasPiWrite supported distros</span></div><div class='line' id='LC92'>	<span class="n">links</span>  <span class="o">=</span> <span class="nb">list</span><span class="p">()</span></div><div class='line' id='LC93'>	<span class="n">htmlSource</span> <span class="o">=</span> <span class="n">urllib2</span><span class="o">.</span><span class="n">urlopen</span><span class="p">(</span><span class="s">&#39;http://www.raspberrypi.org/downloads&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span></div><div class='line' id='LC94'>	<span class="n">linksList</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="s">&#39;href=&quot;(.*)&quot;&#39;</span><span class="p">,</span><span class="n">htmlSource</span><span class="p">)</span></div><div class='line' id='LC95'>	<span class="k">for</span> <span class="n">link</span> <span class="ow">in</span> <span class="n">linksList</span><span class="p">:</span></div><div class='line' id='LC96'>		<span class="k">if</span> <span class="n">distro</span> <span class="ow">in</span> <span class="n">link</span><span class="p">:</span></div><div class='line' id='LC97'>			<span class="k">if</span> <span class="n">link</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;.zip&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="n">link</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;.tar.bz2&#39;</span><span class="p">):</span></div><div class='line' id='LC98'>				<span class="k">return</span> <span class="n">link</span></div><div class='line' id='LC99'><br/></div><div class='line' id='LC100'><br/></div><div class='line' id='LC101'><span class="k">def</span> <span class="nf">getZipUrl</span><span class="p">(</span><span class="n">url</span><span class="p">):</span> <span class="c">#gets all the urls that end in .zip or .tar.bz2 (only two disk image archive types on the download web page)</span></div><div class='line' id='LC102'>	<span class="n">links</span>  <span class="o">=</span> <span class="nb">list</span><span class="p">()</span></div><div class='line' id='LC103'>	<span class="n">htmlSource</span> <span class="o">=</span> <span class="n">urllib2</span><span class="o">.</span><span class="n">urlopen</span><span class="p">(</span><span class="n">url</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span></div><div class='line' id='LC104'>	<span class="n">linksList</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="s">&#39;&lt;a href=&quot;?([^\s^&quot;]+)&#39;</span><span class="p">,</span><span class="n">htmlSource</span><span class="p">)</span></div><div class='line' id='LC105'>	<span class="k">for</span> <span class="n">link</span> <span class="ow">in</span> <span class="n">linksList</span><span class="p">:</span></div><div class='line' id='LC106'>	    <span class="k">if</span> <span class="n">link</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;.zip&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="n">link</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;.tar.bz2&#39;</span><span class="p">):</span></div><div class='line' id='LC107'>	    	 <span class="n">links</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">link</span><span class="p">)</span></div><div class='line' id='LC108'>	<span class="k">return</span> <span class="n">links</span></div><div class='line' id='LC109'><br/></div><div class='line' id='LC110'><span class="k">def</span> <span class="nf">findDL</span><span class="p">(</span><span class="n">OS</span><span class="p">):</span> <span class="c">#legacy reasons (Rasberry Pi website doesn&#39;t currently list Fedora - http://www.raspberrypi.org/phpBB3/viewtopic.php?f=2&amp;t=5624)</span></div><div class='line' id='LC111'>	<span class="n">fedora</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;http://achtbaan.nikhef.nl/events/rpi/images/fedora/14/r1-06-03-2012/raspberrypi-fedora-remix-14-r1.img.gz&#39;</span><span class="p">,</span></div><div class='line' id='LC112'>			<span class="s">&#39;http://mirror.star.net.uk/raspberrypi/images/fedora/14/r1-06-03-2012/raspberrypi-fedora-remix-14-r1.img.gz&#39;</span><span class="p">,</span></div><div class='line' id='LC113'>			<span class="s">&#39;http://www.sqltuning.cz/raspberry/images/fedora/14/r1-06-03-2012/raspberrypi-fedora-remix-14-r1.img.gz&#39;</span><span class="p">,</span></div><div class='line' id='LC114'>			<span class="s">&#39;http://raspberrypi.peir.com/images/fedora/14/r1-06-03-2012/raspberrypi-fedora-remix-14-r1.img.gz&#39;</span><span class="p">,</span></div><div class='line' id='LC115'>			<span class="s">&#39;http://raspberrypi.mirror.triple-it.nl/images/fedora/14/r1-06-03-2012/raspberrypi-fedora-remix-14-r1.img.gz&#39;</span><span class="p">,</span></div><div class='line' id='LC116'>			<span class="s">&#39;http://ftp.ticklers.org/RaspberryPi/images/fedora/14/r1-06-03-2012/raspberrypi-fedora-remix-14-r1.img.gz&#39;</span><span class="p">,</span></div><div class='line' id='LC117'>			<span class="s">&#39;http://files.velocix.com/c1410/images/fedora/14/r1-06-03-2012/raspberrypi-fedora-remix-14-r1.img.gz&#39;</span><span class="p">,</span></div><div class='line' id='LC118'>			<span class="s">&#39;http://raspberrypi.reon.hu/images/fedora/14/r1-06-03-2012/raspberrypi-fedora-remix-14-r1.img.gz&#39;</span><span class="p">]</span></div><div class='line' id='LC119'>	<span class="k">if</span> <span class="n">OS</span> <span class="o">==</span> <span class="s">&#39;fedora&#39;</span><span class="p">:</span> <span class="k">return</span> <span class="n">choice</span><span class="p">(</span><span class="n">fedora</span><span class="p">)</span></div><div class='line' id='LC120'><br/></div><div class='line' id='LC121'><br/></div><div class='line' id='LC122'><span class="k">def</span> <span class="nf">download</span><span class="p">(</span><span class="n">url</span><span class="p">):</span>		<span class="c">#http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python | Downloads the disk image for the user</span></div><div class='line' id='LC123'>	<span class="n">file_name</span> <span class="o">=</span> <span class="n">url</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC124'>	<span class="n">u</span> <span class="o">=</span> <span class="n">urllib2</span><span class="o">.</span><span class="n">urlopen</span><span class="p">(</span><span class="n">url</span><span class="p">)</span></div><div class='line' id='LC125'>	<span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">file_name</span><span class="p">,</span> <span class="s">&#39;wb&#39;</span><span class="p">)</span></div><div class='line' id='LC126'>	<span class="n">meta</span> <span class="o">=</span> <span class="n">u</span><span class="o">.</span><span class="n">info</span><span class="p">()</span></div><div class='line' id='LC127'>	<span class="n">file_size</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">meta</span><span class="o">.</span><span class="n">getheaders</span><span class="p">(</span><span class="s">&quot;Content-Length&quot;</span><span class="p">)[</span><span class="mi">0</span><span class="p">])</span></div><div class='line' id='LC128'>	<span class="k">print</span> <span class="s">&quot;Downloading: </span><span class="si">%s</span><span class="s"> Bytes: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">file_name</span><span class="p">,</span> <span class="n">file_size</span><span class="p">)</span></div><div class='line' id='LC129'>	<span class="n">file_size_dl</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC130'>	<span class="n">block_sz</span> <span class="o">=</span> <span class="mi">8192</span></div><div class='line' id='LC131'>	<span class="k">while</span> <span class="bp">True</span><span class="p">:</span></div><div class='line' id='LC132'>	    <span class="nb">buffer</span> <span class="o">=</span> <span class="n">u</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="n">block_sz</span><span class="p">)</span></div><div class='line' id='LC133'>	    <span class="k">if</span> <span class="ow">not</span> <span class="nb">buffer</span><span class="p">:</span></div><div class='line' id='LC134'>	        <span class="k">break</span></div><div class='line' id='LC135'>	    <span class="n">file_size_dl</span> <span class="o">+=</span> <span class="nb">len</span><span class="p">(</span><span class="nb">buffer</span><span class="p">)</span></div><div class='line' id='LC136'>	    <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">buffer</span><span class="p">)</span></div><div class='line' id='LC137'>	    <span class="n">status</span> <span class="o">=</span> <span class="s">r&quot;</span><span class="si">%10d</span><span class="s">  [</span><span class="si">%3.2f%%</span><span class="s">]&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">file_size_dl</span><span class="p">,</span> <span class="n">file_size_dl</span> <span class="o">*</span> <span class="mf">100.</span> <span class="o">/</span> <span class="n">file_size</span><span class="p">)</span></div><div class='line' id='LC138'>	    <span class="n">status</span> <span class="o">=</span> <span class="n">status</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mi">8</span><span class="p">)</span><span class="o">*</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">status</span><span class="p">)</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC139'>	    <span class="k">print</span> <span class="n">status</span><span class="p">,</span></div><div class='line' id='LC140'>	<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC141'><br/></div><div class='line' id='LC142'><span class="k">def</span> <span class="nf">cleanOutput</span><span class="p">(</span><span class="n">text2</span><span class="p">):</span>	<span class="c">#cleans up the output from df -h</span></div><div class='line' id='LC143'>	<span class="c">#^(?=.*?\b/\b)(?=.*?\bdisk0)((?!Volume).)*$ &lt;-- regex used</span></div><div class='line' id='LC144'>	<span class="c">#^(?:.(?&lt;!/Volumes))*$</span></div><div class='line' id='LC145'>	<span class="n">removeRootHDD</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&quot;(?=.*?\b/\b)(?=.*?\bdisk0)((?!Volume).)*&quot;</span><span class="p">)</span></div><div class='line' id='LC146'>	<span class="n">blacklist</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&quot;.*Backups|.*Backup.*|.*devfs.*|.*map.*&quot;</span><span class="p">)</span></div><div class='line' id='LC147'>	<span class="n">cleanOutput</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="n">removeRootHDD</span><span class="p">,</span> <span class="s">&#39; &#39;</span><span class="p">,</span> <span class="n">text2</span><span class="p">)</span></div><div class='line' id='LC148'>	<span class="n">filterblacklist</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">&quot;(?m)^\s+&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="n">blacklist</span><span class="p">,</span><span class="s">&#39; &#39;</span><span class="p">,</span> <span class="n">cleanOutput</span><span class="p">))</span></div><div class='line' id='LC149'>	<span class="k">return</span> <span class="n">filterblacklist</span></div><div class='line' id='LC150'><br/></div><div class='line' id='LC151'><span class="k">def</span> <span class="nf">matchSD</span><span class="p">(</span><span class="nb">input</span><span class="p">):</span>	<span class="c">#grabs just the drive&#39;s name from the df -h command (macOSX so far)</span></div><div class='line' id='LC152'>	<span class="n">selectSD</span> <span class="o">=</span> <span class="s">r&quot;(?=/)(.*?)\s&quot;</span></div><div class='line' id='LC153'>	<span class="n">match</span> <span class="o">=</span>  <span class="n">re</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">selectSD</span><span class="p">,</span> <span class="nb">input</span><span class="p">)</span></div><div class='line' id='LC154'>	<span class="k">if</span> <span class="n">match</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC155'>		<span class="n">match</span> <span class="o">=</span> <span class="s">&#39;0&#39;</span></div><div class='line' id='LC156'>	<span class="k">return</span> <span class="n">match</span></div><div class='line' id='LC157'><br/></div><div class='line' id='LC158'><span class="k">def</span> <span class="nf">unmount</span><span class="p">(</span><span class="n">location</span><span class="p">):</span>	<span class="c">#unmounts the drive so that it can be rewrittern</span></div><div class='line' id='LC159'>	<span class="k">global</span> <span class="n">OS</span></div><div class='line' id='LC160'>	<span class="k">print</span> <span class="s">&#39;Unmounting the drive in preparation for writing...&#39;</span></div><div class='line' id='LC161'>	<span class="k">if</span> <span class="n">OS</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="s">&#39;Darwin&#39;</span><span class="p">:</span></div><div class='line' id='LC162'>		<span class="n">output</span> <span class="o">=</span> <span class="n">getoutput</span><span class="p">(</span><span class="s">&#39;umount &#39;</span> <span class="o">+</span> <span class="n">location</span><span class="p">)</span></div><div class='line' id='LC163'>	<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC164'>		<span class="n">output</span> <span class="o">=</span> <span class="n">getoutput</span><span class="p">(</span><span class="s">&#39;diskutil unmount &#39;</span> <span class="o">+</span> <span class="n">location</span><span class="p">)</span></div><div class='line' id='LC165'>	<span class="k">print</span> <span class="n">output</span></div><div class='line' id='LC166'>	<span class="k">if</span> <span class="s">&#39;Unmount failed for&#39;</span> <span class="ow">in</span> <span class="n">output</span><span class="p">:</span></div><div class='line' id='LC167'>		<span class="k">print</span> <span class="n">WARNING</span> <span class="o">+</span> <span class="s">&#39;Error, the Following drive couldn</span><span class="se">\&#39;</span><span class="s">t be unmounted, exiting...&#39;</span> <span class="o">+</span> <span class="n">end</span></div><div class='line' id='LC168'>		<span class="nb">exit</span><span class="p">()</span></div><div class='line' id='LC169'><br/></div><div class='line' id='LC170'><span class="k">class</span> <span class="nc">transferInBackground</span> <span class="p">(</span><span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="p">):</span> 	<span class="c">#Runs the dd command in a thread so that I can give a waiting... indicator</span></div><div class='line' id='LC171'><br/></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">run</span> <span class="p">(</span> <span class="bp">self</span> <span class="p">):</span></div><div class='line' id='LC173'>	<span class="k">global</span> <span class="n">SDsnip</span></div><div class='line' id='LC174'>	<span class="k">global</span> <span class="n">path</span></div><div class='line' id='LC175'>	<span class="k">if</span> <span class="n">OS</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="s">&#39;Darwin&#39;</span><span class="p">:</span></div><div class='line' id='LC176'>		<span class="n">copyString</span> <span class="o">=</span> <span class="s">&#39;dd bs=1M if=</span><span class="si">%s</span><span class="s"> of=</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">path</span><span class="p">,</span><span class="n">SDsnip</span><span class="p">)</span></div><div class='line' id='LC177'>	<span class="k">else</span></div><div class='line' id='LC178'>		<span class="n">copyString</span> <span class="o">=</span> <span class="s">&#39;dd bs=1m if=</span><span class="si">%s</span><span class="s"> of=</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">path</span><span class="p">,</span><span class="n">SDsnip</span><span class="p">)</span></div><div class='line' id='LC179'>	<span class="k">print</span> <span class="s">&#39;Running &#39;</span> <span class="o">+</span> <span class="n">copyString</span> <span class="o">+</span> <span class="s">&#39;...&#39;</span></div><div class='line' id='LC180'><br/></div><div class='line' id='LC181'>	<span class="k">print</span> <span class="n">getoutput</span><span class="p">(</span><span class="n">copyString</span><span class="p">)</span></div><div class='line' id='LC182'>	<span class="k">print</span> <span class="s">&#39;done!&#39;</span></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC184'><br/></div><div class='line' id='LC185'><span class="k">def</span> <span class="nf">transfer</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span><span class="n">archiveType</span><span class="p">,</span><span class="n">obtain</span><span class="p">,</span><span class="n">SD</span><span class="p">,</span><span class="n">URL</span><span class="p">):</span>	<span class="c">#unzips the disk image</span></div><div class='line' id='LC186'>	<span class="k">global</span> <span class="n">path</span></div><div class='line' id='LC187'>	<span class="k">if</span> <span class="n">archiveType</span> <span class="o">==</span> <span class="s">&#39;zip&#39;</span><span class="p">:</span> </div><div class='line' id='LC188'>		<span class="c">#path =  file.replace(&quot;.zip&quot;, &quot;&quot;) + &#39;/&#39; + file.replace(&quot;.zip&quot;, &quot;.img&quot;) &lt;- my old code</span></div><div class='line' id='LC189'>		<span class="n">path</span> <span class="o">=</span> <span class="nb">file</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;.zip&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span> <span class="o">+</span> <span class="s">&#39;/&#39;</span> <span class="o">+</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="nb">file</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;.zip&quot;</span><span class="p">,</span> <span class="s">&quot;.img&quot;</span><span class="p">)</span> <span class="c">#Thanks to Lewis Boon</span></div><div class='line' id='LC190'>		<span class="n">extractCMD</span> <span class="o">=</span> <span class="s">&#39;unzip &#39;</span> <span class="o">+</span> <span class="nb">file</span></div><div class='line' id='LC191'><br/></div><div class='line' id='LC192'>	<span class="k">if</span> <span class="n">archiveType</span> <span class="o">==</span> <span class="s">&#39;img&#39;</span><span class="p">:</span> </div><div class='line' id='LC193'>		<span class="n">path</span> <span class="o">=</span>  <span class="nb">file</span><span class="p">;</span></div><div class='line' id='LC194'>		<span class="n">extractCMD</span> <span class="o">=</span> <span class="s">&#39;echo No extracttion required for &#39;</span> <span class="o">+</span> <span class="nb">file</span></div><div class='line' id='LC195'><br/></div><div class='line' id='LC196'>	<span class="k">if</span> <span class="n">archiveType</span> <span class="o">==</span> <span class="s">&#39;gz&#39;</span><span class="p">:</span> </div><div class='line' id='LC197'>		<span class="n">path</span> <span class="o">=</span>  <span class="nb">file</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;.gz&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span> <span class="c">#&lt;-- verify</span></div><div class='line' id='LC198'>		<span class="n">extractCMD</span> <span class="o">=</span> <span class="s">&#39;gunzip &#39;</span> <span class="o">+</span> <span class="nb">file</span></div><div class='line' id='LC199'><br/></div><div class='line' id='LC200'>	<span class="k">if</span> <span class="n">archiveType</span> <span class="o">==</span> <span class="s">&#39;bz2&#39;</span><span class="p">:</span> </div><div class='line' id='LC201'>		<span class="n">path</span> <span class="o">=</span> <span class="s">&#39;&#39;</span> <span class="c">#probably don&#39;t need, but I found during debug that the interpreter would complain about the var not being defined</span></div><div class='line' id='LC202'>		<span class="c">#QtonPi making me jump through hoops:</span></div><div class='line' id='LC203'>		<span class="n">basePath</span> <span class="o">=</span>  <span class="nb">file</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;.tar.bz2&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC204'>		<span class="c">#this path is actually changed to something that the script can locate, such as the basepath</span></div><div class='line' id='LC205'>		<span class="n">extractPath</span> <span class="o">=</span>  <span class="nb">file</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;.tar.bz2&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span> <span class="o">+</span> <span class="s">&#39;/sdcard-img/&#39;</span> <span class="o">+</span> <span class="n">re</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="s">r&quot;(?=qtonpi)([^&gt;]*)(?=-)&quot;</span><span class="p">,</span> <span class="nb">file</span><span class="p">)</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span> <span class="o">+</span> <span class="s">&#39;-sdcard&#39;</span> <span class="o">+</span> <span class="n">re</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="s">r&quot;(?=-)([^&gt;]*)(?=.tar)&quot;</span><span class="p">,</span> <span class="nb">file</span><span class="p">)</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span> <span class="o">+</span> <span class="s">&#39;.img.bz2&#39;</span> <span class="c">#&lt;-- verify</span></div><div class='line' id='LC206'>		<span class="n">finalPath</span> <span class="o">=</span> <span class="nb">file</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;.tar.bz2&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span> <span class="o">+</span> <span class="s">&#39;/sdcard-img/&#39;</span> <span class="o">+</span> <span class="n">re</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="s">r&quot;(?=qtonpi)([^&gt;]*)(?=-)&quot;</span><span class="p">,</span> <span class="nb">file</span><span class="p">)</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span> <span class="o">+</span> <span class="s">&#39;-sdcard&#39;</span> <span class="o">+</span> <span class="n">re</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="s">r&quot;(?=-)([^&gt;]*)(?=.tar)&quot;</span><span class="p">,</span> <span class="nb">file</span><span class="p">)</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span> <span class="o">+</span> <span class="s">&#39;.img&#39;</span></div><div class='line' id='LC207'>		<span class="n">extractCMD</span> <span class="o">=</span> <span class="s">&#39;tar jxf &#39;</span> <span class="o">+</span> <span class="nb">file</span></div><div class='line' id='LC208'>		<span class="n">path</span> <span class="o">=</span> <span class="n">basePath</span></div><div class='line' id='LC209'><br/></div><div class='line' id='LC210'>	<span class="k">if</span> <span class="n">obtain</span> <span class="o">==</span> <span class="s">&#39;dl&#39;</span><span class="p">:</span> </div><div class='line' id='LC211'>		<span class="n">obtainType</span> <span class="o">=</span> <span class="s">&#39;Downloaded by this client (reliable and safe)&#39;</span></div><div class='line' id='LC212'>		<span class="k">if</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">path</span><span class="p">)):</span></div><div class='line' id='LC213'>			<span class="k">print</span> <span class="s">&#39;archive already has been extracted, skipping unzipping...&#39;</span></div><div class='line' id='LC214'>			<span class="k">if</span> <span class="n">archiveType</span> <span class="o">==</span> <span class="s">&#39;bz2&#39;</span><span class="p">:</span></div><div class='line' id='LC215'>				<span class="n">path</span> <span class="o">=</span> <span class="n">extractPath</span></div><div class='line' id='LC216'>				<span class="k">if</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">path</span><span class="p">)):</span></div><div class='line' id='LC217'>					<span class="k">print</span> <span class="s">&#39;Unzipping image..&#39;</span></div><div class='line' id='LC218'>					<span class="k">print</span> <span class="n">getoutput</span><span class="p">(</span><span class="s">&#39;bunzip2 &#39;</span> <span class="o">+</span> <span class="n">path</span><span class="p">)</span></div><div class='line' id='LC219'>				<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC220'>					<span class="k">print</span> <span class="s">&#39;Image has already been unzipped&#39;</span></div><div class='line' id='LC221'>				<span class="n">path</span> <span class="o">=</span> <span class="n">finalPath</span></div><div class='line' id='LC222'>		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC223'>			<span class="n">download</span><span class="p">(</span><span class="n">URL</span><span class="p">)</span></div><div class='line' id='LC224'>			<span class="k">print</span> <span class="s">&#39;Ok... Unzipping the disk , this may take a while...&#39;</span></div><div class='line' id='LC225'>			<span class="k">print</span> <span class="n">getoutput</span><span class="p">(</span><span class="n">extractCMD</span><span class="p">)</span> <span class="c">#extract here!</span></div><div class='line' id='LC226'>			<span class="k">if</span> <span class="n">archiveType</span> <span class="o">==</span> <span class="s">&#39;bz2&#39;</span><span class="p">:</span></div><div class='line' id='LC227'>				<span class="n">path</span> <span class="o">=</span> <span class="n">extractPath</span></div><div class='line' id='LC228'>				<span class="k">if</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">path</span><span class="p">)):</span></div><div class='line' id='LC229'>					<span class="k">print</span> <span class="s">&#39;Unzipping image..&#39;</span></div><div class='line' id='LC230'>					<span class="k">print</span> <span class="n">getoutput</span><span class="p">(</span><span class="s">&#39;bunzip2 &#39;</span> <span class="o">+</span> <span class="n">path</span><span class="p">)</span></div><div class='line' id='LC231'>				<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC232'>					<span class="k">print</span> <span class="s">&#39;Image has already been unzipped&#39;</span></div><div class='line' id='LC233'>				<span class="n">path</span> <span class="o">=</span> <span class="n">finalPath</span></div><div class='line' id='LC234'>	<span class="k">if</span> <span class="n">obtain</span> <span class="o">==</span> <span class="s">&#39;usr&#39;</span><span class="p">:</span> </div><div class='line' id='LC235'>		<span class="n">obtainType</span> <span class="o">=</span> <span class="s">&#39;Obtained by user and passed in (potentially dangerous)&#39;</span></div><div class='line' id='LC236'>		<span class="k">print</span> <span class="s">&#39;Found archive inputted by user, extracting...&#39;</span></div><div class='line' id='LC237'>		<span class="k">if</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">path</span><span class="p">)):</span></div><div class='line' id='LC238'>			<span class="k">print</span> <span class="s">&#39;archive already has been extracted, skipping unzipping...&#39;</span></div><div class='line' id='LC239'>			<span class="k">if</span> <span class="n">archiveType</span> <span class="o">==</span> <span class="s">&#39;bz2&#39;</span><span class="p">:</span></div><div class='line' id='LC240'>				<span class="n">path</span> <span class="o">=</span> <span class="n">extractPath</span></div><div class='line' id='LC241'>				<span class="k">if</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">path</span><span class="p">)):</span></div><div class='line' id='LC242'>					<span class="k">print</span> <span class="s">&#39;Unzipping image..&#39;</span></div><div class='line' id='LC243'>					<span class="k">print</span> <span class="n">getoutput</span><span class="p">(</span><span class="s">&#39;bunzip2 &#39;</span> <span class="o">+</span> <span class="n">path</span><span class="p">)</span></div><div class='line' id='LC244'>				<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC245'>					<span class="k">print</span> <span class="s">&#39;Image has already been unzipped&#39;</span></div><div class='line' id='LC246'>				<span class="n">path</span> <span class="o">=</span> <span class="n">finalPath</span></div><div class='line' id='LC247'><br/></div><div class='line' id='LC248'>			<span class="k">if</span> <span class="n">OS</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="s">&#39;Darwin&#39;</span><span class="p">:</span></div><div class='line' id='LC249'>				<span class="k">print</span> <span class="n">getoutput</span><span class="p">(</span><span class="s">&#39;pwd&#39;</span><span class="p">)</span></div><div class='line' id='LC250'>				<span class="n">path</span> <span class="o">=</span> <span class="n">getoutput</span><span class="p">(</span><span class="s">&quot;pwd&quot;</span><span class="p">)</span><span class="o">+</span> <span class="s">&quot;/&quot;</span> <span class="o">+</span> <span class="nb">file</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&quot;/&quot;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;.zip&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span> <span class="o">+</span> <span class="s">&quot;/&quot;</span> <span class="o">+</span> <span class="nb">file</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&quot;/&quot;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;.zip&quot;</span><span class="p">,</span> <span class="s">&quot;.img&quot;</span><span class="p">)</span></div><div class='line' id='LC251'>				<span class="k">print</span> <span class="n">path</span></div><div class='line' id='LC252'>				<span class="k">print</span> <span class="s">&quot;Not Darwin</span><span class="se">\n</span><span class="s">&quot;</span></div><div class='line' id='LC253'>		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC254'>			<span class="k">print</span> <span class="s">&#39;Ok... Unzipping the disk , this may take a while...&#39;</span></div><div class='line' id='LC255'>			<span class="k">print</span> <span class="n">getoutput</span><span class="p">(</span><span class="n">extractCMD</span><span class="p">)</span> <span class="c">#extract here!</span></div><div class='line' id='LC256'>			<span class="k">if</span> <span class="n">archiveType</span> <span class="o">==</span> <span class="s">&#39;bz2&#39;</span><span class="p">:</span></div><div class='line' id='LC257'>				<span class="n">path</span> <span class="o">=</span> <span class="n">extractPath</span></div><div class='line' id='LC258'>				<span class="k">if</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">path</span><span class="p">)):</span></div><div class='line' id='LC259'>					<span class="k">print</span> <span class="s">&#39;Unzipping image..&#39;</span></div><div class='line' id='LC260'>					<span class="k">print</span> <span class="n">getoutput</span><span class="p">(</span><span class="s">&#39;bunzip2 &#39;</span> <span class="o">+</span> <span class="n">path</span><span class="p">)</span></div><div class='line' id='LC261'>				<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC262'>					<span class="k">print</span> <span class="s">&#39;Image has already been unzipped&#39;</span></div><div class='line' id='LC263'>				<span class="n">path</span> <span class="o">=</span> <span class="n">finalPath</span></div><div class='line' id='LC264'><br/></div><div class='line' id='LC265'>			<span class="k">if</span> <span class="n">OS</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="s">&#39;Darwin&#39;</span><span class="p">:</span></div><div class='line' id='LC266'>				<span class="k">print</span> <span class="n">getoutput</span><span class="p">(</span><span class="s">&#39;pwd&#39;</span><span class="p">)</span></div><div class='line' id='LC267'>				<span class="n">path</span> <span class="o">=</span> <span class="n">getoutput</span><span class="p">(</span><span class="s">&quot;pwd&quot;</span><span class="p">)</span><span class="o">+</span> <span class="s">&quot;/&quot;</span> <span class="o">+</span> <span class="nb">file</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&quot;/&quot;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;.zip&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span> <span class="o">+</span> <span class="s">&quot;/&quot;</span> <span class="o">+</span> <span class="nb">file</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&quot;/&quot;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;.zip&quot;</span><span class="p">,</span> <span class="s">&quot;.img&quot;</span><span class="p">)</span></div><div class='line' id='LC268'>				<span class="k">print</span> <span class="n">path</span></div><div class='line' id='LC269'>				<span class="k">print</span> <span class="s">&quot;Not Darwin</span><span class="se">\n</span><span class="s">&quot;</span></div><div class='line' id='LC270'>	<span class="k">global</span> <span class="n">SDsnip</span></div><div class='line' id='LC271'>	<span class="k">if</span> <span class="p">(</span><span class="n">SD</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s">&quot;/dev/mmcblk&quot;</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span></div><div class='line' id='LC272'>		<span class="n">SDsnip</span> <span class="o">=</span> <span class="s">&quot;/dev/mmcblk&quot;</span> <span class="o">+</span> <span class="n">SD</span><span class="p">[</span><span class="mi">11</span><span class="p">]</span></div><div class='line' id='LC273'>	<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC274'>		<span class="k">if</span> <span class="n">OS</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="s">&#39;Darwin&#39;</span><span class="p">:</span> </div><div class='line' id='LC275'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	<span class="n">SDsnip</span> <span class="o">=</span>  <span class="n">SD</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC276'>&nbsp;		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC277'>&nbsp;			<span class="c"># remove weird partition notation in OS X partition names</span></div><div class='line' id='LC278'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	<span class="n">SDsnip</span> <span class="o">=</span>  <span class="n">SD</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)[:</span><span class="o">-</span><span class="mi">2</span><span class="p">]</span></div><div class='line' id='LC279'><br/></div><div class='line' id='LC280'>	<span class="k">print</span> <span class="n">path</span></div><div class='line' id='LC281'>	<span class="k">print</span> <span class="s">&#39;</span><span class="se">\n\n</span><span class="s">###################################################################&#39;</span></div><div class='line' id='LC282'>	<span class="k">print</span> <span class="s">&#39;About to start the transfer procedure, here is your setup:&#39;</span></div><div class='line' id='LC283'>	<span class="k">print</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC284'><span class="s">&gt; OS Choice: </span><span class="si">%s</span><span class="s"></span></div><div class='line' id='LC285'><span class="s">&gt; SD Card: </span><span class="si">%s</span><span class="s"></span></div><div class='line' id='LC286'><span class="s">&gt; Type: </span><span class="si">%s</span><span class="s"></span></div><div class='line' id='LC287'><span class="s">	&quot;&quot;&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="nb">file</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;.zip&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">),</span> <span class="n">SDsnip</span><span class="p">,</span> <span class="n">obtainType</span><span class="p">)</span></div><div class='line' id='LC288'>	<span class="k">print</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC289'><span class="s">Please remember that neither Matt Jump, exaviorn.com or any contributors can be held to warranty for any destruction of data or hardware </span></div><div class='line' id='LC290'><span class="s">(excerpt from GNU GPL, which can be found in the script&#39;s source, as well as inside the script&#39;s folder):</span></div><div class='line' id='LC291'><span class="s">-----------------------------------------------------------------</span></div><div class='line' id='LC292'><span class="s">This program is distributed in the hope that it will be useful,</span></div><div class='line' id='LC293'><span class="s">but WITHOUT ANY WARRANTY; without even the implied warranty of</span></div><div class='line' id='LC294'><span class="s">MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the</span></div><div class='line' id='LC295'><span class="s">GNU General Public License for more details.</span></div><div class='line' id='LC296'><span class="s">-----------------------------------------------------------------</span></div><div class='line' id='LC297'><span class="s">	&quot;&quot;&quot;</span></div><div class='line' id='LC298'>	<span class="k">print</span> <span class="s">&#39;###################################################################</span><span class="se">\n</span><span class="s">&#39;</span></div><div class='line' id='LC299'>	<span class="n">confirm</span> <span class="o">=</span> <span class="nb">raw_input</span><span class="p">(</span><span class="n">boldStart</span> <span class="o">+</span> <span class="s">&#39;Please verify this information before typing </span><span class="se">\&#39;</span><span class="s">accept</span><span class="se">\&#39;</span><span class="s"> to accept the terms and to start the process, if this information isn</span><span class="se">\&#39;</span><span class="s">t correct, please press ctrl + c (^C), or type </span><span class="se">\&#39;</span><span class="s">exit</span><span class="se">\&#39;</span><span class="s"> to quit: &#39;</span> <span class="o">+</span> <span class="n">end</span><span class="p">)</span></div><div class='line' id='LC300'>	<span class="k">if</span> <span class="n">confirm</span> <span class="o">==</span> <span class="s">&#39;accept&#39;</span><span class="p">:</span></div><div class='line' id='LC301'>&nbsp;&nbsp;&nbsp;		<span class="n">thread1</span> <span class="o">=</span> <span class="n">transferInBackground</span><span class="p">()</span></div><div class='line' id='LC302'>&nbsp;&nbsp;&nbsp;		<span class="n">thread1</span><span class="o">.</span><span class="n">start</span><span class="p">()</span></div><div class='line' id='LC303'>		<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&quot;Waiting&quot;</span><span class="p">)</span></div><div class='line' id='LC304'>&nbsp;&nbsp;&nbsp;		<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span></div><div class='line' id='LC305'>		<span class="k">while</span> <span class="n">thread1</span><span class="o">.</span><span class="n">isAlive</span><span class="p">():</span></div><div class='line' id='LC306'>			<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span></div><div class='line' id='LC307'>			<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&quot;.&quot;</span><span class="p">)</span></div><div class='line' id='LC308'>&nbsp;&nbsp;&nbsp;			<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span></div><div class='line' id='LC309'>&nbsp;&nbsp;&nbsp;		<span class="k">print</span> <span class="s">&#39;Transfer Complete! Please remove the SD card&#39;</span></div><div class='line' id='LC310'>&nbsp;&nbsp;&nbsp;		<span class="k">print</span> <span class="s">&quot;&quot;&quot;###########################################</span></div><div class='line' id='LC311'><span class="s">Relevent information:</span></div><div class='line' id='LC312'><span class="s">&gt; Debian - Login is pi/raspberry</span></div><div class='line' id='LC313'><span class="s">&gt; Arch - Login is root/root</span></div><div class='line' id='LC314'><span class="s">&gt; Fedora - Login is root/fedoraarm</span></div><div class='line' id='LC315'><span class="s">&gt; QtonPi - Login is root/rootme</span></div><div class='line' id='LC316'><span class="s">###########################################</span></div><div class='line' id='LC317'><span class="s">Thank You for using RasPiWrite, you are now free to eject your drive </span></div><div class='line' id='LC318'><span class="s">   		&quot;&quot;&quot;</span></div><div class='line' id='LC319'>	<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC320'>		<span class="k">print</span> <span class="s">&#39;ENDING WITHOUT COPYING ANY DATA ACROSS, SD CARD HAS BEEN UNMOUNTED&#39;</span></div><div class='line' id='LC321'>		<span class="nb">exit</span><span class="p">()</span></div><div class='line' id='LC322'><br/></div><div class='line' id='LC323'><span class="k">def</span> <span class="nf">getImage</span><span class="p">(</span><span class="n">SD</span><span class="p">):</span> <span class="c">#gives the user a bunch of options to download an image, or select their own, it then passes the user on to the transfer function</span></div><div class='line' id='LC324'>	<span class="k">global</span> <span class="n">boldStart</span></div><div class='line' id='LC325'>	<span class="k">global</span> <span class="n">end</span></div><div class='line' id='LC326'>	<span class="n">userChoice</span> <span class="o">=</span> <span class="nb">raw_input</span><span class="p">(</span><span class="s">&#39;Do you wish to Download a Raspberry Pi compatible image (choose yes if you don</span><span class="se">\&#39;</span><span class="s">t have one) (Y/n): &#39;</span><span class="p">)</span></div><div class='line' id='LC327'>	<span class="k">if</span> <span class="p">(</span><span class="n">userChoice</span> <span class="o">==</span> <span class="s">&#39;Y&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">userChoice</span> <span class="o">==</span> <span class="s">&#39;y&#39;</span><span class="p">):</span></div><div class='line' id='LC328'>		<span class="k">print</span> <span class="n">boldStart</span> <span class="o">+</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC329'><span class="s">&gt; Debian </span><span class="se">\&quot;</span><span class="s">Squeeze</span><span class="se">\&quot;</span><span class="s"> [OPTION 1]&quot;&quot;&quot;</span> <span class="o">+</span> <span class="n">end</span> <span class="o">+</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC330'><span class="s">Reference root filesystem from Gray and Dom, containing LXDE, Midori, development tools </span></div><div class='line' id='LC331'><span class="s">and example source code for multimedia functions.</span></div><div class='line' id='LC332'><span class="s">		&quot;&quot;&quot;</span></div><div class='line' id='LC333'>		<span class="k">print</span> <span class="n">boldStart</span> <span class="o">+</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC334'><span class="s">&gt; Arch Linux [OPTION 2]&quot;&quot;&quot;</span> <span class="o">+</span> <span class="n">end</span> <span class="o">+</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC335'><span class="s">Arch Linux ARM is based on Arch Linux, which aims for simplicity and full control to the </span></div><div class='line' id='LC336'><span class="s">end user. Note that this distribution may not be suitable for beginners.</span></div><div class='line' id='LC337'><span class="s">		&quot;&quot;&quot;</span></div><div class='line' id='LC338'>		<span class="k">print</span> <span class="n">boldStart</span> <span class="o">+</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC339'><span class="s">&gt; Fedora 14 [OPTION 3]&quot;&quot;&quot;</span> <span class="o">+</span> <span class="n">end</span> <span class="o">+</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC340'><span class="s">(raspberrypi-fedora-remix-14-r1)</span></div><div class='line' id='LC341'><span class="s">The Raspberry Pi recommended choice for beginners, features a full GUI and applications for </span></div><div class='line' id='LC342'><span class="s">productivity and programming</span></div><div class='line' id='LC343'><span class="s">		&quot;&quot;&quot;</span></div><div class='line' id='LC344'>		<span class="k">print</span> <span class="n">boldStart</span> <span class="o">+</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC345'><span class="s">&gt; QtonPi [OPTION 4]&quot;&quot;&quot;</span> <span class="o">+</span> <span class="n">end</span> <span class="o">+</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC346'><span class="s">QtonPi is an Embedded Linux platform plus SDK optimized for developing and running Qt 5 Apps on Raspberry Pi.</span></div><div class='line' id='LC347'><span class="s">		&quot;&quot;&quot;</span></div><div class='line' id='LC348'>		<span class="n">osChoice</span> <span class="o">=</span> <span class="nb">raw_input</span><span class="p">(</span><span class="s">&#39;Your Choice e.g: </span><span class="se">\&#39;</span><span class="s">1</span><span class="se">\&#39;</span><span class="s"> : &#39;</span><span class="p">)</span></div><div class='line' id='LC349'>		<span class="k">if</span> <span class="n">osChoice</span> <span class="o">==</span> <span class="s">&#39;1&#39;</span><span class="p">:</span></div><div class='line' id='LC350'>			<span class="n">URL</span> <span class="o">=</span> <span class="n">choice</span><span class="p">(</span><span class="n">getZipUrl</span><span class="p">(</span><span class="n">grabRoot</span><span class="p">(</span><span class="s">&#39;debian&#39;</span><span class="p">)))</span></div><div class='line' id='LC351'>			<span class="c">#URL = findDL(&#39;debian&#39;)</span></div><div class='line' id='LC352'>			<span class="k">print</span> <span class="s">&#39;Downloading Debian from [</span><span class="si">%s</span><span class="s">]&#39;</span><span class="o">%</span> <span class="n">URL</span></div><div class='line' id='LC353'>			<span class="n">match</span> <span class="o">=</span> <span class="n">grabRoot</span><span class="p">(</span><span class="s">&#39;debian&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">rpartition</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">)</span></div><div class='line' id='LC354'>			<span class="n">transfer</span><span class="p">(</span><span class="n">match</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span><span class="s">&#39;zip&#39;</span><span class="p">,</span><span class="s">&#39;dl&#39;</span><span class="p">,</span><span class="n">SD</span><span class="p">,</span><span class="n">URL</span><span class="p">)</span></div><div class='line' id='LC355'>		<span class="k">if</span> <span class="n">osChoice</span> <span class="o">==</span> <span class="s">&#39;2&#39;</span><span class="p">:</span></div><div class='line' id='LC356'>			<span class="n">URL</span> <span class="o">=</span> <span class="n">choice</span><span class="p">(</span><span class="n">getZipUrl</span><span class="p">(</span><span class="n">grabRoot</span><span class="p">(</span><span class="s">&#39;arch&#39;</span><span class="p">)))</span></div><div class='line' id='LC357'>			<span class="k">print</span> <span class="s">&#39;Downloading Arch Linux from [</span><span class="si">%s</span><span class="s">]&#39;</span><span class="o">%</span> <span class="n">URL</span></div><div class='line' id='LC358'>			<span class="n">match</span> <span class="o">=</span> <span class="n">grabRoot</span><span class="p">(</span><span class="s">&#39;arch&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">rpartition</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">)</span></div><div class='line' id='LC359'>			<span class="n">transfer</span><span class="p">(</span><span class="n">match</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span><span class="s">&#39;zip&#39;</span><span class="p">,</span><span class="s">&#39;dl&#39;</span><span class="p">,</span><span class="n">SD</span><span class="p">,</span><span class="n">URL</span><span class="p">)</span></div><div class='line' id='LC360'>		<span class="k">if</span> <span class="n">osChoice</span> <span class="o">==</span> <span class="s">&#39;3&#39;</span><span class="p">:</span></div><div class='line' id='LC361'>			<span class="n">URL</span> <span class="o">=</span> <span class="n">findDL</span><span class="p">(</span><span class="s">&#39;fedora&#39;</span><span class="p">)</span></div><div class='line' id='LC362'>			<span class="k">print</span> <span class="s">&#39;Downloading Fedora 14 from [</span><span class="si">%s</span><span class="s">]&#39;</span><span class="o">%</span> <span class="n">URL</span></div><div class='line' id='LC363'>			<span class="n">transfer</span><span class="p">(</span><span class="s">&#39;raspberrypi-fedora-remix-14-r1.img.gz&#39;</span><span class="p">,</span><span class="s">&#39;gz&#39;</span><span class="p">,</span><span class="s">&#39;dl&#39;</span><span class="p">,</span><span class="n">SD</span><span class="p">,</span> <span class="n">URL</span><span class="p">)</span></div><div class='line' id='LC364'>		<span class="k">if</span> <span class="n">osChoice</span> <span class="o">==</span> <span class="s">&#39;4&#39;</span><span class="p">:</span></div><div class='line' id='LC365'>			<span class="n">URL</span> <span class="o">=</span> <span class="n">choice</span><span class="p">(</span><span class="n">getZipUrl</span><span class="p">(</span><span class="n">grabRoot</span><span class="p">(</span><span class="s">&#39;qtonpi&#39;</span><span class="p">)))</span></div><div class='line' id='LC366'>			<span class="k">print</span> <span class="s">&#39;Downloading QtonPi 14 from [</span><span class="si">%s</span><span class="s">]&#39;</span><span class="o">%</span> <span class="n">URL</span></div><div class='line' id='LC367'>			<span class="n">match</span> <span class="o">=</span> <span class="n">grabRoot</span><span class="p">(</span><span class="s">&#39;qtonpi&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">rpartition</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">)</span></div><div class='line' id='LC368'>			<span class="n">transfer</span><span class="p">(</span><span class="n">match</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span><span class="s">&#39;bz2&#39;</span><span class="p">,</span><span class="s">&#39;dl&#39;</span><span class="p">,</span><span class="n">SD</span><span class="p">,</span> <span class="n">URL</span><span class="p">)</span></div><div class='line' id='LC369'><br/></div><div class='line' id='LC370'>	<span class="k">if</span> <span class="p">(</span><span class="n">userChoice</span> <span class="o">==</span> <span class="s">&#39;N&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">userChoice</span> <span class="o">==</span> <span class="s">&#39;n&#39;</span><span class="p">):</span></div><div class='line' id='LC371'>		<span class="n">userLocate</span> <span class="o">=</span> <span class="nb">raw_input</span><span class="p">(</span><span class="s">&#39;Please locate the disk image (.zip, .img.gz, .tar.bz2 (.tar.bz2 only working with QtonPi distros currently): &#39;</span><span class="p">)</span></div><div class='line' id='LC372'>		<span class="k">if</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">userLocate</span><span class="p">)):</span></div><div class='line' id='LC373'>			<span class="n">matchZip</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s">&#39;^.*\.zip$&#39;</span><span class="p">,</span><span class="n">userLocate</span><span class="p">)</span></div><div class='line' id='LC374'>			<span class="n">matchGzip</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s">&#39;^.*\.img.gz$&#39;</span><span class="p">,</span><span class="n">userLocate</span><span class="p">)</span></div><div class='line' id='LC375'>			<span class="n">matchBzip</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s">&#39;^.*\.tar.bz2$&#39;</span><span class="p">,</span><span class="n">userLocate</span><span class="p">)</span></div><div class='line' id='LC376'>			<span class="n">matchImg</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s">&#39;^.*\.img$&#39;</span><span class="p">,</span><span class="n">userLocate</span><span class="p">)</span></div><div class='line' id='LC377'><br/></div><div class='line' id='LC378'>			<span class="k">if</span> <span class="n">matchImg</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC379'>				<span class="k">print</span> <span class="s">&#39;Found Image file&#39;</span></div><div class='line' id='LC380'>				<span class="n">transfer</span><span class="p">(</span><span class="n">userLocate</span><span class="p">,</span><span class="s">&#39;img&#39;</span><span class="p">,</span><span class="s">&#39;usr&#39;</span><span class="p">,</span><span class="n">SD</span><span class="p">,</span><span class="s">&#39;none&#39;</span><span class="p">)</span></div><div class='line' id='LC381'>			<span class="k">if</span> <span class="n">matchZip</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC382'>				<span class="k">print</span> <span class="s">&#39;Found Zip&#39;</span></div><div class='line' id='LC383'>				<span class="n">transfer</span><span class="p">(</span><span class="n">userLocate</span><span class="p">,</span><span class="s">&#39;zip&#39;</span><span class="p">,</span><span class="s">&#39;usr&#39;</span><span class="p">,</span><span class="n">SD</span><span class="p">,</span><span class="s">&#39;none&#39;</span><span class="p">)</span></div><div class='line' id='LC384'>			<span class="k">if</span> <span class="n">matchGzip</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC385'>				<span class="k">print</span> <span class="s">&#39;found Gzip&#39;</span></div><div class='line' id='LC386'>				<span class="n">transfer</span><span class="p">(</span><span class="n">userLocate</span><span class="p">,</span> <span class="s">&#39;gz&#39;</span><span class="p">,</span> <span class="s">&#39;usr&#39;</span><span class="p">,</span><span class="n">SD</span><span class="p">,</span><span class="s">&#39;none&#39;</span><span class="p">)</span></div><div class='line' id='LC387'>			<span class="k">if</span> <span class="n">matchBzip</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC388'>				<span class="k">print</span> <span class="s">&#39;found Bz2&#39;</span></div><div class='line' id='LC389'>				<span class="n">transfer</span><span class="p">(</span><span class="n">userLocate</span><span class="p">,</span> <span class="s">&#39;bz2&#39;</span><span class="p">,</span> <span class="s">&#39;usr&#39;</span><span class="p">,</span><span class="n">SD</span><span class="p">,</span><span class="s">&#39;none&#39;</span><span class="p">)</span></div><div class='line' id='LC390'>&nbsp;&nbsp;&nbsp;&nbsp;		</div><div class='line' id='LC391'><br/></div><div class='line' id='LC392'>		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC393'>			<span class="k">print</span> <span class="s">&#39;sorry, the file you have specified doesn</span><span class="se">\&#39;</span><span class="s">t exist, please try again&#39;</span></div><div class='line' id='LC394'>			<span class="k">print</span> <span class="s">&#39;Press ctrl + c (^C) to quit&#39;</span></div><div class='line' id='LC395'>			<span class="nb">exit</span><span class="p">()</span></div><div class='line' id='LC396'><br/></div><div class='line' id='LC397'><span class="k">def</span> <span class="nf">driveTest</span><span class="p">(</span><span class="n">SD</span><span class="p">):</span></div><div class='line' id='LC398'><br/></div><div class='line' id='LC399'>		<span class="n">sdID</span> <span class="o">=</span> <span class="nb">raw_input</span><span class="p">(</span><span class="s">&quot;I believe this is your SD card: &quot;</span> <span class="o">+</span> <span class="n">SD</span> <span class="o">+</span> <span class="s">&quot; is that correct? (Y/n) &quot;</span><span class="p">)</span></div><div class='line' id='LC400'>		<span class="k">if</span> <span class="p">(</span><span class="n">sdID</span> <span class="o">==</span> <span class="s">&#39;Y&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">sdID</span> <span class="o">==</span> <span class="s">&#39;y&#39;</span><span class="p">):</span> <span class="c">#continue</span></div><div class='line' id='LC401'>			<span class="n">unmount</span><span class="p">(</span><span class="n">SD</span><span class="p">)</span> <span class="c">#&lt;--works, so don&#39;t need to test</span></div><div class='line' id='LC402'>			<span class="n">getImage</span><span class="p">(</span><span class="n">SD</span><span class="p">)</span></div><div class='line' id='LC403'><br/></div><div class='line' id='LC404'>		<span class="k">if</span> <span class="p">(</span><span class="n">sdID</span> <span class="o">==</span> <span class="s">&#39;N&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">sdID</span> <span class="o">==</span> <span class="s">&#39;n&#39;</span><span class="p">):</span></div><div class='line' id='LC405'>			<span class="n">manualID</span> <span class="o">=</span> <span class="nb">raw_input</span><span class="p">(</span><span class="s">&quot;Please enter the location you believe holds the SD Card: &quot;</span><span class="p">)</span></div><div class='line' id='LC406'>			<span class="n">driveTest</span><span class="p">(</span><span class="n">manualID</span><span class="p">)</span></div><div class='line' id='LC407'><br/></div><div class='line' id='LC408'><span class="c">#logic:</span></div><div class='line' id='LC409'><span class="c">#most of this stuff is pretty self explanitory, some of it could be put into a function, but I don&#39;t like </span></div><div class='line' id='LC410'><span class="c">#having loads of micro functions (the ones I do have are going to be expanded to cover all unix based OS&#39;s)</span></div><div class='line' id='LC411'><span class="k">print</span> <span class="n">getoutput</span><span class="p">(</span><span class="s">&#39;clear&#39;</span><span class="p">)</span></div><div class='line' id='LC412'><span class="k">print</span> <span class="n">boldStart</span> <span class="o">+</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC413'><span class="s">  ;d0KOd.  .oOK0x:  </span></div><div class='line' id='LC414'><span class="s"> 0xlllcoxolkolllloX </span></div><div class='line' id='LC415'><span class="s"> ;OccloddKNdxdocckc </span></div><div class='line' id='LC416'><span class="s">  .dkddkWNNMOdoxd,  </span></div><div class='line' id='LC417'><span class="s">  .o:,x0....xd,ck&#39;  </span></div><div class='line' id='LC418'><span class="s">  K:xOoloOOccloocW  </span></div><div class='line' id='LC419'><span class="s">.x;N:....xO....&#39;K;k,</span></div><div class='line' id='LC420'><span class="s">O..Nc...:XNl...:X.,X</span></div><div class='line' id='LC421'><span class="s">.kkx0NXk&#39;...dNNxldK&#39;</span></div><div class='line' id='LC422'><span class="s"> &#39;k...0o....,O...d: </span></div><div class='line' id='LC423'><span class="s">  ;o;&#39;oM0olkWc.;oc  </span></div><div class='line' id='LC424'><span class="s">    .cOx....dOl.    </span></div><div class='line' id='LC425'><span class="s">       .x00k.    </span></div><div class='line' id='LC426'><span class="s">&quot;&quot;&quot;</span> <span class="o">+</span> <span class="n">end</span></div><div class='line' id='LC427'><span class="k">print</span> <span class="s">&quot;&quot;&quot;//////////////////////// &quot;&quot;&quot;</span> <span class="o">+</span> <span class="n">boldStart</span> <span class="o">+</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC428'><span class="s">* Raspberry Pi SD Writer &quot;&quot;&quot;</span> <span class="o">+</span> <span class="n">end</span> <span class="o">+</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC429'><span class="s">* Matt Jump</span></div><div class='line' id='LC430'><span class="s">* exaviorn.com</span></div><div class='line' id='LC431'><span class="s">////////////////////////</span></div><div class='line' id='LC432'><span class="s">(Version 1.15 -MACOSX-)</span></div><div class='line' id='LC433'><span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC434'><span class="k">if</span> <span class="n">OS</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="s">&#39;Darwin&#39;</span><span class="p">:</span> <span class="c">#if Mac OS, will change to posix once I have worked around some of the command differences</span></div><div class='line' id='LC435'>	<span class="k">print</span> <span class="n">WARNING</span> <span class="o">+</span> <span class="s">&#39;I</span><span class="se">\&#39;</span><span class="s">m sorry, but your OS isn</span><span class="se">\&#39;</span><span class="s">t supported at this time, Linux/Unix users - please tune in soon for a POSIX version&#39;</span> <span class="o">+</span> <span class="n">end</span></div><div class='line' id='LC436'><span class="c">#	exit()</span></div><div class='line' id='LC437'><span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">geteuid</span><span class="p">()</span><span class="o">==</span><span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC438'>	<span class="k">print</span> <span class="n">WARNING</span> <span class="o">+</span> <span class="s">&#39;Please run the script using sudo e.g. sudo python raspiwrite.py, or sudo ./raspiwrite.py (need to chmod +x first)&#39;</span> <span class="o">+</span> <span class="n">end</span></div><div class='line' id='LC439'>	<span class="nb">exit</span><span class="p">()</span></div><div class='line' id='LC440'><span class="n">checkforUpdate</span><span class="p">()</span></div><div class='line' id='LC441'><span class="k">print</span> <span class="s">&#39;The following script is designed to copy a Raspberry Pi compatible disk image to an SD Card&#39;</span></div><div class='line' id='LC442'><span class="k">print</span> <span class="n">boldStart</span> <span class="o">+</span> <span class="s">&#39;INCORRECTLY FOLLOWING THE WIZARD COULD RESULT IN THE CORRUPTION OF YOUR HARD DISK, PARTITIONS OR A BACKUP USB DRIVE (INCLUDING MOUNTED TIME MACHINE BACKUP DRIVES)&#39;</span> <span class="o">+</span><span class="n">end</span></div><div class='line' id='LC443'><span class="k">print</span> <span class="s">&#39;It is advisable to remove any other USB HDDs or memory sticks, the wizard might select that one, </span><span class="si">%s</span><span class="s"> if you have multiple hard drives installed, please take a LOT of care selecting the right drive </span><span class="si">%s</span><span class="s">&#39;</span><span class="o">%</span> <span class="p">(</span><span class="n">boldStart</span><span class="p">,</span> <span class="n">end</span><span class="p">)</span> </div><div class='line' id='LC444'><span class="n">text</span> <span class="o">=</span> <span class="n">getoutput</span><span class="p">(</span><span class="s">&#39;df -h&#39;</span><span class="p">)</span></div><div class='line' id='LC445'><span class="nb">raw_input</span><span class="p">(</span><span class="s">&#39;Now insert your SD Card, press enter when you are ready...&#39;</span><span class="p">)</span></div><div class='line' id='LC446'><span class="n">text2</span> <span class="o">=</span> <span class="n">getoutput</span><span class="p">(</span><span class="s">&#39;df -h&#39;</span><span class="p">)</span></div><div class='line' id='LC447'><span class="k">print</span> <span class="s">&quot;&quot;&quot;</span></div><div class='line' id='LC448'><span class="se">\n</span><span class="s">---------------------------------------------------------</span></div><div class='line' id='LC449'><span class="s">&quot;&quot;&quot;</span> <span class="o">+</span> <span class="n">boldStart</span> <span class="o">+</span> <span class="s">&quot;&quot;&quot;The following drives were found, please verify the name of the SD card in finder with the name under the </span><span class="se">\&#39;</span><span class="s">Mounted On</span><span class="se">\&#39;</span><span class="s"> column (after </span><span class="se">\&#39;</span><span class="s">/volumes/</span><span class="se">\&#39;</span><span class="s">):</span></div><div class='line' id='LC450'><span class="s">&quot;&quot;&quot;</span> <span class="o">+</span> <span class="n">end</span></div><div class='line' id='LC451'><span class="n">volumes</span> <span class="o">=</span>  <span class="n">cleanOutput</span><span class="p">(</span><span class="n">text2</span><span class="p">)</span></div><div class='line' id='LC452'><span class="k">print</span> <span class="n">volumes</span></div><div class='line' id='LC453'><span class="k">print</span> <span class="s">&#39;---------------------------------------------------------</span><span class="se">\n</span><span class="s">&#39;</span></div><div class='line' id='LC454'><span class="k">if</span> <span class="n">matchSD</span><span class="p">(</span><span class="n">volumes</span><span class="p">)</span> <span class="o">==</span> <span class="s">&#39;0&#39;</span><span class="p">:</span> <span class="c">#if no  device found</span></div><div class='line' id='LC455'>	<span class="k">print</span> <span class="n">WARNING</span> <span class="o">+</span> <span class="s">&quot;&quot;&quot; </span></div><div class='line' id='LC456'><span class="s">	#############################################################</span></div><div class='line' id='LC457'><span class="s">	WARNING: No reliable SD Card location could be found, please </span></div><div class='line' id='LC458'><span class="s">	insert a SD card device and try again, if you are certain </span></div><div class='line' id='LC459'><span class="s">	about the location of the SD card, you can manually override </span></div><div class='line' id='LC460'><span class="s">	it below</span></div><div class='line' id='LC461'><span class="s">	#############################################################</span></div><div class='line' id='LC462'><span class="s">	&quot;&quot;&quot;</span> <span class="o">+</span> <span class="n">end</span></div><div class='line' id='LC463'>	<span class="n">manualID</span> <span class="o">=</span> <span class="nb">raw_input</span><span class="p">(</span><span class="s">&quot;Please enter the location you believe holds the SD Card: &quot;</span><span class="p">)</span></div><div class='line' id='LC464'>	<span class="n">driveTest</span><span class="p">(</span><span class="n">manualID</span><span class="p">)</span></div><div class='line' id='LC465'><span class="k">else</span><span class="p">:</span> <span class="c">#otherwise...</span></div><div class='line' id='LC466'>	<span class="n">SD</span> <span class="o">=</span> <span class="n">matchSD</span><span class="p">(</span><span class="n">volumes</span><span class="p">)</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span> <span class="c">#selects the first SD/USB drive located</span></div><div class='line' id='LC467'>	<span class="n">driveTest</span><span class="p">(</span><span class="n">SD</span><span class="p">)</span> <span class="c">#action gets delegated to driveTest, which then leads on to the next step, I found this to be the easiest way</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;">
    <button type="submit" class="button">Go</button>
  </form>
</div>
          </div>
        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div>
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2013 <span title="0.05949s from fe3.rs.github.com">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/exaviorn/RasPiWrite/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

    
  </body>
</html>

