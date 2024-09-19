from enum import Enum


class OsidbApiV1TrackersListAffectsFlawSource(str, Enum):
    VALUE_0 = ""
    ADOBE = "ADOBE"
    APPLE = "APPLE"
    ASF = "ASF"
    BIND = "BIND"
    BK = "BK"
    BUGTRAQ = "BUGTRAQ"
    BUGZILLA = "BUGZILLA"
    CERT = "CERT"
    CERTIFI = "CERTIFI"
    CORELABS = "CORELABS"
    CUSTOMER = "CUSTOMER"
    CVE = "CVE"
    CVEORG = "CVEORG"
    DAILYDAVE = "DAILYDAVE"
    DEBIAN = "DEBIAN"
    DISTROS = "DISTROS"
    FEDORA = "FEDORA"
    FETCHMAIL = "FETCHMAIL"
    FREEDESKTOP = "FREEDESKTOP"
    FREERADIUS = "FREERADIUS"
    FRSIRT = "FRSIRT"
    FULLDISCLOSURE = "FULLDISCLOSURE"
    GAIM = "GAIM"
    GENTOO = "GENTOO"
    GENTOOBZ = "GENTOOBZ"
    GIT = "GIT"
    GNOME = "GNOME"
    GNUPG = "GNUPG"
    GOOGLE = "GOOGLE"
    HP = "HP"
    HW_VENDOR = "HW_VENDOR"
    IBM = "IBM"
    IDEFENSE = "IDEFENSE"
    INTERNET = "INTERNET"
    ISC = "ISC"
    ISEC = "ISEC"
    IT = "IT"
    JBOSS = "JBOSS"
    JPCERT = "JPCERT"
    KERNELBUGZILLA = "KERNELBUGZILLA"
    KERNELSEC = "KERNELSEC"
    LKML = "LKML"
    LWN = "LWN"
    MACROMEDIA = "MACROMEDIA"
    MAGEIA = "MAGEIA"
    MAILINGLIST = "MAILINGLIST"
    MILW0RM = "MILW0RM"
    MIT = "MIT"
    MITRE = "MITRE"
    MOZILLA = "MOZILLA"
    MUTTDEV = "MUTTDEV"
    NETDEV = "NETDEV"
    NISCC = "NISCC"
    NVD = "NVD"
    OCERT = "OCERT"
    OPENOFFICE = "OPENOFFICE"
    OPENSSL = "OPENSSL"
    OPENSUSE = "OPENSUSE"
    ORACLE = "ORACLE"
    OSS = "OSS"
    OSSSECURITY = "OSSSECURITY"
    OSV = "OSV"
    PHP = "PHP"
    PIDGIN = "PIDGIN"
    POSTGRESQL = "POSTGRESQL"
    PRESS = "PRESS"
    REAL = "REAL"
    REDHAT = "REDHAT"
    RESEARCHER = "RESEARCHER"
    RT = "RT"
    SAMBA = "SAMBA"
    SECALERT = "SECALERT"
    SECUNIA = "SECUNIA"
    SECURITYFOCUS = "SECURITYFOCUS"
    SKO = "SKO"
    SQUID = "SQUID"
    SQUIRRELMAIL = "SQUIRRELMAIL"
    SUN = "SUN"
    SUNSOLVE = "SUNSOLVE"
    SUSE = "SUSE"
    TWITTER = "TWITTER"
    UBUNTU = "UBUNTU"
    UPSTREAM = "UPSTREAM"
    VENDORSEC = "VENDORSEC"
    VULNWATCH = "VULNWATCH"
    WIRESHARK = "WIRESHARK"
    XCHAT = "XCHAT"
    XEN = "XEN"
    XPDF = "XPDF"

    def __str__(self) -> str:
        return str(self.value)
