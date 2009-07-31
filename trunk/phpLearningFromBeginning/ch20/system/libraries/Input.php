<?php  if (!defined('BASEPATH')) exit('No direct script access allowed');
/**
 * CodeIgniter
 *
 * An open source application development framework for PHP 4.3.2 or newer
 *
 * @package		CodeIgniter
 * @author		Rick Ellis
 * @copyright	Copyright (c) 2006, EllisLab, Inc.
 * @license		http://www.codeignitor.com/user_guide/license.html
 * @link		http://www.codeigniter.com
 * @since		Version 1.0
 * @filesource
 */

// ------------------------------------------------------------------------

/**
 * Input Class
 *
 * Pre-processes global input data for security
 *
 * @package		CodeIgniter
 * @subpackage	Libraries
 * @category	Input
 * @author		Rick Ellis
 * @link		http://www.codeigniter.com/user_guide/libraries/input.html
 */
class CI_Input {
	var $use_xss_clean		= FALSE;
	var $ip_address			= FALSE;
	var $user_agent			= FALSE;
	var $allow_get_array	= FALSE;
	
	/**
	 * Constructor
	 *
	 * Sets whether to globally enable the XSS processing
	 * and whether to allow the $_GET array
	 *
	 * @access	public
	 */	
	function CI_Input()
	{	
		log_message('debug', "Input Class Initialized");
	
		$CFG =& load_class('Config');
		$this->use_xss_clean	= ($CFG->item('global_xss_filtering') === TRUE) ? TRUE : FALSE;
		$this->allow_get_array	= ($CFG->item('enable_query_strings') === TRUE) ? TRUE : FALSE;		
		$this->_sanitize_globals();
	}
	
	// --------------------------------------------------------------------
	
	/**
	 * Sanitize Globals
	 *
	 * This function does the following:
	 *
	 * Unsets $_GET data (if query strings are not enabled)
	 *
	 * Unsets all globals if register_globals is enabled
	 *
	 * Standardizes newline characters to \n
	 *
	 * @access	private
	 * @return	void
	 */
	function _sanitize_globals()
	{
		// Would kind of be "wrong" to unset any of these GLOBALS.
		$protected = array('_SERVER', '_GET', '_POST', '_FILES', '_REQUEST', '_SESSION', '_ENV', 'GLOBALS', 'HTTP_RAW_POST_DATA');
		
		// Unset globals for securiy. 
		// This is effectively the same as register_globals = off
		foreach (array($_GET, $_POST, $_COOKIE) as $global)
		{
			if ( ! is_array($global))
			{
				if ( ! in_array($global, $protected))
				{
					global $global;
					$$global = NULL;
				}
			}
			else
			{
				foreach ($global as $key => $val)
				{
					if ( ! in_array($key, $protected))
					{
						global $$key;
						$$key = NULL;
					}
				}	
			}
		}

		// Is $_GET data allowed? If not we'll set the $_GET to an empty array
		if ($this->allow_get_array == FALSE)
		{
			$_GET = array();
		}
		else
		{
			if (is_array($_GET) AND count($_GET) > 0)
			{
				foreach($_GET as $key => $val)
				{
					$_GET[$this->_clean_input_keys($key)] = $this->_clean_input_data($val);
				}
			}
		}
		
		// Clean $_POST Data
		if (is_array($_POST) AND count($_POST) > 0)
		{
			foreach($_POST as $key => $val)
			{				
				$_POST[$this->_clean_input_keys($key)] = $this->_clean_input_data($val);
			}			
		}
	
		// Clean $_COOKIE Data
		if (is_array($_COOKIE) AND count($_COOKIE) > 0)
		{
			foreach($_COOKIE as $key => $val)
			{			
				$_COOKIE[$this->_clean_input_keys($key)] = $this->_clean_input_data($val);
			}	
		}
		
		log_message('debug', "Global POST and COOKIE data sanitized");
	}	
	
	// --------------------------------------------------------------------
	
	/**
	 * Clean Input Data
	 *
	 * This is a helper function. It escapes data and
	 * standardizes newline characters to \n
	 *
	 * @access	private
	 * @param	string
	 * @return	string
	 */	
	function _clean_input_data($str)
	{
		if (is_array($str))
		{
			$new_array = array();
			foreach ($str as $key => $val)
			{
				$new_array[$this->_clean_input_keys($key)] = $this->_clean_input_data($val);
			}
			return $new_array;
		}
		
		// We strip slashes if magic quotes is on to keep things consistent
		if (get_magic_quotes_gpc())
		{
			$str = stripslashes($str);
		}
		
		// Should we filter the input data?
		if ($this->use_xss_clean === TRUE)
		{
			$str = $this->xss_clean($str);
		}
		
		// Standardize newlines
		return preg_replace("/\015\012|\015|\012/", "\n", $str);
	}
	
	// --------------------------------------------------------------------
	
	/**
	 * Clean Keys
	 *
	 * This is a helper function. To prevent malicious users
	 * from trying to exploit keys we make sure that keys are
	 * only named with alpha-numeric text and a few other items.
	 *
	 * @access	private
	 * @param	string
	 * @return	string
	 */
	function _clean_input_keys($str)
	{	
		 if ( ! preg_match("/^[a-z0-9:_\/-]+$/i", $str))
		 {
			exit('Disallowed Key Characters.');
		 }

		return $str;
	}

	// --------------------------------------------------------------------
	
	/**
	 * Fetch an item from the GET array
	 *
	 * @access	public
	 * @param	string
	 * @param	bool
	 * @return	string
	 */
	function get($index = '', $xss_clean = FALSE)
	{		
		if ( ! isset($_GET[$index]))
		{
			return FALSE;
		}

		if ($xss_clean === TRUE)
		{
			if (is_array($_GET[$index]))
			{
				foreach($_GET[$index] as $key => $val)
				{					
					$_GET[$index][$key] = $this->xss_clean($val);
				}
			}
			else
			{
				return $this->xss_clean($_GET[$index]);
			}
		}

		return $_GET[$index];
	}
	
	// --------------------------------------------------------------------
	
	/**
	 * Fetch an item from the POST array
	 *
	 * @access	public
	 * @param	string
	 * @param	bool
	 * @return	string
	 */
	function post($index = '', $xss_clean = FALSE)
	{		
		if ( ! isset($_POST[$index]))
		{
			return FALSE;
		}

		if ($xss_clean === TRUE)
		{
			if (is_array($_POST[$index]))
			{
				foreach($_POST[$index] as $key => $val)
				{					
					$_POST[$index][$key] = $this->xss_clean($val);
				}
			}
			else
			{
				return $this->xss_clean($_POST[$index]);
			}
		}

		return $_POST[$index];
	}
	
	// --------------------------------------------------------------------
	
	/**
	 * Fetch an item from the COOKIE array
	 *
	 * @access	public
	 * @param	string
	 * @param	bool
	 * @return	string
	 */
	function cookie($index = '', $xss_clean = FALSE)
	{
		if ( ! isset($_COOKIE[$index]))
		{
			return FALSE;
		}

		if ($xss_clean === TRUE)
		{
			if (is_array($_COOKIE[$index]))
			{
				$cookie = array();
				foreach($_COOKIE[$index] as $key => $val)
				{
					$cookie[$key] = $this->xss_clean($val);
				}
		
				return $cookie;
			}
			else
			{
				return $this->xss_clean($_COOKIE[$index]);
			}
		}
		else
		{
			return $_COOKIE[$index];
		}
	}

	// --------------------------------------------------------------------
	
	/**
	 * Fetch an item from the SERVER array
	 *
	 * @access	public
	 * @param	string
	 * @param	bool
	 * @return	string
	 */
	function server($index = '', $xss_clean = FALSE)
	{		
		if ( ! isset($_SERVER[$index]))
		{
			return FALSE;
		}

		if ($xss_clean === TRUE)
		{
			return $this->xss_clean($_SERVER[$index]);
		}
		
		return $_SERVER[$index];
	}
	
	// --------------------------------------------------------------------
	
	/**
	 * Fetch the IP Address
	 *
	 * @access	public
	 * @return	string
	 */
	function ip_address()
	{
		if ($this->ip_address !== FALSE)
		{
			return $this->ip_address;
		}
		
		if ($this->server('REMOTE_ADDR') AND $this->server('HTTP_CLIENT_IP'))
		{
			 $this->ip_address = $_SERVER['HTTP_CLIENT_IP'];
		}
		elseif ($this->server('REMOTE_ADDR'))
		{
			 $this->ip_address = $_SERVER['REMOTE_ADDR'];
		}
		elseif ($this->server('HTTP_CLIENT_IP'))
		{
			 $this->ip_address = $_SERVER['HTTP_CLIENT_IP'];
		}
		elseif ($this->server('HTTP_X_FORWARDED_FOR'))
		{
			 $this->ip_address = $_SERVER['HTTP_X_FORWARDED_FOR'];
		}
		
		if ($this->ip_address === FALSE)
		{
			$this->ip_address = '0.0.0.0';
			return $this->ip_address;
		}
		
		if (strstr($this->ip_address, ','))
		{
			$x = explode(',', $this->ip_address);
			$this->ip_address = end($x);
		}
		
		if ( ! $this->valid_ip($this->ip_address))
		{
			$this->ip_address = '0.0.0.0';
		}
				
		return $this->ip_address;
	}
	
	// --------------------------------------------------------------------
	
	/**
	 * Validate IP Address
	 *
	 * Updated version suggested by Geert De Deckere
	 * 
	 * @access	public
	 * @param	string
	 * @return	string
	 */
	function valid_ip($ip)
	{
		$ip_segments = explode('.', $ip);
		
		// Always 4 segments needed
		if (count($ip_segments) != 4)
		{
			return FALSE;
		}
		// IP can not start with 0
		if (substr($ip_segments[0], 0, 1) == '0')
		{
			return FALSE;
		}
		// Check each segment
		foreach ($ip_segments as $segment)
		{
			// IP segments must be digits and can not be 
			// longer than 3 digits or greater then 255
			if (preg_match("/[^0-9]/", $segment) OR $segment > 255 OR strlen($segment) > 3)
			{
				return FALSE;
			}
		}
		
		return TRUE;
	}
	
	// --------------------------------------------------------------------
	
	/**
	 * User Agent
	 *
	 * @access	public
	 * @return	string
	 */
	function user_agent()
	{
		if ($this->user_agent !== FALSE)
		{
			return $this->user_agent;
		}
	
		$this->user_agent = ( ! isset($_SERVER['HTTP_USER_AGENT'])) ? FALSE : $_SERVER['HTTP_USER_AGENT'];
		
		return $this->user_agent;
	}
	
	// --------------------------------------------------------------------
	
	/**
	 * Filename Security
	 *
	 * @access	public
	 * @param	string
	 * @return	string
	 */
	function filename_security($str)
	{
		$bad = array(
						"../",
						"./",
						"<!--",
						"-->",
						"<",
						">",
						"'",
						'"',
						'&',
						'$',
						'#',
						'{',
						'}',
						'[',
						']',
						'=',
						';',
						'?',
						"%20",
						"%22",
						"%3c",		// <
						"%253c", 	// <
						"%3e", 		// >
						"%0e", 		// >
						"%28", 		// (  
						"%29", 		// ) 
						"%2528", 	// (
						"%26", 		// &
						"%24", 		// $
						"%3f", 		// ?
						"%3b", 		// ;
						"%3d"		// =
        			);
        			
        return stripslashes(str_replace($bad, '', $str));   
	}
	
	// --------------------------------------------------------------------
	
	/**
	 * XSS Clean
	 *
	 * Sanitizes data so that Cross Site Scripting Hacks can be
	 * prevented.